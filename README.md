# BeatBot: ML-Based Music Recommendation System 🎵

BeatBot is a music recommendation system built with **Streamlit** that utilizes **Spotify's API** to find songs similar to your favorite track. It leverages machine learning (KNN) to suggest music based on audio features like danceability, energy, tempo, and valence.

---

## Features 🚀

1. **Track Search**  
   Search for a song you like using Spotify's extensive library.

2. **Audio Features Analysis**  
   Analyze Spotify's audio features (danceability, energy, tempo, valence) for a given track.

3. **Music Recommendations**  
   Get up to 10 song recommendations based on a custom-trained K-Nearest Neighbors (KNN) model.

4. **Interactive Player**  
   Listen to track previews and view album art directly in the app.

---

## How It Works 🛠️

1. The app authenticates with Spotify using its **Client ID** and **Client Secret**.
2. Users enter the name of a track they like.
3. The app retrieves audio features for the selected track.
4. A pre-collected dataset of Spotify tracks is used to build a KNN model.
5. Recommendations are generated based on the similarity of the audio features.
6. Results (with preview and album art) are displayed interactively.

---

## Installation 📥

1. Clone this repository:  
   ```bash
   git clone https://github.com/TejasX2004/bea.git
