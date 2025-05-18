class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, direction, maze):
        dx, dy = {
            'w': (-1, 0),
            's': (1, 0),
            'a': (0, -1),
            'd': (0, 1)
        }.get(direction, (0, 0))

        nx, ny = self.x + dx, self.y + dy
        if maze[nx][ny] != '#':
            self.x, self.y = nx, ny
            return True
        return False
