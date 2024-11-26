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
   git clone https://github.com/TejasX2004/Music-Recommendation.git
   ```
2. Install Dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app
   ```bash
   streamlit run app.py
   ```
## Configuration

To use the Spotify API, you need to set up a developer account and create an app to obtain Client ID and Client Secret.

1. Go to the Spotify Developer Dashboard.

2. Create a new app and note down the Client ID and Client Secret.

3. Replace the placeholders in the app.py file with your credentials:
   ```python
   CLIENT_ID = 'your_client_id'
   CLIENT_SECRET = 'your_client_secret'
   ```
## Usage 🎶
1. Enter the name of a song in the search bar.
2. Click Get Recommendations.
3. View your selected song's details, including a preview.
3. Browse through recommended tracks and listen to previews.

## Preview
![photo-collage png](https://github.com/user-attachments/assets/15f726b6-51de-4fda-997b-255b25b53284)


##Acknowledgments 🙏
1. Spotify API for providing the foundation for this project.
2. The open-source community for libraries like Streamlit and scikit-learn.
