
import random

def get_astrological_data(date):
    return {
        "moon_phase": random.choice(["Full Moon", "New Moon", "Waning"]),
        "saturn_position": random.randint(0, 360),
        "pluto_position": random.randint(0, 360)
    }
