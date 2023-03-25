from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1, participation_fee=5, doc=""
)

SESSION_CONFIGS = [
    # dict(
    #     name='persuasion_H70',
    #     display_name='persuasion_H70',
    #     num_demo_participants=2,
    #     app_sequence=['quiz_HC', 'persuasion_H70', 'questionnaire', 'pay_persuasion']
    # ),
    # dict(
    #     name='persuasion_L70',
    #     display_name='persuasion_L70',
    #     num_demo_participants=2,
    #     app_sequence=['quiz_LC', 'persuasion_L70', 'questionnaire', 'pay_persuasion']
    # ),
    # dict(
    #     name='Partial',
    #     display_name='Partial',
    #     num_demo_participants=2,
    #     app_sequence=['Partial']
    # ),
    # dict(
    #     name='persuasion_L70_New',
    #     display_name='persuasion_L70_New',
    #     num_demo_participants=2,
    #     app_sequence=['quiz_LC_New', 'persuasion_L70_New', 'questionnaire', 'pay_persuasion']
    # ),
    # dict(
    #     name='persuasion_L30',
    #     display_name='persuasion_L30',
    #     num_demo_participants=2,
    #     app_sequence=['quiz_LC', 'persuasion_L30', 'questionnaire', 'pay_persuasion']
    # ),
    dict(
        name='test',
        display_name='test',
        num_demo_participants=2,
        app_sequence=['Partial', 'Elicitation_wtp', 'Partial_2', 'pay']
    ),
    # dict(
    #     name='Complex_Elicitation',
    #     display_name='Complex_Elicitation',
    #     num_demo_participants=2,
    #     app_sequence=['quiz_complex','Simple_Before','Complex_Before','Elicitation_Train','Elicitation','Simple_After','Complex_After','MemoryCards','Cognitive','questionnaire','pay_elicitation']
    # ),
    # dict(
    #     name='Endo_Elicitation',
    #     display_name='Endo_Elicitation',
    #     num_demo_participants=2,
    #     app_sequence=['quiz_complex', 'Simple_Before', 'Endo_Before', 'Elicitation_Train', 'Elicitation',
    #                   'Simple_After', 'Endo_After', 'MemoryCards','Cognitive', 'questionnaire', 'pay_elicitation']
    # ),
    # dict(
    #     name='EndoAD_Elicitation',
    #     display_name='EndoAD_Elicitation',
    #     num_demo_participants=2,
    #     app_sequence=['quiz_complex', 'Simple_Before', 'EndoAD_Before','Elicitation_Train', 'Elicitation',
    #                   'Simple_After', 'EndoAD_After','MemoryCards', 'Cognitive', 'questionnaire', 'pay_elicitation']
    # ),
    # dict(
    #     name='Complex_EndoAD',
    #     display_name='Complex_EndoAD',
    #     num_demo_participants=2,
    #     app_sequence=['quiz_pay','Complex_EndoAD','MemoryCards','Cognitive','Dice','questionnaire','pay_complexity']
    # ),
    # dict(
    #     name='Fourty_Complex',
    #     display_name='Fourty_Complex',
    #     num_demo_participants=2,
    #     app_sequence=['quiz_fourty','Fourty_Complex','MemoryCards','Cognitive','Dice','questionnaire','pay_complexity']
    # ),
    # dict(
    #     name='Fourty_Question',
    #     display_name='Fourty_Question',
    #     num_demo_participants=2,
    #     app_sequence=['quiz_fourty','Fourty_Question','MemoryCards','Cognitive','Dice','questionnaire','pay_complexity']
    # ),
    # dict(
    #     name='Fourty_Detection',
    #     display_name='Fourty_Detection',
    #     num_demo_participants=2,
    #     app_sequence=['quiz_fourty','Fourty_Detection', 'MemoryCards','Cognitive','Dice','questionnaire','pay_complexity']
    # ),
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ROOMS = [
    # dict(
    #     name='econ101',
    #     display_name='Econ 101 class',
    #     participant_label_file='_rooms/econ101.txt',
    # ),
    # dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
    # dict(
    #     name='persuasion',
    #     display_name='persuasion',
    #     participant_label_file='_rooms/persuasion.txt',
    # ),
    # dict(
    #     name='complexity',
    #     display_name='complexity',
    #     participant_label_file='_rooms/complexity.txt',
    # ),
    dict(
        name='persuasion_S1',
        display_name='persuasion_S1',
        participant_label_file='_rooms/persuasion_S1.txt',
    ),
    # dict(
    #     name='persuasion_S2',
    #     display_name='persuasion_S2',
    #     participant_label_file='_rooms/persuasion_S2.txt',
    # ),
]


ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

# don't share this with anybody.
SECRET_KEY = '6lertt4wlb09zj@4wyuy-p-6)i$vh!ljwx&r9bti6kgw54k-h8'

INSTALLED_APPS = ['otree']

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# inactive session configs
# dict(name='trust', display_name="Trust Game", num_demo_participants=2, app_sequence=['trust', 'payment_info']),
# dict(name='prisoner', display_name="Prisoner's Dilemma", num_demo_participants=2,
#      app_sequence=['prisoner', 'payment_info']),
# dict(name='volunteer_dilemma', display_name="Volunteer's Dilemma", num_demo_participants=3,
#      app_sequence=['volunteer_dilemma', 'payment_info']),
# dict(name='cournot', display_name="Cournot Competition", num_demo_participants=2, app_sequence=[
#     'cournot', 'payment_info'
# ]),
# dict(name='dictator', display_name="Dictator Game", num_demo_participants=2,
#      app_sequence=['dictator', 'payment_info']),
# dict(name='matching_pennies', display_name="Matching Pennies", num_demo_participants=2, app_sequence=[
#     'matching_pennies',
# ]),
# dict(name='traveler_dilemma', display_name="Traveler's Dilemma", num_demo_participants=2,
#      app_sequence=['traveler_dilemma', 'payment_info']),
# dict(name='bargaining', display_name="Bargaining Game", num_demo_participants=2,
#      app_sequence=['bargaining', 'payment_info']),
# dict(name='common_value_auction', display_name="Common Value Auction", num_demo_participants=3,
#      app_sequence=['common_value_auction', 'payment_info']),
# dict(name='bertrand', display_name="Bertrand Competition", num_demo_participants=2, app_sequence=[
#     'bertrand', 'payment_info'
# ]),
# dict(name='public_goods_simple', display_name="Public Goods (simple version from tutorial)",
#      num_demo_participants=3, app_sequence=['public_goods_simple', 'payment_info']),
# dict(name='trust_simple', display_name="Trust Game (simple version from tutorial)", num_demo_participants=2,
#      app_sequence=['trust_simple']),
