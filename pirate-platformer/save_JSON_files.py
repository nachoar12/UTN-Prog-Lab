import json

# Paths to image files
image_paths = {
    "bgm_music": "assets/sounds/bgm.mp3",
    "coin_sound": "assets/sounds/coin.wav",
    "jump_sound": "assets/sounds/jump.mp3",
    "game_over_sound": "assets/sounds/game_over.mp3",
    "hurt_sound": "assets/sounds/hurt.mp3",
    "ranged_sound": "assets/sounds/ranged.mp3",
    "projectile_sound": "assets/sounds/projectile.mp3",
    "hit_sound": "assets/sounds/hit.mp3",
    "power_sound": "assets/sounds/power.mp3"


}

# Save the image paths to a JSON file
with open('sound_paths.json', 'w') as json_file:
    json.dump(image_paths, json_file, indent=4)
