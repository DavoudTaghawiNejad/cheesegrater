title = 'Cheesegrater: an editable simulator of an insurance market'

text = """ (drag and drop me)
           <h2> How it works </h2>
           This simulation simulates three insurance firms in a simple setting that you
           - the user - designs.

           <h4> Insurable risks </h4>
           You first establish the insurable risks. Every risk has two characteristics
           a and b. a and b are calculated based on underlying random variables. If a
           and b share a random variable they are correlated.

           The Riskprocess, establishes the probability of an event of damage to occur,
           it should dependent on characteristics of the risk.

           The damage, when its occurs is always 100 pounds.

           <h4> 3 stylized insurance firms </h4>
           The 3 stylized insurance firms, have a risk model, that is based on imprecise
           observations of the characteristics a and b.

           The risk model calculates aprobability of an event to occur.

           The premium formula calculates the premium an insurance asks to
           insure a risk.

           The reserve formula calculates how much reserves an insurance firm must
           encumber in order to underwrite an additional risk.

           The firms start of with a capital of 10000.

           <h4> Customers </h4>
           The customers each hold a risk. They try to get insurance. They always
           buy the cheapest insurance. If a risk is damaged and they have sufficient
           money they buy a new risk.

           <h4> Contracts </h4>
           When an event of damage happens, the insurance pays and the contract
           gets extinguished. The price of the contract has to be payed upfront.

           <h2> Baseline scenario </h2>
           For example in the Baseline scenario. Characteristics a and b have a
           correlation of 50%, because they share the random variable u0.

           The probability of an insurance event is higher the closer a risk is
           to the midpoint of characteristic a and also the closer a risk is
           to the midpoint of characteristic b.

           Insurances have a symmetric and correct risk model but an imprecise
           ability to observe the characteristics a and b.

           <h2> Minimal Viable Experiment </h2>
           This is not a full fledged insurance model as ISLE is. It is rather a
           minimal and user friendly model, aimed at co-creating a simulator, to
           look at different scenarios.
           At this point it is important that you use this simulator and give us
           feedback what variables need to be introduced or exposed.

           <h2> Language for formulas </h2>
           You can use standard mathematical notation to express the formulas.
           Note that power is ** not ^.
           All python functions can be used. For example you can use int(u1 * 100),
           in order to have discrete values for a characteristic. Further useful
           functions are abs(.) for absolute values; exp(.) for exponential

           """

names = {'riskprocess': """<h5> Riskprocess </h5>
                           The probability of a risk to explode depending on
                           characteristics <b>a</b> and <b>b</b>""",
         'characteristic_a': """<h5> Risk characteristics a </h5>
                                characteristic a and b can be calculated using 6
                                random variables <b>u0</b>, <b>u1</b>, <b>u2</b>,
                                <b>n0</b>, <b>n1</b>, <b>n2</b>. Where the
                                former are uniform distributed between 0 and 1 and
                                the later follow a gaussian distribution with mean
                                0 and sigma 1.<br>
                                If characteristics a and b use a joint random variable,
                                they will be correlated.""",
         'characteristic_b': """<h5> Risk characteristics b <h5>""",
         '0riskmodel': """<h5>Insurance firm 0 Risk Model</h5>
                          use imprecise observation of characteristics <b>a</b> and <b>b</b> to calculate
                          probability of insurance case""",
         '0premium_formula': """<h5>Insurance firm 0 Calculation of premium</h5>
                                use - <b>pe</b> for the probability estimate of an insurance case
                                    - <b>v</b> insured value
                                    - <b>l</b> for length o contract """,
         '0reserve_formula':  """<h5>Insurance firm 0 Calculation of reserves</h5>
                                 use - <b>pe</b> for the probability estimate of insurance case
                                     - <b>v</b> insured value
                                     - <b>l</b> for length of contract
                                     - characteristic <b>a</b>, <b>b</b>
                                     - <b>premium</b> for premium""",

         '0imprecision_a':  """<h5>Insurance firm 0 imprecision of observing characteristic a</h5>
                               standard deviation of estimate around real property of a""",
         '0imprecision_b':  '<h5>Insurance firm 0 imprecision of observing characteristic b</h5>',

         '1riskmodel': """<h5>Insurance firm 1 Risk Model</h5>""",
         '1premium_formula': """<h5>Insurance firm 1 Calculation of premium</h5>""",
         '1reserve_formula':  """<h5>Insurance firm 1 Calculation of reserves</h5>""",
         '1imprecision_a':  '<h5>Insurance firm 1 imprecision of observing characteristic a</h5>',
         '1imprecision_b':  '<h5>Insurance firm 1 imprecision of observing characteristic b</h5>',

         '2riskmodel': """<h5>Insurance firm 2 Risk Model</h5>""",
         '2premium_formula': """<h5>Insurance firm 2 Calculation of premium</h5>""",
         '2reserve_formula':  """<h5>Insurance firm 2 Calculation of reserves</h5>""",
         '2imprecision_a':  '<h5>Insurance firm 2 imprecision of observing characteristic a</h5>',
         '2imprecision_b':  '<h5>Insurance firm 2 imprecision of observing characteristic b</h5>',
         }


