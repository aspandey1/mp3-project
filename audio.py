from mutagen.id3 import ID3, TIT2, TDRC, TPE1, TALB, APIC
from mutagen.mp3 import MP3
from PIL import Image, ImageDraw
import os

def get_artwork(mp3_file):
    audio = mp3_file

    for tag in audio.tags.values():
        if isinstance(tag, APIC):  # Check if the tag is album artwork
            with open("album_cover.jpg", "wb") as img_file:
                img_file.write(tag.data)  # Save artwork as an image file
            return "album_cover.jpg"  # Return saved image path

    return "images/default_cover.jpg"  # Return None if no artwork is found

def get_info(path) -> dict[str: str]:
    audio = MP3(path, ID3=ID3)
    file_name = os.path.basename(path)

    # Check and update title
    if "TIT2" not in audio:
        audio.tags["TIT2"] = TIT2(encoding=3, text="New Song Title")

    # Check and update artist
    if "TPE1" not in audio:
        audio.tags["TPE1"] = TPE1(encoding=3, text="null")

    # Check and update year
    if "TDRC" not in audio:
        audio.tags["TDRC"] = TDRC(encoding=3, text="0000")

    if "TALB" not in audio:
        audio.tags["TALB"] = TALB(encoding=3, text="null")
    
    title = audio.tags["TIT2"]
    artist = audio.tags["TPE1"]
    year = audio.tags["TDRC"]
    album = audio.tags["TALB"]

    return {"file_name": file_name, "title": title, "artist": artist, "year": year, "album": album, "art_path": get_artwork(audio)}