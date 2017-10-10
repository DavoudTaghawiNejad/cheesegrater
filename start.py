""" Every round the following sequence of events happens:

    - Customers, who have risks, ask for insurance offers.
    - Firms offer contracts
    - Customers buy the cheapest contract
    - Insurance firms underwrite the policy
    - Customers pay the premium
    - The check their risks and claim
    - Insurance firms pay
    - Insurance firms encumber money for expired contracts
    - Customers buy new risks
    """
from abce import Simulation, gui
from customer import Customer
from insurancecompany import InsuranceCompany
from risk import Risk
from random import randrange, shuffle
from tools import seperate_agents_parameters
from guitext import names, text, title, google_docs, header
from collections import OrderedDict


insurance_firm_models = OrderedDict([('0riskmodel', '(abs(a - 50) / 200 + abs(b - 50) / 200) / 100'),
                                     ('0premium_formula', '(1 - (1 - pe) ** l) * v * 1.001'),
                                     ('0reserve_formula', 'v * 0.6'),
                                     ('0imprecision_a', 1.0),
                                     ('0imprecision_b', 1.0),
                                     ('1riskmodel', '(abs(a - 50) / 200 + abs(b - 50) / 200) / 100'),
                                     ('1premium_formula', '(1 - (1 - pe) ** l) * v * 1.001'),
                                     ('1reserve_formula', 'v * 0.6'),
                                     ('1imprecision_a', 1.0),
                                     ('1imprecision_b', 1.0),
                                     ('2riskmodel', '(abs(a - 50) / 200 + abs(b - 50) / 200) / 100'),
                                     ('2premium_formula', '(1 - (1 - pe) ** l) * v * 1.001'),
                                     ('2reserve_formula', 'v * 0.6'),
                                     ('2imprecision_a', 1.0),
                                     ('2imprecision_b', 1.0)])

riskprocess = '(abs(a - 50) / 200 + abs(b - 50) / 200) / 100'
characteristic_a = '0.5 * u1 * 100 + 0.5 * u0 * 100'
characteristic_b = '0.5 * u2 * 100 + 0.5 * u0 * 100'

parameters = OrderedDict([('characteristic_a', characteristic_a),
                          ('characteristic_b', characteristic_b),
                          ('riskprocess', riskprocess)])

parameters.update(insurance_firm_models)


@gui(parameters, names=names, texts=[text], title=title,
     pages=[('Comments', google_docs)], header=header, serve=False,
     histograms=[999])
def main(parameters):
    simulation_parameters, insurance_firm_models = seperate_agents_parameters(parameters)

    simulation = Simulation(processes=1)

    risks = [Risk(simulation_parameters['characteristic_a'], simulation_parameters['characteristic_b'], value=100, riskprocess=riskprocess)
             for i in range(100)]
    shuffle(risks)

    customers = simulation.build_agents(Customer, 'customer',
                                        parameters={'riskprocess': riskprocess,
                                                    'characteristic_a': simulation_parameters['characteristic_a'],
                                                    'characteristic_b': simulation_parameters['characteristic_a']},
                                        agent_parameters=risks)
    insurance_companies = simulation.build_agents(InsuranceCompany, 'insurance_company', agent_parameters=insurance_firm_models)

    try:
        for r in range(1000):
            simulation.advance_round(r)
            customers.get_insurance()
            insurance_companies.offer()
            customers.subscribe()
            insurance_companies.sign()
            customers.pay()
            customers.check_risk_and_claim()
            insurance_companies.pay()
            insurance_companies.unencumber()
            insurance_companies.panel_log(['encumbered'],
                                              ['money'],
                                              {'free_cash': lambda self: self.possession('money') - self.encumbered},
                                              len=['contracts'])
            # insurance_companies.agg_log(['encumbered'],
            #                             ['money'],
            #                             {'free_cash': lambda self: self.possession('money') - self.encumbered},
            #                             len=['contracts'])
    except:
        pass
    finally:
        simulation.finalize()

if __name__ == '__main__':
    main(parameters)
