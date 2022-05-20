class Song:
    def __init__(self, name, uri = None, analysis = None):
        self.name = name
        self.uri = uri
        self.analysis = analysis
    

    def print_data(self):
        print(f"""
    Song Name: {self.name}
        
    Musical Analysis:
    
- Duration: {self.analysis['duration_s']}
- Key: {self.analysis['key']}
- Mode: {self.analysis['mode']}
- Tempo: {self.analysis['tempo']}
- Time Signature: {self.analysis['time_signature']}
- Valence: {self.analysis['valence']}
- Energy: {self.analysis['energy']}
- Loudness: {self.analysis['loudness']}
- Spechiness: {self.analysis['speechiness']}
- Acousticness: {self.analysis['acousticness']}
- Instrumentalness: {self.analysis['instrumentalness']}
- Liveness: {self.analysis['liveness']}
        """)
