"""Задача 4. Счетчик Очков в Игрe
Создайте класс GameScore для отслеживания очков игрока. В этом классе должны быть методы для добавления и уменьшения
очков. Однако:
● Очки не могут быть отрицательными.
● Если игрок пытается добавить больше очков, чем 1000, должно быть
выброшено исключение ScoreLimitExceededError.
Создайте пользовательское исключение ScoreLimitExceededError."""

class ScoreLimitExceededError(Exception):
    def __init__(self, game_score, max_game_score):
        self.game_score = game_score
        self.max_game_score = max_game_score

    def __str__(self):
        return f"{self.max_game_score} is max game_score.  {self.game_score} is greater than 1000. "


class GameScore:
    def __init__(self, max_points):
        self._game_score = 0
        self._max_points = max_points

    def add_points (self, points: int):
        if not isinstance(points, int) or not (points > 0):
            raise ValueError("Points added should be a positive integer.")

        self.game_score += points

    def sub_points(self, points: int):
        if not isinstance(points, int) or not (points > 0):
            raise ValueError("Points added should be a positive integer.")
        self.game_score -= points

    @property
    def game_score(self):
        return self._game_score

    @game_score.setter
    def game_score(self, value):
        if value < 0:
            raise ValueError("Game score cannot be negative.")
        elif value > self._max_points:
            raise ScoreLimitExceededError(value, self._max_points)
        self._game_score = value


if __name__ == '__main__':
    game_score = GameScore(1000)
    game_score.add_points(50)
    print(game_score.game_score)
    game_score.sub_points(5)
    print(game_score.game_score)
    game_score.add_points(50)
    print(game_score.game_score)
    game_score.add_points(1000)

