from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
import itertools
import ast

class init_calc(WaitPage):
    def after_all_players_arrive(self):
        self.group.get_state()
        self.group.get_random_attributes()
        self.group.get_random_pay()

class Instructions_first(Page):
    def is_displayed(self):
        return self.round_number == 1


class Question(Page):
    timeout_seconds = Constants.time
    def is_displayed(self):
        return self.player.id_in_group == 2

#
# class Receiver_choice(Page):
#     form_model = 'group'
#     form_fields = ['random_first', 'random_second', 'random_third']
#
#
#     def random_first_choices(self):
#         return[[0, 'What is the background color of the first card?'], [1, 'What is the center shape of the first card?'], [2, 'What is the center letter of the first card?'],
#                [3,'What is the number of the first card?'], [4, 'What is the mathematical symbol of the first card?'],
#                [5, 'What is the background color of the second card?'], [6, 'What is the center shape of the second card?'], [7, 'What is the center letter of the second card?'],
#                [8, 'What is the number of the second card?'], [9, 'What is the mathematical symbol of the second card?'],
#                [10, 'What is the background color of the third card?'], [11, 'What is the center shape of the third card?'], [12, 'What is the center letter of the third card?'],
#                [13, 'What is the number of the third card?'], [14, 'What is the mathematical symbol of the third card?'],
#                [15, 'What is the background color of the fourth card?'], [16, 'What is the center shape of the fourth card?'], [17, 'What is the center letter of the fourth card?'],
#                [18, 'What is the number of the fourth card?'], [19, 'What is the mathematical symbol of the fourth card?'],]
#
#
#     def random_second_choices(self):
#         return[[0, 'What is the background color of the first card?'], [1, 'What is the center shape of the first card?'], [2, 'What is the center letter of the first card?'],
#                [3,'What is the number of the first card?'], [4, 'What is the mathematical symbol of the first card?'],
#                [5, 'What is the background color of the second card?'], [6, 'What is the center shape of the second card?'], [7, 'What is the center letter of the second card?'],
#                [8, 'What is the number of the second card?'], [9, 'What is the mathematical symbol of the second card?'],
#                [10, 'What is the background color of the third card?'], [11, 'What is the center shape of the third card?'], [12, 'What is the center letter of the third card?'],
#                [13, 'What is the number of the third card?'], [14, 'What is the mathematical symbol of the third card?'],
#                [15, 'What is the background color of the fourth card?'], [16, 'What is the center shape of the fourth card?'], [17, 'What is the center letter of the fourth card?'],
#                [18, 'What is the number of the fourth card?'], [19, 'What is the mathematical symbol of the fourth card?'],]
#
#
#     def random_third_choices(self):
#         return[[0, 'What is the background color of the first card?'], [1, 'What is the center shape of the first card?'], [2, 'What is the center letter of the first card?'],
#                [3,'What is the number of the first card?'], [4, 'What is the mathematical symbol of the first card?'],
#                [5, 'What is the background color of the second card?'], [6, 'What is the center shape of the second card?'], [7, 'What is the center letter of the second card?'],
#                [8, 'What is the number of the second card?'], [9, 'What is the mathematical symbol of the second card?'],
#                [10, 'What is the background color of the third card?'], [11, 'What is the center shape of the third card?'], [12, 'What is the center letter of the third card?'],
#                [13, 'What is the number of the third card?'], [14, 'What is the mathematical symbol of the third card?'],
#                [15, 'What is the background color of the fourth card?'], [16, 'What is the center shape of the fourth card?'], [17, 'What is the center letter of the fourth card?'],
#                [18, 'What is the number of the fourth card?'], [19, 'What is the mathematical symbol of the fourth card?'],]
#
#
#     def error_message(self, values):
#         print('values is', values)
#         if values['random_first'] == values['random_second'] or values['random_first'] == values['random_third'] or values['random_second'] == values['random_third']:
#             return 'You must choose three different questions to ask. '
#
#     def is_displayed(self):
#         return self.player.id_in_group == 2




class Instructions_second(Page):
    def is_displayed(self):
        return self.round_number == 1


class Observation(Page):
    timeout_seconds = Constants.time



class WaitforP2(WaitPage):
    wait_for_all_groups = True


class Payment(Page):
    pass

class Sender_report(Page):

    form_model = 'group'
    form_fields = ['message', 'report_first', 'report_second', 'report_third']


    def is_displayed(self):
        return self.player.id_in_group == 1



class WaitforP1(WaitPage):
    def after_all_players_arrive(self):
        self.group.get_correct_attributes()
        self.group.get_check_first()
        self.group.get_check_second()
        self.group.get_check_third()


class Receiver_guess(Page):

    form_model = 'group'
    form_fields = ['guess']


    def is_displayed(self):
        return self.player.id_in_group == 2

    def vars_for_template(self):
        message = self.group.message
        return{'message': message}


