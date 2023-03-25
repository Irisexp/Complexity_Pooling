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

import random
import copy
import itertools

author = 'Junya Zhou'

doc = """
Complex Endogenous with assistance (New Payoff)
"""


class Constants(BaseConstants):

    name_in_url = 'Complex_EndoAD'
    players_per_group = 2
    num_rounds = 20
    time = 15

# if this number changes, the following dim_ report should also change

    initial_prior = 1/3
    sender_payoffs_first = [c(15), c(12), c(12)]
    sender_payoffs_second = [c(15), c(3), c(3)]
    receiver_payoffs = [c(15), c(12), c(8), c(3)]

class Subsession(BaseSubsession):


    def creating_session(self):
        self.group_randomly(fixed_id_in_group = True)
#set 1 2 3  Up Middle Down

        Up_first = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 7, 7, 8, 8, 12, 12, 10, 11, 11]

        Middle_first = [3, 3, 1, 1, 2, 5, 6, 6, 4, 4, 8, 8, 9, 9, 7, 10, 11, 12, 12, 10]

        Down_first = [2, 1, 3, 2, 1, 6, 5, 4, 6, 5, 9, 9, 8, 7, 9, 11, 10, 11, 10, 12]

        Up_second = [5, 6, 6, 5, 5, 8, 7, 9, 9, 8, 11, 10, 12, 12, 11, 3, 3, 2, 2, 1]

        Middle_second = [4, 5, 4, 4, 6, 9, 8, 8, 7, 7, 12, 12, 11, 10, 10, 2, 1, 1, 3, 3]

        Down_second = [6, 4, 5, 6, 4, 7, 9, 7, 8, 9, 10, 11, 10, 11, 12, 1, 2, 3, 1, 2]

        Up_third = [12, 10, 12, 11, 11, 2, 2, 3, 3, 1, 6, 5, 5, 6, 6, 9, 7, 8, 8, 9]

        Middle_third = [10, 12, 10, 10, 12, 1, 3, 2, 1, 3, 4, 4, 6, 5, 4, 7, 8, 7, 9, 8]

        Down_third = [11, 11, 11, 12, 10, 3, 1, 1, 2, 2, 5, 6, 4, 4, 5, 8, 9, 9, 7, 7]

#Middle, Down, Up

        Up_fourth = [3, 3, 1, 1, 2, 5, 6, 6, 4, 4, 8, 8, 9, 9, 7, 10, 11, 12, 12, 10]

        Middle_fourth = [2, 1, 3, 2, 1, 6, 5, 4, 6, 5, 9, 9, 8, 7, 9, 11, 10, 11, 10, 12]

        Down_fourth = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 7, 7, 8, 8, 12, 12, 10, 11, 11]

        Up_fifth = [4, 5, 4, 4, 6, 9, 8, 8, 7, 7, 12, 12, 11, 10, 10, 2, 1, 1, 3, 3]

        Middle_fifth = [6, 4, 5, 6, 4, 7, 9, 7, 8, 9, 10, 11, 10, 11, 12, 1, 2, 3, 1, 2]

        Down_fifth = [5, 6, 6, 5, 5, 8, 7, 9, 9, 8, 11, 10, 12, 12, 11, 3, 3, 2, 2, 1]

        Up_sixth = [10, 12, 10, 10, 12, 1, 3, 2, 1, 3, 4, 4, 6, 5, 4, 7, 8, 7, 9, 8]

        Middle_sixth = [11, 11, 11, 12, 10, 3, 1, 1, 2, 2, 5, 6, 4, 4, 5, 8, 9, 9, 7, 7]

        Down_sixth = [12, 10, 12, 11, 11, 2, 2, 3, 3, 1, 6, 5, 5, 6, 6, 9, 7, 8, 8, 9]

