# 🎵 Music Generator
Generate music by providing a text prompt or an audio input.
<br><br>
<img src = "https://github.com/Kushmathur1206/Music-Generator/assets/99969817/447e552d-6951-4d3f-ba82-2bf56956c02d"  alt="Music Generator" width="500"/>
<br><br><br><br>
This project is an AI-powered music generation system that uses deep learning techniques to create original melodies. By training on musical sequences and learning patterns in note progression, it can autonomously generate short musical clips that are tuneful and unique.

🔍 Project Highlights
- Sequence Learning with LSTM
  Utilizes Long Short-Term Memory (LSTM) neural networks to learn temporal dependencies in musical notes.
  
- Custom Dataset
  Trained on a dataset of MIDI files, enabling the generation of stylistically coherent tunes.
  
- End-to-End Pipeline
  From data preprocessing to model training and MIDI generation, the project is a complete pipeline for music creation using AI.

💡 Use Cases for Emerging Brands & Creators
- Custom Music for Social Media Reels & Stories
- Small brands can auto-generate background music for Instagram reels, YouTube Shorts, and TikToks without needing to license expensive stock music.
- Use AI-generated jingles to develop a signature audio identity that plays in ads, intros, or product videos, enhancing brand recall.
- Run multi-video campaigns with different AI-generated background tracks to avoid repetition and keep content fresh and engaging.
- Startups and influencers can save time and money by generating royalty-free music instead of hiring a composer or buying music licenses.
- Personalized Music for Customer Experience
- E-commerce platforms can use AI-generated tunes for personalized thank-you pages, festive greetings, or even hold music during customer service calls.


<img src="https://github.com/user-attachments/assets/15917998-95c1-4648-b290-3c60a489e44e" alt="Music Generator" width="350"/><img src = "https://github.com/Kushmathur1206/Music-Generator/assets/99969817/1caa4f5f-896f-461c-9f46-ec89f8b2807c"  alt="Music Generator" width="400"/>


FOR MUSIC GENERATION USING AUDIO INPUT
LSTM-Based Music Model Training
Dataset Preparation(preprocess.py)
- Loads symbolic music files (.krn) using music21.
- Filters pieces based on acceptable note durations.
- Transposes music to a common key (C major / A minor).

Encoding & Transformation(preprocess.py)
- Converts musical notation into numerical sequences (MIDI-like format).
- Uses symbols (r for rests, _ for sustained notes).
- Stores encoded sequences for training.

Training the LSTM Model(train.py)
- Reads processed sequences and creates input-output pairs for training.
- Uses one-hot encoding to transform inputs.
- Trains an LSTM-based sequence model to predict the next musical note.
- Saves the trained model (model.h5) for later use.

Generating Music with Trained Model(generate.py)
- Takes a seed sequence as input.
- Predicts and extends sequences step-by-step.
- Outputs a structured symbolic composition.

Tech Stack
- TensorFlow/Keras – LSTM model for sequence prediction.
- music21 – Processing symbolic music notation.
- NumPy – Handling sequence encoding and mappings.
- Streamlit – UI for interacting with symbolic music generation.
![image](https://github.com/Kushmathur1206/Music-Generator/assets/99969817/268319c3-3602-45a3-a3a7-7d85d3cda070)
The training data for the model consists of a collection of piano Kern files obtained from the Deutschl dataset. 
Its task is be able to anticipate the next note in a sequence based on the notes it has already seen. 

FOR MUSIC GENERATION USING A PROMPT 
Meta's AudioCraft for prompt-to-Music Generation
It consists of two core components:
AudioGen – Sound Effect & Audio Generation
- Designed for text-to-audio conversion, generating realistic sound effects and instrumental tones.
- Uses deep learning models trained on various sound datasets to synthesize high-quality waveforms.
- Enables users to create custom sounds based on descriptive text inputs like "soft piano melody" or "ambient jazz tune."

MusicGen – Melody & Composition Generation
- Specialized for text-to-music creation, focusing on structured melodies, harmonies, and rhythms.
- Generates entire musical compositions based on user-defined styles, genres, and moods.
- Uses pre-trained models on diverse musical datasets to simulate human-like compositions.

Working
- User provides a text prompt describing the desired music.
- The model interprets the prompt and applies deep-learning techniques to synthesize audio.
- The system outputs a generated audio file that matches the described characteristics.
- The user can listen to or further refine the generated music.

Tech Stack
- Meta AudioCraft – AI-driven audio and music generation.
- Python – Backend integration for text prompt processing.
- Streamlit – Frontend interface for user interaction.


We use an open source library called audiocraft for the prompt to audio generation part.

<img src="https://github.com/Kushmathur1206/Music-Generator/assets/99969817/7244161c-309d-453a-ac87-3aa461eb1937" alt="Music Generator" width="400"/><img src = "https://github.com/Kushmathur1206/Music-Generator/assets/99969817/82567ec8-78e6-4a61-9589-9b47eabbbd33"  alt="Music Generator" width="400"/>

Music Generation can be done by desrcribing various factors like mood, theme, genre, era and many more.


Audiocraft is an advanced python library developed by Meta AI which utilizes various deep-learning approaches. It offers 2 main functionalities music generation and sound effect creation.
Music Generation can be done by dercribing various factors like mood, theme, genere, era and many more.
AudioGen is another audiocraft model used to generate sound effects on textual descriptions.




