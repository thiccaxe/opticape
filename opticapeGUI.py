import tkinter as tk
import pyautogui
import requests, json, os, shutil

window = tk.Tk()
VALIDCHARS = dict.fromkeys("abcedefghijklnopqrstuvwxyz0123456789_")
save_path = os.getcwd().replace('\\', '/')
header = tk.Label(
    text="           Optifine Cape Downloader            \nBy thiccaxe",
    fg="#7289da",  # Set the text color to white
    bg="#23272a",  # Set the background color to black
    height=8
)
usernameIntro = tk.Label(
    text="Enter a username: ",
    fg="#99aab5",
    bg="#23272a",

)
usernameField = tk.Entry(fg="#ffffff", bg="#23272a")


def Download():

    name=usernameField.get()
    if 16 >= len(name) >= 3 and all(c in VALIDCHARS for c in name.lower()):
        r = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{name}")
        if r.status_code == 200:
            r = r.json()
            if 'name' in r.keys():
                valid_name = r['name']
                r = requests.get(f"https://optifine.net/capes/{valid_name}.png", stream=True)
                if r.status_code == 200:
                    choice = pyautogui.confirm(text=f'Downloade cape for {valid_name}?', title='Opticape Downloader', buttons=['OK', 'Cancel'])
                    if choice == 'OK':
                        usernameField.delete(0, len(name))
                        with open(f"{save_path}/{valid_name}.png", 'wb') as file:
                            r.raw.decode_content = True
                            shutil.copyfileobj(r.raw, file)
                            pyautogui.alert(text='Downloaded', title='Opticape Downloader', button='OK')
                else:
                    pyautogui.alert(text='Person does NOT have a cape!!\nWhat a non', title='Opticape Downloader', button='OK')
    else:
        pyautogui.alert(text='Invalid Username!', title='Opticape Downloader', button='OK')



submitButton = tk.Button(
    text="Download",
    fg="#99aab5",
    bg="#ffffff",
    command=Download
)

header.pack(fill=tk.X); usernameIntro.pack(fill=tk.X); usernameField.pack(fill=tk.X); submitButton.pack(fill=tk.X)

window.mainloop()