#Down Up Middle

        Up_seventh = [2, 1, 3, 2, 1, 6, 5, 4, 6, 5, 9, 9, 8, 7, 9, 11, 10, 11, 10, 12]

        Middle_seventh = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 7, 7, 8, 8, 12, 12, 10, 11, 11]

        Down_seventh = [3, 3, 1, 1, 2, 5, 6, 6, 4, 4, 8, 8, 9, 9, 7, 10, 11, 12, 12, 10]

        Up_eighth = [6, 4, 5, 6, 4, 7, 9, 7, 8, 9, 10, 11, 10, 11, 12, 1, 2, 3, 1, 2]

        Middle_eighth = [5, 6, 6, 5, 5, 8, 7, 9, 9, 8, 11, 10, 12, 12, 11, 3, 3, 2, 2, 1]

        Down_eighth = [4, 5, 4, 4, 6, 9, 8, 8, 7, 7, 12, 12, 11, 10, 10, 2, 1, 1, 3, 3]

        Up_ninth = [11, 11, 11, 12, 10, 3, 1, 1, 2, 2, 5, 6, 4, 4, 5, 8, 9, 9, 7, 7]

        Middle_ninth = [12, 10, 12, 11, 11, 2, 2, 3, 3, 1, 6, 5, 5, 6, 6, 9, 7, 8, 8, 9]

        Down_ninth = [10, 12, 10, 10, 12, 1, 3, 2, 1, 3, 4, 4, 6, 5, 4, 7, 8, 7, 9, 8]


#set 4 5, 6

        Up_tenth = [7, 7, 7, 8, 8, 12, 12, 10, 11, 11, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]

        Middle_tenth = [8, 8, 9, 9, 7, 10, 11, 12, 12, 10, 3, 3, 1, 1, 2, 5, 6, 6, 4, 4]

        Down_tenth = [9, 9, 8, 7, 9, 11, 10, 11, 10, 12, 2, 1, 3, 2, 1, 6, 5, 4, 6, 5]

        Up_eleventh = [3, 3, 2, 2, 1, 8, 7, 9, 9, 8, 11, 10, 12, 12, 11, 5, 6, 6, 5, 5]

        Middle_eleventh = [2, 1, 1, 3, 3, 9, 8, 8, 7, 7, 12, 12, 11, 10, 10, 4, 5, 4, 4, 6]

        Down_eleventh = [1, 2, 3, 1, 2, 7, 9, 7, 8, 9, 10, 11, 10, 11, 12, 6, 4, 5, 6, 4]

        Up_twelfth = [6, 5, 5, 6, 6, 2, 2, 3, 3, 1, 9, 7, 8, 8, 9, 12, 10, 12, 11, 11]

        Middle_twelfth = [4, 4, 6, 5, 4, 1, 3, 2, 1, 3, 7, 8, 7, 9, 8, 10, 12, 10, 10, 12]

        Down_twelfth = [5, 6, 4, 4, 5, 3, 1, 1, 2, 2, 8, 9, 9, 7, 7, 11, 11, 11, 12, 10]

#Middle Down Up

        Up_thirteenth = [8, 8, 9, 9, 7, 10, 11, 12, 12, 10, 3, 3, 1, 1, 2, 5, 6, 6, 4, 4]

        Middle_thirteenth = [9, 9, 8, 7, 9, 11, 10, 11, 10, 12, 2, 1, 3, 2, 1, 6, 5, 4, 6, 5]

        Down_thirteenth = [7, 7, 7, 8, 8, 12, 12, 10, 11, 11, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]

        Up_fourteenth = [2, 1, 1, 3, 3, 9, 8, 8, 7, 7, 12, 12, 11, 10, 10, 4, 5, 4, 4, 6]

        Middle_fourteenth = [1, 2, 3, 1, 2, 7, 9, 7, 8, 9, 10, 11, 10, 11, 12, 6, 4, 5, 6, 4]

        Down_fourteenth = [3, 3, 2, 2, 1, 8, 7, 9, 9, 8, 11, 10, 12, 12, 11, 5, 6, 6, 5, 5]

        Up_fifteenth = [4, 4, 6, 5, 4, 1, 3, 2, 1, 3, 7, 8, 7, 9, 8, 10, 12, 10, 10, 12]

        Middle_fifteenth = [5, 6, 4, 4, 5, 3, 1, 1, 2, 2, 8, 9, 9, 7, 7, 11, 11, 11, 12, 10]

        Down_fifteenth = [6, 5, 5, 6, 6, 2, 2, 3, 3, 1, 9, 7, 8, 8, 9, 12, 10, 12, 11, 11]


