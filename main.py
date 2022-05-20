from req import MusicAnalysis

from album import Album
from artist import Artist
from song import Song

if __name__ == '__main__':
    
    # Initiator
    while True:
        print("\n\n")
        print('Welcome to Music Analyzer!')
        print('With simple steps you can access to all Spotify Music Data!')
        print('To start you will enter an artist, then, with numbers, you will select the data.')
        print('Enjoy!!')
        while True:
            artist_to_search = input('Search an Artist:')
            if artist_to_search:
                r = MusicAnalysis.searcher(artist_to_search)
                Artist.artist_name = r['artist']
                Artist.genres = r['genres']
                Artist.uri = r['uri']
                Artist.print_data()
                break
            else:
                print('Enter a valid name: ')
                continue

        albums_list = []
        idx_album = []
        songs_list = []
        idx_songs = []
        # 
        while True:
            for idx, data in enumerate(MusicAnalysis.extract_albums_data(Artist.uri)):
                albums_list.append(Album(data['name'], data['release_date'], data['uri']))
                idx_album.append(idx)
                print(f'{idx} - {data["name"]}')
            
            a = input('Enter a number to select an album to analize. Type \"back\" to return to select artist: ')
            if a == "back":
                print('\n\n')
                break
            
            elif int(a) in idx_album:
                a = int(a)
                while True:
                    albums_list[a].print_data()
                    for idx, data in enumerate(MusicAnalysis.extract_songs_data(albums_list[a].uri)):
                        songs_list.append(Song(data['name'], data['uri'], MusicAnalysis.song_analysis(data['uri'])))
                        idx_songs.append(idx)
                        print(f'{idx} - {data["name"]}')
            
                    select = input('Enter a number to select a song to analize. Type \"back\" to return to select album: ')
                    if select == "back":
                        print('\n\n')
                        break
                    elif int(select) in idx_songs:
                        select = int(select)
                        songs_list[select].print_data()
                        input('Press any key to return to albums: ')
