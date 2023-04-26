from unittest.mock import patch, call
import categories_pl
from categories_pl import main

categories = ["Państwo", "Miasto", "Roślina", "Zwierzę", "Imię", "Rzecz"]


@patch("builtins.print")
@patch("builtins.input")
@patch.object(categories_pl, "possible_letters", ["a", "p"])  # possible_letters are sorted before the test, so we get p
def test_system_happy_path(input_mock, print_mock):
    input_mock.side_effect = [
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
    main()
    # TODO: missing messages added with input, but tbh we could just assert for the last message
    #  who wins with how many points
    expected_prints = [
        call("Witamy w grze Państwa-Miasta!"),
        call("Wszyscy gotowi? Więc zaczynamy!"),
        call("Odpowiada Rafal. Litera p"),
        call("Odpowiada Gosia. Litera p"),
        call("Rafal ma 45 pkt."),
        call("Gosia ma 60 pkt."),
        call("Dziękujemy za wspólną grę!"),
        call("Gosia zwycięża z liczbą 60 punktów."),
    ]
    print_mock.assert_has_calls(expected_prints)
