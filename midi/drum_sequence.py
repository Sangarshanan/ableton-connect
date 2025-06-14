import time
from utils import send_notes, midi_out

# Drums: Yakiman Kit

kick = 36
snare = 38
clap = 39
hihat = 42
cymbal = 46


def send_multiple_notes(notes):
    """
    Send multiple notes simultaneously
    """
    if notes:
        print(f"Playing notes: {', '.join(map(str, notes))}")
        # Actually trigger each note with no delay between them
        for note in notes:
            send_notes(note, sleep_time=0)

def play_drum_beat(bars=4):
    """
    Play a chill lofi beat with proper timing.
    """
    print("Starting chill lofi beat...")
    
    sixteenth_note = 0.1875  # seconds
    
    for bar in range(bars):
        print(f"\nBar {bar+1}")
        
        # Basic pattern: 16 steps per bar
        for step in range(16):
            current_notes = []
            
            # Kick pattern for lofi
            if step == 0 or step == 7 or step == 11:
                current_notes.append(kick)
            
            # Snare & Clap on beats 2 and 4
            if step == 4 or step == 12:
                current_notes.append(snare)
                current_notes.append(clap)
            
            # Hi-hat pattern: 8th notes, skipping when snare hits for simplicity
            if step % 2 == 0 and step not in [4, 12]:
                current_notes.append(hihat)
            
            # Cymbal (soft crash) at the start of every 4-bar phrase
            if bar % 4 == 0 and step == 0:
                current_notes.append(cymbal)
                    
            # Play all notes for this step simultaneously
            send_multiple_notes(current_notes)
            
            # Wait for the next 16th note
            time.sleep(sixteenth_note)

if __name__ == "__main__":
    # Uncomment the beat pattern you want to play
    midi_out.open_port(0)
    play_drum_beat(10)
