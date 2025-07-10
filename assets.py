import pygame
import json
import os

SETTINGS_PATH = "config/settings.json"

def load_fonts():
    return {
        "large": pygame.font.Font("assets/fonts/retro.ttf", 60),
        "medium": pygame.font.Font("assets/fonts/retro.ttf", 48),
        "small": pygame.font.Font("assets/fonts/retro.ttf", 42)
    }

def load_sounds():
    pygame.mixer.init()
    return {
        "hover": pygame.mixer.Sound("assets/sounds/hover.wav"),
        "select": pygame.mixer.Sound("assets/sounds/select.wav")
    }

def save_settings(settings):
    os.makedirs(os.path.dirname(SETTINGS_PATH), exist_ok=True)
    with open(SETTINGS_PATH, "w") as f:
        json.dump(settings, f)

def load_settings():
    if os.path.exists(SETTINGS_PATH):
        with open(SETTINGS_PATH, "r") as f:
            return json.load(f)
    return {"display_mode": "windowed"}