import pygame
import sys
import math
from knight_intro import knight_intro
from options import show_options

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

def show_menu(screen, clock, fonts, sounds, switch_mode_callback):
    menu_options = ["New Game", "Options", "Exit"]
    selected = 0
    if "New Game" found, 
        menu_options = ["Continue", "New Game", "Options", "Exit"]

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

    t = 0
    last_selected = selected

    while True:
        t += 0.01
        bg_x = int((zoomed_bg.get_width() - screen.get_width()) / 2 + 20 * math.sin(t))
        bg_y = int((zoomed_bg.get_height() - screen.get_height()) / 2 + 10 * math.cos(t * 0.7))

        screen.blit(blurred_bg, (-bg_x, -bg_y))

        title = fonts["large"].render("ASH OF VIRETH", True, (255, 255, 200))
        title_shadow = fonts["large"].render("ASH OF VIRETH", True, (50, 50, 50))
        screen.blit(title_shadow, (screen.get_width()//2 - title.get_width()//2 + 3, 103))
        screen.blit(title, (screen.get_width()//2 - title.get_width()//2, 100))

        for i, option in enumerate(menu_options):
            color = (255, 255, 255) if i == selected else (150, 150, 150)
            box_color = (30, 30, 50) if i == selected else (20, 20, 40)
            hover = i == selected
            draw_text_with_box(
                screen,
                option,
                fonts["small"],
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
                    sounds["select"].play()
                    if selected == 0:
                        select_character(screen, clock, fonts, sounds)
                    elif selected == 1:
                        new_mode = show_options(screen, clock, fonts, sounds, "windowed")
                        switch_mode_callback(new_mode)
                    elif selected == 2:
                        pygame.quit()
                        sys.exit()

        if last_selected != selected:
            sounds["hover"].play()
            last_selected = selected

        pygame.display.flip()
        clock.tick(60)

def select_character(screen, clock, fonts, sounds):
    classes = ["Knight", "Mage", "Dwarf"]
    selected = 0
    last_selected = selected

    while True:
        screen.fill((15, 15, 30))
        title_text = fonts["medium"].render("Select Your Story", True, (255, 255, 200))
        screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, 100))

        spacing = screen.get_width() // (len(classes) + 1)

        for i, char_class in enumerate(classes):
            color = (255, 255, 255) if i == selected else (100, 100, 100)
            box_color = (30, 30, 50) if i == selected else (20, 20, 40)
            hover = i == selected
            x = spacing * (i + 1) - fonts["small"].render(char_class, True, color).get_width() // 2
            y = 300 if i == selected else 320
            draw_text_with_box(screen, char_class, fonts["small"], x, y, color, box_color, hover=hover)

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
                    sounds["select"].play()
                    if classes[selected] == "Knight":
                        knight_intro(screen, clock)
                    elif classes[selected] == "Mage":
                        pass  # mage_intro(screen, clock)
                    elif classes[selected] == "Dwarf":
                        pass  # dwarf_intro(screen, clock)
                elif event.key == pygame.K_ESCAPE:
                    return

        if last_selected != selected:
            sounds["hover"].play()
            last_selected = selected

        pygame.display.flip()
        clock.tick(60)