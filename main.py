import pygame
from assets import load_fonts, load_sounds, load_settings
from menu import show_menu

def main():
    pygame.init()
    settings = load_settings()
    flags = pygame.RESIZABLE if settings["display_mode"] == "windowed" else pygame.FULLSCREEN
    screen = pygame.display.set_mode((1280, 720), flags)
    pygame.display.set_caption("Ash of Vireth")
    clock = pygame.time.Clock()

    fonts = load_fonts()
    sounds = load_sounds()
    current_mode = settings["display_mode"]

    def switch_mode(new_mode):
        nonlocal current_mode
        current_mode = new_mode

    while True:
        show_menu(screen, clock, fonts, sounds, switch_mode)

if __name__ == "__main__":
    main()