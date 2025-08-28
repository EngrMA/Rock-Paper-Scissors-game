import random 


class RockPaperScissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissor']

    def play(self):
        user_choice = self.get_user_choice()
        print(f"your choice: {user_choice}")
        computer_choice = self.get_computer_choice()
        print(f"computer choice : {computer_choice}")
        print(self.winner_recognizer(user_choice, computer_choice))

    def get_user_choice(self):
        user_choice = input(f"please enter your choice from this list({self.choices}) :")
        if user_choice.lower() in self.choices:
            return user_choice.lower()
        
        print(f"invalid input please try again, select from this list ({self.choices})")
        return self.get_user_choice()
    
    def get_computer_choice(self):
        return random.choice(self.choices)
    
    def winner_recognizer(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "it is a Tie!"
        
        win_conditions = [('rock', 'scissor'), ('paper', 'rock'), ('scissor', 'paper')]
        for win_con in win_conditions:
            if (user_choice == win_con[0]) and (computer_choice == win_con[1]):
                return "congrats, you have won!"
        return "oh sorry, you loss"



if __name__ == "__main__":
    while True:
        game = RockPaperScissors()
        game.play()
    
        continue_value = input("do you wanna play again(press any key) or not(q/Q): ")
        if continue_value.lower() == "q":
            break 