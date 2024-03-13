import urllib.request
import re
def get_youtube_url(song_name: str, artist_name: str) -> str:
     
    """
     Generate YouTube URL for a given song name and artist name.

     Args:
     song_name (str): Name of the song.
     artist_name (str): Name of the artist.

     Returns:
     str: YouTube URL for the song.
    

    """
    
    formatted_song = '+'.join(song_name.split())
    formatted_artist = '+'.join(artist_name.split())

    # Construct YouTube URL
    youtube_search_url = f"https://www.youtube.com/results?search_query={formatted_song}+{formatted_artist}"
    html = urllib.request.urlopen(youtube_search_url)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    count=0
    
    youtube_url=[]
    
    for vid in video_ids:
        vids="https://www.youtube.com/watch?v=" + vid
        if vids not in youtube_url:
            
            youtube_url.append("https://www.youtube.com/watch?v=" + vid)
            if len(youtube_url)==3:
                break
            

    
    return  youtube_url


#Dummy list for functioning::
"""
Dummy_song_Name = [
    "Moonlight Sonata",
    "Canon in D",
    "Für Elise",
    "Symphony No. 9",
    "Clair de Lune",
    "The Four Seasons",
    "Eine kleine Nachtmusik",
    "Ride of the Valkyries",
    "Ave Maria",
    "Symphony No. 5"
]

Dummy_artist_name = [
    "Ludwig van Beethoven",
    "Johann Pachelbel",
    "Ludwig van Beethoven",
    "Ludwig van Beethoven",
    "Claude Debussy",
    "Antonio Vivaldi",
    "Wolfgang Amadeus Mozart",
    "Richard Wagner",
    "Franz Schubert",
    "Ludwig van Beethoven"
    
    
]
for i in range(10):
  song_name=Dummy_song_Name[i]
  artist_name=Dummy_artist_name[i]

"""


# Example usage:
song_name = input("Song Name: ")
artist_name = input("Artist_Name: ")
youtube_urll= get_youtube_url(song_name, artist_name)
for i in range(3):
  print("YouTube URL:", youtube_urll[i])