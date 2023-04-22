import random
from prettytable import PrettyTable

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u',
            'w', 'z']
random.shuffle(alphabet)

categories = ['Państwo', 'Miasto', 'Roślina', 'Zwierzę', 'Imię', 'Rzecz']


def get_answers(letter, categories):
    answers = []
    for category in categories:
        answer = input(f'{category} na literę {letter}: ')
        answers.append(answer)
    return answers


def check_answers(answers, letter):
    for i in range(len(answers)):
        if len(answers[i]) == 0 or answers[i][0].lower() != letter:
            answers[i] = '-'
    return answers


def print_sheet(categories, answers):
    player_sheet = PrettyTable(categories)
    player_sheet.add_rows(answers)
    print(player_sheet)


class Player:
    def __init__(self, name):
        self.name = name
        self.answer_sheet = []
        self.points = 0


def setup():
    num_players = int(input("Ilu graczy będzie brało udział w rozgrywce? "))
    players = {}
    for i in range(num_players):
        name = input(f"Podaj imię gracza numer {i+1}: ")
        players.update({name: Player(name)})
    return players


def single_game(alphabet, players):
    letter = alphabet.pop()
    for player in players.values():
        print(f"Odpowiada {player.name}")
        answers = get_answers(letter, categories)
        answers = check_answers(answers, letter)
        player.answer_sheet.append(answers)
        print(player.answer_sheet)
    # score the game


def main():
    print("Witamy w grze Państwa-Miasta!")
    players = setup()
    print("Wszyscy gotowi? Więc zaczynamy!")
    single_game(alphabet, players)
    while len(alphabet) > 0:
        play_again = input("Czy chcesz zagrać jeszcze raz? (Y/N) ").upper()
        if play_again == "Y":
            single_game(alphabet, players)
        else:
            print("Dziękujemy za wspólną grę!")
            print("Wygrywa ZWYCIĘZCA")
            return
    print("Nie ma już więcej liter.")
    print("Wygrywa ZWYCIĘZCA")


main()
