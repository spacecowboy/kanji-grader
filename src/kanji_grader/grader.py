from .levels import Levels


def grade_text_by_jlpt(levels: Levels, text: str) -> dict[str, str]:
  """
  Given a piece of text, returns a map from the grade to the percent
  of characters which are contained in that level.

  Non-exhaustive example: { "N5": "100%" }
  """
  # The level of a single kanji can be gotten from 'levels', for example
  #
  # l = levels.get_jlpt_level("一")
  raise ValueError("TODO")


def grade_file_by_jlpt(levels: Levels, filepath: str) -> dict[str, str]:
  """
  Given a filepath, read the file, then pass the contents to grade_text_by_jlpt
  """
  raise ValueError("TODO")
