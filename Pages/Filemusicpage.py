from preprocess import *
import os
import json
import music21 as m21
import numpy as np
import tensorflow.keras as keras
import os
from pydub import AudioSegment
from melodygenerator import *
import streamlit as st
import time

def midi_to_wav(midi_file, soundfont, wav_file):
    # Convert MIDI to WAV using fluidsynth
    wav_file = wav_file.replace('.mid', '.wav')
    os.system(f'fluidsynth -ni {soundfont} {midi_file} -F {wav_file} -r 44100')
    audio = AudioSegment.from_wav(wav_file)
    audio.export(mp3_file, format='wav')

ACCEPTABLE_DURATIONS = [
    0.25, # 16th note
    0.5, # 8th note
    0.75,
    1.0, # quarter note
    1.5,
    2, # half note
    3,
    4 # whole note
]
encoded_song = "nope"

acceptable_durations = [
        0.25,  # 16th note
        0.5,   # 8th note
        0.75,
        1.0,   # quarter note
        1.5,
        2,     # half note
        3,
        4      # whole note
    ]

def quantize_duration(duration):
    """Quantize duration to the nearest acceptable duration."""
    acceptable_durations = [
        0.25,  # 16th note
        0.5,   # 8th note
        0.75,
        1.0,   # quarter note
        1.5,
        2,     # half note
        3,
        4      # whole note
    ]
    nearest_duration = min(acceptable_durations, key=lambda x: abs(x - duration))
    return nearest_duration

def quantize_song(song_kern):
    """Quantize the durations of notes and rests in the song."""
    # Parse KERN data into a music21.stream.Score object
    song = m21.converter.parseData(song_kern)

    # Quantize the durations of notes and rests
    for event in song.flatten().notesAndRests:  # Use .flatten() instead of .flat
        # handle notes
        if isinstance(event, m21.note.Note):
            event.duration.quarterLength = quantize_duration(event.duration.quarterLength)
        # handle rests
        elif isinstance(event, m21.note.Rest):
            event.duration.quarterLength = quantize_duration(event.duration.quarterLength)
    return song

def quantize_song(song_kern):
    """Quantize the durations of notes and rests in the song."""
    # Parse KERN data into a music21.stream.Score object
    song = m21.converter.parseData(song_kern)

    # Quantize the durations of notes and rests
    for event in song.flat.notesAndRests:  # Use .flatten() instead of .flat
        # handle notes
        if isinstance(event, m21.note.Note):
            original_duration = event.duration.quarterLength
            quantized_duration = quantize_duration(original_duration)
            print(f"Original duration: {original_duration}, Quantized duration: {quantized_duration}")
            event.duration.quarterLength = quantized_duration
        # handle rests
        elif isinstance(event, m21.note.Rest):
            original_duration = event.duration.quarterLength
            quantized_duration = quantize_duration(original_duration)
            print(f"Original duration: {original_duration}, Quantized duration: {quantized_duration}")
            event.duration.quarterLength = quantized_duration
    return song

def encode_midi_to_string(file_path):
    # Load MIDI file
    midi_stream = m21.converter.parse(file_path)

    encoded_notes = []

    # Iterate over notes and rests in the MIDI file
    for event in midi_stream.flat.notesAndRests:
        if isinstance(event, m21.note.Note):
            encoded_notes.append(str(event.pitch.midi))
        elif isinstance(event, m21.note.Rest):
            encoded_notes.append("r")

    # Join the encoded notes into a single string
    encoded_string = " ".join(encoded_notes)

    return encoded_string

