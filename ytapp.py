from pytube import YouTube

SAVE_PATH = input('Enter the destination directory')

link = input("   Enter video's link ...\n   ")
try:
    yt = YouTube(link)
except:
    print('     Something went wrong')
    print('     Check if your link is valid')
    exit('     Exiting app ...')

res = input('   Choose the number of the resolution you like!\n   0: 360p\n   1: 480p\n   2: 720p\n   3: 1080p\n  ')
options = [ '360p', '480p', '720p', '1080p' ]

try:
    chosen_stream = yt.streams.filter(file_extension = 'mp4', resolution = options[int(res)])
except:
    print('This resolution is not available')
    exit('Exiting app ...')
try:
    download_stream = chosen_stream[0].download(SAVE_PATH)
    print('Video is downloaded')
    print('Saved in',SAVE_PATH)
except:
    print('Enter the destination directory in proper format.')
    exit('Exiting app ...')
