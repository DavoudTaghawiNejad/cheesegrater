import abce
from riskmodel import RiskModel
from insurancecontract import InsuranceContract
from copy import copy
from tools import run_or_eval

class InsuranceCompany(abce.Agent):
    def init(self, sp, ap):
        self.riskmodel = RiskModel(ap['riskmodel'], ap['imprecision_a'], ap['imprecision_b'])
        self.premium_formula = ap['premium_formula']
        self.reserve_formula = ap['reserve_formula']
        self.contracts = abce.contracts.Contracts()
        self.create('money', 10000)
        self.encumbered = 0

    def offer(self):
        free_cash = self.possession('money') - self.encumbered
        for request in self.get_messages('request_quote'):
            customer = (request.sender_group, request.sender_id)
            contract = InsuranceContract(request.content['risk'],
                                         self.riskmodel,
                                         self.premium_formula,
                                         request.content['value'],
                                         (self.group, self.id),
                                         customer,
                                         round=self.round,
                                         length=52)
            provision = run_or_eval(self.reserve_formula, contract.vars)
            free_cash -= provision
            if  free_cash > 0:
                self.message(request.sender_group, request.sender_id, 'contract', contract)
            else:
                break

    def sign(self):
        for message in self.get_messages('addcontract'):
            contract = message.content
            self.encumbered += run_or_eval(self.reserve_formula, contract.vars)
            self.contracts.add(contract)

    def pay(self):
        payout = 0
        print(self.name, self.possession('money'), self.possession('money') - self.encumbered, len(self.contracts))
        for contract in self.contracts:
            obligation = contract.get_obligation('insurance_company', 'money')
            if obligation > 0:
                contract.pay_out(self,
                                            von='insurance_company',
                                            to='customer',
                                            delivery={'money': obligation},
                                            r=self.round)
                payout += obligation
                print('pay claim', self.id, obligation)
                contract.terminated = True
                self.encumbered -= run_or_eval(self.reserve_formula, contract.vars)
        self.log('payout', payout)

    def unencumber(self):
        for contract in self.contracts:
            if contract.check_ended(self.round):
                self.encumbered -= run_or_eval(self.reserve_formula, contract.vars)





