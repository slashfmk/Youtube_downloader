# Developed by Yannick Fumukani
# This program downloads a youtube playlist for you

import os
import shutil
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

from pytube import Playlist


def playListDownloader(url):
    yt = Playlist(url)
    playDirectory = yt.title

    if os.path.isdir(playDirectory):
        print(playDirectory + " directory already exist!")
        response = input("If you want to continue, press y to delete it and create a new one or any key to cancel ")

        if response == 'y':
            shutil.rmtree(playDirectory)
            downloadPlayList(url)
        else:
            print("See you!!")
            return

    else:
        downloadPlayList(url)


# download a youTube playlist
def downloadPlayList(url):
    yt = Playlist(url)
    playDirectory = yt.title

    print("\nThe playlist [", yt.title, "] has", yt.length, "videos to download!\n")
    os.mkdir(playDirectory)

    for video in yt.videos:
        print("Downloading ...", video.title)
        video.streams.get_highest_resolution().download(playDirectory)
        print("done!")

    print("\nAll", yt.length, "videos have been successfully downloaded!!")


def main():
    playListUrl = input("Please paste your youtube playlist url ")

    if playListUrl.isdigit():
        print("A youtube url cannot be numbers")

    while playListUrl == '' or playListUrl.isdigit():
        print("A valid playlist url is required")
        playListUrl = input("Please paste your youtube playlist url ")

    playListDownloader(playListUrl)


main()
