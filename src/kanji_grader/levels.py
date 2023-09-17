from typing import Union
import json
import os


class Levels:
  """
  Returns levels for kanji

  >>> l = Levels()
  >>> l.get_jlpt_level("a") == None
  True
  >>> l.get_jlpt_level("一")
  5
  >>> l.get_jlpt_level("茎")
  1
  >>> l.get_grade_level("一")
  1
  >>> l.get_grade_level("悠")
  8
  >>> l.get_jlpt_level("abc")
  Traceback (most recent call last):
        ...
  ValueError: get_jlpt_level accepts a single character, but your text was 3 characters.
  >>> l.get_jlpt_level("")
  Traceback (most recent call last):
        ...
  ValueError: get_jlpt_level accepts a single character, but you gave it nothing.
  >>> l.get_jlpt_level(None)
  Traceback (most recent call last):
        ...
  ValueError: get_jlpt_level accepts a single character, but you gave it nothing.
  >>> l.get_grade_level("abc")
  Traceback (most recent call last):
        ...
  ValueError: get_grade_level accepts a single character, but your text was 3 characters.
  >>> l.get_grade_level("")
  Traceback (most recent call last):
        ...
  ValueError: get_grade_level accepts a single character, but you gave it nothing.
  >>> l.get_grade_level(None)
  Traceback (most recent call last):
        ...
  ValueError: get_grade_level accepts a single character, but you gave it nothing.
  """

  def __init__(self):
    script_path = os.path.dirname(os.path.abspath(__file__))
    json_filepath = os.path.join(
      script_path,
      "resources",
      "kanji-jouyou.json"
    )
    with open(json_filepath, 'r') as f:
      self.data = json.load(f)

  def get_jlpt_level(self, kanji: str) -> Union[int, None]:
    """
    Given a string like "日", returns the JLPT level like "N5"

    If the character is not part of any JLPT level, then None is returned
    """
    if kanji is None or len(kanji) < 1:
      raise ValueError("get_jlpt_level accepts a single character, but you gave it nothing.")
    elif len(kanji) > 1:
      raise ValueError(f"get_jlpt_level accepts a single character, but your text was {len(kanji)} characters.")

    entry = self.data.get(kanji, None)

    if entry is None:
      return None

    return entry['jlpt_new']

  def get_grade_level(self, kanji: str) -> Union[int, None]:
    """
    Given a string like "日", returns the grade level like "G3"

    If the character is not part of any grade level, then None is returned
    """
    if kanji is None or len(kanji) < 1:
      raise ValueError("get_grade_level accepts a single character, but you gave it nothing.")
    elif len(kanji) > 1:
      raise ValueError(f"get_grade_level accepts a single character, but your text was {len(kanji)} characters.")

    entry = self.data.get(kanji, None)

    if entry is None:
      return None

    return entry['grade']
