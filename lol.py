liked_songs = {'Khelani': 'Folded', 'SZA': 'Another Life', 'Kendrick Lamar': 'luther',
               'SZA': 'Get Behind Me', 'Pink Pantheress': 'Pain', 'Pink Pantheress': 'Illegal'
               }


def write_liked_songs_to_file(liked_songs, file_name):
    with open(file_name, 'w') as file:
        file.write('Liked Songs:\n')
        for artist, song in liked_songs.items():
            file.write(f' {song} by {artist}\n')


write_liked_songs_to_file(liked_songs, "liked_songs.txt")