#Down Up Middle

        Up_sixteenth = [9, 9, 8, 7, 9, 11, 10, 11, 10, 12, 2, 1, 3, 2, 1, 6, 5, 4, 6, 5]

        Middle_sixteenth = [7, 7, 7, 8, 8, 12, 12, 10, 11, 11, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]

        Down_sixteenth = [8, 8, 9, 9, 7, 10, 11, 12, 12, 10, 3, 3, 1, 1, 2, 5, 6, 6, 4, 4]

        Up_seventeenth =  [1, 2, 3, 1, 2, 7, 9, 7, 8, 9, 10, 11, 10, 11, 12, 6, 4, 5, 6, 4]

        Middle_seventeenth = [3, 3, 2, 2, 1, 8, 7, 9, 9, 8, 11, 10, 12, 12, 11, 5, 6, 6, 5, 5]

        Down_seventeenth = [2, 1, 1, 3, 3, 9, 8, 8, 7, 7, 12, 12, 11, 10, 10, 4, 5, 4, 4, 6]

        Up_eighteenth = [5, 6, 4, 4, 5, 3, 1, 1, 2, 2, 8, 9, 9, 7, 7, 11, 11, 11, 12, 10]

        Middle_eighteenth = [6, 5, 5, 6, 6, 2, 2, 3, 3, 1, 9, 7, 8, 8, 9, 12, 10, 12, 11, 11]

        Down_eighteenth = [4, 4, 6, 5, 4, 1, 3, 2, 1, 3, 7, 8, 7, 9, 8, 10, 12, 10, 10, 12]

        Up_nineteenth = [7, 7, 7, 8, 8, 4, 4, 5, 5, 6, 1, 2, 2, 3, 3, 12, 12, 10, 11, 11]

        Middle_nineteenth = [8, 8, 9, 9, 7, 5, 6, 6, 4, 4, 3, 3, 1, 1, 2, 10, 11, 12, 12, 10]

        Down_nineteenth = [9, 9, 8, 7, 9, 6, 5, 4, 6, 5, 2, 1, 3, 2, 1, 11, 10, 11, 10, 12]

        Up_twentieth = [8, 8, 9, 9, 7, 5, 6, 6, 4, 4, 3, 3, 1, 1, 2, 10, 11, 12, 12, 10]

        Middle_twentieth = [9, 9, 8, 7, 9, 6, 5, 4, 6, 5, 2, 1, 3, 2, 1, 11, 10, 11, 10, 12]

        Down_twentieth =  [7, 7, 7, 8, 8, 4, 4, 5, 5, 6, 1, 2, 2, 3, 3, 12, 12, 10, 11, 11]


        self.session.vars['Up'] = [Up_first, Up_second, Up_third, Up_fourth, Up_fifth, Up_sixth, Up_seventh, Up_eighth, Up_ninth, Up_tenth, Up_eleventh, Up_twelfth, Up_thirteenth, Up_fourteenth, Up_fifteenth, Up_sixteenth, Up_seventeenth, Up_eighteenth, Up_nineteenth, Up_twentieth]
        self.session.vars['Middle'] = [Middle_first, Middle_second, Middle_third, Middle_fourth, Middle_fifth, Middle_sixth, Middle_seventh, Middle_eighth, Middle_ninth, Middle_tenth, Middle_eleventh, Middle_twelfth, Middle_thirteenth, Middle_fourteenth, Middle_fifteenth, Middle_sixteenth, Middle_seventeenth, Middle_eighteenth, Middle_nineteenth, Middle_twentieth]
        self.session.vars['Down'] = [Down_first, Down_second, Down_third, Down_fourth, Down_fifth, Down_sixth, Down_seventh, Down_eighth, Down_ninth, Down_tenth, Down_eleventh, Down_twelfth, Down_thirteenth, Down_fourteenth, Down_fifteenth, Down_sixteenth, Down_seventeenth, Down_eighteenth, Down_nineteenth, Down_twentieth]


