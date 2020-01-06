import random

# target = random.choice()


class MasterMindGameMaster:
    def __init__(self):
        target = []
        for x in range(0, 4):
            target.append(random.choice(range(0, 10)))
        self.target = target
        self.guess_collector = []
        self.win_state = False
        my_dict = {}
        for x in range(0, 10):
            count = 0
            for y in self.target:
                if x == y:
                    count += 1
            my_dict[x] = count
        self.target_dict = my_dict

    def print_counter(self):
        turn_counter = len(guess_collector)
        print(turn_counter)

    def print_guesses(self):
        print("Here's what you've guessed so far:")
        for eachGuess in self.guess_collector:
            print(eachGuess)

    def add_guess(self, guess):
        self.guess_collector.append(guess)

    def analyse_guess(self, guess):
        my_dict = {}
        for x in range(0, 10):
            count = 0
            for y in list(guess):
                if int(y) == x:
                    count += 1
            my_dict[x] = count
        return(my_dict)

    def correct_guesses(self, guess):
        counter = 0
        guess_dict = self.analyse_guess(guess)
        # print("Using this dictionary: ", guess_dict)
        for x in range(0, 10):
            A = guess_dict[x]
            B = self.target_dict[x]
            if A >= B:
                counter += B
            else:
                counter += A
        print("You have guessed {} numbers correctly.".format(counter))

    def winner(self):
        print("You won! It only took you {} rounds to do it too!".format(len(self.guess_collector)))
        self.win_state = True

    def correct_positions(self, guess):  # compare the
        counter = 0
        for i, j in zip(self.target, list(guess)):
            # print("Checking {} against {}...".format(i, j))
            if i == int(j):
                counter += 1
        if counter == 4:
            print("Hey! You guessed it!")
            self.winner()
        else:
            print("Your guess has {} numbers in the correct position".format(counter))


class Guess_Handler(MasterMindGameMaster):
    def __init__(self, guess_collector, guess):
        self.guess_collector = guess_collector
        self.guess = guess

    def print_guess(self):
        print(self.guess)

    def verify(self):
        if not self.guess.isnumeric():
            print("Ummm... You're trying to guess a four digit NUMBER. Try again.")
            return(False)
        elif len(self.guess) > 4 or len(self.guess) < 4:
            print("The aim of the game is to guess a four digit number. You've entered {} digits. Try again. And pull yourself together".format(
                len(self.guess)))
            return(False)
        elif self.guess in self.guess_collector:
            print("Ya numpty, you've tried that one before!")
        else:
            return(True)


def main():
    game = MasterMindGameMaster()  # sets target and initialises
    print("I'm thinking of a 4 digit number. Guess it if you can.")
    print("Pssst. Hint. It's {}".format(game.target))
    while not game.win_state:
        user_guess = input("Guess away Compadre!")
        checked_guess = Guess_Handler(game.guess_collector, user_guess)
        while not checked_guess.verify():  # escape condition: a valid input
            user_guess = input("Guess Again Commander Ben!")
            # create a new instance of the validator class
            checked_guess = Guess_Handler(game.guess_collector, user_guess)
        # Add the valid guess to the guess collector
        game.add_guess(user_guess)
        # say how many correct numbers there are
        game.correct_guesses(user_guess)
        # say how many numbers are in the correct position
        # correct_positions will call the end of the game if all correct
        game.correct_positions(user_guess)
        # print the list of guesses so far
        game.print_guesses()


if __name__ == '__main__':
    main()
