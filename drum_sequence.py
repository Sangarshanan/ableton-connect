import time
from utils import send_notes

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
    Play a more complex techno beat with variations and build-ups
    with proper timing
    """
    print("Starting advanced techno beat...")
    
    # Set the timing for 16th notes at 128 BPM
    sixteenth_note = 0.117  # seconds
    
    for bar in range(bars):
        print(f"\nBar {bar+1}")
        
        # Create build-up effect in the last bar
        is_final_bar = (bar == bars - 1)
        
        # Basic pattern: 16 steps per bar
        for step in range(16):
            # Collect all notes that should play at this step
            current_notes = []
            
            # Four-on-the-floor kick pattern
            if step % 4 == 0:
                current_notes.append(kick)
            
            # Progressive hi-hat pattern that gets more intense
            if bar < 2:
                # Simple off-beat hi-hats in first two bars
                if step % 2 == 1:
                    current_notes.append(hihat)
            else:
                # More complex hi-hat pattern in later bars
                if step % 2 == 0 and step % 4 != 0:
                    current_notes.append(hihat)
                elif step % 2 == 1:
                    current_notes.append(hihat)
            
            # Snare/clap combination on beats 5 and 13
            if step == 4 or step == 12:
                current_notes.append(snare)
                current_notes.append(clap)
                
                # In the final bar, add more snare hits for build-up
                if is_final_bar and step > 8:
                    current_notes.append(snare)  # Double snare for emphasis
            
            # Cymbal on certain beats to create variation
            if step % 8 == 7 or (is_final_bar and step % 4 == 3):
                current_notes.append(cymbal)
            
            # Add extra kick drum embellishments in the third bar
            if bar == 2 and (step == 2 or step == 10 or step == 14):
                current_notes.append(kick)
            
            # Add drum roll effect in the final bar's final beats
            if is_final_bar and step >= 12 and step % 2 == 0:
                current_notes.append(hihat)
                    
            # Play all notes for this step simultaneously
            send_multiple_notes(current_notes)
            
            # Wait for the next 16th note
            time.sleep(sixteenth_note)

if __name__ == "__main__":
    # Uncomment the beat pattern you want to play
    # play_techno_beat(4)
    play_drum_beat(10)