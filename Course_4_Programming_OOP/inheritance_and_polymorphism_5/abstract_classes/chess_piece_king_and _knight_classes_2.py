from abc import ABC, abstractmethod


class ChessPiece(ABC):
    def __init__(self, horizontal: str, vertical: int):
        if horizontal not in 'abcdefgh':
            raise ValueError("Горизонтальная координата должна быть от 'a' до 'h'")
        if not (1 <= vertical <= 8):
            raise ValueError("Вертикальная координата должна быть от 1 до 8")
        self.horizontal = horizontal
        self.vertical = vertical

    @abstractmethod
    def can_move(self, horizontal: str, vertical: int) -> bool:
        pass


class King(ChessPiece):
    def can_move(self, horizontal: str, vertical: int) -> bool:
        dx = abs(ord(horizontal) - ord(self.horizontal))
        dy = abs(vertical - self.vertical)
        return dx <= 1 and dy <= 1 and (dx != 0 or dy != 0)


class Knight(ChessPiece):
    def can_move(self, horizontal: str, vertical: int) -> bool:
        dx = abs(ord(horizontal) - ord(self.horizontal))
        dy = abs(vertical - self.vertical)
        return (dx, dy) in [(1, 2), (2, 1)]
