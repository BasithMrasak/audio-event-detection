# 🎧 Audio Event Detection using Deep Learning (ESC-50)

This project implements an end-to-end audio event detection system that classifies environmental sounds into predefined categories using a Convolutional Neural Network (CNN).

The system is trained and evaluated on the ESC-50 environmental sound dataset and supports inference through a simple Flask-based web interface where users can upload an audio file and receive a predicted sound event.

The project includes data loading, augmentation, log-mel spectrogram feature extraction, CNN training, test-fold evaluation, and a web UI for live predictions.

# Project Structure

```audio-event-detection/
│
├── audio-event-detection.ipynb   # End-to-end training + evaluation notebook
├── app/
│   ├── app.py                    # Flask inference server
│   └── templates/
│       └── index.html            # UI page
├── models/
│   └── best_model.pt             # Trained model
├── src/
│   └── dataset.py                # ESC-50 dataset indexing utilities
└── README.md
```

# Setup Instructions

# 1.Clone the repository
`git clone https://github.com/BasithMrasak/audio-event-detection.git
cd audio-event-detection`

# 2.Install dependencies
pip install torch librosa numpy pandas scikit-learn flask tqdm matplotlib

# 3.Dataset setup
Download the ESC-50 dataset and place it in your system (or Google Drive if using Colab).

Inside the training notebook, update the dataset path:
`ESC50_ROOT = "/path/to/ESC-50-master"`

# 4.Training and evaluation
Training and evaluation: audio-event-detection.ipynb

This notebook contains:

=> dataset loading

=> data augmentation

=> feature extraction

=> model training

=> test fold evaluation

=> ROC-AUC, confusion matrix and classification metrics

The best model is saved as: best_model.pt

# 5.Running the web application
Move the trained model into: models/best_model.pt

Then run:
cd app
python app.py

Open in browser: http://127.0.0.1:5000
Upload a .wav file to get the predicted sound class.

# Solution Approach
=>Audio preprocessing

Each audio file is resampled to 22,050 Hz and converted into a
log-mel spectrogram representation.

=>Data augmentation

To improve generalization, the training pipeline applies:

random time shifting

additive noise

SpecAugment (time and frequency masking)

Augmentation is applied only to the training split.

=>Model architecture

A CNN is used to process log-mel spectrograms as 2D inputs.
The network consists of multiple convolutional blocks followed by
global average pooling and fully connected layers.

=>Training strategy

Cross-entropy loss

Adam optimizer

Best model is selected using test-fold accuracy

Model checkpoints are saved during training

=>Evaluation

The model is evaluated on the ESC-50 test fold using:

accuracy

precision, recall and F1-score

confusion matrix

macro-averaged ROC-AUC (one-vs-rest)

macro ROC curve

top-5 accuracy

=>Deployment

A Flask web interface allows users to upload an audio file, performs
log-mel feature extraction and runs the trained CNN to predict the
sound event.


