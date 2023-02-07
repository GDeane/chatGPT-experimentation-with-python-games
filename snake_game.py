import random
import time

WIDTH = 30
HEIGHT = 20

def initial_snake(snake):
    x = WIDTH // 2
    y = HEIGHT // 2
    snake.append((x, y))
    return snake

def move_snake(snake, direction):
    x, y = snake[-1]
    if direction == "left":
        x -= 1
    elif direction == "right":
        x += 1
    elif direction == "up":
        y -= 1
    elif direction == "down":
        y += 1
    snake.append((x, y))
    return snake

def generate_food(snake, food):
    while True:
        x = random.randint(0, WIDTH-1)
        y = random.randint(0, HEIGHT-1)
        if (x, y) not in snake:
            food.append((x, y))
            break
    return food

def draw_game(snake, food):
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if (j, i) in snake:
                print("S", end="")
            elif (j, i) in food:
                print("F", end="")
            else:
                print(" ", end="")
        print()
    print()

def main():
    snake = []
    food = []
    snake = initial_snake(snake)
    food = generate_food(snake, food)

    while True:
        draw_game(snake, food)
        direction = input("Enter direction (left, right, up, down): ")
        snake = move_snake(snake, direction)
        if snake[-1] in food:
            food = generate_food(snake, food)
        else:
            snake.pop(0)
        if snake[-1][0] == 0 or snake[-1][0] == WIDTH-1 or snake[-1][1] == 0 or snake[-1][1] == HEIGHT-1:
            print("Game Over")
            break
        time.sleep(0.5)

if __name__ == "__main__":
    main()
