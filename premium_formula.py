class PremiumFormula:
    """ A risk process is formulated by two formulas.
    The probability of a damage given the a and b position of the property.

    """
    def __init__(self, premium_formula):
        """ The calculation of the premium depending on probability p and value v.

        Args:
            premium_formula:
                Is a string e.G. 'p * v * 1.1'
                Or a function::
                    def(a, b):
                        return p * v * 1.1
        """
        self.premium_formula = premium_formula
