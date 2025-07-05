def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
    grades['top_grade'] = max(grades['grades'])
    grades.pop('grades')
    return grades
