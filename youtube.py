from pytube import YouTube,Search
import pprint

def downloadVideo():
    url = input("Enter a Video URL: ")
    try:
        YouTube(url).streams.order_by('resolution').desc().filter(file_extension='mp4')[0]
    except:
        print('Your youtube video link' + url + 'mwas invalid')

def searchYoutube():
    artists = ['Travis Scott','Juice Wrld']
    searchResults = {}
    for a in artists:
        s = Search(a)
        for v in s.results:
            if 'REACTION' not in v.title and 'Audio' in v.title :
                searchResults[v.title] = v.watch_url
                song = YouTube(v.watch_url).streams.order_by('resolution').desc().filter(file_extension='mp4')[0]
                print(song) 
                break     

    pprint.pprint(searchResults)


searchYoutube()







