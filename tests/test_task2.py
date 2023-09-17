from kanji_grader.levels import Levels
from kanji_grader.grader import grade_file_by_jlpt
import os


levels = Levels()


def test_rashoumon():
  file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "rashoumon.txt"
  )
  result = grade_file_by_jlpt(levels, file_path)

  assert result == {'N1': '96%', 'N2': '84%', 'N3': '75%', 'N4': '56%', 'N5': '33%'}
