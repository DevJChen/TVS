import os
import time
import json
from TikTokApi import TikTokApi

start = time.time()
time.sleep(1)
api = TikTokApi.get_instance(custom_verifyFp="verify_ko4syt8j_IQnuDlVm_vKwF_4TyJ_93ZD_FX0roM6MnLa0", generate_static_did=True)
amount = 2000
count = 0
counter = 0
view = 0
trendingPage = api.by_trending(count=amount)
#print(json.dumps(trendingPage, indent=3))
path="C:\\Users\\john\\PycharmProjects\\AutomatedTVS\\.tiktokVid\\"
#trendingPage[count]["stats"]["playCount"] >= 10000000 and
#trendingPage[count]["authorStats"]["followerCount"] <= 1000000\
#trendingPage[count]["stats"]["shareCount"] >= 100000
while count < amount:
    view += trendingPage[count]["stats"]["playCount"]
    shares = trendingPage[count]["stats"]["shareCount"]
    followers = trendingPage[count]["authorStats"]["followerCount"]
    likes = trendingPage[count]["stats"]["diggCount"]
    comments = trendingPage[count]["stats"]["commentCount"]
    plays = trendingPage[count]["stats"]["playCount"]
    if (trendingPage[count]["music"]["original"] == True and
            trendingPage[count]["video"]["duration"] <= 60 and
            ((shares + likes + comments)/plays) >= .15 and
            followers <= 4000000 and
            shares >= 70000):
        """video_bytes = api.get_video_by_tiktok(trendingPage[count])
        title = trendingPage[count]["desc"]
        tiktok_vid = path + title + ".mp4"
        with open(file=tiktok_vid, mode="wb") as o:
            o.write(video_bytes)"""
        print(counter)
        print("SHARES: " + str(trendingPage[count]["stats"]["shareCount"]))
        print("FOLLOWERS: " + str(trendingPage[count]["authorStats"]["followerCount"]))
        print("LIKES: " + str(trendingPage[count]["stats"]["diggCount"]))
        print("COMMENTS: " + str(trendingPage[count]["stats"]["commentCount"]))
        print("PLAYS: " + str(trendingPage[count]["stats"]["playCount"]))
        print(trendingPage[count]["video"]["downloadAddr"])
        counter+=1
        count+=1
    else:
        count+=1
avgview = view/amount
print(counter)
print(avgview)
end = time.time()
print(end-start)


"""api = TikTokApi.get_instance(custom_verifyFp="verify_knw4mfwf_wlnkCb1z_IbyS_4vuB_8qnB_dV0pV3LgX1a7")
amount = 1
trendingPage = api.by_trending(count=amount)
print(json.dumps(trendingPage, indent=3))"""

"""path = "C:\\Users\\john\\PycharmProjects\\Automated Test\\tiktok\\"
ass = "ass"
os.path.exists(path)
with open(file=path+ass, mode="w") as fp:
    pass"""

"""video_bytes = api.get_video_by_tiktok(trendingPage[count])
        title = trendingPage[count]["desc"]
        tiktok_vid = path + title + ".mp4"
        with open(file=tiktok_vid, mode="wb") as o:
            o.write(video_bytes)"""