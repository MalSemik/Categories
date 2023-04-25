import os
import random
from collections import Counter
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


def score_answers(players):
    latest_answers = [player.answer_sheet[-1] for player in players.values()]
    categories = [[latest_answers[j][i].lower() for j in range(len(latest_answers))] for i in range(len(latest_answers[0]))]

    for category in categories:
        count = Counter(list(category))
        for i in range(len(category)):
            if category[i] == '-':
                category[i] = 0
            elif count[category[i]] > 1:
                category[i] = 5
            elif count['-'] == len(category) - 1:
                category[i] = 15
            else:
                category[i] = 10

    results = [sum([categories[j][i] for j in range(len(categories))]) for i in range(len(categories[0]))]

    for player in players.values():
        player.points = player.points + results[0]
        results.pop(0)

    for player in players.values():
        print(f'{player.name} ma {player.points} pkt.' )


def check_winner(players):
    points = [player.points for player in players.values()]
    max_points = max(points)
    if points.count(max_points) > 1:
        draws = []
        for player in players.values():
            if player.points == max_points:
                draws.append(player.name)
        print(f"Gracze {draws} remisują z liczbą {max_points} punktów.")
    else:
        for player in players.values():
            if player.points == max_points:
                print(f"{player.name} zwycięża z liczbą {player.points} punktów.")


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
        print_sheet(categories, player.answer_sheet)
        os.system('cls')
    score_answers(players)


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
            check_winner(players)
            return
    print("Nie ma już więcej liter.")
    check_winner(players)


main()
input("")
