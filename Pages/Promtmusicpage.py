import streamlit as st
from audiocraft.models import MusicGen
import streamlit as st 
import torch 
import torchaudio
import os 
import numpy as np
import base64
import os
from melodygenerator import *
from IPython.display import Audio
import streamlit as st
from new import *
from midi2audio import FluidSynth
import time


@st.cache_resource



def load_model():
    model = MusicGen.get_pretrained('facebook/musicgen-small')
    return model

def generate_music_tensors(description, duration: int):
    print("Description: ", description)
    print("Duration: ", duration)
    model = load_model()

    model.set_generation_params(
        use_sampling=True,
        top_k=250,
        duration=duration
    )

    output = model.generate(
        descriptions=[description],
        progress=True,
        return_tokens=True
    )

    return output[0]


def save_audio(samples: torch.Tensor):
    """Renders an audio player for the given audio samples and saves them to a local directory.

    Args:
        samples (torch.Tensor): a Tensor of decoded audio samples
            with shapes [B, C, T] or [C, T]
        sample_rate (int): sample rate audio should be displayed with.
        save_path (str): path to the directory where audio should be saved.
    """

    print("Samples (inside function): ", samples)
    sample_rate = 32000
    save_path = "audio_output/"
    assert samples.dim() == 2 or samples.dim() == 3

    samples = samples.detach().cpu()
    if samples.dim() == 2:
        samples = samples[None, ...]

    for idx, audio in enumerate(samples):
        audio_path = os.path.join(save_path, f"audio_{idx}.wav")
        torchaudio.save(audio_path, audio, sample_rate)

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href

st.set_page_config(
    page_icon= "🎵",
    page_title= "Music Generator"
)
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://images.pexels.com/photos/3784566/pexels-photo-3784566.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
background-size: 100%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

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

    text_area = st.text_area("Enter your song description.......")
    time_slider = st.slider("Select time duration (In Seconds)", 0, 20, 10)

    if text_area and time_slider:
        st.json({
            'Your Description': text_area,
            'Selected Time Duration (in Seconds)': time_slider
        })
        if st.button("Generate song"):
            progress_text = "Music Generation in progress. Please wait."
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(0,25):
                time.sleep(0.05)
                my_bar.progress(percent_complete + 1, text=progress_text)
            
            st.subheader("Generated Music")
            for percent_complete in range(25,80):
                time.sleep(0.05)
                my_bar.progress(percent_complete + 1, text=progress_text)
            music_tensors = generate_music_tensors(text_area, time_slider)
            print("Musci Tensors: ", music_tensors)
            for percent_complete in range(80,90):
                time.sleep(0.05)
                my_bar.progress(percent_complete + 1, text=progress_text)
            save_music_file = save_audio(music_tensors)
            audio_filepath = 'audio_output/audio_0.wav'
            audio_file = open(audio_filepath, 'rb')
            audio_bytes = audio_file.read()
            for percent_complete in range(90,100):
                time.sleep(0.05)
                my_bar.progress(percent_complete + 1, text=progress_text)
            st.audio(audio_bytes)
            st.markdown(get_binary_file_downloader_html(audio_filepath, 'Audio'), unsafe_allow_html=True)
            time.sleep(1)
            my_bar.empty()


if __name__ == "__main__":
    main()
    


