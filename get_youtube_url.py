def get_youtube_url(song_name: str, artist_name: str) -> str:
    """
    Generate YouTube URL for a given song name and artist name.

    Args:
    song_name (str): Name of the song.
    artist_name (str): Name of the artist.

    Returns:
    str: YouTube URL for the song.
    """
    # Format song and artist names for the YouTube search query
    formatted_song = '+'.join(song_name.split())
    formatted_artist = '+'.join(artist_name.split())

    # Construct YouTube URL
    youtube_search_url = f"https://www.youtube.com/results?search_query={formatted_song}+{formatted_artist}"
    
    """
    get youtube_song_url
    .
    .
    .
    .
    .
    """
        
    return youtube_song_url

# Example usage:
song_name = "Shape of You"
artist_name = "Ed Sheeran"
youtube_url = get_youtube_url(song_name, artist_name)
print("YouTube URL:", youtube_url)
