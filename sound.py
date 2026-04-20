try:
    # winsound is Windows-only; safe to ignore IDE warnings
    import winsound
    SOUND_AVAILABLE = True
except ImportError:
    SOUND_AVAILABLE = False

class SoundManager:
    @staticmethod
    def click():
        if SOUND_AVAILABLE:
            winsound.Beep(800, 80)

    @staticmethod
    def win():
        if SOUND_AVAILABLE:
            winsound.Beep(1000, 150)
            winsound.Beep(1200, 150)

    @staticmethod
    def draw():
        if SOUND_AVAILABLE:
            winsound.Beep(600, 300)

    @staticmethod
    def restart():
        if SOUND_AVAILABLE:
            winsound.Beep(700, 100)
