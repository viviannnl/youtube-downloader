from pytube import YouTube

def Download(link):
    print('Download in progress...')
    
    def on_progress(stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining 
        percentage_of_completion = bytes_downloaded / total_size * 100
        print(str(round(percentage_of_completion, 2))+'% completed')
    
    youtubeObject = YouTube(link, on_progress_callback=on_progress)
    yt = youtubeObject.streams.get_highest_resolution()
    

    try:
        path = yt.download('/Users/vivianli/vivinnnli Dropbox/Vivian Li/Mac/Downloads')
    except:
        print("There has been an error in downloading your youtube video")
    
    print("Download completed in " + path)

link = input("URL: ")
Download(link)
