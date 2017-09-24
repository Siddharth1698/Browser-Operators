import time
import webbrowser
import random


def UrlOpen(UrlSong):
    x = int(input("How many Breaks u want"))
    y = 0
    z = int(input("Enter time interval in hours"))
    while y < x:
        time.sleep(z*60*60)
        webbrowser.open(UrlSong)
        y = y + 1


def playlist():
    playsong = ["https://www.youtube.com/watch?v=rc2jsjnt-HY", "https://www.youtube.com/watch?v=V1bFr2SWP1I",
                "https://www.youtube.com/watch?v=RB-RcX5DS5A", "https://www.youtube.com/watch?v=YykjpeuMNEk",
                "https://www.youtube.com/watch?v=FM7MFYoylVs", "https://www.youtube.com/watch?v=foE1mO2yM04"]
    x = len(playsong)
    song1 = random.randrange(0, x)
    SongUrl1 = str(playsong[song1])
    UrlOpen(SongUrl1)


playlist()




