import urllib.request
import socket
import time
import os
import requests
import time
import socket
from ping3 import ping, verbose_ping
from discord_webhook import DiscordWebhook
from colorama import Fore, init
from PIL import Image, ImageDraw, ImageFont

init()

green = Fore.LIGHTGREEN_EX
yellow = Fore.LIGHTYELLOW_EX
reset = Fore.RESET

def check_download_speed(url, file_size):
    start_time = time.time()
    file_url = urllib.request.urlopen(url)
    downloaded_data = file_url.read(file_size)
    end_time = time.time()
    file_url.close()

    download_time = end_time - start_time
    download_speed = (file_size / download_time) / (1024 * 1024)

    return download_speed

def check_upload_speed(url, file_size):
    start_time = time.time()
    with open("upload_file.txt", "wb") as file:
        file.write(b"0" * file_size)
    end_time = time.time()

    upload_time = end_time - start_time
    upload_speed = (file_size / upload_time) / (1024 * 1024)

    os.remove("upload_file.txt")

    return upload_speed

def check_ping(url):
    response_time = ping(url)
    return response_time

print("-------------------------------------------")
print(f"{green}Checking Wi-Fi Info:{yellow}")
time.sleep(1)

response = requests.get('https://ipinfo.io')
data = response.json()
public_ip = data['ip']
isp = data['org']

print(f"Public IP Address: {public_ip}")
print(f"ISP: {isp}")

print(f"{reset}-------------------------------------------")
print(f"{green}Checking Network Speed:{yellow}")
time.sleep(1)

file_url = "https://google.com"
file_size = 10 * 1024 * 1024
download_speed = round(check_download_speed(file_url, file_size), 2)
upload_speed = round(check_upload_speed(file_url, file_size), 2)
ping_time = round(check_ping("google.com"), 2)

print(f"Ping > {ping_time} Ms")
print(f"Download Speed > {download_speed} Mbps")
print(f"Upload Speed > {upload_speed} Mbps")

time.sleep(3)

print(f"{reset}-------------------------------------------")
print(f"""{green}Rate The Tool:{yellow}
1
2
3
4
5
""")

while True:
    rate = input(f"{reset}> ")
    if rate.isdigit() and 1 <= int(rate) <= 5:
        break
    else:
        print("Invalid Rating. Please Enter A Number Between 1 And 5.")

webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1129458474758176779/TSuyrG4KK0o5K-8SWkfgbEs1P5dlFaiKxNzuOGT_0uhTnbj9pJgUduPja782iP9Zkm6s", content=f"""
Rating: `{rate}`
""")
response = webhook.execute()

print(f"{green}Rated Successfully!{reset}")

print(f"-------------------------------------------")
print(f"{green}Do You Want To Create A Report And Share The Results To Your Friends? y/n{reset}")
report = input("> ")
report = report.lower()

if report == "n":
    print(f"{red}Report Declined! Leaving...{reset}")
    exit()

elif report == "y":
    image_width = 800
    image_height = 300
    background_color = (0, 0, 0)
    text_color = (255, 255, 255)
    font_path = "arial.ttf"
    font_size = 20

    image = Image.new("RGB", (image_width, image_height), background_color)
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype(font_path, font_size)

    report_title = "Report Generated On"
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    isp_text = f"ISP: {isp}"
    ping_text = f"Ping: {ping_time} Ms"
    download_speed_text = f"Download Speed: {download_speed} Mbps"
    upload_speed_text = f"Upload Speed: {upload_speed} Mbps"

    report_title_position = (image_width // 2, 10)
    current_time_position = (image_width // 2, 40)
    isp_position = (image_width // 2, 90)
    ping_position = (image_width // 2, 130)
    download_speed_position = (image_width // 2, 170)
    upload_speed_position = (image_width // 2, 210)

    draw.text(report_title_position, report_title, font=font, fill=text_color, anchor="mt")
    draw.text(current_time_position, current_time, font=font, fill=text_color, anchor="mt")
    draw.text(isp_position, isp_text, font=font, fill=text_color, anchor="mt")
    draw.text(ping_position, ping_text, font=font, fill=text_color, anchor="mt")
    draw.text(download_speed_position, download_speed_text, font=font, fill=text_color, anchor="mt")
    draw.text(upload_speed_position, upload_speed_text, font=font, fill=text_color, anchor="mt")

    image.save("report_image.png")

    print(f"{green}Report Image Generated Successfully: report_image.png{reset}")

else:
    print(f"{red}Report Declined! Leaving...{reset}")
    exit()
