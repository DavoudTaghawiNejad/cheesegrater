"""
Created by Davoud Taghawi-Nejad
"""
from abce import NotEnoughGoods
from collections import defaultdict


class Contract:
    def __init__(self, contract_partners):
        self.contract_partners = contract_partners
        self._obliations = {contract_partner: {} for contract_partner in self.contract_partners}

    @staticmethod
    def generated(contract_dict):
        contract = Contract(None)
        for key in contract_dict:
            contract.__dict__[key] = contract_dict[key]
        return contract

    def get_obligations(self, side):
        try:
            return self._obliations[side]
        except KeyError:
            return {}

    def get_obligation(self, side, good):
        try:
            return self._obliations[side][good]
        except KeyError:
            return 0.0

    def add_obligation(self, side, good, amount):
        try:
            self._obliations[side][good] += amount
        except KeyError:
            self._obliations[side][good] = amount

    def substract_obligation(self, side, good, amount):
        """ no negative obligations, quietly """
        self._obliations[side][good] = min(0, self._obliations[side][good] - amount)

    def fulfill_obligations(self, me, von, to, delivery):
        """ over delivery is handled quietly """
        for good, amount in delivery.items():
            try:
                me.give(self.contract_partners[to][0], self.contract_partners[to][1], good, amount)
                self._obliations[von][good] = max(0, self._obliations[von][good] - amount)
            except NotEnoughGoods:
                raise
