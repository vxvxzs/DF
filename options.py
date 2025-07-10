import pygame
from assets import save_settings

def show_options(screen, clock, fonts, sounds, current_mode):
    options = ["Fullscreen", "Windowed"]
    selected = 0 if current_mode == "fullscreen" else 1
    running = True

    while running:
        screen.fill((20, 20, 40))
        title = fonts["medium"].render("Graphics Mode", True, (255, 255, 200))
        screen.blit(title, (screen.get_width() // 2 - title.get_width() // 2, 100))

        for i, option in enumerate(options):
            color = (255, 255, 255) if i == selected else (100, 100, 100)
            text = fonts["small"].render(option, True, color)
            screen.blit(text, (screen.get_width() // 2 - 100, 200 + i * 70))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    sounds["select"].play()
                    mode = "fullscreen" if selected == 0 else "windowed"
                    if mode == "fullscreen":
                        pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
                    else:
                        pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
                    save_settings({"display_mode": mode})
                    return mode
                elif event.key == pygame.K_ESCAPE:
                    return current_mode