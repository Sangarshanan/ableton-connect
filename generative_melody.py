import random
from utils import send_notes

# Define a simple Markov chain for pitches
markov_chain = {
    60: [62, 64, 67],  # C -> D, E, G
    62: [60, 64],     # D -> C, E
    64: [60, 62, 67, 69],  # E -> C, D, G, A
    67: [60, 64, 69, 72],  # G -> C, E, A, C (octave higher)
    69: [64, 67, 72],  # A -> E, G, C
    72: [67, 69]      # C -> G, A
}

def generate_markov_sequence(start_pitch=60, length=20):
    """Generates a sequence of pitches using a Markov chain."""
    sequence = [start_pitch]
    current_pitch = start_pitch
    for _ in range(length - 1):
        next_pitch = random.choice(markov_chain.get(current_pitch, [60]))  # Default to C if no transition
        sequence.append(next_pitch)
        current_pitch = next_pitch
    return sequence

# Generate a sequence of pitches using the Markov chain
pitches = generate_markov_sequence(start_pitch=60, length=1000)

# Send each pitch to the send_notes function
for pitch in pitches:
    send_notes(pitch=pitch, repeat=1, sleep_time=random.uniform(0.1, 0.5))
