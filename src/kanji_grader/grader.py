from .levels import Levels


def grade_text_by_jlpt(levels: Levels, text: str) -> dict[str, str]:
    """
    Given a piece of text, returns a map from the grade to the percent
    of characters which are contained in that level.

    Non-exhaustive example: { "N5": "100%" }
    """
    count = 0
    level_counts = {"N5": 0, "N4": 0, "N3": 0, "N2": 0, "N1": 0}

    for c in text:
        try:
            l = levels.get_jlpt_level(c)
        except:
            continue

        count += 1

        if not l:
            continue

        nl = f"N{l}"
        level_counts[nl] = level_counts[nl] + 1

    result = {}
    levels = ["N1", "N2", "N3", "N4", "N5"]
    for i, level in enumerate(levels):
        if count == 0:
            result[level] = "100%"
        else:
            level_count = sum(level_counts[l] for l in levels[i:])
            result[level] = "{:.0f}%".format(100 * level_count / count)

    return result


def grade_file_by_jlpt(levels: Levels, filepath: str) -> dict[str, str]:
    """
    Given a filepath, read the file, then pass the contents to grade_text_by_jlpt
    """
    with open(filepath, "r") as f:
        text = "\n".join(f.readlines())

    return grade_text_by_jlpt(levels, text)


def grade_text_by_grade(levels: Levels, text: str) -> dict[str, str]:
    """
    Given a piece of text, returns a map from the grade to the percent
    of characters which are contained in that level.

    Non-exhaustive example: { "G5": "100%" }
    """
    count = 0
    level_counts = {f"G{g}": 0 for g in range(1, 9)}

    for c in text:
        try:
            l = levels.get_jlpt_level(c)
        except:
            continue

        count += 1

        if not l:
            continue

        nl = f"G{l}"
        level_counts[nl] = level_counts[nl] + 1

    result = {}
    levels = [f"G{g}" for g in reversed(range(1, 9))]
    for i, level in enumerate(levels):
        if count == 0:
            result[level] = "100%"
        else:
            level_count = sum(level_counts[l] for l in levels[i:])
            result[level] = "{:.0f}%".format(100 * level_count / count)

    return result


def grade_file_by_grade(levels: Levels, filepath: str) -> dict[str, str]:
    """
    Given a filepath, read the file, then pass the contents to grade_text_by_jlpt
    """
    with open(filepath, "r") as f:
        text = "\n".join(f.readlines())

    return grade_text_by_grade(levels, text)
