from pythonosc.udp_client import SimpleUDPClient

ip = "127.0.0.1"
to_ableton = 11000
from_ableton = 11001
client = SimpleUDPClient(ip, to_ableton)

# Set tempo
client.send_message("/live/song/set/tempo", [140])

# Create clip
client.send_message("/live/clip_slot/create_clip", (0, 0, 4))

# Send notes
client.send_message("/live/clip/add/notes", (0, 0,
                                                60, 0.0, 0.25, 64, False,
                                                67, -0.25, 0.5, 32, False))
client.send_message("/live/clip/add/notes", (0, 0,
                                                72, 0.0, 0.25, 64, False,
                                                60, 3.0, 0.5, 32, False))

# Fire up the clip
client.send_message("/live/clip/fire", (0, 0))

# # Stop the clips
# client.send_message("/live/song/stop_all_clips", None)
