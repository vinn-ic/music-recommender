# Spotify Recent Tracks Analyzer & Recommender

![Python](https://img.shields.io/badge/python-3.8%2B-blue)

A Python script that fetches your recently played tracks from Spotify and generates music recommendations based on your listening habits (genres and artists).

## Features

- � Fetches your recently played tracks from Spotify Web API
- 🧠 Analyzes your listening patterns (top genres, frequent artists)
- 💡 Generates personalized music recommendations
- 🔒 Secure OAuth 2.0 authentication


## Prerequisites

Before you begin, ensure you have:

- Python 3.8 or higher installed
- A Spotify developer account
- Registered your application on Spotify Developer Dashboard to get:
  - `SPOTIPY_CLIENT_ID`
  - `SPOTIPY_CLIENT_SECRET`
  - `SPOTIPY_REDIRECT_URI`
- internet connection
  ## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/vinn-ic/music-recommender.git

2. Install the required packages:
  ```bash
  pip instal spotipy
  ```
3. Create a .env file in the root directory with your credentials:
   ```bash
     CLIENT_ID=yourkey
     CLIENT_SECRET=yourkey
   ```
