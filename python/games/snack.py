import tkinter as tk
import pygame
import random

# Pygame 실행 함수
def run_snake_game():
    pygame.init()

    # 화면 크기
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("지렁이 게임")

    # 색상 설정
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (200, 0, 0)
    green = (0, 200, 0)

    # 게임 설정
    block_size = 20
    speed = 15
    clock = pygame.time.Clock()

    font = pygame.font.SysFont(None, 35)

    # 점수 표시
    def show_score(score):
        value = font.render(f"Score: {score}", True, white)
        screen.blit(value, [10, 10])

    # 게임 루프
    def game_loop():
        x = screen_width // 2
        y = screen_height // 2
        x_change = 0
        y_change = 0

        snake = [[x, y]]
        snake_length = 1

        food_x = random.randint(0, (screen_width - block_size) // block_size) * block_size
        food_y = random.randint(0, (screen_height - block_size) // block_size) * block_size

        running = True
        game_over = False

        while running:
            while game_over:
                screen.fill(black)
                message = font.render("Game Over! Press C to Restart or Q to Quit", True, red)
                screen.blit(message, [screen_width // 8, screen_height // 3])
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            running = False
                            game_over = False
                        if event.key == pygame.K_c:
                            game_loop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and x_change == 0:
                        x_change = -block_size
                        y_change = 0
                    elif event.key == pygame.K_RIGHT and x_change == 0:
                        x_change = block_size
                        y_change = 0
                    elif event.key == pygame.K_UP and y_change == 0:
                        y_change = -block_size
                        x_change = 0
                    elif event.key == pygame.K_DOWN and y_change == 0:
                        y_change = block_size
                        x_change = 0

            x += x_change
            y += y_change

            if x < 0 or x >= screen_width or y < 0 or y >= screen_height:
                game_over = True

            screen.fill(black)
            pygame.draw.rect(screen, green, [food_x, food_y, block_size, block_size])

            snake.append([x, y])
            if len(snake) > snake_length:
                del snake[0]

            for block in snake[:-1]:
                if block == [x, y]:
                    game_over = True

            for block in snake:
                pygame.draw.rect(screen, white, [block[0], block[1], block_size, block_size])

            if x == food_x and y == food_y:
                food_x = random.randint(0, (screen_width - block_size) // block_size) * block_size
                food_y = random.randint(0, (screen_height - block_size) // block_size) * block_size
                snake_length += 1

            show_score(snake_length - 1)
            pygame.display.update()
            clock.tick(speed)

        pygame.quit()

    game_loop()

# Tkinter GUI
def start_game():
    root.destroy()
    run_snake_game()

root = tk.Tk()
root.title("지렁이 게임")
root.geometry("300x200")

label = tk.Label(root, text="지렁이 게임", font=("Arial", 16))
label.pack(pady=20)

start_button = tk.Button(root, text="게임 시작", command=start_game, font=("Arial", 12), bg="lightblue")
start_button.pack(pady=20)

root.mainloop()
