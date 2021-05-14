from TikTokApi import TikTokApi
import os
import time
from Google import Create_Service, Video_Service, Comment_Service
from googleapiclient.http import MediaFileUpload

def AutomatedTVS():
    start = time.time()
    time.sleep(1)
    api = TikTokApi.get_instance(custom_verifyFp="verify_ko4syt8j_IQnuDlVm_vKwF_4TyJ_93ZD_FX0roM6MnLa0")
    amount = 2000
    count = 0
    trendingPage = api.by_trending(count=amount)
    path = "C:\\Users\\john\\PycharmProjects\\AutomatedTVS\\tiktok\\"
    vid_path = "C:\\Users\\john\\PycharmProjects\\AutomatedTVS\\.tiktokVid\\"
    while (count < amount):
        shares = trendingPage[count]["stats"]["shareCount"]
        followers = trendingPage[count]["authorStats"]["followerCount"]
        likes = trendingPage[count]["stats"]["diggCount"]
        comments = trendingPage[count]["stats"]["commentCount"]
        plays = trendingPage[count]["stats"]["playCount"]
        if (trendingPage[count]["music"]["original"] == True and
                trendingPage[count]["video"]["duration"] <= 60 and
                ((shares + likes + comments) / plays) >= .15 and
                followers <= 4000000 and
                shares >= 70000):
            title = trendingPage[count]["desc"]
            while (len(title) > 50):
                title_list = title.split()
                title_list.pop()
                title = " ".join(title_list)
            title = title.replace('\"', '')
            title = title.replace("/", "")
            title = title.replace(":", "")
            title = title.replace("*", "")
            title = title.replace("?", "")
            title = title.replace('"', '')
            title = title.replace("<", "")
            title = title.replace(">", "")
            title = title.replace("|", "")
            tiktok = path + title
            if (os.path.exists(tiktok)):
                print("uploaded tiktok before")
                count+=1
            else:
                url = trendingPage[count]["video"]["downloadAddr"]
                user = trendingPage[count]["author"]["uniqueId"]
                with open(file=tiktok, mode="w") as fp:
                    pass
                video_bytes = api.get_video_by_tiktok(trendingPage[count])
                title = trendingPage[count]["desc"]
                tiktok_vid = vid_path + title + ".mp4"
                with open(file=tiktok_vid, mode="wb") as o:
                    o.write(video_bytes)
                print(title)
                print(user)
                print(url)
                break
        else:
            count+=1
    tags = "try not to laugh, unusual videos, unusual videos compilation, the most unusual videos, tik tok memes, funny videos, shorts, funny viral videos, comedy, robe prank, mom pranks son, mom prank on son, memetok, moktok, #moktok, pranks, best pranks, memes, funny memes, meme videos, tiktok memes, funny pranks, afv funny videos, best memes, funny memes tik tok, tik tok, tiktok best, best tiktok memes, dank memes, tik tok memes funny, funny, weird meme compilation"
    split_tags = tags.split(", ")

    """Upload Video Type Beat"""
    CLIENT_SECRET_FILE = "client_secret.json"
    API_NAME = "youtube"
    API_VERSION = "v3"
    UPLOADSCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

    upload_service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, UPLOADSCOPES)
    request_body = {
        "snippet": {
            'categoryId': 23,
            'title': "Insert Video Title Here",
            'description': "Credit: " + user + "\n\nBest of TikTok / Funniest of Tiktok / Craziest of Tiktok\n\nBusiness Inquiries: moktok.bizofficial@gmail.com\n\nAre you tired of having to scroll through cringey stuff on TikTok to find the funny ones? Don't worry, we as a team already have done that for you! Our goal is to have a place where people can find the best of TikTok without having to endlessly scroll. We hope that you will be able to find some entertainment here at MokTok!\n\nSubscribe to MokTok for the best of Tiktok:\nhttps://www.youtube.com/channel/UCGabpSXZR6MFRZWIiXOQPsA\n\n#Shorts #TikTok #MokTok #Funny #Memes #TikTokMemes #TikTokFunny #FunnyVideos #TikTokLord",
            'tags': split_tags,
        },
        'status': {
            'privacyStatus': 'private',
            'selfDeclaredMadeForKids': False,
        },
        'notifySubscribers': True,
    }
    mediaFile = MediaFileUpload(tiktok_vid)
    upload = upload_service.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=mediaFile
    ).execute()
    video_id = upload["id"]
    end = time.time()
    print("Video: UPLOADED")
    print(end - start)
    return tiktok_vid, video_id

def DeleteVideo(tiktok_vid, video_id):
    "Delete The Video File After Uploading"

    part_string = "processingDetails"
    CLIENT_SECRET_FILE = "client_secret.json"
    API_NAME = "youtube"
    API_VERSION = "v3"
    REQUESTSCOPES = ["https://www.googleapis.com/auth/youtube"]
    request_service = Video_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, REQUESTSCOPES)

    processingDetails = request_service.videos().list(
        part=part_string,
        id=video_id,
    ).execute()
    while processingDetails["items"][0]["processingDetails"]["processingStatus"] != "succeeded":
        processingDetails = request_service.videos().list(
            part=part_string,
            id=video_id,
        ).execute()
    os.unlink(tiktok_vid)
    print("Video: DELETED")

def MakeVideoPrivate(video_id):
    CLIENT_SECRET_FILE = "client_secret.json"
    API_NAME = "youtube"
    API_VERSION = "v3"
    REQUESTSCOPES = ["https://www.googleapis.com/auth/youtube"]
    request_service = Comment_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, REQUESTSCOPES)
    request_body = {
        "status":{
            "privacyStatus":"private"
        },
        "id":video_id
    }
    private = request_service.videos().update(
        part="status,id",
        body=request_body
    ).execute()
    print("Video: PRIVATED")
tiktok_vid, video_id = AutomatedTVS()
DeleteVideo(tiktok_vid, video_id)
MakeVideoPrivate(video_id)


#print(json.dumps(trending, indent=3))
#["id"]
#["author"]["uniqueId"]
#["video"]["duration"]
#["video"]["downloadAddr"]
#['music']["original"]
#["stats"]["playCount"]
#["desc"]
#["authorStats"]["followerCount"]