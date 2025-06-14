import random
import time  # Added for rhythmic timing
from utils import send_notes, midi_out

# --- Configuration for Key and Scale (C Major) ---
SCALE_C_MAJOR = {
    60: "C4", 62: "D4", 64: "E4", 65: "F4", 67: "G4", 69: "A4", 71: "B4",
    72: "C5"
}
SCALE_NOTES_C_MAJOR = list(SCALE_C_MAJOR.keys())
SCALE_ROOT_C_MAJOR = 60

# Markov chain specifically for C Major
# Transitions aim to be diatonic and reasonably melodic.
MARKOV_CHAIN_C_MAJOR = {
    60: [62, 64, 67],          # C4 -> D4, E4, G4
    62: [60, 64, 65],          # D4 -> C4, E4, F4
    64: [62, 65, 67, 60],      # E4 -> D4, F4, G4, C4
    65: [64, 67, 60, 72],      # F4 -> E4, G4, C4, C5
    67: [65, 69, 60, 72],      # G4 -> F4, A4, C4, C5
    69: [67, 71, 64],          # A4 -> G4, B4, E4
    71: [69, 72, 67],          # B4 -> A4, C5, G4
    72: [71, 69, 67, 65, 60]   # C5 -> B4, A4, G4, F4, C4 (more options for variety from octave)
}

def generate_markov_sequence(start_pitch=SCALE_ROOT_C_MAJOR, length=20, chain=MARKOV_CHAIN_C_MAJOR, scale_root=SCALE_ROOT_C_MAJOR):
    """Generates a sequence of pitches using a Markov chain, staying within a key."""
    sequence = [start_pitch]
    current_pitch = start_pitch
    for _ in range(length - 1):
        possible_next_pitches = chain.get(current_pitch)
        if not possible_next_pitches:
            # Fallback if current pitch isn't in chain or has no transitions defined
            # This could happen if start_pitch is not in the chain keys.
            # Or, choose randomly from all scale notes as a broader fallback.
            next_pitch = random.choice(list(chain.keys())) # Choose a random valid starting note from the chain
        else:
            next_pitch = random.choice(possible_next_pitches)
        
        sequence.append(next_pitch)
        current_pitch = next_pitch
    return sequence

# --- Configuration for Rhythm and Structure ---
QUARTER_NOTE_DURATION = 1.5

NUM_LOOPS = 300      # How many times the 4-bar phrase repeats
BARS_PER_LOOP = 4  # Each phrase is 4 bars long
NOTES_PER_BAR = 4  # Playing 4 quarter notes per bar

# Generate a sequence of pitches for the entire piece
total_notes_needed = NUM_LOOPS * BARS_PER_LOOP * NOTES_PER_BAR
pitches = generate_markov_sequence(start_pitch=random.choice(SCALE_NOTES_C_MAJOR), length=total_notes_needed)
pitch_idx = 0

if __name__ == "__main__":
    try:
        midi_out.open_port(1)
        for loop_num in range(NUM_LOOPS):
            print(f"  Melody Loop {loop_num + 1}/{NUM_LOOPS}")
            for bar_num in range(BARS_PER_LOOP):
                # print(f"    Bar {bar_num + 1}/{BARS_PER_LOOP}")
                for note_in_bar_num in range(NOTES_PER_BAR):
                    if pitch_idx < len(pitches):
                        current_pitch = pitches[pitch_idx]
                        note_on_duration = QUARTER_NOTE_DURATION * 0.8 
                        rhythmic_slot_duration = QUARTER_NOTE_DURATION
                        print(f"Playing pitch: {current_pitch}, ON for: {note_on_duration:.2f}s, Slot: {rhythmic_slot_duration:.2f}s")
                        send_notes(pitch=current_pitch,
                                   repeat=1,
                                   sleep_time=note_on_duration)
                        time_to_sleep_for_rhythm = rhythmic_slot_duration - note_on_duration
                        if time_to_sleep_for_rhythm > 0:
                            time.sleep(time_to_sleep_for_rhythm)
                        pitch_idx += 1
                    else:
                        print("Melody sequence finished early (all generated pitches played).")
                        break 
                if pitch_idx >= len(pitches): break
            if pitch_idx >= len(pitches): break
        
        print("Generative melody playback complete.")

    except Exception as e:
        print(f"An error occurred in generative_melody: {e}")
    finally:
        if midi_out.is_port_open():
            midi_out.close_port()
