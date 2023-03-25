from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Junya Zhou'
doc = """
Comprehension quiz for the complexity experiment
"""


class Constants(BaseConstants):
    name_in_url = 'quiz_fourty'
    players_per_group = None
    num_rounds = 1
    # cost = c(4)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    round_payoff = models.CurrencyField()

    Color_choice = models.IntegerField(
    choices=[
        [0, 'No'],
        [1, 'Yes'],
    ],
    label='Do you have any problem in identifying the following colors?',
    widget=widgets.RadioSelect,
)


    Q1_choice = models.IntegerField(
    choices=[
        [1, 'True'],
        [2, 'False'],
    ],
    label='1. When sender reports the messages, he can only see the drawn set of cards in this round, but not the other two unrealized set of cards.',
    widget=widgets.RadioSelect,
)

    Q2_choice = models.IntegerField(
    choices=[
        [1, 'Cross'],
        [2, 'Pentagon'],
        [3, 'Heart'],
        [4, 'Diamond']
    ],
    label='',
    widget=widgets.RadioSelect,
)


    Q3_choice = models.IntegerField(
    choices=[
        [1, '(Yellow, 16, P)'],
        [2, '(Pink, 12, A)'],
        [3, '(Green, 7, H)'],
        [4, '(Blue, 8, G)']
    ],
    label='',
    widget=widgets.RadioSelect
)


    Q4_choice = models.IntegerField(
        choices = [
            [1, '(Sender 15, Receiver 15)'],
            [2, '(Sender 3, Receiver 3)'],
            [3, '(Sender 15, Receiver 3)'],
            [4,'(Sender 3, Receiver 15)']
        ],
    label='',
    widget=widgets.RadioSelect
    )

    Q5_choice = models.IntegerField(
        choices = [
            [1, 'Up'],
            [2, 'Middle'],
            [3, 'Down']
        ],
    label='',
    widget=widgets.RadioSelect
    )

#     Q5_choice = models.IntegerField(
#     choices=[
#         [1, 'Sender 15, Receiver 11'],
#         [2, 'Sender 5, Receiver 11'],
#         [3, 'Sender 15, Receiver 1'],
#         [4, 'Sender 5, Receiver 1'],
#     ],
#     widget=widgets.RadioSelect
# )

    correct = models.IntegerField()
    correct_1 = models.IntegerField()
    correct_2 = models.IntegerField()
    correct_3 = models.IntegerField()
    correct_4 = models.IntegerField()
    correct_5 = models.IntegerField()
    # correct_5 = models.IntegerField()


    def num_correct(self):
        if self.Q1_choice == 1:
            self.correct_1 = 1
        else:
            self.correct_1 = 0
        if self.Q2_choice == 2:
            self.correct_2 = 1
        else:
            self.correct_2 = 0
        if self.Q3_choice == 3:
            self.correct_3 = 1
        else:
            self.correct_3 = 0
        if self.Q4_choice == 4:
            self.correct_4 = 1
        else:
            self.correct_4 = 0
        if self.Q5_choice == 3:
            self.correct_5 = 1
        else:
            self.correct_5 = 0
        self.correct = self.correct_1 + self.correct_2 + self.correct_3 + self.correct_4 + self.correct_5
        return self.correct


