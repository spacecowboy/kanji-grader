# Kanji Grader

The purpose of this task is to build a program which can grade a Japanese text
by how many different types of kanji (characters, 漢字) are used.

Japanese kanji can be grouped in different ways. In this exercise we will use the
Japanese Language Proficency Test (JLPT) grouping. There are 5 levels.

* Level 5 (N5) roughly contains 80 kanji
* Level 4 (N4) has a *further* 170 kanji
* Level 3 (N3) then has 370 kanji more
* Level 2 (N2) has 380 kanji
* Level 1 (N1) has a final 1136 kanji

If one has mastered N1, then it is implied than one has also mastered N5-N4.

The end goal of this exercise is to create a commandline program which can be invoked as follows with an output similar to

```
> kanji_grader my_japanese_book.txt

N5: 55%
N4: 69%
N3: 83%
N2: 95%
N1: 99%
```

## How to run the tests

First install [poetry](https://python-poetry.org/docs/).

And then run

```
poetry run pytest
```

This should result in an output ending with

```
FAILED tests/test_task1.py::test_one_n5 - ValueError: TODO
FAILED tests/test_task1.py::test_irrelevant_chars - ValueError: TODO
FAILED tests/test_task1.py::test_mix_of_chars - ValueError: TODO
```

Then everything is good!

Write your code in `grader.py`. Task 1 is finished when tests in `test_task1` are green.
