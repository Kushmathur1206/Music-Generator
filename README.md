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
  TensorFlow/Keras – LSTM model for sequence prediction.
  music21 – Processing symbolic music notation.
  NumPy – Handling sequence encoding and mappings.
  Streamlit – UI for interacting with symbolic music generation.


Generate music by providing a text prompt or an audio input.
![Screenshot (1458)](https://github.com/Kushmathur1206/Music-Generator/assets/99969817/447e552d-6951-4d3f-ba82-2bf56956c02d)


We use an open source library called audiocraft for the prompt to audio generation part.
![Screenshot (1460)](https://github.com/Kushmathur1206/Music-Generator/assets/99969817/7244161c-309d-453a-ac87-3aa461eb1937)


Music Generation can be done by desrcribing various factors like mood, theme, genre, era and many more.
![Screenshot (1459)](https://github.com/Kushmathur1206/Music-Generator/assets/99969817/82567ec8-78e6-4a61-9589-9b47eabbbd33)


FOR MUSIC GENERATION USNING AUDIO INPUT
![image](https://github.com/Kushmathur1206/Music-Generator/assets/99969817/268319c3-3602-45a3-a3a7-7d85d3cda070)
The training data for the model will consist of a collection of piano Kern files obtained from the Deutschl dataset. 
Its task is be able to anticipate the next note in a sequence based on the notes it has already seen. 
In our model training, we'll utilize three variables to encode a note: pitch, step, and duration.


FOR MUSIC GENERATION USING A PROMPT
![image](https://github.com/Kushmathur1206/Music-Generator/assets/99969817/1caa4f5f-896f-461c-9f46-ec89f8b2807c)
Audiocraft is an advanced python library developed by Meta AI which utilizes various deep-learning approaches. It offers 2 main functionalities music generation and sound effect creation.
Music Generation can be done by dercribing various factors like mood, theme, genere, era and many more.
AudioGen is another audiocraft model used to generate sound effects on textual descriptions.




