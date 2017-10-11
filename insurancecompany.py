from copy import copy
import abce
from riskmodel import RiskModel
from insurancecontract import InsuranceContract
from tools import run_or_eval
from abce import NotEnoughGoods

class InsuranceCompany(abce.Agent):
    def init(self, sp, ap):
        self.riskmodel = RiskModel(ap['riskmodel'], ap['imprecision_a'], ap['imprecision_b'])
        self.premium_formula = ap['premium_formula']
        self.reserve_formula = ap['reserve_formula']
        self.contracts = abce.contracts.Contracts()
        self.create('money', 10000)
        self.encumbered = 0

    def offer(self):
        """ Each insurance firm send an insurance contract offer for each
        request it got. The length of the insurance contract is 52 weeks.
        Risk model and premium are according the the formulas specified.
        Insurance firms only offer a contract if the have sufficient
        unencumbered funds.
        """

        free_cash = self.possession('money') - self.encumbered
        for request in self.get_messages('request_quote'):
            customer = request.sender
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
                self.send(request.sender, 'contract', contract)
            else:
                break

    def sign(self):
        """ Insurance firms underwrite the contract and encumber capital """
        for message in self.get_messages('addcontract'):
            contract = message.content
            self.encumbered += run_or_eval(self.reserve_formula, contract.vars)
            self.contracts.add(contract)

    def pay(self):
        """ Insurance firms pay out claims """
        payout = 0
        #print(self.name, self.possession('money'), self.possession('money') - self.encumbered, len(self.contracts))
        for contract in self.contracts:
            obligation = contract.get_obligation('insurance_company', 'money')
            if obligation > 0:
                try:
                    contract.pay_out(self,
                                     von='insurance_company',
                                     to='customer',
                                     delivery={'money': obligation},
                                     r=self.round)
                except NotEnoughGoods:
                    self.destroy('money')
                    return self.name
                payout += obligation
                print('pay claim', self.id, obligation)
                contract.terminated = True
                self.encumbered -= run_or_eval(self.reserve_formula, contract.vars)
        self.log('payout', payout)

    def unencumber(self):
        """ The money encumbered for contracts that have ended is unencumbered"""
        for contract in self.contracts:
            if contract.check_ended(self.round):
                self.encumbered -= run_or_eval(self.reserve_formula, contract.vars)






