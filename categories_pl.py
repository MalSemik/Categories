import random
from prettytable import PrettyTable

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u',
            'w', 'z']
random.shuffle(alphabet)
letter = alphabet.pop()
categories = ['Państwo', 'Miasto', 'Roślina', 'Zwierzę', 'Imię', 'Rzecz']


def get_answers(letter, categories):
    answers = []
    for category in categories:
        answer = input(f'{category} na literę {letter}: ')
        answers.append(answer)
    return answers


def check_answers(answers, letter):
    for i in range(len(answers)):
        if answers[i][0].lower() != letter:
            answers[i] = '-'
    return answers


# answers = get_answers(letter, categories)
# check_answers(answers, letter)

# Create and update player_sheet
player_sheet = PrettyTable(categories)
# player_sheet.add_row(answers)
# print(player_sheet)


class Player:
    def __init__(self, name, player_sheet):
        self.name = name
        self.sheet = player_sheet
        self.points = 0


def setup():
    num_players = int(input("Ilu graczy będzie brało udział w rozgrywce? "))
    players = {}
    for i in range(num_players):
        name = input(f"Podaj imię gracza numer {i+1}: ")
        players.update({name: Player(name, player_sheet)})
    print(players)


def main():
    print("Witamy w grze Państwa-Miasta!")
    setup()


main()
