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

  assert result["N5"] == 1.0
  assert result["N4"] == 1.0
  assert result["N3"] == 1.0
  assert result["N2"] == 1.0
  assert result["N1"] == 1.0
  assert set(result.keys()) == set(["N1", "N2", "N3", "N4", "N5"])
