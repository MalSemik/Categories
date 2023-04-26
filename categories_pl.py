import os
import random
from sys import platform
from collections import Counter

from prettytable import PrettyTable


possible_letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "ł",
    "m",
    "n",
    "o",
    "p",
    "r",
    "s",
    "t",
    "u",
    "w",
    "z",
]
random.shuffle(possible_letters)

categories = ["Państwo", "Miasto", "Roślina", "Zwierzę", "Imię", "Rzecz"]


def get_answers(letter, categories):
    answers = []
    for category in categories:
        answer = input(f"{category} na literę {letter}: ")
        answers.append(answer.capitalize())
    return answers


def check_answers(answers, letter):
    for i in range(len(answers)):
        if len(answers[i]) == 0 or answers[i][0].lower() != letter:
            answers[i] = "-"
    return answers


def group_by_categories(players_answers_last_round):
    """
    >>> group_by_categories([["Polska", "Poznan"], ["Pakistan", "Pcim"]])
    [('Polska', 'Pakistan'), ('Poznan', 'Pcim')]
    """
    return list(zip(*players_answers_last_round))


def score_answers(players_by_name):
    players_answers_last_round = [player.answer_sheet[-1] for player in players_by_name.values()]
    category_answers = group_by_categories(players_answers_last_round)

    all_scores = []
    for category in category_answers:
        count = Counter(list(category))
        score = []
        for i in range(len(category)):
            if category[i] == "-":
                score.append(0)
            elif count[category[i]] > 1:
                score.append(5)
            elif count["-"] == len(category) - 1:
                score.append(15)
            else:
                score.append(10)
        all_scores.append(score)

    players_round_scores = list(zip(*all_scores))
    sums_of_scores = []
    for player_round_scores in players_round_scores:
        sums_of_scores.append(sum(list(player_round_scores)))

    for player, points in zip(players_by_name.values(), sums_of_scores):
        player.points += points

    for player in players_by_name.values():
        print(f"{player.name} ma {player.points} pkt.")


def check_winner(players_by_name):
    points = [player.points for player in players_by_name.values()]
    max_points = max(points)
    if points.count(max_points) > 1:
        draws = []
        for player in players_by_name.values():
            if player.points == max_points:
                draws.append(player)
        return draws

    else:
        for player in players_by_name.values():
            if player.points == max_points:
                return player


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
    players_by_name = {}
    for i in range(num_players):
        name = input(f"Podaj imię gracza numer {i+1}: ")
        players_by_name.update({name: Player(name)})
    return players_by_name


def single_game(alphabet, players_by_name):
    letter = alphabet.pop()
    for player in players_by_name.values():
        print(f"Odpowiada {player.name}")
        answers = get_answers(letter, categories)
        answers = check_answers(answers, letter)
        player.answer_sheet.append(answers)
        # print_sheet(categories, player.answer_sheet)
        if platform == "win32":
            os.system("cls")
        else:
            os.system("clear")
    score_answers(players_by_name)


def main():
    print("Witamy w grze Państwa-Miasta!")
    players_by_name = setup()
    print("Wszyscy gotowi? Więc zaczynamy!")
    single_game(possible_letters, players_by_name)
    while len(possible_letters) > 0:
        play_again = input("Czy chcesz zagrać jeszcze raz? (Y/N) ").upper()
        if play_again == "Y":
            single_game(possible_letters, players_by_name)
        else:
            print("Dziękujemy za wspólną grę!")
            winner = check_winner(players_by_name)
            if isinstance(winner, list):
                names = [player.name for player in winner]
                print(f"Gracze {', '.join(names)} remisują z liczbą {winner[0].points} punktów.")
            else:
                print(f"{winner.name} zwycięża z liczbą {winner.points} punktów.")
            return
    print("Nie ma już więcej liter.")
    winner = check_winner(players_by_name)
    if isinstance(winner, list):
        names = [player.name for player in winner]
        print(f"Gracze {', '.join(names)} remisują z liczbą {winner[0].points} punktów.")
    else:
        print(f"{winner.name} zwycięża z liczbą {winner.points} punktów.")


if __name__ == "__main__":
    main()
    input("Naciśnij dowolny przycisk aby zakończyć.")
