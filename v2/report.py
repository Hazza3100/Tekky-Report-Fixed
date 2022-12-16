from colorama import Fore
from pystyle import Colorate, Colors, Center
from os import system
from threading import Thread

import requests

report_video = 0
report_user = 0


def get_id(username):
    try:
        headers = {'authority': 'www.tiktok.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'en-US,en;q=0.9','cookie': 'msToken=cxfL0lxGWTg_UmhgLz8U_Nv3ecxsgvBu5OJ1FtmVgMd3cHWoFCxQnyHSUzoCzEMMh0XeZzSw_gjF8XhG8Qp9qiE7yi9Yjm5B64hK4qdEMnhOvQCK6bL2bP8h6pAAVdphB3w_yBje2nj3iFw=','sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',}

        response = requests.get(f'https://www.tiktok.com/@{username}', headers=headers)
        return response.text.split('authorId":"')[1].split('","')[0]
    except:
        print(f"{Fore.BLUE}[ {Fore.RED}x {Fore.BLUE}]{Fore.RESET} Username Invalid")



def status(report_video, report_user):
    print(
        Colorate.Horizontal(
            Colors.blue_to_cyan,
            "[i] User Report(s): {} | Video Report(s): {}".format(
                report_user, report_video
            ),
        ),
        end="\r",
    )


def report(id, aweme_id, sessionid):
    global report_video

    url = "https://api31-normal-useast1a.tiktokv.com/aweme/v1/aweme/feedback/?request_tag_from=h5&reason=111&owner_id={}&report_type=video&object_id={}&report_desc=%EF%BF%BDUser%20violates%20community%20guidelines%20on%20multiple%20occasions%20by%20spreading%20illegal%20activities%2Fscams%20and%20by%20insulting%2Fharassing%20people%20please%20remove%20this%20content!%20(Offending%20content%20in%20video%20and%20caption)%EF%BF%BD&aid=1180".format(
        id, aweme_id
    )

    headers = {
        "accept-encoding": "gzip",
        "sdk-version": "2",
        "cookie": "sessionid={}".format(sessionid),
        "user-agent": "com.ss.android.ugc.trill/240303 (Linux; U; Android 12; en_US; Pixel 6 Pro; Build/SP2A.220405.004;tt-ok/3.10.0.2)",
    }

    while True:
        try:
            requests.get(url, headers=headers)

            report_video += 1

            status(report_video, report_user)
        except Exception:
            continue
        break


def banner():
    system("cls")
    print(
        Colorate.Horizontal(
            Colors.blue_to_cyan,
            Center.XCenter(
                """
                    ████████╗██╗██╗  ██╗██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗
                    ╚══██╔══╝██║██║ ██╔╝██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝
                       ██║   ██║█████╔╝ ██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║   
                       ██║   ██║██╔═██╗ ██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║   
                       ██║   ██║██║  ██╗██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║   
                       ╚═╝   ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝                                                 
                """
            ),
        )
    )


if __name__ == "__main__":
    banner()

    sessionid = input(Colorate.Horizontal(Colors.blue_to_cyan, "[?] Session ID >>> "))

    banner()

    username = input(Colorate.Horizontal(Colors.blue_to_cyan, "[?] Username >>> "))
    id = get_id(username)

    banner()

    print(Colorate.Horizontal(Colors.blue_to_cyan, "[i] Please wait..."), end="\r")

    url = "https://api31-normal-useast1a.tiktokv.com/aweme/v1/aweme/feedback/?request_tag_from=h5&reason=311&owner_id={}&report_type=user&object_id={}&report_desc=%EF%BF%BDUser%20violates%20community%20guidelines%20on%20multiple%20occasions%20by%20spreading%20illegal%20activities%2Fscams%20and%20by%20insulting%2Fharassing%20people%20please%20remove%20this%20content!%20(Offending%20content%20in%20video%20and%20caption)%EF%BF%BD&aid=1180".format(
        id, id
    )

    headers = {
        "accept-encoding": "gzip",
        "sdk-version": "2",
        "cookie": "sessionid={}".format(sessionid),
        "user-agent": "com.ss.android.ugc.trill/240303 (Linux; U; Android 12; en_US; Pixel 6 Pro; Build/SP2A.220405.004;tt-ok/3.10.0.2)",
    }

    requests.get(url, headers=headers)

    report_user += 1

    status(report_video, report_user)
    while True:
        max_cursor = 0

        while True:
            url = "https://api2-19-h2.musical.ly/aweme/v1/aweme/post/?max_cursor={}&user_id={}&count=200&retry_type=no_retry&mcc_mnc=&app_language=en&language=en&region=US&sys_region=US&carrier_region=&carrier_region_v2=&build_number=10.1.7&timezone_offset=3600&timezone_name=Europe%2FBerlin&is_my_cn=0&fp=&pass-region=1&pass-route=1&iid=7127307272354596614&device_id=7083579838678386182&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=100107&version_name=10.1.7&device_platform=android&ab_version=10.1.7&ssmix=a&device_type=Pixel%2B6%2BPro&device_brand=google&os_api=30&os_version=12&openudid=fe44d963d8b2c849&manifest_version_code=2019021215&resolution=1080*2268&dpi=443&update_version_code=2019021215&_rticket=1659461968895&ts=1659461970&as=a1iosdfgh&cp=androide1".format(
                max_cursor, id
            )

            headers = {
                "Host": "api2-19-h2.musical.ly",
                "Connection": "keep-alive",
                "Accept-Encoding": "gzip",
                "cookie": "sessionid={}".format(sessionid),
                "sdk-version": "1",
                "User-Agent": "com.zhiliaoapp.musically/2019021215 (Linux; U; Android 12; en_US; Pixel 6 Pro; Build/SP2A.220405.004; Cronet/58.0.2991.0)",
            }
            try:
                response = requests.get(url, headers=headers).json()
            except:
                pass

            try:
                if response["status_msg"] == "No more videos":
                    break
            except Exception:
                try:
                    max_cursor = response["max_cursor"]
                except Exception:
                    break

            aweme_list = response["aweme_list"]

            for aweme in aweme_list:
                Thread(
                    target=report,
                    args=(
                        id,
                        aweme["aweme_id"],
                        sessionid,
                    ),
                ).start()
