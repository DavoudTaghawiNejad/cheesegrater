#pylint: disable=C0111, C0301
import abce
from risk import Risk


class Customer(abce.Agent):
    """ Insurance customers hold a risk and cash.
    """
    def init(self, sp, risk):
        self.risk = risk
        self.riskprocess = sp['riskprocess']
        self.characteristic_a = sp['characteristic_a']
        self.characteristic_b = sp['characteristic_b']
        self.insurance_companies = range(3)
        self.contracts = abce.contracts.Contracts()
        self.create('money', 1000)

    def get_insurance(self):
        """ If agents have a risk and the risk is not insured they seek coverage, by sending a message to
        each insurance company.
        (In the first 52 rounds not all agents look for risks to avoid expiration waves)
        """
        if (not self.contracts) and (not self.risk is None) and self.id % 52 < self.round:
            for insurance_company in self.insurance_companies:
                self.send(('insurance_company', insurance_company), 'request_quote', {'risk': self.risk, 'a': self.risk.a, 'b': self.risk.b, 'value': self.risk.value})

    def subscribe(self):
        """ Customers subscribe to the cheapest contract """
        contracts = self.get_messages('contract')
        if contracts:
            premia = {contract.content.premium: contract for contract in contracts}
            cheapest = premia[min(premia)]
            if self['money'] > min(premia):
                self.send(cheapest.sender, 'addcontract', cheapest.content)
                self.contracts.add(cheapest.content)

    def pay(self):
        """ Customers pay the premiums """
        for contract in self.contracts:
            obligations = contract.get_obligations('customer')
            contract.fulfill_obligations(self,
                                         von='customer',
                                         to='insurance_company',
                                         delivery=obligations)

    def check_risk_and_claim(self):
        """ Customers check whether they have an insurance claim. If yes the ask the insurance firm to pay """
        for contract in self.contracts:
            if contract.risk.time == self.round:
                contract.execute()
                self.risk = None


    def new_risk(self):
        """ Customers buy new risks """
        if self.risk is None and self.possession('money') >= 100:
            self.destroy('money', 100)
            self.risk = Risk(self.characteristic_a, self.characteristic_b, 100, self.riskprocess)




