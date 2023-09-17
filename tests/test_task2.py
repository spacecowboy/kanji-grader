from kanji_grader.levels import Levels
from kanji_grader.grader import grade_file_by_jlpt
import os


levels = Levels()


def test_rashoumon():
  rashoumon_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "rashoumon.txt"
  )
  result = grade_file_by_jlpt(levels, rashoumon_path)

  assert result["N5"] == "34%"
  assert result["N4"] == "58%"
  assert result["N3"] == "78%"
  assert result["N2"] == "88%"
  assert result["N1"] == "100%"
  assert set(result.keys()) == set(["N1", "N2", "N3", "N4", "N5"])
