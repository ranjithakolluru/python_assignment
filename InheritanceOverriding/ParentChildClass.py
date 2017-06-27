import webbrowser
class parentVideo():
    def __init__(self,title,run_time,youtube_url):
        self.Title=title
        self.Run_time=run_time
        self.youtube_url=youtube_url

class movies(parentVideo):
    def __init__(self,title,run_time,story,youtube_url,posterimage_url):
        parentVideo.__init__(self, title, run_time,youtube_url)
        self.story=story
        self.posterimage_url=posterimage_url
    def open_video(self):
        webbrowser.open(self.youtube_url)

class TvShows(parentVideo):
    def __init__(self,title,run_time,episodeno,NoofSeasons,youtube_url):
        parentVideo.__init__(self,title,run_time,youtube_url)
        self.episodeno=episodeno
        self.NoofSeasons=NoofSeasons
        
        