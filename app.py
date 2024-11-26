import streamlit as st
import requests
import base64
import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler

st.title('ML-Based Music Recommendation - BeatBot')

# Spotify Credentials
CLIENT_ID = '06efd7289817442293ffea29b7962ce5'
CLIENT_SECRET = '55119dd838f644ca98159fddaa886a6d'

# Function to get Spotify API access token
def get_access_token(client_id, client_secret):
    auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    token_url = 'https://accounts.spotify.com/api/token'
    data = {'grant_type': 'client_credentials'}
    headers = {'Authorization': f'Basic {auth_header}'}
    response = requests.post(token_url, data=data, headers=headers)
    return response.json().get('access_token') if response.status_code == 200 else None

# Function to search for a track
def search_track(track_name, access_token):
    headers = {"Authorization": f"Bearer {access_token}"}
    url = "https://api.spotify.com/v1/search"
    params = {"q": track_name, "type": "track", "limit": 1}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        items = data.get('tracks', {}).get('items', [])
        if items:
            track = items[0]
            return {
                'id': track['id'],
                'name': track['name'],
                'poster': track['album']['images'][0]['url'],
                'preview': track['preview_url']
            }
    return None

# Function to get audio features
def get_audio_features(track_id, access_token):
    headers = {"Authorization": f"Bearer {access_token}"}
    url = f"https://api.spotify.com/v1/audio-features/{track_id}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return None

# Function to build a custom KNN model
def build_knn_model(track_data):
    features = np.array([
        [
            track['danceability'],
            track['energy'],
            track['tempo'],
            track['valence']
        ]
        for track in track_data
    ])
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    model = NearestNeighbors(n_neighbors=10, metric='cosine')
    model.fit(features_scaled)
    return model, scaler

# Function to recommend songs using the trained model
def recommend_songs(base_features, track_data, model, scaler):
    base_scaled = scaler.transform([[
        base_features['danceability'],
        base_features['energy'],
        base_features['tempo'],
        base_features['valence']
    ]])
    distances, indices = model.kneighbors(base_scaled)
    recommendations = [track_data[i] for i in indices[0]]
    return recommendations

# Load pre-collected Spotify track data
def load_track_data(access_token):
    # Example: Fetch a pre-collected dataset of Spotify tracks and their features
    # Ideally, you would have a dataset of track IDs to query and retrieve features
    all_tracks = []
    track_ids = [
        "3n3Ppam7vgaVa1iaRUc9Lp", "0rYTfL0v1cEhzIA7eC8Dqo", "1dNIEtp7AY3oDAKCGg2XkH"
    ]
    for track_id in track_ids:
        features = get_audio_features(track_id, access_token)
        if features:
            all_tracks.append({
                'id': track_id,
                'name': f"Track {track_id}",
                'poster': "https://via.placeholder.com/150",  # Placeholder image
                'preview': None,
                'danceability': features['danceability'],
                'energy': features['energy'],
                'tempo': features['tempo'],
                'valence': features['valence']
            })
    return all_tracks

# App Interface
selected_music_name = st.text_input('Enter a song you like:')
if st.button('Get Recommendations'):
    access_token = get_access_token(CLIENT_ID, CLIENT_SECRET)
    if access_token:
        # Search for the base track
        base_track = search_track(selected_music_name, access_token)
        if base_track:
            st.subheader('Your Selected Track')
            st.text(base_track['name'])
            st.image(base_track['poster'])
            st.markdown(
                f'<audio src="{base_track["preview"]}" controls style="width: 100%;"></audio>',
                unsafe_allow_html=True
            )

            # Fetch all track data
            track_data = load_track_data(access_token)

            # Build a custom model
            knn_model, scaler = build_knn_model(track_data)

            # Get audio features of the base track
            audio_features = get_audio_features(base_track['id'], access_token)
            if audio_features:
                # Recommend songs
                recommendations = recommend_songs(audio_features, track_data, knn_model, scaler)

                if recommendations:
                    st.subheader('Recommended Tracks')
                    for track in recommendations:
                        col1, col2 = st.columns([1, 3])
                        with col1:
                            st.image(track['poster'], width=100)
                            st.text(track['name'])
                        with col2:
                            if track['preview']:
                                st.markdown(
                                    f'<audio src="{track["preview"]}" controls style="width: 100%;"></audio>',
                                    unsafe_allow_html=True
                                )
                else:
                    st.write("No recommendations found.")
        else:
            st.write("Song not found.")
    else:
        st.write("Failed to authenticate with Spotify.")