"""
CSC111 Winter 2023 Final Project
RhythmRadar: Underground Song Recommendation System
A module that contains the computations on the similarity between songs.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of the CSC111 course department
at the University of Toronto St. George campus. All forms of distribution of this code,
whether as given or with any changes, are strictly prohibited. For more information on
copyright for CSC111 project materials, please consult our Course Syllabus.

This file is Copyright (c) 2023 of Mahek Cheema, Kelsang Tsomo, Olindi Mallika Appuhamilage, and Bea Alyssandra Castro
"""
from typing import Any
import math
import random
import playlist as plist

class Computations(plist.Playlist):
    """"
    A class that represents all computations for calculating the distance of the user's current song and the current
    dataset csv song.
    """

    def __init__(self) -> None:
        """Initialize this playlist."""
        super().__init__()

    def remove_out_of_range(self, user_songs: list[str]) -> dict[str: list[tuple[str, plist.Channel]]]:
        """Remove the songs that do not have any channels.
        A song without channels means there were either no songs from the dataset that were within the user's songs'
        danceability, valence, energy, and loudness or the similar song found from the dataset is the same song from
        the user's playlist.
        """
        total_songs = {}

        for u in user_songs:
            channels = []
            for c in self._songs[u].channels:
                channel = self._songs[u].channels[c]
                channels.append((c, channel))
            total_songs[u] = channels
        return total_songs

    def similar_song_helper(self, user_id: str, total_songs: dict[str: list[tuple[str, plist.Channel]]]) \
            -> list[tuple[str, float]]:
        """Append the minimum distances to lst_so_far and then append the end_point ids to end_point_ids."""
        distance_lst = []

        for channel_tuple in total_songs[user_id]:
            channel_id = channel_tuple[0]
            channel = channel_tuple[1]
            user_song = self._songs[user_id]

            end_point = channel.get_other_endpoint(user_song)
            distance = self.euclidean_distance(user_song.valence, end_point.valence,
                                               user_song.danceability, end_point.danceability)

            next_distance = self.euclidean_distance(user_song.energy, end_point.energy,
                                                    user_song.loudness, end_point.loudness)
            total_distance = distance + next_distance
            distance_lst.append((channel_id, total_distance))
        return distance_lst

    def compute_similar_song(self, total_songs: dict[str: list[tuple[str, plist.Channel]]]) -> \
            dict[str: list[tuple[str, float]]]:
        """Return the dictionary mapping the song id of a song from the user's playlist to a tuple containing
        the song id of a similar song from the dataset to the

        >>> # https://open.spotify.com/playlist/10RDYOInFIIVTUC98kA8qW?si=8d4e3b1907ad4dc6
        >>> c = Computations()
        >>> us = c.get_playlist_songs()
        >>> dataset_songs = c.get_dataset_songs()
        >>> c.get_songs_in_range(us, dataset_songs)
        >>> ts = c.remove_out_of_range(us)
        >>> sim_songs = c.compute_similar_song(ts)
        >>> import pprint
        >>> pprint.pprint(sim_songs)
        """
        dict_so_far = {}
        for s in total_songs:
            user_song_lst = self.similar_song_helper(s, total_songs)
            dict_so_far[s] = user_song_lst
        return dict_so_far

    def euclidean_distance(self, x1: float, y1: float, x2: float, y2: float) -> float:
        """Returns the float value representing the distance between the user's song and the current song
        from our spotify dataset.
        """
        return math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

    def sort_similar_songs(self, sp: Any, playlist_URI: Any) -> Any:
        """Return the songs that are similar to the user song  by checking through whether the genres of the dataset song
        is in the genre of the input song. It also compares popularity score and returns top ten songs added to the
        recommended songs list"""

        recommend_song = []
        user_songs = self.get_playlist_songs()
        nums = []
        popularity_score = []
        songs_so_far = []
        dataset_songs = self.get_dataset_songs()
        self.get_songs_in_range(user_songs, dataset_songs)
        total_songs = self.remove_out_of_range(user_songs)
        similar_songs = self.compute_similar_song(total_songs)

        # loop through similar songs and their distances
        for song, distances in similar_songs.items():
            for distance in distances:
                song_id, dist = distance

                # check if song genres overlap with user's genres
                common_genres = set(self._songs[song].genres) & set(self._songs[song_id].genres)

                if common_genres:
                    # get the distance for the common genre(s)
                    common_genre_dists = [d for s, d in distances if set(self._songs[s].genres) & common_genres]
                    common_genre_dists.sort()
                    common_genre_dist = common_genre_dists[0]

                    # add the song to the recommendation if it's the closest one for a common genre
                    if dist == common_genre_dist and self._songs[song_id].id not in recommend_song:
                        recommend_song.append(self._songs[song_id].id)

                else:
                    # add the distance and popularity score to their respective lists
                    nums.append(dist)
                    popularity_score.append(self._songs[song_id].popularity)

        # sort distances and popularity scores
        popular_songs = sorted(popularity_score)
        smallest_distance = sorted(nums)

        # add the songs with the smallest distance and popularity score to songs_so_far
        for i in range(min(len(popular_songs), len(smallest_distance))):
            choose_randomly = random.choice([smallest_distance[i], popular_songs[i]])
            for song, distances in similar_songs.items():
                for distance in distances:
                    if distance[0] == choose_randomly or self._songs[distance[0]].popularity == choose_randomly:
                        songs_so_far.append(distance[0])

        # add more songs from songs_so_far to the recommendation if necessary
        if len(recommend_song) < 10:
            for i in range(0, 10 - len(recommend_song)):
                recommend_song.append(songs_so_far[i])

        return recommend_song[:10]


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['math', 'playlist', 'random'],  # the names (strs) of imported modules
        'disable': ['too-many-branches'],
        'allowed-io': [],  # the names (strs) of functions that call
        'max-line-length': 120
    })
