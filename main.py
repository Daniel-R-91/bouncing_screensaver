import pygame

pygame.init()

screen_height = 600
screen_width = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("SCREENSAVER")

font = pygame.font.Font(None, 50)
text_surface = font.render("HELLOWORLD", True, (255, 255, 255))
text_rect = text_surface.get_rect(topleft=(0, 0))

is_running = True
clock = pygame.time.Clock()

speed_x = 2
speed_y = 2

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    screen.fill((0, 0, 0))
    screen.blit(text_surface, text_rect)

    text_rect.x += speed_x
    text_rect.y += speed_y

    if text_rect.right >= screen_width or text_rect.left <= 0:
        speed_x *= -1

    if text_rect.bottom >= screen_height or text_rect.top <= 0:
        speed_y *= -1

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
