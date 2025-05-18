import keyboard
import time
from .maze import generate_maze
from .player import Player

def play_game():
    stage = 1
    while True:
        print(f"\n--- Stage {stage} ---")
        width = 15 + stage * 2
        height = 15 + stage * 2
        maze = generate_maze(width, height)
        player = Player(1, 1)

        while True:
            print_maze(maze, player)
            key = wait_for_arrow_key()
            if key:
                if player.move(key, maze):
                    if maze[player.x][player.y] == 'E':
                        print("Stage Cleared!\n")
                        break
            time.sleep(0.1)

        stage += 1

def print_maze(maze, player):
    print("\033[H\033[J", end="")  # 터미널 화면 지우기
    for i, row in enumerate(maze):
        line = ""
        for j, cell in enumerate(row):
            if i == player.x and j == player.y:
                line += 'P'
            else:
                line += cell
        print(line)

def wait_for_arrow_key():
    if keyboard.is_pressed('up'):
        return 'w'
    elif keyboard.is_pressed('down'):
        return 's'
    elif keyboard.is_pressed('left'):
        return 'a'
    elif keyboard.is_pressed('right'):
        return 'd'
    return None
