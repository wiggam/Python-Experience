""" See https://www.youtube.com/watch?v=Vf9Yh9BuN-w&t=4s&ab_channel=GeorgeWiggam for a video on how to use the program and a walkthrough of the code """


import tkinter
from tkinter import Tk


class CardCounter(Tk):

    def __init__(self):
        super().__init__()
        # instance variables used in the class methods
        self.deck = {}
        self.cards_remaining = []
        self.probability = 0

        # configure the root window
        self.title("Card Counter")
        self.geometry("460x325")
        self.resizable(False, False)
        self.configure(background='grey')
        self.main_frame = tkinter.Frame(self, relief='sunken', borderwidth=2, background='grey')
        self.main_frame.grid(row=0, column=0, padx=8, pady=8, sticky='nsew')

        # number of decks text
        tkinter.Label(self.main_frame, text="Number of Decks:", background='grey', fg='white')\
            .grid(row=1, column=1, sticky='nw', padx=5, pady=5)

        # number of decks entry
        self.num_decks = tkinter.IntVar()
        deck_entry = tkinter.Entry(self.main_frame, textvariable=self.num_decks)
        deck_entry.grid(row=1, column=2, sticky='ne', pady=5)

        # number of deck button
        deck_button = tkinter.Button(self.main_frame, text='Enter', command=self.create_deck)
        deck_button.grid(row=1, column=3, sticky='nw', padx=5, pady=5)

        # number of decks result label
        self.deck_result_label = tkinter.Label(self.main_frame, background='grey', fg='#5bfba3')
        self.deck_result_label.grid(row=2, column=1, sticky='nw', columnspan=2, padx=5)

        # remove cards text
        tkinter.Label(self.main_frame, text="Remove Card:", background='grey', fg='white')\
            .grid(row=3, column=1, sticky='nw', padx=5)
        tkinter.Label(self.main_frame, text="Value (A, K, 7, 4):", background='grey', fg='white')\
            .grid(row=4, column=1, sticky='e', padx=2)
        tkinter.Label(self.main_frame, text="Suite (H, D, S, C):", background='grey', fg='white')\
            .grid(row=5, column=1, sticky='e', padx=2)

        # remove cards entry
        self.face = tkinter.StringVar()
        face_entry = tkinter.Entry(self.main_frame, textvariable=self.face)
        face_entry.grid(row=4, column=2, sticky='ne')
        self.suite = tkinter.StringVar()
        suite_entry = tkinter.Entry(self.main_frame, textvariable=self.suite)
        suite_entry.grid(row=5, column=2, sticky='ne')

        # remove cards button
        face_button = tkinter.Button(self.main_frame, text='Remove Card', command=self.remove_card)
        face_button.grid(row=5, column=3, sticky='nw', padx=5)

        # remove cards result label
        self.card_result_label1 = tkinter.Label(self.main_frame, background='grey', fg='#5bfba3')
        self.card_result_label1.grid(row=6, column=1, sticky='nw')
        self.card_result_label2 = tkinter.Label(self.main_frame, background='grey', fg='#fda1a1')
        self.card_result_label2.grid(row=6, column=2, sticky='nw')

        # target cards text
        tkinter.Label(self.main_frame, text="Target Cards (234):", background='grey', fg='white')\
            .grid(row=7, column=1, sticky='nw', padx=5)

        # target cards entry
        self.selected_cards = tkinter.StringVar()
        target_entry = tkinter.Entry(self.main_frame, textvariable=self.selected_cards)
        target_entry.grid(row=7, column=2, sticky='ne')

        # target cards button
        target_button = tkinter.Button(self.main_frame, text='Enter', command=self.count_selected)
        target_button.grid(row=7, column=3, sticky='nw', padx=5)

        # target cards result label
        self.target_card_result = tkinter.Label(self.main_frame, background='grey', fg='white')
        self.target_card_result.grid(row=8, column=1, sticky='nw', columnspan=3)

        # remaining cards label and result
        tkinter.Label(self.main_frame, text="Remaining Cards:", background='grey', fg='white')\
            .grid(row=1, column=4, sticky='nw', padx=5)
        self.remaining_probability_label = tkinter.Label(self.main_frame, background='grey', fg='white')
        self.remaining_probability_label.grid(row=2, column=4, rowspan=8, sticky='ne', padx=5)

        # reset button
        reset_button = tkinter.Button(self.main_frame, text='Reset', command=self.reset_deck)
        reset_button.grid(row=10, column=4, sticky='se', pady=5, padx=5)

        # blank row in order to help with sizing of remaining cards message (long vertical message)
        tkinter.Label(self.main_frame, background='grey', fg='white', pady=30).grid(row=9, column=4, sticky='e')

        # count suites label and results
        tkinter.Label(self.main_frame, text="Remaining Suites:", background='grey', fg='white')\
            .grid(row=9, column=1, sticky='sw', padx=5)
        self.remaining_suites_label = tkinter.Label(self.main_frame, background='grey', fg='white')
        self.remaining_suites_label.grid(row=10, column=1, columnspan=2, sticky='nw', padx=5)

    def create_deck(self):
        """Updates deck to match the number of decks being used"""
        card_deck = {
            "H": ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"],
            "D": ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"],
            "C": ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"],
            "S": ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"],
        }
        suit_list = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
        new_suit_list = []

        # creates the duplicates of the cards
        for x in suit_list:
            for _ in range(self.num_decks.get()):
                new_suit_list.append(x)

        # updates the card_deck, MUST USE COPY SO DICT VALUES DO NOT SHARE SAME ID
        for suite in card_deck:
            card_deck[suite] = new_suit_list.copy()
        self.deck = card_deck

        # return text to show user deck has been updated
        return_text = "Updated with {} decks".format(self.num_decks.get())
        self.deck_result_label.config(text=return_text)

        # create a list of all the cards (regardless of suit)
        for suite in self.deck:
            for cards in self.deck[suite]:
                self.cards_remaining.append(cards)

        # count the number of suites
        self.count_suites()
        self.count_cards()

    def count_cards(self):
        """Counts the remaining cards and give the probability of receiving each card"""
        # fills an empty dictionary with the results
        face_list = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
        all_card_prob = {}
        for card in face_list:
            all_card_prob[card] = "{}, {:.2f}%".format(self.cards_remaining.count(card),
                                                       self.cards_remaining.count(card) /
                                                       len(self.cards_remaining) * 100)

        # Translate the dictionary into a string so that it is printable
        printable_results = f"{len(self.cards_remaining)}\n"
        for key in all_card_prob:
            printable_results += f"{key}: {all_card_prob[key]}\n"

        self.remaining_probability_label.config(text=printable_results)

    def count_suites(self):
        """Counts the number of cards left in each suite"""
        suite_prob = {}
        for suite in self.deck:
            suite_prob[suite] = "{}".format(len(self.deck[suite]))

        # Translate the dictionary into a string so that it is printable, splits the string so that 2 suites
        # go on each line, red and black
        printable_results = ""
        new_line = 0
        for suite in suite_prob:
            if new_line != 1:
                printable_results += f"{suite}: {suite_prob[suite]}, " \
                                     f"{(int(suite_prob[suite])/len(self.cards_remaining))*100:.2f}%  "
                new_line += 1
            else:
                printable_results += f"{suite}: {suite_prob[suite]}, " \
                                     f"{(int(suite_prob[suite])/len(self.cards_remaining))*100:.2f}%\n  "
                new_line += 1

        # return the printable string
        self.remaining_suites_label.config(text=printable_results)

    def remove_card(self):

        try:
            # remove card from deck, because we didn't use .copy() the objects are the same, do not have to re-assign
            suite = self.suite.get()
            card_list = self.deck[suite.upper()]
            face = self.face.get()
            card_index = card_list.index(face.upper())
            card_list.pop(card_index)

            # remove card from remaining card list
            card_index = self.cards_remaining.index(face.upper())
            self.cards_remaining.pop(card_index)

            # return label for user
            self.card_result_label1.config(text="Card Removed")
            self.deck_result_label.after(2000, self.reset_card_text)
        except ValueError as error:
            self.card_result_label2.config(text="Card is not in the deck")
            self.deck_result_label.after(2000, self.reset_card_text)

        # update remaining cards list
        self.count_cards()
        self.count_suites()

    def count_selected(self):
        """Counts the remaining cards, and gives the probability for each card"""
        number_of_selected_cards = 0
        for card in self.cards_remaining:
            if card in self.selected_cards.get():
                number_of_selected_cards += 1

        self.probability = (number_of_selected_cards / len(self.cards_remaining)) * 100

        # return text to show target card probability
        text_to_return = f"The probability of receiving a {(self.selected_cards.get())} is {self.probability:.2f}%"
        self.target_card_result.config(text=text_to_return)

    def reset_deck(self):
        """Clears instance variables, destroys and re-creates certain widgets """
        # reset instance variables
        self.deck = {}
        self.cards_remaining = []
        self.probability = 0

        # reset the deck confirmation label
        self.deck_result_label.destroy()
        self.deck_result_label = tkinter.Label(self.main_frame, background='grey', fg='#5bfba3')
        self.deck_result_label.grid(row=2, column=1, sticky='nw', columnspan=2)

        # reset the remaining cards list
        self.remaining_probability_label.destroy()
        self.remaining_probability_label = tkinter.Label(self.main_frame, background='grey', fg='white')
        self.remaining_probability_label.grid(row=2, column=4, rowspan=8, sticky='ne', padx=5)

        # reset target cards label
        self.target_card_result.destroy()
        self.target_card_result = tkinter.Label(self.main_frame, background='grey', fg='white')
        self.target_card_result.grid(row=8, column=1, sticky='nw', columnspan=3)

        # reset remaining suites list
        self.remaining_suites_label.destroy()
        self.remaining_suites_label = tkinter.Label(self.main_frame, background='grey', fg='white')
        self.remaining_suites_label.grid(row=10, column=1, columnspan=2, sticky='nw', padx=5)

    def reset_card_text(self):
        """Destroys and re-creates cards removed label, so that the user knows that card has or has not been removed"""
        # Card removed label
        self.card_result_label1.destroy()
        self.card_result_label1 = tkinter.Label(self.main_frame, background='grey', fg='#5bfba3')
        self.card_result_label1.grid(row=6, column=1, sticky='nw')
        # Card not removed label
        self.card_result_label2.destroy()
        self.card_result_label2 = tkinter.Label(self.main_frame, background='grey', fg='#fda1a1')
        self.card_result_label2.grid(row=6, column=2, sticky='nw')


if __name__ == "__main__":
    lets_run_it = CardCounter()
    lets_run_it.mainloop()






















