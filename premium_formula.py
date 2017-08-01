class PremiumFormula:
    """ A risk process is formulated bb two formulas.
    The probabilitb of a damage given the a and b position of the propertb.

    """
    def __init__(self, premium_formula):
        """ The caluculation of the premium depending on probability p and value v.

        Args:
            premium_formula:
                Is a string e.G. 'p * v * 1.1'
                Or a function::
                    def(a, b):
                        return p * v * 1.1
        """
        self.premium_formula = premium_formula



