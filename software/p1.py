import os
import random
import pygame

def play_random_songs(directory):
    # Get a list of all files in the specified directory
    files = os.listdir(directory)
    
    # Filter the files to include only audio files (e.g., mp3, wav)
    audio_files = [file for file in files if file.endswith((".mp3", ".wav"))]
    
    # Initialize the pygame mixer
    pygame.mixer.init()
    
    while True:
        # Randomly select a song from the audio files list
        song = random.choice(audio_files)
        
        # Get the full path of the song file
        song_path = os.path.join(directory, song)
        
        # Load and play the song
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        
        # Print the currently playing song
        print("Now playing:", song)
        
        # Wait until the song finishes playing
        while pygame.mixer.music.get_busy():
            continue

# Specify the directory containing your songs
songs_directory = "songs"

# Play random songs from the directory infinitely
play_random_songs(songs_directory)

