#importing library
from apiclient.discovery import build
import pprint
import pandas as pd

#develper keys
DEVELOPER_KEY = "KEY"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
youtube = build(YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION,developerKey = DEVELOPER_KEY)

#function to get videos description and title
def video_details(video_id):
    list_videos_byid = youtube.videos().list(id = video_id,part = "snippet").execute()

    results = list_videos_byid.get("items", [])
    if(results):
        for result in results:
            Description.append(result["snippet"]["description"])
            Title.append(result["snippet"]["title"])
    else:
        video_ids.append("/watch?v="+video_id)

dflink=pd.read_csv("Videourl.csv")
Description=[]
Title=[]
video_ids=[]
#removing the videourl where no description founf
for x in dflink["Videourl"]:
    newstr = x.replace("/watch?v=", "")
    video_details(newstr)

list1 = [item for item in video_ids if item not in dflink["Videourl"]]
for y in list1:
    indexs=dflink[(dflink["Videourl"]==y)]
    dflink=dflink.drop(indexs.index[0])

#storing title into DataFrame
dflink['Title']=Title
#storing description into DataFrame
dflink['Description']=Description
dflink.drop_duplicates(subset='Videourl', inplace=True)
#storing data into csv
dflink.to_csv("finalYoutube.csv",index=False)
