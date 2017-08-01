def run_or_eval(formula_or_function, parameters):
    """ runs or evaluates a formula or function """
    try:
        return formula_or_function(**parameters)
    except TypeError:
        return eval(formula_or_function, parameters)

def seperate_agents_parameters(parameters):
    simulation_parameters = {}
    agent_parameters = [{}, {}, {}]
    for key, value in parameters.items():
        try:
            firm_nr = int(key[0])
            agent_parameters[firm_nr][key[1:]] = value
        except ValueError:
            simulation_parameters[key] = value
    return simulation_parameters, agent_parameters
