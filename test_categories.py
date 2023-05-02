from categories_pl import check_answers


class TestCheckAnswers:
    def test_all_valid_answers_should_return_same_list(self):
        answers = ["Polska", "Pakistan", "Porost"]
        # make a copy of answers, because check_answers is modyfing the list in place
        assert check_answers(list(answers), "p") == answers

    def test_answer_is_case_insensitive(self):
        assert check_answers(["Polska", "pakistan"], "p") == ["Polska", "pakistan"]

    def test_empty_answers_or_answers_starting_with_wrong_letter_are_changed_removed(self):
        assert check_answers(["", "Andrzej", "Polska"], "p") == ["-", "-", "Polska"]