class Group(BaseGroup):

    true_state = models.IntegerField(label="")

    profile_num = models.IntegerField(label="")

    random_first = models.IntegerField(label="The first question is:")

    random_second = models.IntegerField(label="The second question is:")

    random_third = models.IntegerField(label="The third question is:")

    attribute_first = models.IntegerField(label="")

    attribute_second = models.IntegerField(label="")

    attribute_third = models.IntegerField(label="")

    report_first = models.IntegerField(label="")

    report_second = models.IntegerField(label="")

    report_third = models.IntegerField(label="")

    message = models.IntegerField(label="")

    guess = models.IntegerField(label="")

    check_first = models.IntegerField(label="")

    check_second = models.IntegerField(label="")

    check_third = models.IntegerField(label="")

    random_pay = models.IntegerField(label="")



    def report_first_choices(self):
        if self.random_first == 0:
            return [[1, 'White'], [2, 'Orange'], [3, 'Grey'], [4, 'Purple'], [5, 'Red'], [6, 'Blue'], [7, 'Pink'],
                    [8, 'Yellow'], [9, 'Green'], [10, 'Maroon'], [11, 'Black'], [12, 'Navy']]
        elif self.random_first == 1:
            return [[1, 'Square'], [2, 'Round'], [3, 'Triangle'], [4, 'Heart'], [5, 'Parallelogram'], [6, 'Cross'],
                    [7, 'Pentagon'], [8, 'Diamond'], [9, 'Star'], [10, 'Drop'], [11, 'Moon'], [12, 'Cubic']]
        elif self.random_first == 2:
            return [[1, 'B'], [2, 'F'], [3, 'J'], [4, 'D'], [5, 'G'], [6, 'M'], [7, 'E'], [8, 'L'], [9, 'K'], [10, 'A'],
                    [11, 'H'], [12, 'P']]
        elif self.random_first == 3:
            return [[1, '2'], [2, '11'], [3, '18'], [4, '6'], [5, '9'], [6, '15'], [7, '8'], [8, '13'], [9, '19'],
                    [10, '7'], [11, '12'], [12, '16']]
        elif self.random_first == 4:
            return [[1, '\u002B'], [2, '\u2212'], [3, '\u00D7'], [4, '\u003C'], [5, '\u003E'], [6, '\u003D'],
                    [7, '\u221A'], [8, '\u0025'], [9, '\u00F7'], [10, '\u2229'], [11, '\u2205'], [12, '\u221E']]
        elif self.random_first == 5:
            return [[1, 'White'], [2, 'Orange'], [3, 'Grey'], [4, 'Purple'], [5, 'Red'], [6, 'Blue'], [7, 'Pink'],
                    [8, 'Yellow'], [9, 'Green'], [10, 'Maroon'], [11, 'Black'], [12, 'Navy']]
        elif self.random_first == 6:
            return [[1, 'Square'], [2, 'Round'], [3, 'Triangle'], [4, 'Heart'], [5, 'Parallelogram'], [6, 'Cross'],
                    [7, 'Pentagon'], [8, 'Diamond'], [9, 'Star'], [10, 'Drop'], [11, 'Moon'], [12, 'Cubic']]
        elif self.random_first == 7:
            return [[1, 'B'], [2, 'F'], [3, 'J'], [4, 'D'], [5, 'G'], [6, 'M'], [7, 'E'], [8, 'L'], [9, 'K'], [10, 'A'],
                    [11, 'H'], [12, 'P']]
        elif self.random_first == 8:
            return [[1, '2'], [2, '11'], [3, '18'], [4, '6'], [5, '9'], [6, '15'], [7, '8'], [8, '13'], [9, '19'],
                    [10, '7'], [11, '12'], [12, '16']]
        elif self.random_first == 9:
            return [[1, '\u002B'], [2, '\u2212'], [3, '\u00D7'], [4, '\u003C'], [5, '\u003E'], [6, '\u003D'],
                    [7, '\u221A'], [8, '\u0025'], [9, '\u00F7'], [10, '\u2229'], [11, '\u2205'], [12, '\u221E']]
        elif self.random_first == 10:
            return [[1, 'White'], [2, 'Orange'], [3, 'Grey'], [4, 'Purple'], [5, 'Red'], [6, 'Blue'], [7, 'Pink'],
                    [8, 'Yellow'], [9, 'Green'], [10, 'Maroon'], [11, 'Black'], [12, 'Navy']]
        elif self.random_first == 11:
            return [[1, 'Square'], [2, 'Round'], [3, 'Triangle'], [4, 'Heart'], [5, 'Parallelogram'], [6, 'Cross'],
                    [7, 'Pentagon'], [8, 'Diamond'], [9, 'Star'], [10, 'Drop'], [11, 'Moon'], [12, 'Cubic']]
        elif self.random_first == 12:
            return [[1, 'B'], [2, 'F'], [3, 'J'], [4, 'D'], [5, 'G'], [6, 'M'], [7, 'E'], [8, 'L'], [9, 'K'], [10, 'A'],
                    [11, 'H'], [12, 'P']]
        elif self.random_first == 13:
            return [[1, '2'], [2, '11'], [3, '18'], [4, '6'], [5, '9'], [6, '15'], [7, '8'], [8, '13'], [9, '19'],
                    [10, '7'], [11, '12'], [12, '16']]
        elif self.random_first == 14:
            return [[1, '\u002B'], [2, '\u2212'], [3, '\u00D7'], [4, '\u003C'], [5, '\u003E'], [6, '\u003D'],
                    [7, '\u221A'], [8, '\u0025'], [9, '\u00F7'], [10, '\u2229'], [11, '\u2205'], [12, '\u221E']]
        elif self.random_first == 15:
            return [[1, 'White'], [2, 'Orange'], [3, 'Grey'], [4, 'Purple'], [5, 'Red'], [6, 'Blue'], [7, 'Pink'],
                    [8, 'Yellow'], [9, 'Green'], [10, 'Maroon'], [11, 'Black'], [12, 'Navy']]
        elif self.random_first == 16:
            return [[1, 'Square'], [2, 'Round'], [3, 'Triangle'], [4, 'Heart'], [5, 'Parallelogram'], [6, 'Cross'],
                    [7, 'Pentagon'], [8, 'Diamond'], [9, 'Star'], [10, 'Drop'], [11, 'Moon'], [12, 'Cubic']]
        elif self.random_first == 17:
            return [[1, 'B'], [2, 'F'], [3, 'J'], [4, 'D'], [5, 'G'], [6, 'M'], [7, 'E'], [8, 'L'], [9, 'K'], [10, 'A'],
                    [11, 'H'], [12, 'P']]
        elif self.random_first == 18:
            return [[1, '2'], [2, '11'], [3, '18'], [4, '6'], [5, '9'], [6, '15'], [7, '8'], [8, '13'], [9, '19'],
                    [10, '7'], [11, '12'], [12, '16']]
        elif self.random_first == 19:
            return [[1, '\u002B'], [2, '\u2212'], [3, '\u00D7'], [4, '\u003C'], [5, '\u003E'], [6, '\u003D'],
                    [7, '\u221A'], [8, '\u0025'], [9, '\u00F7'], [10, '\u2229'], [11, '\u2205'], [12, '\u221E']]

    def report_second_choices(self):
        if self.random_second == 0:
            return [[1, 'White'], [2, 'Orange'], [3, 'Grey'], [4, 'Purple'], [5, 'Red'], [6, 'Blue'], [7, 'Pink'],
                    [8, 'Yellow'], [9, 'Green'], [10, 'Maroon'], [11, 'Black'], [12, 'Navy']]
        elif self.random_second == 1:
            return [[1, 'Square'], [2, 'Round'], [3, 'Triangle'], [4, 'Heart'], [5, 'Parallelogram'], [6, 'Cross'],
                    [7, 'Pentagon'], [8, 'Diamond'], [9, 'Star'], [10, 'Drop'], [11, 'Moon'], [12, 'Cubic']]
        elif self.random_second == 2:
            return [[1, 'B'], [2, 'F'], [3, 'J'], [4, 'D'], [5, 'G'], [6, 'M'], [7, 'E'], [8, 'L'], [9, 'K'], [10, 'A'],
                    [11, 'H'], [12, 'P']]
        elif self.random_second == 3:
            return [[1, '2'], [2, '11'], [3, '18'], [4, '6'], [5, '9'], [6, '15'], [7, '8'], [8, '13'], [9, '19'],
                    [10, '7'], [11, '12'], [12, '16']]
        elif self.random_second == 4:
            return [[1, '\u002B'], [2, '\u2212'], [3, '\u00D7'], [4, '\u003C'], [5, '\u003E'], [6, '\u003D'],
                    [7, '\u221A'], [8, '\u0025'], [9, '\u00F7'], [10, '\u2229'], [11, '\u2205'], [12, '\u221E']]
        elif self.random_second == 5:
            return [[1, 'White'], [2, 'Orange'], [3, 'Grey'], [4, 'Purple'], [5, 'Red'], [6, 'Blue'], [7, 'Pink'],
                    [8, 'Yellow'], [9, 'Green'], [10, 'Maroon'], [11, 'Black'], [12, 'Navy']]
        elif self.random_second == 6:
            return [[1, 'Square'], [2, 'Round'], [3, 'Triangle'], [4, 'Heart'], [5, 'Parallelogram'], [6, 'Cross'],
                    [7, 'Pentagon'], [8, 'Diamond'], [9, 'Star'], [10, 'Drop'], [11, 'Moon'], [12, 'Cubic']]
        elif self.random_second == 7:
            return [[1, 'B'], [2, 'F'], [3, 'J'], [4, 'D'], [5, 'G'], [6, 'M'], [7, 'E'], [8, 'L'], [9, 'K'], [10, 'A'],
                    [11, 'H'], [12, 'P']]
        elif self.random_second == 8:
            return [[1, '2'], [2, '11'], [3, '18'], [4, '6'], [5, '9'], [6, '15'], [7, '8'], [8, '13'], [9, '19'],
                    [10, '7'], [11, '12'], [12, '16']]
        elif self.random_second == 9:
            return [[1, '\u002B'], [2, '\u2212'], [3, '\u00D7'], [4, '\u003C'], [5, '\u003E'], [6, '\u003D'],
                    [7, '\u221A'], [8, '\u0025'], [9, '\u00F7'], [10, '\u2229'], [11, '\u2205'], [12, '\u221E']]
        elif self.random_second == 10:
            return [[1, 'White'], [2, 'Orange'], [3, 'Grey'], [4, 'Purple'], [5, 'Red'], [6, 'Blue'], [7, 'Pink'],
                    [8, 'Yellow'], [9, 'Green'], [10, 'Maroon'], [11, 'Black'], [12, 'Navy']]
        elif self.random_second == 11:
            return [[1, 'Square'], [2, 'Round'], [3, 'Triangle'], [4, 'Heart'], [5, 'Parallelogram'], [6, 'Cross'],
                    [7, 'Pentagon'], [8, 'Diamond'], [9, 'Star'], [10, 'Drop'], [11, 'Moon'], [12, 'Cubic']]
        elif self.random_second == 12:
            return [[1, 'B'], [2, 'F'], [3, 'J'], [4, 'D'], [5, 'G'], [6, 'M'], [7, 'E'], [8, 'L'], [9, 'K'], [10, 'A'],
                    [11, 'H'], [12, 'P']]
        elif self.random_second == 13:
            return [[1, '2'], [2, '11'], [3, '18'], [4, '6'], [5, '9'], [6, '15'], [7, '8'], [8, '13'], [9, '19'],
                    [10, '7'], [11, '12'], [12, '16']]
        elif self.random_second == 14:
            return [[1, '\u002B'], [2, '\u2212'], [3, '\u00D7'], [4, '\u003C'], [5, '\u003E'], [6, '\u003D'],
                    [7, '\u221A'], [8, '\u0025'], [9, '\u00F7'], [10, '\u2229'], [11, '\u2205'], [12, '\u221E']]
        elif self.random_second == 15:
            return [[1, 'White'], [2, 'Orange'], [3, 'Grey'], [4, 'Purple'], [5, 'Red'], [6, 'Blue'], [7, 'Pink'],
                    [8, 'Yellow'], [9, 'Green'], [10, 'Maroon'], [11, 'Black'], [12, 'Navy']]
        elif self.random_second == 16:
            return [[1, 'Square'], [2, 'Round'], [3, 'Triangle'], [4, 'Heart'], [5, 'Parallelogram'], [6, 'Cross'],
                    [7, 'Pentagon'], [8, 'Diamond'], [9, 'Star'], [10, 'Drop'], [11, 'Moon'], [12, 'Cubic']]
        elif self.random_second == 17:
            return [[1, 'B'], [2, 'F'], [3, 'J'], [4, 'D'], [5, 'G'], [6, 'M'], [7, 'E'], [8, 'L'], [9, 'K'], [10, 'A'],
                    [11, 'H'], [12, 'P']]
        elif self.random_second == 18:
            return [[1, '2'], [2, '11'], [3, '18'], [4, '6'], [5, '9'], [6, '15'], [7, '8'], [8, '13'], [9, '19'],
                    [10, '7'], [11, '12'], [12, '16']]
        elif self.random_second == 19:
            return [[1, '\u002B'], [2, '\u2212'], [3, '\u00D7'], [4, '\u003C'], [5, '\u003E'], [6, '\u003D'],
                    [7, '\u221A'], [8, '\u0025'], [9, '\u00F7'], [10, '\u2229'], [11, '\u2205'], [12, '\u221E']]

    def report_third_choices(self):
        if self.random_third == 0:
            return [[1, 'White'], [2, 'Orange'], [3, 'Grey'], [4, 'Purple'], [5, 'Red'], [6, 'Blue'], [7, 'Pink'],
                    [8, 'Yellow'], [9, 'Green'], [10, 'Maroon'], [11, 'Black'], [12, 'Navy']]
        elif self.random_third == 1:
            return [[1, 'Square'], [2, 'Round'], [3, 'Triangle'], [4, 'Heart'], [5, 'Parallelogram'], [6, 'Cross'],
                    [7, 'Pentagon'], [8, 'Diamond'], [9, 'Star'], [10, 'Drop'], [11, 'Moon'], [12, 'Cubic']]
        elif self.random_third == 2:
            return [[1, 'B'], [2, 'F'], [3, 'J'], [4, 'D'], [5, 'G'], [6, 'M'], [7, 'E'], [8, 'L'], [9, 'K'], [10, 'A'],
                    [11, 'H'], [12, 'P']]
        elif self.random_third == 3:
            return [[1, '2'], [2, '11'], [3, '18'], [4, '6'], [5, '9'], [6, '15'], [7, '8'], [8, '13'], [9, '19'],
                    [10, '7'], [11, '12'], [12, '16']]
        elif self.random_third == 4:
            return [[1, '\u002B'], [2, '\u2212'], [3, '\u00D7'], [4, '\u003C'], [5, '\u003E'], [6, '\u003D'],
                    [7, '\u221A'], [8, '\u0025'], [9, '\u00F7'], [10, '\u2229'], [11, '\u2205'], [12, '\u221E']]
        elif self.random_third == 5:
            return [[1, 'White'], [2, 'Orange'], [3, 'Grey'], [4, 'Purple'], [5, 'Red'], [6, 'Blue'], [7, 'Pink'],
                    [8, 'Yellow'], [9, 'Green'], [10, 'Maroon'], [11, 'Black'], [12, 'Navy']]
        elif self.random_third == 6:
            return [[1, 'Square'], [2, 'Round'], [3, 'Triangle'], [4, 'Heart'], [5, 'Parallelogram'], [6, 'Cross'],
                    [7, 'Pentagon'], [8, 'Diamond'], [9, 'Star'], [10, 'Drop'], [11, 'Moon'], [12, 'Cubic']]
        elif self.random_third == 7:
            return [[1, 'B'], [2, 'F'], [3, 'J'], [4, 'D'], [5, 'G'], [6, 'M'], [7, 'E'], [8, 'L'], [9, 'K'], [10, 'A'],
                    [11, 'H'], [12, 'P']]
        elif self.random_third == 8:
            return [[1, '2'], [2, '11'], [3, '18'], [4, '6'], [5, '9'], [6, '15'], [7, '8'], [8, '13'], [9, '19'],
                    [10, '7'], [11, '12'], [12, '16']]
        elif self.random_third == 9:
            return [[1, '\u002B'], [2, '\u2212'], [3, '\u00D7'], [4, '\u003C'], [5, '\u003E'], [6, '\u003D'],
                    [7, '\u221A'], [8, '\u0025'], [9, '\u00F7'], [10, '\u2229'], [11, '\u2205'], [12, '\u221E']]
        elif self.random_third == 10:
            return [[1, 'White'], [2, 'Orange'], [3, 'Grey'], [4, 'Purple'], [5, 'Red'], [6, 'Blue'], [7, 'Pink'],
                    [8, 'Yellow'], [9, 'Green'], [10, 'Maroon'], [11, 'Black'], [12, 'Navy']]
        elif self.random_third == 11:
            return [[1, 'Square'], [2, 'Round'], [3, 'Triangle'], [4, 'Heart'], [5, 'Parallelogram'], [6, 'Cross'],
                    [7, 'Pentagon'], [8, 'Diamond'], [9, 'Star'], [10, 'Drop'], [11, 'Moon'], [12, 'Cubic']]
        elif self.random_third == 12:
            return [[1, 'B'], [2, 'F'], [3, 'J'], [4, 'D'], [5, 'G'], [6, 'M'], [7, 'E'], [8, 'L'], [9, 'K'], [10, 'A'],
                    [11, 'H'], [12, 'P']]
        elif self.random_third == 13:
            return [[1, '2'], [2, '11'], [3, '18'], [4, '6'], [5, '9'], [6, '15'], [7, '8'], [8, '13'], [9, '19'],
                    [10, '7'], [11, '12'], [12, '16']]
        elif self.random_third == 14:
            return [[1, '\u002B'], [2, '\u2212'], [3, '\u00D7'], [4, '\u003C'], [5, '\u003E'], [6, '\u003D'],
                    [7, '\u221A'], [8, '\u0025'], [9, '\u00F7'], [10, '\u2229'], [11, '\u2205'], [12, '\u221E']]
        elif self.random_third == 15:
            return [[1, 'White'], [2, 'Orange'], [3, 'Grey'], [4, 'Purple'], [5, 'Red'], [6, 'Blue'], [7, 'Pink'],
                    [8, 'Yellow'], [9, 'Green'], [10, 'Maroon'], [11, 'Black'], [12, 'Navy']]
        elif self.random_third == 16:
            return [[1, 'Square'], [2, 'Round'], [3, 'Triangle'], [4, 'Heart'], [5, 'Parallelogram'], [6, 'Cross'],
                    [7, 'Pentagon'], [8, 'Diamond'], [9, 'Star'], [10, 'Drop'], [11, 'Moon'], [12, 'Cubic']]
        elif self.random_third == 17:
            return [[1, 'B'], [2, 'F'], [3, 'J'], [4, 'D'], [5, 'G'], [6, 'M'], [7, 'E'], [8, 'L'], [9, 'K'], [10, 'A'],
                    [11, 'H'], [12, 'P']]
        elif self.random_third == 18:
            return [[1, '2'], [2, '11'], [3, '18'], [4, '6'], [5, '9'], [6, '15'], [7, '8'], [8, '13'], [9, '19'],
                    [10, '7'], [11, '12'], [12, '16']]
        elif self.random_third == 19:
            return [[1, '\u002B'], [2, '\u2212'], [3, '\u00D7'], [4, '\u003C'], [5, '\u003E'], [6, '\u003D'],
                    [7, '\u221A'], [8, '\u0025'], [9, '\u00F7'], [10, '\u2229'], [11, '\u2205'], [12, '\u221E']]

    def message_choices(self):
        return [[1, 'Up'], [2, 'Middle'], [3, 'Down']]


    def guess_choices(self):
        return[[1, 'Up'], [2, 'Middle'], [3, 'Down']]


    def get_state(self):
        self.true_state = random.choices([1, 2, 3], weights = [Constants.initial_prior, Constants.initial_prior, Constants.initial_prior])[0]
        print(self.true_state)
        return self.true_state


    def get_random_attributes(self):
        list = range(20)
        random_list = [
            list[i] for i in sorted(random.sample(range(len(list)), 3))
        ]
        print(random_list)
        # self.participant.vars['random_list'] = random_list
        self.random_first = random_list[0]
        self.random_second = random_list[1]
        self.random_third = random_list[2]


    def get_correct_attributes(self):
        # print(self.session.vars['Up'])
        # print(self.session.vars['Middle'])
        # print(self.session.vars['Down'])
        if self.message == 1:
            self.attribute_first =  self.session.vars['Up'][self.round_number - 1][self.random_first]
            self.attribute_second =  self.session.vars['Up'][self.round_number - 1][self.random_second]
            self.attribute_third =  self.session.vars['Up'][self.round_number - 1][self.random_third]
        elif self.message == 2:
            self.attribute_first = self.session.vars['Middle'][self.round_number - 1][self.random_first]
            self.attribute_second = self.session.vars['Middle'][self.round_number - 1][self.random_second]
            self.attribute_third = self.session.vars['Middle'][self.round_number - 1][self.random_third]
        else:
            self.attribute_first =  self.session.vars['Down'][self.round_number - 1][self.random_first]
            self.attribute_second =  self.session.vars['Down'][self.round_number - 1][self.random_second]
            self.attribute_third =  self.session.vars['Down'][self.round_number - 1][self.random_third]
        print(self.attribute_first)
        print(self.attribute_second)
        print(self.attribute_third)
        return self.attribute_first, self.attribute_second, self.attribute_third


    def get_random_pay(self):
        self.random_pay = random.choices([0, 1], weights=[1/2, 1/2])[0]


    def get_check_first(self):
        if self.attribute_first == self.report_first:
            self.check_first = 1
        else:
            self.check_first = 0
        print(self.random_first)
        print(self.attribute_first)
        print(self.report_first)
        print(self.check_first)
        return self.check_first


    def get_check_second(self):
        if self.attribute_second == self.report_second:
            self.check_second = 1
        else:
            self.check_second = 0
        print(self.random_second)
        print(self.attribute_second)
        print(self.report_second)
        print(self.check_second)
        print(self.check_second)
        return self.check_second


    def get_check_third(self):
        if self.attribute_third == self.report_third:
            self.check_third = 1
        else:
            self.check_third = 0
        print(self.random_third)
        print(self.attribute_third)
        print(self.report_third)
        print(self.check_third)
        print(self.check_third)
        return self.check_third




#when the final set is decided, add a function to examine whether the sender is truthfully reporting.

class Player(BasePlayer):

    round_payoff = models.CurrencyField()

    other_payoff = models.CurrencyField()


    def role(self):
        if self.id_in_group == 1:
            return 'Sender'
        else:
            return 'Receiver'

