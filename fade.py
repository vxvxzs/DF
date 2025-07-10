import pygame

def fade_in(screen, speed=5):
    fade = pygame.Surface((screen.get_width(), screen.get_height()))
    fade.fill((0, 0, 0))
    for alpha in range(255, -1, -speed):
        fade.set_alpha(alpha)
        screen.fill((0, 0, 0))
        screen.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(30)