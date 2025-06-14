import time
import rtmidi

midi_out = rtmidi.MidiOut()

def send_notes(pitch=60, repeat=1, sleep_time=0.5, port=0):
    """Sends MIDI notes to the specified track."""
    for _ in range(repeat):
        note_on = [0x90, pitch, 112]  # 0x90 is Note On, add channel
        note_off = [0x80, pitch, 0]  # 0x80 is Note Off, add channel
        midi_out.send_message(note_on)
        time.sleep(sleep_time)
        midi_out.send_message(note_off)
