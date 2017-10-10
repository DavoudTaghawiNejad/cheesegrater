from tools import run_or_eval
from contract import Contract

class InsuranceContract(Contract):
    def __init__(self, risk, riskmodel, premium_formula, value, insurance_company, customer, length, round):
        Contract.__init__(self, contract_partners={'insurance_company': insurance_company,
                                                   'customer': customer})
        self.risk = risk
        a = riskmodel.estimate_a(risk.a)
        b = riskmodel.estimate_b(risk.b)

        probability_estimate = run_or_eval(riskmodel.riskmodel, {'a': a, 'b': b})
        self.premium = run_or_eval(premium_formula, {'a': a, 'b': b, 'pe': probability_estimate, 'v': value, 'l': length})
        assert 0 <= probability_estimate <= 1, (a, b, probability_estimate)

        self.add_obligation('customer', 'money', self.premium)
        self.value = value
        self.end_date = length + round
        self.terminated = False

        self.vars = {'a': a, 'b': b, 'pe': probability_estimate, 'v': value, 'l': length, 'premium': self.premium}

    def execute(self):
        self.add_obligation('insurance_company', 'money', self.value)

    def pay_out(self, me, von, to, delivery, r):
        super().fulfill_obligations(me,
                                  von=von,
                                  to=to,
                                  delivery=delivery)
        self.terminated = True
        assert r <= self.end_date, (r, self.end_date)

    def check_ended(self, round):
        if self.end_date == round and not self.terminated:
            self.terminated = True
            return True
        else:
            return False



