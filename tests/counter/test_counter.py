from src.pre_built.counter import count_ocurrences


def test_counter():
    path = "data/jobs.csv"
    word = "python"

    result = count_ocurrences(path, word)

    assert result == 1639

    assert count_ocurrences(path, "PYTHON") == 1639
    assert count_ocurrences(path, "Python") == 1639
    assert count_ocurrences(path, "pYThOn") == 1639
