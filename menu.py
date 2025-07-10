import pygame
import sys
import math
from knight_intro import knight_intro

# Retro font path (replace with actual .ttf path)
FONT_PATH = "assets/fonts/retro.ttf"

def draw_text_with_box(screen, text, font, x, y, text_color, box_color, hover=False):
    text_surface = font.render(text, True, text_color)
    padding = 15 if hover else 10
    box_rect = pygame.Rect(
        x - padding,
        y - padding,
        text_surface.get_width() + 2 * padding,
        text_surface.get_height() + 2 * padding
    )
    pygame.draw.rect(screen, box_color, box_rect, border_radius=10)
    screen.blit(text_surface, (x, y))

def show_menu(screen, clock):
    font = pygame.font.Font(FONT_PATH, 60)
    small_font = pygame.font.Font(FONT_PATH, 42)

    menu_options = ["New Game", "Options", "Exit"]
    selected = 0

    background = pygame.image.load("assets/backgrounds/menu_bg.png").convert()
    zoom_factor = 1.4
    bg_w, bg_h = background.get_width(), background.get_height()
    zoomed_bg = pygame.transform.smoothscale(
        background,
        (int(bg_w * zoom_factor), int(bg_h * zoom_factor))
    )

    blur_scale = 0.3
    small_bg = pygame.transform.smoothscale(
        zoomed_bg,
        (int(zoomed_bg.get_width() * blur_scale), int(zoomed_bg.get_height() * blur_scale))
    )
    blurred_bg = pygame.transform.smoothscale(
        small_bg,
        (zoomed_bg.get_width(), zoomed_bg.get_height())
    )

    bg_x, bg_y = 0, 0
    t = 0

    pygame.mixer.init()
    hover_sound = pygame.mixer.Sound("assets/sounds/hover.wav")
    select_sound = pygame.mixer.Sound("assets/sounds/select.wav")

    last_selected = selected

    while True:
        t += 0.01
        bg_x = int((zoomed_bg.get_width() - screen.get_width()) / 2 + 20 * math.sin(t))
        bg_y = int((zoomed_bg.get_height() - screen.get_height()) / 2 + 10 * math.cos(t * 0.7))

        screen.blit(blurred_bg, (-bg_x, -bg_y))

        title = font.render("ASH OF VIRETH", True, (255, 255, 200))
        title_shadow = font.render("ASH OF VIRETH", True, (50, 50, 50))
        screen.blit(title_shadow, (screen.get_width()//2 - title.get_width()//2 + 3, 103))
        screen.blit(title, (screen.get_width()//2 - title.get_width()//2, 100))

        for i, option in enumerate(menu_options):
            color = (255, 255, 255) if i == selected else (150, 150, 150)
            box_color = (30, 30, 50) if i == selected else (20, 20, 40)
            hover = i == selected
            draw_text_with_box(
                screen,
                option,
                small_font,
                screen.get_width()//2 - 100,
                250 + i * 70,
                color,
                box_color,
                hover=hover
            )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    select_sound.play()
                    if selected == 0:
                        select_character(screen, clock)
                    elif selected == 1:
                        show_options(screen, clock)
                    elif selected == 2:
                        pygame.quit()
                        sys.exit()

        if last_selected != selected:
            hover_sound.play()
            last_selected = selected

        pygame.display.flip()
        clock.tick(60)

def select_character(screen, clock):
    font = pygame.font.Font(FONT_PATH, 48)
    title_font = pygame.font.Font(FONT_PATH, 44)
    classes = ["Knight", "Mage", "Dwarf"]
    selected = 0

    pygame.mixer.init()
    hover_sound = pygame.mixer.Sound("assets/sounds/hover.wav")
    select_sound = pygame.mixer.Sound("assets/sounds/select.wav")

    last_selected = selected

    while True:
        screen.fill((15, 15, 30))
        title_text = title_font.render("Select Your Story", True, (255, 255, 200))
        screen.blit(title_text, (screen.get_width()//2 - title_text.get_width()//2, 100))

        spacing = screen.get_width() // (len(classes) + 1)

        for i, char_class in enumerate(classes):
            color = (255, 255, 255) if i == selected else (100, 100, 100)
            box_color = (30, 30, 50) if i == selected else (20, 20, 40)
            hover = i == selected
            x = spacing * (i + 1) - font.render(char_class, True, color).get_width() // 2
            y = 300 if i == selected else 320
            draw_text_with_box(screen, char_class, font, x, y, color, box_color, hover=hover)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    selected = (selected - 1) % len(classes)
                elif event.key == pygame.K_RIGHT:
                    selected = (selected + 1) % len(classes)
                elif event.key == pygame.K_RETURN:
                    select_sound.play()
                    if classes[selected] == "Knight":
                        knight_intro(screen, clock)
                elif event.key == pygame.K_ESCAPE:
                    return

        if last_selected != selected:
            hover_sound.play()
            last_selected = selected

        pygame.display.flip()
        clock.tick(60)

def show_options(screen, clock):
    font = pygame.font.Font(FONT_PATH, 48)
    options = ["Fullscreen", "Windowed"]
    selected = 0

    pygame.mixer.init()
    hover_sound = pygame.mixer.Sound("assets/sounds/hover.wav")
    select_sound = pygame.mixer.Sound("assets/sounds/select.wav")

    last_selected = selected

    while True:
        screen.fill((20, 20, 40))
        title = font.render("Graphics Mode", True, (255, 255, 200))
        screen.blit(title, (screen.get_width()//2 - title.get_width()//2, 100))

        for i, opt in enumerate(options):
            color = (255, 255, 255) if i == selected else (100, 100, 100)
            box_color = (30, 30, 50) if i == selected else (20, 20, 40)
            hover = i == selected
            draw_text_with_box(
                screen,
                opt,
                font,
                screen.get_width()//2 - 100,
                200 + i * 70,
                color,
                box_color,
                hover=hover
            )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    select_sound.play()
                    if options[selected] == "Fullscreen":
                        pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
                    else:
                        pygame.display.set_mode((1280, 720))
                    return
                elif event.key == pygame.K_ESCAPE:
                    return


        if last_selected != selected:
            hover_sound.play()
            last_selected = selected

        pygame.display.flip()
        clock.tick(60)