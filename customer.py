import abce
from risk import Risk
from random import randrange


class Customer(abce.Agent):
    def init(self, sp, risk):
        self.risk = risk
        self.riskprocess = sp['riskprocess']
        self.insurance_companies = range(3)
        self.contracts = abce.contracts.Contracts()
        self.create('money', 1000)


    def get_insurance(self):
        if (not self.contracts) and (not self.risk is None) and self.id % 52 < self.round:
            for insurance_company in self.insurance_companies:
                self.message('insurance_company', insurance_company, 'request_quote', {'risk': self.risk, 'a': self.risk.a, 'b': self.risk.b, 'value': self.risk.value})


    def subscribe(self):
        contracts = self.get_messages('contract')
        if contracts:
            premia = {contract.content.premium: contract for contract in contracts}
            cheapest = premia[min(premia)]
            self.message(cheapest.sender_group, cheapest.sender_id, 'addcontract', cheapest.content)
            self.contracts.add(cheapest.content)

    def pay(self):
        for contract in self.contracts:
            obligations = contract.get_obligations('customer')
            contract.fulfill_obligations(self,
                                        von='customer',
                                        to='insurance_company',
                                        delivery=obligations)

    def check_risk_and_claim(self):
        for contract in self.contracts:
            if contract.risk.time == self.round:
                contract.execute()
                self.risk = None


    def new_risk(self):
        if self.risk is None and self.possession('money') >= 100:
            self.destroy('money', 100)
            self.risk = Risk(randrange(100), randrange(100), 100, self.riskprocess)




