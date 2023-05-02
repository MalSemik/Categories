from unittest.mock import patch, call
import categories_pl
from categories_pl import main
from contextlib import redirect_stdout
import io


@patch("builtins.input")
@patch.object(categories_pl, "possible_letters", ["a", "p"])  # possible_letters are sorted before the test, so we get p
def test_system_happy_path(input_mock):
    user_inputs = [
        # how many players?
        "2",
        # player names
        "Rafal",
        "Gosia",
        # Rafal answers for P
        "Polska",
        "Poznan",
        "Porost",
        "Pingwin",
        "Patrycja",
        "Kurde nie wiem",
        # Gosia answers for P
        "Polska",
        "Przemysl",
        "Pietruszka",
        "Pyton",
        "Paweł",
        "Pustak",
        # Asks if wants to play again
        "Nie chce znowu grac",
    ]
    user_inputs_iter = iter(user_inputs)

    def input_(message):
        print(message)
        return next(user_inputs_iter)

    input_mock.side_effect = input_

    console = io.StringIO()
    with redirect_stdout(console):
        main()
    console_output = console.getvalue()
    # this will likely change a lot, so let's print it every time for an easy copy-paste
    print(console_output)
    assert (
        console_output
        == """Witamy w grze Państwa-Miasta!
Ilu graczy będzie brało udział w rozgrywce? 
Podaj imię gracza numer 1: 
Podaj imię gracza numer 2: 
Wszyscy gotowi? Więc zaczynamy!
Odpowiada Rafal. Litera p
Państwo na literę p: 
Miasto na literę p: 
Roślina na literę p: 
Zwierzę na literę p: 
Imię na literę p: 
Rzecz na literę p: 
Odpowiada Gosia. Litera p
Państwo na literę p: 
Miasto na literę p: 
Roślina na literę p: 
Zwierzę na literę p: 
Imię na literę p: 
Rzecz na literę p: 
Rafal ma 45 pkt.
Gosia ma 60 pkt.
Czy chcesz zagrać jeszcze raz? (Y/N) 
Dziękujemy za wspólną grę!
Gosia zwycięża z liczbą 60 punktów.
"""
    )
    # TODO: Previous assert might be to specific, maybe we only need to assert the final verdict
    #  not the whole game? Asserting against the whole output will make use edit this test a lot
    assert "Gosia zwycięża z liczbą 60 punktów." in console_output
