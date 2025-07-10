import pygame
import sys
from menu import show_menu

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Ash of Vireth")
clock = pygame.time.Clock()

def main():
    show_menu(screen, clock)

if __name__ == "__main__":
    main()