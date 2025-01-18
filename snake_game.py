import pygame
import random
import time

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 35)

# Snake and food properties
block_size = 20
snake_speed = 15

def draw_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], block_size, block_size])

def game_loop():
    game_over = False
    game_close = False

    x1 = WIDTH // 2
    y1 = HEIGHT // 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, WIDTH - block_size) / block_size) * block_size
    foody = round(random.randrange(0, HEIGHT - block_size) / block_size) * block_size

    score = 0

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            message = font.render("Game Over! Press C to Play Again or Q to Quit", True, RED)
            screen.blit(message, [WIDTH / 6, HEIGHT / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [foodx, foody, block_size, block_size])
        
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(block_size, snake_list)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, [0, 0])
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - block_size) / block_size) * block_size
            foody = round(random.randrange(0, HEIGHT - block_size) / block_size) * block_size
            length_of_snake += 1
            score += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

if __name__ == "__main__":
    game_loop()
