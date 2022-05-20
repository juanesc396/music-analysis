
class Artist:
    def __init__(self, artist_name, genres, members, uri):
        self.artist_name = artist_name
        self.genres = genres
        self.members = members
        self.uri = uri
    
    def print_data():
        print(f"""
    Artist: {Artist.artist_name}        
    Genres: {Artist.genres}   
    """)
