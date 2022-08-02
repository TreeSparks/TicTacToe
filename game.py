import json
import sys

import pygame as py

py.joystick.init()
py.font.init()

# Constants
WIDTH, HEIGHT = 801, 801 # 600,600
FPS = 60

# Game Setup
screen = py.display.set_mode((WIDTH, HEIGHT), py.NOFRAME)
clock = py.time.Clock()

# Colors/Fonts
WHITE = (255, 255, 255)
LIGHT_BLUE = (153, 204, 255)
RED = (255, 0, 0)
GREEN = (0, 250, 0)
comicsans_font = py.font.SysFont('comicsansms', 50)

# Images
player_X = py.image.load('Assets/Player_X.png')
player_X = py.transform.scale(player_X, (WIDTH // 3, HEIGHT // 3))
player_O = py.image.load('Assets/Player_O.png')
player_O = py.transform.scale(player_O, (WIDTH // 3, HEIGHT // 3))

# Selection
current_square = 1  # 1-9 top to bottom left to right
selection_square = py.rect.Rect(0, 0, WIDTH // 3, HEIGHT // 3)

# Game Board
board = []
for x in range(3):
    row = [0] * 3
    board.append(row)

# Turns
turn = 1  # if 1: X elif: -1: O

# Winner 1=X -1=O 2=CAT
winner = 0
Player_X_Win_Text = comicsans_font.render("Player 'X' Wins", True, GREEN)
Player_O_Win_Text = comicsans_font.render("Player 'O' Wins", True, GREEN)
No_Winner = comicsans_font.render("No Winner", True, GREEN)

run = True
while run:
    clock.tick(FPS)
    joysticks = [py.joystick.Joystick(i) for i in range(py.joystick.get_count())]
    for joy in joysticks:
        joy.init()

    for event in py.event.get():
        if event.type == py.QUIT:
            sys.exit()
        if event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                sys.exit()
        for joy in joysticks:
            if joy.get_name() == "usb gamepad":
                with open("Assets/usb_gamepad_keys.json", 'r+') as file:
                    usb_button_keys = json.load(file)
                if event.type == py.JOYBUTTONDOWN and event.button == usb_button_keys['start'] and (winner == 1 or winner == -1 or winner == 2):
                    winner = 0
                    for x in range(3):
                        for y in range(3):
                            board[x][y] = 0
                    current_square = 1
                    turn = 1
        if winner == 0:
            for joy in joysticks:
                if joy.get_name() == "usb gamepad":
                    if event.type == py.JOYAXISMOTION:
                        usb_analog_keys = {0: 0, 1: 0, event.axis: event.value}
                        if abs(usb_analog_keys[0]) > .4:
                            if usb_analog_keys[0] < -.7:
                                if current_square == 2:
                                    current_square = 1
                                elif current_square == 3:
                                    current_square = 2
                                elif current_square == 5:
                                    current_square = 4
                                elif current_square == 6:
                                    current_square = 5
                                elif current_square == 8:
                                    current_square = 7
                                elif current_square == 9:
                                    current_square = 8
                            if usb_analog_keys[0] > .7:
                                if current_square == 1:
                                    current_square = 2
                                elif current_square == 2:
                                    current_square = 3
                                elif current_square == 4:
                                    current_square = 5
                                elif current_square == 5:
                                    current_square = 6
                                elif current_square == 7:
                                    current_square = 8
                                elif current_square == 8:
                                    current_square = 9
                        if abs(usb_analog_keys[1]) > .4:
                            if usb_analog_keys[1] < -.7:
                                if current_square == 4:
                                    current_square = 1
                                elif current_square == 5:
                                    current_square = 2
                                elif current_square == 6:
                                    current_square = 3
                                elif current_square == 7:
                                    current_square = 4
                                elif current_square == 8:
                                    current_square = 5
                                elif current_square == 9:
                                    current_square = 6
                            if usb_analog_keys[1] > .7:
                                if current_square == 1:
                                    current_square = 4
                                elif current_square == 2:
                                    current_square = 5
                                elif current_square == 3:
                                    current_square = 6
                                elif current_square == 4:
                                    current_square = 7
                                elif current_square == 5:
                                    current_square = 8
                                elif current_square == 6:
                                    current_square = 9
                    if event.type == py.JOYBUTTONDOWN:
                        with open("Assets/usb_gamepad_keys.json", 'r+') as file:
                            usb_button_keys = json.load(file)

                        if event.button == usb_button_keys['a']:
                            if current_square == 1:
                                x, y = 0, 0
                            elif current_square == 2:
                                x, y = 0, 1
                            elif current_square == 3:
                                x, y = 0, 2
                            elif current_square == 4:
                                x, y = 1, 0
                            elif current_square == 5:
                                x, y = 1, 1
                            elif current_square == 6:
                                x, y = 1, 2
                            elif current_square == 7:
                                x, y = 2, 0
                            elif current_square == 8:
                                x, y = 2, 1
                            elif current_square == 9:
                                x, y = 2, 2

                            # Check if spot is empty
                            if board[x][y] == 0:
                                # Change game board
                                if turn == 1:
                                    board[x][y] = 1
                                elif turn == -1:
                                    board[x][y] = -1
                                # Change turns
                                turn *= -1

            if event.type == py.KEYDOWN:
                if event.key == py.K_UP:
                    if current_square == 4:
                        current_square = 1
                    elif current_square == 5:
                        current_square = 2
                    elif current_square == 6:
                        current_square = 3
                    elif current_square == 7:
                        current_square = 4
                    elif current_square == 8:
                        current_square = 5
                    elif current_square == 9:
                        current_square = 6
                if event.key == py.K_DOWN:
                    if current_square == 1:
                        current_square = 4
                    elif current_square == 2:
                        current_square = 5
                    elif current_square == 3:
                        current_square = 6
                    elif current_square == 4:
                        current_square = 7
                    elif current_square == 5:
                        current_square = 8
                    elif current_square == 6:
                        current_square = 9
                if event.key == py.K_LEFT:
                    if current_square == 2:
                        current_square = 1
                    elif current_square == 3:
                        current_square = 2
                    elif current_square == 5:
                        current_square = 4
                    elif current_square == 6:
                        current_square = 5
                    elif current_square == 8:
                        current_square = 7
                    elif current_square == 9:
                        current_square = 8
                if event.key == py.K_RIGHT:
                    if current_square == 1:
                        current_square = 2
                    elif current_square == 2:
                        current_square = 3
                    elif current_square == 4:
                        current_square = 5
                    elif current_square == 5:
                        current_square = 6
                    elif current_square == 7:
                        current_square = 8
                    elif current_square == 8:
                        current_square = 9
                if event.key == py.K_x:
                    if current_square == 1:
                        x, y = 0, 0
                    elif current_square == 2:
                        x, y = 0, 1
                    elif current_square == 3:
                        x, y = 0, 2
                    elif current_square == 4:
                        x, y = 1, 0
                    elif current_square == 5:
                        x, y = 1, 1
                    elif current_square == 6:
                        x, y = 1, 2
                    elif current_square == 7:
                        x, y = 2, 0
                    elif current_square == 8:
                        x, y = 2, 1
                    elif current_square == 9:
                        x, y = 2, 2

                    # Check if spot is empty
                    if board[x][y] == 0:
                        # Change game board
                        if turn == 1:
                            board[x][y] = 1
                        elif turn == -1:
                            board[x][y] = -1
                        # Change turns
                        turn *= -1

            if event.type == py.MOUSEBUTTONDOWN:
                mouse_pos = py.mouse.get_pos()
                # Determine what square was clicked
                x = -1
                y = -1
                a0 = (WIDTH // 3) * 0
                a1 = (WIDTH // 3) * 1
                a2 = (WIDTH // 3) * 2
                a3 = (WIDTH // 3) * 3
                if a0 <= mouse_pos[a0] <= a1 and a0 <= mouse_pos[1] <= a1:
                    x = a0
                    y = a0
                elif a1 <= mouse_pos[a0] <= a2 and a0 <= mouse_pos[1] <= a1:
                    x = a0
                    y = 1
                elif a2 <= mouse_pos[a0] <= a3 and a0 <= mouse_pos[1] <= a1:
                    x = a0
                    y = 2
                elif a0 < mouse_pos[a0] < a1 and a1 < mouse_pos[1] < a2:
                    x = 1
                    y = a0
                elif a1 < mouse_pos[a0] < a2 and a1 < mouse_pos[1] < a2:
                    x = 1
                    y = 1
                elif a2 < mouse_pos[a0] < a3 and a1 < mouse_pos[1] < a2:
                    x = 1
                    y = 2
                elif a0 <= mouse_pos[a0] <= a1 and a2 <= mouse_pos[1] <= a3:
                    x = 2
                    y = a0
                elif a1 <= mouse_pos[a0] <= a2 and a2 <= mouse_pos[1] <= a3:
                    x = 2
                    y = 1
                elif a2 <= mouse_pos[a0] <= a3 and a2 <= mouse_pos[1] <= a3:
                    x = 2
                    y = 2

                # Check if spot is empty
                if board[x][y] == 0:
                    # Change game board
                    if turn == 1:
                        board[x][y] = 1
                    elif turn == -1:
                        board[x][y] = -1
                    # Change turns
                    turn *= -1
        if event.type == py.KEYDOWN and event.key == py.K_SPACE and (winner == 1 or winner == -1 or winner == 2):
            winner = 0
            for x in range(3):
                for y in range(3):
                    board[x][y] = 0
            current_square = 1
            turn = 1

    screen.fill(LIGHT_BLUE)

    for x in range(1, 3):
        py.draw.line(screen, WHITE, (0, x * (WIDTH // 3)), (WIDTH, x * (WIDTH // 3)), 6)
        py.draw.line(screen, WHITE, (x * (HEIGHT // 3), 0), (x * (HEIGHT // 3), HEIGHT), 6)

    for x in range(3):
        for y in range(3):
            if board[x][y] == 1:
                screen.blit(player_X, ((WIDTH // 3) * y, (WIDTH // 3) * x))
            elif board[x][y] == -1:
                screen.blit(player_O, ((WIDTH // 3) * y, (WIDTH // 3) * x))

    full = True
    for x in range(3):
        for y in range(3):
            if board[x][y] == 0:
                full = False
    if full and winner == 0:
        winner = 2

    # Selection
    if current_square == 1:
        selection_square.x = 0
        selection_square.y = 0
    elif current_square == 2:
        selection_square.x = WIDTH // 3 * 1
        selection_square.y = 0
    elif current_square == 3:
        selection_square.x = WIDTH // 3 * 2
        selection_square.y = 0
    elif current_square == 4:
        selection_square.x = 0
        selection_square.y = HEIGHT // 3 * 1
    elif current_square == 5:
        selection_square.x = WIDTH // 3 * 1
        selection_square.y = HEIGHT // 3 * 1
    elif current_square == 6:
        selection_square.x = WIDTH // 3 * 2
        selection_square.y = HEIGHT // 3 * 1
    elif current_square == 7:
        selection_square.x = 0
        selection_square.y = HEIGHT // 3 * 2
    elif current_square == 8:
        selection_square.x = WIDTH // 3 * 1
        selection_square.y = HEIGHT // 3 * 2
    elif current_square == 9:
        selection_square.x = WIDTH // 3 * 2
        selection_square.y = HEIGHT // 3 * 2

    py.draw.rect(screen, RED, selection_square, 4)

    # X-Player Win
    if board[1][1] == 1 and board[0][0] == 1 and board[2][2] == 1:
        py.draw.line(screen, RED, (0, 0), (WIDTH, HEIGHT), 20)
        winner = 1
    if board[1][1] == 1 and board[0][1] == 1 and board[2][1] == 1:
        py.draw.line(screen, RED, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 20)
        winner = 1
    if board[1][1] == 1 and board[0][2] == 1 and board[2][0] == 1:
        py.draw.line(screen, RED, (WIDTH, 0), (0, HEIGHT), 20)
        winner = 1
    if board[1][1] == 1 and board[1][0] == 1 and board[1][2] == 1:
        py.draw.line(screen, RED, (0, HEIGHT // 2), (WIDTH, HEIGHT // 2), 20)
        winner = 1
    if board[0][0] == 1 and board[0][1] == 1 and board[0][2] == 1:
        py.draw.line(screen, RED, (0, (HEIGHT // 3) // 2), (600, (HEIGHT // 3) // 2), 20)
        winner = 1
    if board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1:
        py.draw.line(screen, RED, ((HEIGHT // 3) // 2, 0), ((HEIGHT // 3) // 2, HEIGHT), 20)
        winner = 1
    if board[2][2] == 1 and board[1][2] == 1 and board[0][2] == 1:
        py.draw.line(screen, RED, (WIDTH - ((WIDTH // 3) // 2), HEIGHT), (WIDTH - ((WIDTH // 3) // 2), 0), 20)
        winner = 1
    if board[2][2] == 1 and board[2][1] == 1 and board[2][0] == 1:
        py.draw.line(screen, RED, (0, HEIGHT - ((HEIGHT // 3) // 2)), (WIDTH, HEIGHT - ((HEIGHT // 3) // 2)), 20)
        winner = 1
    # O-Player Win
    if board[1][1] == -1 and board[0][0] == -1 and board[2][2] == -1:
        py.draw.line(screen, RED, (0, 0), (WIDTH, HEIGHT), 20)
        winner = -1
    if board[1][1] == -1 and board[0][1] == -1 and board[2][1] == -1:
        py.draw.line(screen, RED, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 20)
        winner = -1
    if board[1][1] == -1 and board[0][2] == -1 and board[2][0] == -1:
        py.draw.line(screen, RED, (WIDTH, 0), (0, HEIGHT), 20)
        winner = -1
    if board[1][1] == -1 and board[1][0] == -1 and board[1][2] == -1:
        py.draw.line(screen, RED, (0, HEIGHT // 2), (WIDTH, HEIGHT // 2), 20)
        winner = -1
    if board[0][0] == -1 and board[0][1] == -1 and board[0][2] == -1:
        py.draw.line(screen, RED, (0, (HEIGHT // 3) // 2), (600, (HEIGHT // 3) // 2), 20)
        winner = -1
    if board[0][0] == -1 and board[1][0] == -1 and board[2][0] == -1:
        py.draw.line(screen, RED, ((HEIGHT // 3) // 2, 0), ((HEIGHT // 3) // 2, HEIGHT), 20)
        winner = -1
    if board[2][2] == -1 and board[1][2] == -1 and board[0][2] == -1:
        py.draw.line(screen, RED, (WIDTH - ((WIDTH // 3) // 2), HEIGHT), (WIDTH - ((WIDTH // 3) // 2), 0), 20)
        winner = -1
    if board[2][2] == -1 and board[2][1] == -1 and board[2][0] == -1:
        py.draw.line(screen, RED, (0, HEIGHT - ((HEIGHT // 3) // 2)), (WIDTH, HEIGHT - ((HEIGHT // 3) // 2)), 20)
        winner = -1

    if winner == 1:
        screen.blit(Player_X_Win_Text, (WIDTH // 2 - 150, HEIGHT // 2))
    elif winner == -1:
        screen.blit(Player_O_Win_Text, (WIDTH // 2 - 150, HEIGHT // 2))
    elif winner == 2:
        screen.blit(No_Winner, (WIDTH // 2 - 150, HEIGHT // 2))
    py.display.update()
