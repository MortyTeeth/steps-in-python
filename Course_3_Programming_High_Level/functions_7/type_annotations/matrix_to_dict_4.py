def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
    return {key: value for key, value in enumerate(matrix, start=1)}
