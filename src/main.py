"""
Author: EngrMA
Popular Rock Paper Scissor Game 

Refactored By: EngrMH
"""

import random 


class RockPaperScissors:
    """the main class for Rock Paper Scissor Game"""
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissor']

    def play(self):
        """method to play the game."""
        user_choice: str = self.get_user_choice()
        print(f"your choice: {user_choice}")
        computer_choice: str = self.get_computer_choice()
        print(f"computer choice : {computer_choice}")
        print(self.winner_recognizer(user_choice, computer_choice))

    def get_user_choice(self):
        """to get choices of users

        :return: choice of users
        :rtype: str
        """ 
        user_choice = input(f"please enter your choice from this list({self.choices}) :")
        if user_choice.lower() in self.choices:
            return user_choice.lower()
        
        print(f"invalid input please try again, select from this list ({self.choices})")
        return self.get_user_choice()
    
    def get_computer_choice(self):
        """to get choices from computer by random.

        :return: gvie choices of a computer
        :rtype: str
        """
        return random.choice(self.choices)
    
    def winner_recognizer(self, user_choice: str, computer_choice: str) -> str:
        """decide whether user or computer won, or even it is a tie!

        :param user_choice: choice of users from the list of choices
        :param computer_choice: choice of a computer according to the list
        :return: results of the game. who won
        """
        if user_choice == computer_choice:
            return "it is a Tie!"
        
        win_conditions = [('rock', 'scissor'), ('paper', 'rock'), ('scissor', 'paper')]
        for win_con in win_conditions:
            if (user_choice == win_con[0]) and (computer_choice == win_con[1]):
                return "congrats, you have won!"
        return "oh sorry, you loss"



if __name__ == "__main__":
    game = RockPaperScissors()

    while True:
        game.play()
    
        continue_value = input("do you wanna play again(press any key) or not(q/Q): ")
        if continue_value.lower() == "q":
            break 
