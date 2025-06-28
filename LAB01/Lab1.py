# lab1.py

def wins_rock_scissors_paper(player, opponent):
    player = player.lower()
    opponent = opponent.lower()
    
    if player == opponent:
        return False

    if (player == 'rock' and opponent == 'scissors') or \
       (player == 'scissors' and opponent == 'paper') or \
       (player == 'paper' and opponent == 'rock'):
        return True
    return False


def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def sum_to_goal(numbers, goal):
    seen = set()
    for number in numbers:
        complement = goal - number
        if complement in seen:
            return number * complement
        seen.add(number)
    return 0


class UpCounter:
    def __init__(self, step=1):
        self.step = step
        self._count = 0

    def count(self):
        return self._count

    def update(self):
        self._count += self.step


class DownCounter(UpCounter):
    def update(self):
        self._count -= self.step
