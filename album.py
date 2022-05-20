
class Album:
    def __init__(self, album_name, release, uri):
        self.album_name = album_name
        self.release = release
        self.uri = uri
    
    def print_data(self):
        print(f"""        
    Album Name: {self.album_name}
    Release Date: {self.release}
    """)