def encode_song2(song, time_step=0.25):
    """Converts a score into a time-series-like music representation. Each item in the encoded list represents 'min_duration'
    quarter lengths. The symbols used at each step are: integers for MIDI notes, 'r' for representing a rest, and '_'
    for representing notes/rests that are carried over into a new time step. Here's a sample encoding:

        ["r", "_", "60", "_", "_", "_", "72" "_"]

    :param song (m21 stream): Piece to encode
    :param time_step (float): Duration of each time step in quarter length
    :return:
    """

    encoded_song = []
    symbol = None  # Initialize symbol

    for event in song.flat.notesAndRests:

        # handle notes
        if isinstance(event, m21.note.Note):
            symbol = event.pitch.midi  # 60
        # handle rests
        elif isinstance(event, m21.note.Rest):
            symbol = "r"

        # convert the note/rest into time series notation
        steps = int(event.duration.quarterLength / time_step)
        for step in range(steps):

            # if it's the first time we see a note/rest, let's encode it. Otherwise, it means we're carrying the same
            # symbol in a new time step
            if step == 0:
                encoded_song.append(symbol)
            else:
                encoded_song.append("_")

    # cast encoded song to str
    encoded_song = " ".join(map(str, encoded_song))

    return encoded_song


#song_test = "C:/Melody Generation using LSTM-RNN/deutschl/test/deut5149.krn"
#song_rel = "deutschl/test/deut5149.krn"

# Parse the Kern format file to obtain a music21 stream object
def func(song_test):
    song_stream = m21.converter.parse(song_test)
    #song_stream = quantize_song(song_stream)

    #if has_acceptable_durations(song_stream, ACCEPTABLE_DURATIONS):
    if has_acceptable_durations(song_stream, ACCEPTABLE_DURATIONS):
        song_stream = transpose(song_stream)
        # encode songs with music time series representation
        encoded_song = encode_song2(song_stream)

    return encoded_song

st.set_page_config(
    page_icon= "🎵",
    page_title= "Music Generator",
    initial_sidebar_state="collapsed"
)
video_html = """
		<style>

		#myVideo {
		  position: fixed;
		  right: 0;
		  bottom: 0;
		  min-width: 100%; 
		  min-height: 100%;
		}

		.content {
		  position: fixed;
		  bottom: 0;
		  background: rgba(0, 0, 0, 0.5);
		  color: #f1f1f1;
		  width: 80%;
		  padding: 20px;
		}

		</style>	
		<video autoplay muted loop id="myVideo">
		  <source src="https://cdn.pixabay.com/video/2022/10/12/134486-759714562_large.mp4")>
		  Your browser does not support HTML5 video.
		</video>
        """

st.markdown(video_html, unsafe_allow_html=True)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

def main():

    st.title("Music Generator 🎵")

# Initialize the MelodyGenerator
    mg = MelodyGenerator()

    uploaded_file = st.file_uploader("Upload MIDI or Kern file", type=["mid", "midi", "krn", "kern", "wav"])

    # Generate button
    if uploaded_file is not None:
        # Save the uploaded file
        if st.button("Generate"):
            progress_text = "Music Generation in progress. Please wait."
            my_bar = st.progress(0, text=progress_text)
            file_path = "input_file"
            for percent_complete in range(0,25):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1, text=progress_text)
            file_ext = os.path.splitext(uploaded_file.name)[1].lower()
            for percent_complete in range(25,100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1, text=progress_text)
            if file_ext in [".mid", ".midi", ".krn", ".kern", ".wav"]:
                file_path += file_ext
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getvalue())
            
                # Generate melody
                res = func(file_path)
                melody = mg.generate_melody(res, num_steps=500, max_sequence_length=SEQUENCE_LENGTH, temperature=0.3)
                
                # Save melody to file
                mg.save_melody(melody, file_name="output.mid")
                with open("output.mid", "rb") as file:
                    st.download_button(label="Download generated melody", data=file, file_name="output.mid", mime="audio/midi")
                # Example usage:
                # Display success message
                st.success("Melody generated and saved as output.mid")
                
            else:
                st.error("Unsupported file format. Please upload a MIDI or Kern file.")
            my_bar.empty()

if __name__ == "__main__":
    main()