#importing library
from bs4 import BeautifulSoup
import requests
import csv
import re
import pandas as pd

##Getting channel Title
def channelTitle(content):
    title = content.h3.a.text
    return title
youtubeIDs=[]
youtubeChannel=[]
videoCate=[]
def mainFunction(searchValue,channel=1):
    youtubeUrl="https://www.youtube.com/results?search_query="
    page = "&page="
    count=1
    pages = 1
    searchQuery=searchValue
    for category in searchQuery:
        count=1
        while count <= pages:
            scrapeURL = youtubeUrl + str(category) + page + str(count)
            print(category)
            source = requests.get(scrapeURL).text
            soup = BeautifulSoup(source, 'lxml')
            #getting the div yt-lockup-content
            for content in soup.find_all('div', class_= "yt-lockup-content"):
                try:
                    ID=content.h3.a
                    matching=bool('/watch' in ID.get('href'))
                    if(matching):
                        youtubeIDs.append(ID.get('href'))
                        videoCate.append(category)
                    else:
                        if(channel):
                            youtubeChannel.append(channelTitle(content))
                except Exception as e:
                    print(e)
                    print("Exception")
                    description = None
            #increasing the count
            count=count+1



searchValue=['Travel+Blogs','Science+and+Technology','Food','Manufacturing','History','Art+and+Music']
mainFunction(searchValue)
#Getting video of youtubeChannel
mainFunction(youtubeChannel,channel=0)
df = {'Videourl': youtubeIDs,'Category':videoCate}
df2=pd.DataFrame(df)
#storing Youtube videos link into csv file
df2.to_csv("Videourl.csv",index=False)
