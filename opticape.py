# Importing required libraries
import urllib.request
import requests, os, json, shutil
# Adding information about user agent
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

save_path = os.getcwd().replace('\\', '/')
cls()
print(save_path)

valid_name = False
print("<{____OPTIFINE_CAPE_DOWNLOADER____}>")
print("<{__________BY__THICCAXE__________}>")
print("<{--------------------------------}>")
input("<{____PRESS_RETURN_TO_CONTINUE____}>")
cls()
while not valid_name:
    print("<{____OPTIFINE_CAPE_DOWNLOADER____}>")
    print("<{__________BY__THICCAXE__________}>")
    print("<{--------------------------------}>")
    name = input("<{________ENTER_A_USERNAME________}>\n>>>> ")
    cls()

    r = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{name}")
    if r.status_code == 200:
        r = r.json()
        if 'name' in r.keys():
            valid_name = r['name']
            r = requests.get(f"https://optifine.net/capes/{valid_name}.png", stream=True)
            if r.status_code == 200:
                with open(f"{save_path}/{valid_name}.png", 'wb') as file:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, file)
                    print("<{____OPTIFINE_CAPE_DOWNLOADER____}>")
                    print("<{__________BY__THICCAXE__________}>")
                    print("<{--------------------------------}>")
                    input("<{_________SAVED_CAPE_TO__________}>" + f"\n{save_path}/{valid_name}.png\n<<<<")
                    cls()
    else:
        print("<{____OPTIFINE_CAPE_DOWNLOADER____}>")
        print("<{__________BY__THICCAXE__________}>")
        print("<{--------------------------------}>")
        input("<{________INVALID_USERNAME________}>\n<<<<")
        cls()



