## Algorithmic music with Python on Ableton

To start with we need to enable communication with ableton. This can be done using "Inter-Application Communication" A driver developed by Apple for their operating systems which allows data to be shared between softwares within the same operating system

- Goto Audio Midi Setup
- Click on Windows -> Show MIDI studio
- Goto IAC Driver (It should be greyed out)
	- Make sure to check the box: Device is Online
	- Add a few MIDI Ports
	- Apply changes
- Goto the MIDI tracks on Ableton and change "MIDI From" from "All Ins" to "IAC Driver (Bus 1)"
- Add a different channel for different MIDI tracks/ Instruments

Now our ableton setup is ready, We just need to send data through Python

Generative melodies with Markov chains

```sh
python generative_melody.py
```
