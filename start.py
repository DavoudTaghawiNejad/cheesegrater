from abce import Simulation, gui
from customer import Customer
from insurancecompany import InsuranceCompany
from risk import Risk
from random import randrange, shuffle
from tools import seperate_agents_parameters
from guitext import names, text, title
from collections import OrderedDict


insurance_firm_models = OrderedDict({'0riskmodel': '(abs(a - 50) / 200 + abs(b - 50) / 200) / 100',
                                     '0premium_formula': 'pe * v * 1.1 * l',
                                     '0reserve_formula': 'v * 0.6',
                                     '0imprecision_a': 1.0,
                                     '0imprecision_b': 1.0,
                                     '1riskmodel': '(abs(a - 50) / 200 + abs(b - 50) / 200) / 100',
                                     '1premium_formula': 'pe * v * 1.1 * l',
                                     '1reserve_formula': 'v * 0.6',
                                     '1imprecision_a': 1.0,
                                     '1imprecision_b': 1.0,
                                     '2riskmodel': '(abs(a - 50) / 200 + abs(b - 50) / 200) / 100',
                                     '2premium_formula': 'pe * v * 1.1 * l',
                                     '2reserve_formula': 'v * 0.6',
                                     '2imprecision_a': 1.0,
                                     '2imprecision_b': 1.0})

riskprocess = '(abs(a - 50) / 200 + abs(b - 50) / 200) / 100'
characteristic_a = '0.5 * u1 * 100 + 0.5 * u0 * 100'
characteristic_b = '0.5 * u2 * 100 + 0.5 * u0 * 100'

parameters = OrderedDict({'Name': 'SimulationName',
                          'Describtion': 'Text',
                          'characteristic_a': characteristic_a,
                          'characteristic_b': characteristic_b,
                          'riskprocess': riskprocess})

parameters.update(insurance_firm_models)

@gui(parameters, names=names, text=text, title=title)
def main(parameters):
    simulation_parameters, insurance_firm_models = seperate_agents_parameters(parameters)
    print(insurance_firm_models)
    simulation = Simulation(processes=1)

    risks = [Risk(characteristic_a, characteristic_b, value=100, riskprocess=riskprocess) for i in range(100)]
    shuffle(risks)

    customers = simulation.build_agents(Customer, 'customer',
                                        parameters={'riskprocess': riskprocess,
                                                    'characteristic_a': characteristic_a,
                                                    'characteristic_b': characteristic_b},
                                        agent_parameters=risks)
    insurance_companies = simulation.build_agents(InsuranceCompany, 'insurance_company', agent_parameters=insurance_firm_models)

    try:
      for r in range(500):
          simulation.advance_round(r)
          customers.get_insurance()
          insurance_companies.offer()
          customers.subscribe()
          insurance_companies.sign()
          customers.pay()
          customers.check_risk_and_claim()
          insurance_companies.pay()
          insurance_companies.unencumber()
          customers.new_risk()
    except:
        pass
    simulation.finalize()

if __name__ == '__main__':
    main()
