import pygame
import platform
from pathlib import Path

class AudioManager:
    """Audio manager with web compatibility and user interaction handling"""

    def __init__(self):
        self.is_web = platform.system() == "Emscripten"
        self.sounds_enabled = True
        self.audio_unlocked = False
        self.sounds = {}

        self.init_audio()

    def init_audio(self):
        """Initialize audio with web-compatible settings"""
        try:
            if self.is_web:
                # Web-optimized settings
                pygame.mixer.pre_init(
                    frequency=44100,  # Higher frequency for better web support
                    size=-16,
                    channels=2,
                    buffer=512  # Smaller buffer for web
                )

            pygame.mixer.init()
            print("Audio initialized successfully")

        except pygame.error as e:
            print(f"Audio initialization failed: {e}")
            self.sounds_enabled = False

    def load_sound(self, name, filepath):
        """Load a sound with error handling"""
        if not self.sounds_enabled:
            return False

        try:
            if not Path(filepath).exists():
                print(f"Sound file not found: {filepath}")
                return False

            sound = pygame.mixer.Sound(filepath)
            sound.set_volume(0.7)  # Default volume
            self.sounds[name] = sound
            print(f"Loaded sound: {name}")
            return True

        except pygame.error as e:
            print(f"Failed to load sound {name}: {e}")
            return False

    def unlock_audio(self):
        """Unlock audio context for web browsers"""
        if not self.audio_unlocked and self.sounds_enabled:
            try:
                # Play a silent sound to unlock audio context
                if self.sounds:
                    first_sound = next(iter(self.sounds.values()))
                    first_sound.set_volume(0)
                    first_sound.play()
                    first_sound.set_volume(0.7)

                self.audio_unlocked = True
                print("Audio context unlocked")

            except Exception as e:
                print(f"Failed to unlock audio: {e}")

    def play_sound(self, name, volume=None):
        """Play a sound safely"""
        if not self.sounds_enabled or name not in self.sounds:
            return

        # Auto-unlock on first interaction
        if not self.audio_unlocked:
            self.unlock_audio()

        try:
            sound = self.sounds[name]
            if volume is not None:
                sound.set_volume(volume)
            sound.play()

        except pygame.error as e:
            print(f"Failed to play sound {name}: {e}")
            # Don't disable sounds completely, just this attempt failed

    def set_volume(self, name, volume):
        """Set volume for a specific sound"""
        if name in self.sounds:
            self.sounds[name].set_volume(volume)

    def disable_audio(self):
        """Disable audio completely"""
        self.sounds_enabled = False
        print("Audio disabled")
