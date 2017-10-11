rfrom random import normalvariate


class RiskModel:
    """ A risk model is formulated by two formulas.
    The perceived probability of a damage given the a and b position of the property.

    """
    def __init__(self, riskmodel, imprecision_a, imprecision_b):
        """ The probability of an insurance case depending on a and b or only a.
        The imprecision of observing a and b

        Args:
            riskmodel:
                Is a string e.G. 'a / 100'
                Or a function::

                    def(a, b):
                        return a / 100

            imprecision_a:
                sigma standard deviation of observing a

            imprecision_b:
                sigma standard deviation of observing b


        """
        self.riskmodel = riskmodel
        self.imprecision_a = imprecision_a
        self.imprecision_b = imprecision_b

    def estimate_a(self, a):
        return normalvariate(a, self.imprecision_a)

    def estimate_b(self, b):
        return normalvariate(b, self.imprecision_b)





