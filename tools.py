def run_or_eval(formula_or_function, parameters):
    """ runs or evaluates a formula or function """
    try:
        return formula_or_function(**parameters)
    except TypeError:
        return eval(formula_or_function, parameters)
