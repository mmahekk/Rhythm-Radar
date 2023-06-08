# RhythmRadar

# Background
Spotify is the world’s most popular audio streaming platform with over 11 million artists and creators
and almost 500 million users. With over 100 million tracks from various genres on the platform, the app
allows users to not only listen to their favourite music, but also allows users to create and save playlists
based on their preferences. In order to suggest new tracks to users, Spotify’s current recommendation
integrates collaborative filtering with content-based filtering. To create user-tailored recommendations,
collaborative filtering examines a user’s listening history. On the other hand, content-based filtering suggests music based on the features of a track, akin to mood, genre and danceability (Marius, 2021).

# Problem Context and Motivation
Due to the platform’s large catalogue of songs, it can make users feel overwhelmed and increase the difficulty of discovering new music and artists. Regardless of Spotify’s endeavours to curate personalized
music recommendations, it can nevertheless be difficult for Spotify users to find new music, specifically
from underground musicians. The primary reason for this is due to the platform’s recommendation algorithm being built to give preference to popular mainstream music and artists to attract a wider audience.
For instance, many of Spotify’s playlist recommendations are created by the platform’s team or influential
users, which tend to give spotlight to well-established artists. The exposure and publicity of a track on
Spotify is significantly influenced by these playlists in addition to the recommendation algorithm especially. Hence, underground and new artists are underrepresented on the platform, as it is difficult to get
their music featured on these curated playlists, due to fewer resources and finances, which limits their
possibilities of reaching new listeners (Mitchell, 2022).

# Goal
To address this issue, we seek to develop a music recommendation system that curates playlists
from the users preferred playlist while simultaneously putting emphasis on underground
songs to support small and emerging musicians. The new algorithm will suggest a playlist of ten
songs by lesser-known artists using a myriad of song features, such as energy, danceability, valence, loudness and popularity from the user’s current playlist, compared to the songs in the spotify database. From
the user’s playlist, we will randomly select ten songs to perform computations on, and in return a total of
ten new songs based on these ten songs will be returned to the user
