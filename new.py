from preprocess import *
import os
import json
import music21 as m21
import numpy as np
import tensorflow.keras as keras
import os
from pydub import AudioSegment

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
