'''
Let’s imagine we have a MediaPlayer interface that plays various media formats, but we have a legacy VLCPlayer 
and MP4Player class that can only play their specific formats. The Adapter pattern will allow us to create an 
Adapter that lets the MediaPlayer work with both VLC and MP4 players without changing the existing code.
'''

#Adaptee classes
class VLCPlayer:
    def play_vlc(self):
        print("Playing VLC  video")

class MP4Player:
    def play_mp4(self):
        print("Playing MP4 video")

#Target interface
class MediaPlayer:
    def play(self, media_type):
        pass

#Adapter class
class VLCAdapter(MediaPlayer):
    def __init__(self,vlc_player):
        self.vlc_player = vlc_player
    
    def play(self, media_type):
        if media_type == "VLC":
            self.vlc_player.play_vlc()
        else:
            print("Invalid  media type input")

class MP4Adapter(MediaPlayer):
    def __init__(self,mp4_player):
        self.mp4_player = mp4_player
    
    def play(self, media_type):
        if media_type == "MP4":
            self.mp4_player.play_mp4()
        else:
            print("Invalid media type input")

#Client code
def  play_media(media_type):
    if media_type == "VLC":
        vlc_player = VLCPlayer()
        adapter = VLCAdapter(vlc_player)

    elif media_type == "MP4":
        mp4_player = MP4Player()
        adapter = MP4Adapter(mp4_player)
    else:
        print("Unsupported media type")
        return
    adapter.play(media_type)
    
#Client function calls
play_media("VLC")   # Output: Playing VLC video
play_media("MP4")   # Output: Playing MP4 video
play_media("AVI")   # Output: Unsupported media type

