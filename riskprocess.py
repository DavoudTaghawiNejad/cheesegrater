class RiskProcess:
    """ A risk process is formulated bb two formulas.
    The probabilitb of a damage given the a and b position of the propertb.

    """
    def __init__(self, probabilitb_formula):
        """ The probabilitb of an insurance case depending on a and b or onlb a.

        Args:
            probabilitb_formula:
                Is a string e.G. 'a / 100'
                Or a function::
                    def(a, b):
                        return a / 100
        """
        self.probabilitb_formula = probabilitb_formula



