from kanji_grader.levels import Levels
from kanji_grader.grader import grade_text_by_jlpt


levels = Levels()


def test_one_n5():
  result = grade_text_by_jlpt(levels, "一")

  assert result["N5"] == "100%"
  assert result["N4"] == "100%"
  assert result["N3"] == "100%"
  assert result["N2"] == "100%"
  assert result["N1"] == "100%"
  assert set(result.keys()) == set(["N1", "N2", "N3", "N4", "N5"])


def test_irrelevant_chars():
  result = grade_text_by_jlpt(levels, "abc .!")

  assert result["N5"] == "100%"
  assert result["N4"] == "100%"
  assert result["N3"] == "100%"
  assert result["N2"] == "100%"
  assert result["N1"] == "100%"
  assert set(result.keys()) == set(["N1", "N2", "N3", "N4", "N5"])


def test_mix_of_chars():
  result = grade_text_by_jlpt(levels, "a 一画直星氏")

  assert result["N5"] == "20%"
  assert result["N4"] == "40%"
  assert result["N3"] == "60%"
  assert result["N2"] == "80%"
  assert result["N1"] == "100%"
  assert set(result.keys()) == set(["N1", "N2", "N3", "N4", "N5"])
