import random
from prettytable import PrettyTable

# CREATE ALPHABET
# import string
# alphabet = list(string.ascii_lowercase)
# print(alphabet)

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


answers = get_answers(letter, categories)
check_answers(answers, letter)

# Create and update player_sheet
player_sheet = PrettyTable(categories)
player_sheet.add_row(answers)
print(player_sheet)
