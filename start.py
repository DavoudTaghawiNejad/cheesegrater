from abce import Simulation
from customer import Customer
from insurancecompany import InsuranceCompany
from risk import Risk
from random import randrange, shuffle


insurance_firm_models = [{'riskmodel': '(abs(a - 50) / 200 + abs(b - 50) / 200) / 100',
                          'premium_formula': 'p * v * 1.1 * l',
                          'reserve_formula': 'v * 0.6',
                          'imprecision_a': 1,
                          'imprecision_b': 1},
                         {'riskmodel': '(abs(a - 50) / 200 + abs(b - 50) / 200) / 100',
                          'premium_formula': 'p * v * 1.1 * l',
                          'reserve_formula': 'v * 0.6',
                          'imprecision_a': 1,
                          'imprecision_b': 1},
                         {'riskmodel': '(abs(a - 50) / 200 + abs(b - 50) / 200) / 100',
                          'premium_formula': 'p * v * 1.1 * l',
                          'reserve_formula': 'v * 0.6',
                          'imprecision_a': 1,
                          'imprecision_b': 1}]

riskprocess = '(abs(a - 50) / 200 + abs(b - 50) / 200) / 100'



def main():
    simulation = Simulation(processes=1)

    risks = [Risk(i, i + randrange(10), value=100, riskprocess=riskprocess) for i in range(100)]
    shuffle(risks)

    customers = simulation.build_agents(Customer, 'customer',
                                        parameters={'riskprocess': riskprocess},
                                        agent_parameters=risks)
    insurance_companies = simulation.build_agents(InsuranceCompany, 'insurance_company', agent_parameters=insurance_firm_models)

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

    simulation.graphs()

if __name__ == '__main__':
    main()
