import pygame
import time
from fade import fade_in

def knight_intro(screen, clock):
    fade_in(screen)

    font = pygame.font.Font(None, 50)
    text = font.render("1385 Esghalord", True, (255, 255, 255))
    text_surface = pygame.Surface(text.get_size(), pygame.SRCALPHA)
    text_surface.blit(text, (0, 0))
    for alpha in range(0, 256, 5):
        screen.fill((0, 0, 0))  
        text_surface.set_alpha(alpha)
        screen.blit(text_surface, (screen.get_width()//2 - text.get_width()//2, screen.get_height()//2))
        pygame.display.flip()
        clock.tick(30) 

    time.sleep(1)

    for alpha in range(255, -1, -5):
        screen.fill((0, 0, 0))  
        text_surface.set_alpha(alpha)
        screen.blit(text_surface, (screen.get_width()//2 - text.get_width()//2, screen.get_height()//2))
        pygame.display.flip()
        clock.tick(30)  