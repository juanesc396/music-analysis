import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


# Credentials that you can generate on https://developer.spotify.com/
client_id = ''
client_secret = ''

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# This class work with the library spotipy: https://github.com/plamere/spotipy
class MusicAnalysis():
    def searcher(name):
        """
        This function search an artist 
        """
        a = sp.search(name, type='artist', limit=5, market='US')
        count = 0
        while count <5:        
            temp_name = a['artists']['items'][count]['name']
            temp_genres = a['artists']['items'][count]['genres']
            temp_uri = a['artists']['items'][count]['uri']
            
            c = int(input(f'Is {temp_name} the artist are you searching for? \n Enter 1 for YES \n 2 for search again \n 3 for cancel \n '))

            if c == 1:
                temp = {'artist': temp_name, 'genres': temp_genres, 'uri': temp_uri}
                return temp
            elif c == 2:
                count = count + 1
            elif c == 3:
                quit()
            else:
                print('Enter a valid option.')     

    
    def song_analysis(song):
        """
        This function extract the most important data from songs
        """
        
        temp = {}
        features = sp.audio_features(song)
        
        temp['duration_s'] = features[0]['duration_ms']/1000
        temp['key'] = features[0]['key']
        temp['mode'] = features[0]['mode']
        temp['tempo'] = features[0]['tempo']
        temp['time_signature'] = features[0]['time_signature']
        temp['valence'] = features[0]['valence']
        temp['energy'] = features[0]['energy']
        temp['loudness'] = features[0]['loudness']
        temp['speechiness'] = features[0]['speechiness']
        temp['acousticness'] = features[0]['acousticness']
        temp['instrumentalness'] = features[0]['instrumentalness']
        temp['liveness'] = features[0]['liveness']

        if temp['mode'] == 1:
            temp['mode'] = 'Major'
        elif temp['mode'] == 0:
            temp['mode'] = 'Minor'
        else:
            pass

        if temp['key'] == -1:
            temp['key'] = 'No result.'
        else:
            pitch_class = ['C', 'C♯ - D-bemol','D', 'D♯, E-bemol', 'E', 'F', 'F♯, G-bemol', 'G', 'G♯, A-bemol', 'A', 'G♯, A-bemol', 'B']
            temp['key'] = pitch_class[temp['key']]

        return temp

   
    def extract_albums_data(ref):
        """
        This function extracts the most important data from the artist's albums. 
        """
        
        new_data = sp.artist_albums(ref, album_type='album', market='US')
        extract_data = []
        for i in new_data['items']:
            temp = {}
            temp['name'] = i['name']
            temp['uri'] = i['uri']
            temp['release_date'] = i['release_date']
            extract_data.append(temp)
        
        return extract_data


    def extract_singles_data(ref):
        """
        This function extracts the most important data from the artist's singles. 
        """
        
        new_data = sp.artist_albums(ref, album_type='single', market='US')
        extract_data = []
        for i in new_data['items']:
            temp = {}
            temp['name'] = i['name']
            temp['uri'] = i['uri']
            temp['release_date'] = i['release_date']
            extract_data.append(temp)
        
        return extract_data


    def extract_songs_data(album):
        """
        This function extracts the most important data songs from the artist's albums. 
        """
        new_album_data = sp.album_tracks(album)
        extract_data = []
        for i in new_album_data['items']:
            temp = {}
            temp['name'] = i['name']
            temp['uri'] = i['uri']
            extract_data.append(temp)
        
        return extract_data
