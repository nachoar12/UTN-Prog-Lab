import pygame
import json
import sys
import os
import sqlite3
# functions for the game


def draw_text(text, font, text_color, x, y, screen):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))

# functions to load different types of files


def load_images_from_json(json_file_path):
    images = {}
    abs_dir = os.path.abspath(os.getcwd())
    try:
        with open(json_file_path, 'r') as json_file:
            image_paths = json.load(json_file)
            for key, path in image_paths.items():
                try:
                    abs_path = os.path.join(abs_dir, path)
                    images[key] = pygame.image.load(abs_path)
                except (pygame.error, FileNotFoundError, ValueError) as image_error:
                    print(f"Error loading image '{key}': {image_error}")
                    pygame.quit()
                    sys.exit()
    except (FileNotFoundError, json.JSONDecodeError) as file_error:
        print(f"Error opening or reading JSON file: {file_error}")
    return images


def load_sounds_from_json(json_file_path):
    sounds = {}
    pygame.mixer.init()
    abs_dir = os.path.abspath(os.getcwd())
    try:
        with open(json_file_path, 'r') as json_file:
            sound_paths = json.load(json_file)
            for key, path in sound_paths.items():
                try:
                    abs_path = os.path.join(abs_dir, path)
                    sounds[key] = pygame.mixer.Sound(abs_path)
                except (pygame.error, FileNotFoundError, ValueError) as sound_error:
                    print(f"Error loading sound '{key}': {sound_error}")
                    pygame.quit()
                    sys.exit()
    except (FileNotFoundError, json.JSONDecodeError) as file_error:
        print(f"Error opening or reading JSON file: {file_error}")
    return sounds

conn = sqlite3.connect('game_register.db')
cursor = conn.cursor()

def save_player_data(name, score, max_level):
    cursor.execute('''
        INSERT INTO players (name, score, max_level)
        VALUES (?, ?, ?)
    ''', (name, score, max_level))
    conn.commit()

def get_best_results(quantity):
    cursor.execute('''
        SELECT name, MAX(score) as max_score, MAX(max_level) as max_level
        FROM players
        GROUP BY name
        ORDER BY max_score DESC, max_level DESC
        LIMIT ?
    ''', (quantity,))
    resultados = cursor.fetchall()
    return resultados


