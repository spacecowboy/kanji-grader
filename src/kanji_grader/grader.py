from .levels import Levels


def grade_text_by_jlpt(levels: Levels, text: str) -> dict[str, float]:
  """
  Given a piece of text, returns a map from the grade to the ratio
  of characters which are contained in that level.
  """
  # The level of a single kanji can be gotten from 'levels', for example
  #
  # l = levels.get_jlpt_level("一")
  raise ValueError("TODO")
