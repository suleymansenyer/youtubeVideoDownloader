from pytube import YouTube

def downloadFunc(url):
    return YouTube(url).streams.first().download()
