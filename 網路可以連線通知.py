import requests
import time

while 1:
    try:
        x=input("輸入你要的網址")
        r = requests.head(x)
        print(r.status_code)  # 印出http code
        if r.status_code == 200:  # status code 200代表網頁正常
            headers = {
                "Authorization": "Bearer " + "你的LINE NOtify token",
            }

            params = {"message": x,
                      "message1": "可以發文囉!",
                      "stickerPackageId": 8525,
                      "stickerId": 16581292
                      }

            r = requests.post("https://notify-api.line.me/api/notify",
                              headers=headers, params=params)
            break
        else:
            print("還沒有回應")
            time.sleep(5)
    except:
        print("無法連上網站，網址可能錯誤")
        time.sleep(5)