class Waitforall(WaitPage):

    def after_all_players_arrive(self):

        p1 = self.group.get_player_by_id(1)
        p2 = self.group.get_player_by_id(2)

        if self.group.random_pay == 0:
            if self.group.guess == 1:
                if self.group.true_state == 1:
                    p1.round_payoff = Constants.sender_payoffs_first[0]
                    p2.other_payoff = Constants.sender_payoffs_first[0]
                    p2.round_payoff = Constants.receiver_payoffs[0]
                    p1.other_payoff = Constants.receiver_payoffs[0]
                elif self.group.true_state == 2:
                    p1.round_payoff = Constants.sender_payoffs_first[0]
                    p2.other_payoff = Constants.sender_payoffs_first[0]
                    p2.round_payoff = Constants.receiver_payoffs[2]
                    p1.other_payoff = Constants.receiver_payoffs[2]
                else:
                    p1.round_payoff = Constants.sender_payoffs_first[0]
                    p2.other_payoff = Constants.sender_payoffs_first[0]
                    p2.round_payoff = Constants.receiver_payoffs[3]
                    p1.other_payoff = Constants.receiver_payoffs[3]
            elif self.group.guess == 2:
                if self.group.true_state == 1:
                    p1.round_payoff = Constants.sender_payoffs_first[1]
                    p2.other_payoff = Constants.sender_payoffs_first[1]
                    p2.round_payoff = Constants.receiver_payoffs[1]
                    p1.other_payoff = Constants.receiver_payoffs[1]
                elif self.group.true_state == 2:
                    p1.round_payoff = Constants.sender_payoffs_first[1]
                    p2.other_payoff = Constants.sender_payoffs_first[1]
                    p2.round_payoff = Constants.receiver_payoffs[0]
                    p1.other_payoff = Constants.receiver_payoffs[0]
                else:
                    p1.round_payoff = Constants.sender_payoffs_first[1]
                    p2.other_payoff = Constants.sender_payoffs_first[1]
                    p2.round_payoff = Constants.receiver_payoffs[2]
                    p1.other_payoff = Constants.receiver_payoffs[2]
            else:
                if self.group.true_state == 1:
                    p1.round_payoff = Constants.sender_payoffs_first[2]
                    p2.other_payoff = Constants.sender_payoffs_first[2]
                    p2.round_payoff = Constants.receiver_payoffs[3]
                    p1.other_payoff = Constants.receiver_payoffs[3]
                elif self.group.true_state == 2:
                    p1.round_payoff = Constants.sender_payoffs_first[2]
                    p2.other_payoff = Constants.sender_payoffs_first[2]
                    p2.round_payoff = Constants.receiver_payoffs[1]
                    p1.other_payoff = Constants.receiver_payoffs[1]
                else:
                    p1.round_payoff = Constants.sender_payoffs_first[2]
                    p2.other_payoff = Constants.sender_payoffs_first[2]
                    p2.round_payoff = Constants.receiver_payoffs[0]
                    p1.other_payoff = Constants.receiver_payoffs[0]

        else:
            if self.group.guess == 1:
                if self.group.true_state == 1:
                    p1.round_payoff = Constants.sender_payoffs_second[0]
                    p2.other_payoff = Constants.sender_payoffs_second[0]
                    p2.round_payoff = Constants.receiver_payoffs[0]
                    p1.other_payoff = Constants.receiver_payoffs[0]
                elif self.group.true_state == 2:
                    p1.round_payoff = Constants.sender_payoffs_second[0]
                    p2.other_payoff = Constants.sender_payoffs_second[0]
                    p2.round_payoff = Constants.receiver_payoffs[2]
                    p1.other_payoff = Constants.receiver_payoffs[2]
                else:
                    p1.round_payoff = Constants.sender_payoffs_second[0]
                    p2.other_payoff = Constants.sender_payoffs_second[0]
                    p2.round_payoff = Constants.receiver_payoffs[3]
                    p1.other_payoff = Constants.receiver_payoffs[3]
            elif self.group.guess == 2:
                if self.group.true_state == 1:
                    p1.round_payoff = Constants.sender_payoffs_second[1]
                    p2.other_payoff = Constants.sender_payoffs_second[1]
                    p2.round_payoff = Constants.receiver_payoffs[1]
                    p1.other_payoff = Constants.receiver_payoffs[1]
                elif self.group.true_state == 2:
                    p1.round_payoff = Constants.sender_payoffs_second[1]
                    p2.other_payoff = Constants.sender_payoffs_second[1]
                    p2.round_payoff = Constants.receiver_payoffs[0]
                    p1.other_payoff = Constants.receiver_payoffs[0]
                else:
                    p1.round_payoff = Constants.sender_payoffs_second[1]
                    p2.other_payoff = Constants.sender_payoffs_second[1]
                    p2.round_payoff = Constants.receiver_payoffs[2]
                    p1.other_payoff = Constants.receiver_payoffs[2]
            else:
                if self.group.true_state == 1:
                    p1.round_payoff = Constants.sender_payoffs_second[2]
                    p2.other_payoff = Constants.sender_payoffs_second[2]
                    p2.round_payoff = Constants.receiver_payoffs[3]
                    p1.other_payoff = Constants.receiver_payoffs[3]
                elif self.group.true_state == 2:
                    p1.round_payoff = Constants.sender_payoffs_second[2]
                    p2.other_payoff = Constants.sender_payoffs_second[2]
                    p2.round_payoff = Constants.receiver_payoffs[1]
                    p1.other_payoff = Constants.receiver_payoffs[1]
                else:
                    p1.round_payoff = Constants.sender_payoffs_second[2]
                    p2.other_payoff = Constants.sender_payoffs_second[2]
                    p2.round_payoff = Constants.receiver_payoffs[0]
                    p1.other_payoff = Constants.receiver_payoffs[0]

        for p in self.group.get_players():
            app1_list = p.participant.vars.get('app1_payoffs',[])
            app1_list.append(p.round_payoff)
            p.participant.vars['app1_payoffs'] = app1_list

        for p in self.group.get_players():
            if self.round_number == Constants.num_rounds:
                payoff_list = p.participant.vars.get('payoffs', [])
                app1_list = p.participant.vars.get('app1_payoffs', [])
                payoff_list.append(app1_list)
                p.participant.vars['payoffs'] = payoff_list


class Results(Page):
    def vars_for_template(self):
        round = self.round_number
        return{'round': round}



page_sequence = [init_calc, Instructions_first, Instructions_second, Question, Observation, WaitforP2, Payment, Sender_report, WaitforP1, Receiver_guess, Waitforall, Results]




