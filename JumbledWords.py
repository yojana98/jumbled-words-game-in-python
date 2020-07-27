import random
import time


class Player:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.player1_pnt = 0
        self.player2_pnt = 0


class PlayerGame(Player):

    def __init__(self, player1, player2, rounds, categories):
        super().__init__(player1, player2)
        self.rounds = rounds
        self.categories = categories

    def choose_file(self, select_category):
        dict = {1: "fruits.txt", 2: "vegetables.txt"}
        if select_category in dict.keys():
            file_name = dict[select_category]

        with open(file_name) as fh:
            file = fh.readlines()
            file = list(map(str.lower, file))
            file = list(map(lambda x: x.strip(), file))

        return file

    def choose_word(self, word_list):
        chosen_word = random.choice(word_list)
        return chosen_word

    def jumble_word(self, word_from_list):
        shuffled_word = random.sample(
            word_from_list, len(word_from_list))
        shuffled_word = ''.join(shuffled_word)
        return shuffled_word

    def thank_players(self):
        print(self.player1+"'s score is", self.player1_pnt)
        time.sleep(1)
        print(self.player2+"'s score is", self.player2_pnt)
        time.sleep(1)

    def check_winner(self):
        if self.player1_pnt > self.player2_pnt:
            print(self.player1+" wins")
            time.sleep(1)
        elif self.player2_pnt > self.player1_pnt:
            print(self.player2+" wins")
            time.sleep(1)
        else:
            print("There's been a draw, Well played!")
            time.sleep(1)

    def play_rounds(self):
        turn = 0
        while turn < self.rounds:
            print("*************** Round ",
                  (turn+1), " ***************")
            time.sleep(1)
            for i in range(1, 3):
                if i == 1:
                    print("Player 1 will play first")
                    self.play_game(self.player1, self.player2)
                else:
                    print("Player 2 will play first")
                    self.play_game(self.player2, self.player1)

            turn += 1

    def play_game(self, play_x, play_y):
        word_list = player_obj.choose_file(self.categories)
        chosen_word = player_obj.choose_word(word_list)
        j_word = player_obj.jumble_word(chosen_word)
        print(play_x, "your turn")
        time.sleep(1)
        print("The jumbled word is:", j_word)
        time.sleep(1)
        answer = input("What is in your mind?  ")
        time.sleep(1)
        if answer == chosen_word:
            print("You guessed it right!")
            if play_x == self.player1:
                self.player1_pnt += 1
                print(play_x, "score is", self.player1_pnt)
                time.sleep(1)
            else:
                self.player2_pnt += 1
                print(play_x, "score is", self.player2_pnt)
                time.sleep(1)
        else:
            print("Better luck next time!")
            time.sleep(1)
            print(play_y, "your turn")
            print("The jumbled word is:", j_word)
            time.sleep(1)
            answer = input("What is in your mind?  ")
            if answer == chosen_word:
                print("You guessed it right!")
                if play_y == self.player1:
                    self.player1_pnt += 1
                    print(play_y, "score is", self.player1_pnt)
                    time.sleep(1)
                else:
                    self.player2_pnt += 1
                    print(play_y, "score is", self.player2_pnt)
                    time.sleep(1)
            else:
                print("Better luck next time!")
                time.sleep(1)
                print("Correct Answer is:", chosen_word)
                time.sleep(1)


if __name__ == "__main__":
    player1 = input("Player1, Please enter your name ")
    time.sleep(1)
    player2 = input("Player2, Please enter your name ")
    time.sleep(1)
    rounds = int(input("How many rounds you want to play? "))
    time.sleep(1)

    print("Select from below categories:")
    print("1.fruits 2.vegetables")
    select_category = int(input())
    player_obj = PlayerGame(player1, player2, rounds, select_category)
    player_obj.play_rounds()

    while True:
        print("Do you wish to continue? press 1 or 0 ")
        wish = int(input())
        if wish:
            rounds = int(input("How many rounds you want to play? "))
            print("Select from below categories:")
            print("1.fruits 2.vegetables")
            select_category = int(input())
            time.sleep(1)
            player_obj = PlayerGame(
                player1, player2, rounds, select_category)
            player_obj.play_rounds()
        else:
            player_obj.thank_players()
            player_obj.check_winner()
            break
