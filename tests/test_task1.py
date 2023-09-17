from kanji_grader.levels import Levels
from kanji_grader.grader import grade_text_by_jlpt


levels = Levels()


def test_one_n5():
  result = grade_text_by_jlpt(levels, "一")

  assert result["N5"] == 1.0
  assert result["N4"] == 1.0
  assert result["N3"] == 1.0
  assert result["N2"] == 1.0
  assert result["N1"] == 1.0
  assert set(result.keys()) == set(["N1", "N2", "N3", "N4", "N5"])


def test_irrelevant_chars():
  result = grade_text_by_jlpt(levels, "abc .!")

  assert result["N5"] == 1.0
  assert result["N4"] == 1.0
  assert result["N3"] == 1.0
  assert result["N2"] == 1.0
  assert result["N1"] == 1.0
  assert set(result.keys()) == set(["N1", "N2", "N3", "N4", "N5"])


def test_mix_of_chars():
  result = grade_text_by_jlpt(levels, "a 一画直星氏")

  assert result["N5"] == 0.2
  assert result["N4"] == 0.4
  assert result["N3"] == 0.6
  assert result["N2"] == 0.8
  assert result["N1"] == 1.0
  assert set(result.keys()) == set(["N1", "N2", "N3", "N4", "N5"])
