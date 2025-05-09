debug_mode = False
CURRENT_VERSION = """
2.6.2
"""
CURRENT_VERSION=CURRENT_VERSION.replace('\n','')



import os,sys,random,requests



def get_latest_version_info():
    try:
        response = requests.get(VERSION_CHECK_URL)
        response.raise_for_status()
        return response.json()
    except requests.RequestError as e:
        print(f"Error checking for updates: {e}")
        return None

def download_new_version(download_url, filename):
    try:
        response = requests.get(download_url)
        response.raise_for_status()
        
        directory = os.path.dirname(filename)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
            
        with open(filename, 'wb') as file:
            file.write(response.content)
    except Exception as e:
        print(f"Error saat mengunduh: {e}")
        


try:
    from colorama import init, Fore, Back, Style
    init()
    def color(text, fore=None, back=None):
        color_map = {
            (255,0,0): Fore.RED,
            (0,255,0): Fore.GREEN, 
            (0,0,255): Fore.BLUE,
            (255,255,0): Fore.YELLOW,
            (0,255,255): Fore.CYAN,
            (255,0,255): Fore.MAGENTA
        }
        result = ""
        if fore in color_map:
            result += color_map[fore]
        result += text
        result += Style.RESET_ALL
        return result

    from pystyle import Anime as pyAnime
    from pystyle import Colors as pyColors
    from pystyle import Colorate as pyColorate
    from pystyle import Center as pyCenter
    from pystyle import System as pySystem
    local_ip = requests.get('https://api.ipify.org').text
    response = requests.get(f"https://ipinfo.io/{local_ip}/json")
    data_jaringan = response.json()
except Exception as e:
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("pip install pystyle")
    
    from colorama import init, Fore, Back, Style
    init()
    def color(text, fore=None, back=None):
        color_map = {
            (255,0,0): Fore.RED,
            (0,255,0): Fore.GREEN, 
            (0,0,255): Fore.BLUE,
            (255,255,0): Fore.YELLOW,
            (0,255,255): Fore.CYAN,
            (255,0,255): Fore.MAGENTA
        }
        result = ""
        if fore in color_map:
            result += color_map[fore]
        result += text
        result += Style.RESET_ALL
        return result

    from pystyle import Anime as pyAnime
    from pystyle import Colors as pyColors
    from pystyle import Colorate as pyColorate
    from pystyle import Center as pyCenter
    from pystyle import System as pySystem
    



banner = r"""
░█▄█▒█▀▄░▄▀▄▒█▀
▒█▒█░█▀▄░▀▄▀░█▀                                                                        
                           
 
                   █░█ ▄▀█ █▀▀ █▄▀ █▀▀ █▀█
                   █▀█ █▀█ █▄▄ █░█ ██▄ █▀▄
                    
░▄▀▀▒▄▀▄▒█▀▄░░▒█▀▄▒▄▀▄▒█▀▄░█▄▀░█░█▄░█░▄▀▒░░░█▄▒▄█░█▒█░█▒░░▀█▀░█▒█▀▄░█▒░▒▄▀▄░▀▄▀▒██▀▒█▀▄
░▀▄▄░█▀█░█▀▄▒░░█▀▒░█▀█░█▀▄░█▒█░█░█▒▀█░▀▄█▒░░█▒▀▒█░▀▄█▒█▄▄░▒█▒░█░█▀▒▒█▄▄░█▀█░▒█▒░█▄▄░█▀▄

                         تﻮﻤﻟا فﻭﺮﺣ                                                                  
"""[1:]


pyAnime.Fade(pyCenter.Center(banner), pyColors.red_to_yellow, pyColorate.Vertical, enter=True)


#pyAnime.Fade(pyCenter.Center(text), pyColors.purple_to_red, pyColorate.Vertical, enter=True)
#print(pyColorate.Horizontal(pyColors.red_to_yellow, pyCenter.XCenter(text)))

pySystem.Clear()

#print("\n"*2    )
#print(pyColorate.Horizontal(pyColors.red_to_yellow, pyCenter.XCenter(text)))
#print("\n"*2)




from pystyle import Box
import random
import requests
from time import sleep
import os, signal, sys
from pyfiglet import figlet_format
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.text import Text
from rich.style import Style
import pystyle
from pystyle import Colors, Colorate

from carparktool import CarParkTool

__CHANNEL_USERNAME__ = "HACKER_HROF"
__GROUP_USERNAME__   = "HACKER_HROF"

def signal_handler(sig, frame):
    print("\n Bye Bye...")
    sys.exit(0)

def gradient_text(text, colors):
    lines = text.splitlines()
    height = len(lines)
    width = max(len(line) for line in lines)
    colorful_text = Text()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ' ':
                color_index = int(((x / (width - 1 if width > 1 else 1)) + (y / (height - 1 if height > 1 else 1))) * 0.5 * (len(colors) - 1))
                color_index = min(max(color_index, 0), len(colors) - 1)  # Ensure the index is within bounds
                style = Style(color=colors[color_index])
                colorful_text.append(char, style=style)
            else:
                colorful_text.append(char)
        colorful_text.append("\n")
    return colorful_text

def banner(console):
    os.system('cls' if os.name == 'nt' else 'clear')
    brand_name = figlet_format('HROF', font='big')
    colors = [
        "rgb(255,0,0)", "rgb(255,69,0)", "rgb(255,140,0)", "rgb(255,215,0)", "rgb(173,255,47)", 
    ]
    colorful_text = gradient_text(brand_name, colors)
    console.print(colorful_text)
    print(Colorate.Horizontal(Colors.yellow_to_red, '============================================================'))
    print(Colorate.Horizontal(Colors.yellow_to_red, '\t         ﺓﺍﺩﻷﺍ ﻩﺬﻫ ﻡﺍﺪﺨﺘﺳﺍ ﻞﺒﻗ تﻮﻤﻟا فﻭﺮﺣ ﻦﻣ ﺝﻭﺮﺨﻟﺍ ﻞﻴﺠﺴﺗ ﻰﺟﺮﻳ'))
    print(Colorate.Horizontal(Colors.yellow_to_red, '              ﺎﻫﺮﻈﺣ ﻢﺘﻴﺳﻭ ﺎﻬﺑ ﺡﻮﻤﺴﻣ ﺮﻴﻏ ﻝﻮﺻﻮﻟﺍ ﺡﺎﺘﻔﻣ ﺔﻛﺭﺎﺸﻣ'))
    print(Colorate.Horizontal(Colors.yellow_to_red, f' ‌                ﻡﺍﺮﺠﻠﺗ: @{__CHANNEL_USERNAME__}'))
    print(Colorate.Horizontal(Colors.yellow_to_red, f'                 ﻙﻮﺘﻜﻴﺗ: @{__GROUP_USERNAME__}'))
    print(Colorate.Horizontal(Colors.yellow_to_red, '============================================================'))

def load_player_data(cpm):
    response = cpm.get_player_data()
    if response.get('ok'):
        data = response.get('data')
        if 'floats' in data and 'localID' in data and 'money' in data and 'coin' in data:
        
            print(Colorate.Horizontal(Colors.yellow_to_red, '==========[ ﺐﻋﻼﻟﺍ ﻞﻴﺻﺎﻔﺗ ]=========='))
            
            print(Colorate.Horizontal(Colors.yellow_to_red, f'ﻢﺳﺍ   : {(data.get("Name") if "Name" in data else "UNDEFINED")}.'))
                
            print(Colorate.Horizontal(Colors.yellow_to_red, f'ﻲﻠﺤﻣ ﻑﺮﻌﻣ: {data.get("localID")}.'))
            
            print(Colorate.Horizontal(Colors.yellow_to_red, f'ﻝﺎﻣ  : {data.get("money")}.'))
            
            print(Colorate.Horizontal(Colors.yellow_to_red, f'ﺔﻴﻧﺪﻌﻣ ﺕﻼﻤﻋ  : {data.get("coin")}.'))
            
        else:
            print(Colorate.Horizontal(Colors.yellow_to_red, '! ﺄﻄﺧ: ﻞﻗﻷﺍ ﻰﻠﻋ ﺓﺪﺣﺍﻭ ﺓﺮﻣ ﺔﺒﻌﻠﻟﺍ ﻰﻟﺇ ﻝﻮﺧﺪﻟﺍ ﻞﻴﺠﺴﺗ ﺓﺪﻳﺪﺠﻟﺍ ﺕﺎﺑﺎﺴﺤﻟﺍ ﻰﻠﻋ ﺐﺠﻳ !.'))
    else:
        print(Colorate.Horizontal(Colors.yellow_to_red, '! ﺄﻄﺧ: ﺢﻴﺤﺻ ﻞﻜﺸﺑ ﻪﻄﺒﺿ ﻢﺘﻳ ﻢﻟ ﻚﺑ ﺹﺎﺨﻟﺍ ﻝﻮﺧﺪﻟﺍ ﻞﻴﺠﺴﺗ ﻥﺃ ﻭﺪﺒﻳ !.'))
        exit(1)


def load_key_data(cpm):

    data = cpm.get_key_data()
    
    print(Colorate.Horizontal(Colors.yellow_to_red, '========[ تﻮﻤﻟا فﻭﺮﺣ ]========'))
    
    print(Colorate.Horizontal(Colors.yellow_to_red, f'Access Key : {data.get("access_key")}.'))
    
    print(Colorate.Horizontal(Colors.yellow_to_red, f'Telegram ID: {data.get("telegram_id")}.'))
    
    print(Colorate.Horizontal(Colors.yellow_to_red, f'Balance $  : {(data.get("coins") if not data.get("is_unlimited") else "Unlimited")}.'))
        
    

def prompt_valid_value(content, tag, password=False):
    while True:
        value = Prompt.ask(content, password=password)
        if not value or value.isspace():
            print(Colorate.Horizontal(Colors.yellow_to_red, f'{tag} cannot be empty or just spaces. Please try again.'))
        else:
            return value
            
def load_client_details():
    response = requests.get("http://ip-api.com/json")
    data = response.json()
    print(Colorate.Horizontal(Colors.yellow_to_red, '=============[ تﻮﻤﻟا فﻭﺮﺣ ]============='))
    print(Colorate.Horizontal(Colors.yellow_to_red, f'PI ﻥﺍﻮﻨﻋ : {data.get("query")}.'))
    print(Colorate.Horizontal(Colors.yellow_to_red, f'ﻊﻗﻮﻣ   : {data.get("city")} {data.get("regionName")} {data.get("countryCode")}.'))
    print(Colorate.Horizontal(Colors.yellow_to_red, f'ﺔﻟﻭﺩ    : {data.get("country")} {data.get("zip")}.'))
    print(Colorate.Horizontal(Colors.yellow_to_red, '===============[ تﻮﻤﻟا فﻭﺮﺣ ]==============='))

def interpolate_color(start_color, end_color, fraction):
    start_rgb = tuple(int(start_color[i:i+2], 16) for i in (1, 3, 5))
    end_rgb = tuple(int(end_color[i:i+2], 16) for i in (1, 3, 5))
    interpolated_rgb = tuple(int(start + fraction * (end - start)) for start, end in zip(start_rgb, end_rgb))
    return "{:02x}{:02x}{:02x}".format(*interpolated_rgb)

def rainbow_gradient_string(customer_name):
    modified_string = ""
    num_chars = len(customer_name)
    start_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    end_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    for i, char in enumerate(customer_name):
        fraction = i / max(num_chars - 1, 1)
        interpolated_color = interpolate_color(start_color, end_color, fraction)
        modified_string += f'[{interpolated_color}]{char}'
    return modified_string

if __name__ == "__main__":
    console = Console()
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        banner(console)
        acc_email = prompt_valid_value("[bold][?] ﻲﻧﻭﺮﺘﻜﻟﻹﺍ ﺏﺎﺴﺤﻟﺍ ﺪﻳﺮﺑ[/bold]", "Email", password=False)
        acc_password = prompt_valid_value("[bold][?] ﺏﺎﺴﺤﻟﺍ ﺭﻭﺮﻣ ﺔﻤﻠﻛ[/bold]", "Password", password=False)
        acc_access_key = prompt_valid_value("[bold][?] ﻝﻮﺻﻮﻟﺍ ﺡﺎﺘﻔﻣ[/bold]", "Access Key", password=False)
        console.print("[bold cyan][%] ﻝﻮﺧﺪﻟﺍ ﻞﻴﺠﺴﺗ ﺔﻟﻭﺎﺤﻣ[/bold cyan]: ", end=None)
        cpm = CarParkTool(acc_access_key)
        login_response = cpm.login(acc_email, acc_password)
        if login_response != 0:
            if login_response == 100:
                print(Colorate.Horizontal(Colors.yellow_to_red, 'ﺏﺎﺴﺤﻟﺍ ﻰﻠﻋ ﺭﻮﺜﻌﻟﺍ ﻢﺘﻳ ﻢﻟ.'))
                sleep(2)
                continue
            elif login_response == 101:
                print(Colorate.Horizontal(Colors.yellow_to_red, 'ﺔﺌﻃﺎﺧ ﺭﻭﺮﻤﻟﺍ ﺔﻤﻠﻛ.'))
                sleep(2)
                continue
            elif login_response == 103:
                print(Colorate.Horizontal(Colors.yellow_to_red, 'ﺢﻟﺎﺻ ﺮﻴﻏ ﻝﻮﺻﻮﻟﺍ ﺡﺎﺘﻔﻣ.'))
                sleep(2)
                continue
            else:
                print(Colorate.Horizontal(Colors.yellow_to_red, 'ﺔﻴﻧﺎﺛ ﻝﻭﺎﺣ.'))
                print(Colorate.Horizontal(Colors.yellow_to_red, '! ﺔﻴﻧﺎﺛ ﻝﻭﺎﺣ: ﻝﻮﻘﺤﻟﺍ ﺀﻞﻣ ﻦﻣ ﺪﻛﺄﺗ !.'))
                sleep(2)
                continue
        else:
            print(Colorate.Horizontal(Colors.yellow_to_red, 'ﺢﺟﺎﻧ.'))
            sleep(2)
        while True:
            banner(console)
            load_player_data(cpm)
            load_key_data(cpm)
            load_client_details()
            choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
            print(Colorate.Horizontal(Colors.yellow_to_red, '{01}: ﻝﺎﻤﻟﺍ ﺓﺩﺎﻳﺯ               1.500'))
            print(Colorate.Horizontal(Colors.yellow_to_red, '{02}: ﺔﻴﻧﺪﻌﻤﻟﺍ ﺕﻼﻤﻌﻟﺍ ﺓﺩﺎﻳﺯ     4.500'))
            print(Colorate.Horizontal(Colors.yellow_to_red, '{03}: ﻚﻠﻤﻟﺍ ﺔﺒﺗﺭ                8.000'))
            print(Colorate.Horizontal(Colors.yellow_to_red, '{04}: ﻑﺮﻌﻤﻟﺍ ﺮﻴﻴﻐﺗ              4.500'))
            print(Colorate.Horizontal(Colors.yellow_to_red, '{05}: ﻢﺳﻻﺍ ﺮﻴﻴﻐﺗ                 100'))
            print(Colorate.Horizontal(Colors.yellow_to_red, '{06}: ﺡﺰﻗ ﺱﻮﻗ ﻢﺳﻻﺍ ﺮﻴﻴﻐﺗ         100'))
            print(Colorate.Horizontal(Colors.yellow_to_red, '{07}: ﺕﺍﺭﺎﻴﺴﻟﺍ ﻡﺎﻗﺭﺃ ﺕﺎﺣ         2.000'))
            print(Colorate.Horizontal(Colors.yellow_to_red, '{08}: ﺕﺍﺭﺎﻴﺴﻟﺍ ﻡﺎﻗﺭﺃ ﺕﺎﺣﻮﻟ       ﺎﻧﺎﺠﻣ'))
            print(Colorate.Horizontal(Colors.yellow_to_red, '{09}: ﺏﺎﺴﺤﻟﺍ ﻞﻴﺠﺴﺗ              ﺎﻧﺎﺠﻣ'))
            print(Colorate.Horizontal(Colors.yellow_to_red, '{10}: ﺀﺎﻗﺪﺻﻷﺍ ﻑﺬﺣ               500'))
            print(Colorate.Horizontal(Colors.yellow_to_red, '{11}: ﺔﻋﻮﻓﺪﻤﻟﺍ ﺕﺍﺭﺎﻴﺴﻟﺍ ﺢﺘﻓ      5.000'))
            print(Colorate.Horizontal(Colors.yellow_to_red, '{12}: ﺕﺍﺭﺎﻴﺴﻟﺍ ﻊﻴﻤﺟ ﺢﺘﻓ          6.000'))
            print(Colorate.Horizontal(Colors.yellow_to_red, '{13}: ﺕﺍﺭﺎﻴﺴﻟﺍ ﻊﻴﻤﺟ ﺢﺘﻓ          3.500'))
            print(Colorate.Horizontal(Colors.yellow_to_red, '{14}: ﻉﻮﻓﺪﻣ ﻙﺮﺤﻣ ﺢﺘﻓ             4.000'))
            print(Colorate.Horizontal(Colors.yellow_to_red, '{15}: ﻕﺍﻮﺑﻷﺍ ﻊﻴﻤﺟ ﺢﺘﻓ            3.000'))
            print(Colorate.Horizontal(Colors.yellow_to_red, '{16}: ﺭﺮﻀﻟﺍ ﻞﻴﻄﻌﺗ ﻞﻔﻗ ﺀﺎﻐﻟﺇ      3.000'))
            print(Colorate.Horizontal(Colors.yellow_to_red, '{17}: ﺩﻭﺪﺤﻣ ﺮﻴﻏ ﺩﻮﻗﻭ ﺢﺘﻓ        3.000'))
            print(Colorate.Horizontal(Colors.yellow_to_red, '{18}: ﻝﺰﻨﻤﻟﺍ ﺢﺘﻓ 3              4.000'))
            print(Colorate.Horizontal(Colors.yellow_to_red, '{19}: ﻥﺎﺧﺪﻟﺍ ﺢﺘﻓ                4.000'))
            print(Colorate.Horizontal(Colors.yellow_to_red, '{20}: ﺕﻼﺠﻌﻟﺍ ﺢﺘﻓ                4.000'))
            print(Colorate.Horizontal(Colors.yellow_to_red, '{21}: ﺔﻛﺮﺤﺘﻤﻟﺍ ﻡﻮﺳﺮﻟﺍ ﺢﺘﻓ        2.000'))
            print(Colorate.Horizontal(Colors.yellow_to_red, '{22}: ﻡ ﺕﺍﺪﻌﻤﻟﺍ ﺢﺘﻓ               3.000'))
            print(Colorate.Horizontal(Colors.yellow_to_red, '{23}: ﻑ ﺕﺍﺪﻌﻤﻟﺍ ﺢﺘﻓ               3.000'))
            print(Colorate.Horizontal(Colors.yellow_to_red, '{24}: ﺯﻮﻔﻟﺍ ﻕﺎﺒﺳ ﺮﻴﻴﻐﺗ             1.000'))
            print(Colorate.Horizontal(Colors.yellow_to_red, '{25}: ﺮﺴﺨﻳ ﺮﻴﻴﻐﺘﻟﺍ ﻕﺎﺒﺳ            1.000'))
            print(Colorate.Horizontal(Colors.yellow_to_red, '{26}: ﺏﺎﺴﺤﻟﺍ ﺥﺎﺴﻨﺘﺳﺍ              7.000'))
            print(Colorate.Horizontal(Colors.yellow_to_red, '{27}: ﻙﺮﺤﻣ ﺺﺼﺨﻣ                   2.500'))
            print(Colorate.Horizontal(Colors.yellow_to_red, '{28}: ﺔﺼﺼﺨﻣ ﺔﻳﻭﺍﺯ                 1.500'))
            print(Colorate.Horizontal(Colors.yellow_to_red, '{29}: ﺺﺼﺨﻣ ﺕﺍﺭﺎﻃﺇ ﻕﺭﺎﺣ            1.500'))
            print(Colorate.Horizontal(Colors.yellow_to_red, '{30}: ﺔﺼﺼﺨﻤﻟﺍ ﺕﺍﺭﺎﻴﺴﻟﺍ ﻝﺎﻴ          2.000'))
            print(Colorate.Horizontal(Colors.yellow_to_red, '{31}: ﺔﺼﺼﺨﻤﻟﺍ ﺓﺭﺎﻴﺴﻟﺍ ﻞﻣﺍﺮﻓ          2.000'))
            print(Colorate.Horizontal(Colors.yellow_to_red, '{0} : ﺝﻭﺮﺧ'))
            
            print(Colorate.Horizontal(Colors.yellow_to_red, '===============[ تﻮﻤﻟا فﻭﺮﺣ  ]==============='))
            
            service = IntPrompt.ask(f"[bold][?] Select a Service [red][1-{choices[-1]} or 0][/red][/bold]", choices=choices, show_choices=False)
            
            print(Colorate.Horizontal(Colors.yellow_to_red, '===============[ تﻮﻤﻟا فﻭﺮﺣ ]==============='))
            
            if service == 0: # Exit
                print(Colorate.Horizontal(Colors.yellow_to_red, f'Thank You for using our tool, please join our telegram channel: @{__CHANNEL_USERNAME__}.'))
            elif service == 1: # Increase Money
                print(Colorate.Horizontal(Colors.yellow_to_red, '[?] Insert how much money do you want.'))
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Saving your data: ", end=None)
                if amount > 0 and amount <= 500000000000000000000000000000000:
                    if cpm.set_player_money(amount):
                        print(Colorate.Horizontal(Colors.yellow_to_red, 'ﺢﺟﺎﻧ'))
                        print(Colorate.Horizontal(Colors.yellow_to_red, '======================================'))
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.yellow_to_red, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED.'))
                        print(Colorate.Horizontal(Colors.yellow_to_red, 'Please try again.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'Please use valid values.'))
                    sleep(2)
                    continue
            elif service == 2: # Increase Coins
                print(Colorate.Horizontal(Colors.yellow_to_red, '[?] Insert how much coins do you want.'))
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Saving your data: ", end=None)
                if amount > 0 and amount <= 500000000000000:
                    if cpm.set_player_coins(amount):
                        print(Colorate.Horizontal(Colors.yellow_to_red, 'ﺢﺟﺎﻧ'))
                        print(Colorate.Horizontal(Colors.yellow_to_red, '======================================'))
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.yellow_to_red, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED.'))
                        print(Colorate.Horizontal(Colors.yellow_to_red, 'Please try again.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'Please use valid values.'))
                    sleep(2)
                    continue
            elif service == 3: # King Rank
                console.print("[bold red][!] Note:[/bold red]: if the king rank doesn't appear in game, close it and open few times.", end=None)
                console.print("[bold red][!] Note:[/bold red]: please don't do King Rank on same account twice.", end=None)
                sleep(2)
                console.print("[%] Giving you a King Rank: ", end=None)
                if cpm.set_player_rank():
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'ﺢﺟﺎﻧ'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.yellow_to_red, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 4: # Change ID
                print(Colorate.Horizontal(Colors.yellow_to_red, '[?] Enter your new ID.'))
                new_id = Prompt.ask("[?] ID")
                console.print("[%] Saving your data: ", end=None)
                if len(new_id) >= 0 and len(new_id) <= 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999 and (' ' in new_id) == False:
                    if cpm.set_player_localid(new_id.upper()):
                        print(Colorate.Horizontal(Colors.yellow_to_red, 'ﺢﺟﺎﻧ'))
                        print(Colorate.Horizontal(Colors.yellow_to_red, '======================================'))
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.yellow_to_red, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED.'))
                        print(Colorate.Horizontal(Colors.yellow_to_red, 'Please try again.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'Please use valid ID.'))
                    sleep(2)
                    continue
            elif service == 5: # Change Name
                print(Colorate.Horizontal(Colors.yellow_to_red, '[?] Enter your new Name.'))
                new_name = Prompt.ask("[?] Name")
                console.print("[%] Saving your data: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(new_name):
                        print(Colorate.Horizontal(Colors.yellow_to_red, 'ﺢﺟﺎﻧ'))
                        print(Colorate.Horizontal(Colors.yellow_to_red, '======================================'))
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.yellow_to_red, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED.'))
                        print(Colorate.Horizontal(Colors.yellow_to_red, 'Please try again.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'Please use valid values.'))
                    sleep(2)
                    continue
            elif service == 6: # Change Name Rainbow
                print(Colorate.Horizontal(Colors.yellow_to_red, '[?] Enter your new Rainbow Name.'))
                new_name = Prompt.ask("[?] Name")
                console.print("[%] Saving your data: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(rainbow_gradient_string(new_name)):
                        print(Colorate.Horizontal(Colors.yellow_to_red, 'ﺢﺟﺎﻧ'))
                        print(Colorate.Horizontal(Colors.yellow_to_red, '======================================'))
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.yellow_to_red, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED.'))
                        print(Colorate.Horizontal(Colors.yellow_to_red, 'Please try again.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'Please use valid values.'))
                    sleep(2)
                    continue
            elif service == 7: # Number Plates
                console.print("[%] Giving you a Number Plates: ", end=None)
                if cpm.set_player_plates():
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'ﺢﺟﺎﻧ'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.yellow_to_red, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 8: # Account Delete
                print(Colorate.Horizontal(Colors.yellow_to_red, '[!] After deleting your account there is no going back !!.'))
                answ = Prompt.ask("[?] Do You want to Delete this Account ?!", choices=["y", "n"], default="n")
                if answ == "y":
                    cpm.delete()
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'ﺢﺟﺎﻧ'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, '======================================'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                else: continue
            elif service == 9: # Account Register
                print(Colorate.Horizontal(Colors.yellow_to_red, '[!] Registring new Account.'))
                acc2_email = prompt_valid_value("[?] Account Email", "Email", password=False)
                acc2_password = prompt_valid_value("[?] Account Password", "Password", password=False)
                console.print("[%] Creating new Account: ", end=None)
                status = cpm.register(acc2_email, acc2_password)
                if status == 0:
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'ﺢﺟﺎﻧ'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, '======================================'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, f'INFO: In order to tweak this account with CPMElsedev.'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'you most sign-in to the game using this account.'))
                    sleep(2)
                    continue
                elif status == 105:
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'This email is already exists !.'))
                    sleep(2)
                    continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 10: # Delete Friends
                console.print("[%] Deleting your Friends: ", end=None)
                if cpm.delete_player_friends():
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'ﺢﺟﺎﻧ'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.yellow_to_red, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 11: # Unlock All Paid Cars
                console.print("[!] Note: this function takes a while to complete, please don't cancel.", end=None)
                console.print("[%] Unlocking All Paid Cars: ", end=None)
                if cpm.unlock_paid_cars():
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'ﺢﺟﺎﻧ'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.yellow_to_red, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 12: # Unlock All Cars
                console.print("[%] Unlocking All Cars: ", end=None)
                if cpm.unlock_all_cars():
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'ﺢﺟﺎﻧ'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.yellow_to_red, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 13: # Unlock All Cars Siren
                console.print("[%] Unlocking All Cars Siren: ", end=None)
                if cpm.unlock_all_cars_siren():
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'ﺢﺟﺎﻧ'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.yellow_to_red, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 14: # Unlock w16 Engine
                console.print("[%] Unlocking w16 Engine: ", end=None)
                if cpm.unlock_w16():
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'ﺢﺟﺎﻧ'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.yellow_to_red, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 15: # Unlock All Horns
                console.print("[%] Unlocking All Horns: ", end=None)
                if cpm.unlock_horns():
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'ﺢﺟﺎﻧ'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.yellow_to_red, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 16: # Disable Engine Damage
                console.print("[%] Unlocking Disable Damage: ", end=None)
                if cpm.disable_engine_damage():
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'ﺢﺟﺎﻧ'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.yellow_to_red, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 17: # Unlimited Fuel
                console.print("[%] Unlocking Unlimited Fuel: ", end=None)
                if cpm.unlimited_fuel():
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'ﺢﺟﺎﻧ'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.yellow_to_red, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 18: # Unlock House 3
                console.print("[%] Unlocking House 3: ", end=None)
                if cpm.unlock_houses():
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'ﺢﺟﺎﻧ'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.yellow_to_red, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 19: # Unlock Smoke
                console.print("[%] Unlocking Smoke: ", end=None)
                if cpm.unlock_smoke():
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'ﺢﺟﺎﻧ'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.yellow_to_red, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 20: # Unlock Smoke
                console.print("[%] Unlocking Wheels: ", end=None)
                if cpm.unlock_wheels():
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'ﺢﺟﺎﻧ'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.yellow_to_red, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 21: # Unlock Smoke
                console.print("[%] Unlocking Animations: ", end=None)
                if cpm.unlock_animations():
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'ﺢﺟﺎﻧ'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.yellow_to_red, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 22: # Unlock Smoke
                console.print("[%] Unlocking Equipaments Male: ", end=None)
                if cpm.unlock_equipments_male():
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'ﺢﺟﺎﻧ'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.yellow_to_red, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 23: # Unlock Smoke
                console.print("[%] Unlocking Equipaments Female: ", end=None)
                if cpm.unlock_equipments_female():
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'ﺢﺟﺎﻧ'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.yellow_to_red, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 24: # Change Races Wins
                print(Colorate.Horizontal(Colors.yellow_to_red, '[!] Insert how much races you win.'))
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Changing your data: ", end=None)
                if amount > 0 and amount <= 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999:
                    if cpm.set_player_wins(amount):
                        print(Colorate.Horizontal(Colors.yellow_to_red, 'ﺢﺟﺎﻧ'))
                        print(Colorate.Horizontal(Colors.yellow_to_red, '======================================'))
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.yellow_to_red, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED.'))
                        print(Colorate.Horizontal(Colors.yellow_to_red, 'Please try again.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, '[!] Please use valid values.'))
                    sleep(2)
                    continue
            elif service == 25: # Change Races Loses
                print(Colorate.Horizontal(Colors.yellow_to_red, '[!] Insert how much races you lose.'))
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Changing your data: ", end=None)
                if amount > 0 and amount <= 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999:
                    if cpm.set_player_loses(amount):
                        print(Colorate.Horizontal(Colors.yellow_to_red, 'ﺢﺟﺎﻧ'))
                        print(Colorate.Horizontal(Colors.yellow_to_red, '======================================'))
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.yellow_to_red, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED.'))
                        print(Colorate.Horizontal(Colors.yellow_to_red, '[!] Please use valid values.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, '[!] Please use valid values.'))
                    sleep(2)
                    continue
            elif service == 26: # Clone Account
                print(Colorate.Horizontal(Colors.yellow_to_red, '[!] Please Enter Account Detalis.'))
                to_email = prompt_valid_value("[?] Account Email", "Email", password=False)
                to_password = prompt_valid_value("[?] Account Password", "Password", password=False)
                console.print("[%] Cloning your account: ", end=None)
                if cpm.account_clone(to_email, to_password):
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'ﺢﺟﺎﻧ'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.yellow_to_red, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:     
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, '[!] THAT RECIEVER ACCOUNT IS GMAIL PASSWORD IS NOT VALID OR THAT ACCOUNT IS NOT REGISTERED.'))
                    sleep(2)
                    continue
            elif service == 27:
                console.print("[bold yellow][!] Note[/bold yellow]: original speed can not be restored!.")
                console.print("[bold cyan][!] Enter Car Details.[/bold cyan]")
                car_id = IntPrompt.ask("[bold][?] Car Id[/bold]")
                new_hp = IntPrompt.ask("[bold][?]Enter New HP[/bold]")
                new_inner_hp = IntPrompt.ask("[bold][?]Enter New Inner Hp[/bold]")
                new_nm = IntPrompt.ask("[bold][?]Enter New NM[/bold]")
                new_torque = IntPrompt.ask("[bold][?]Enter New Torque[/bold]")
                console.print("[bold cyan][%] Hacking Car Speed[/bold cyan]:",end=None)
                if cpm.hack_car_speed(car_id, new_hp, new_inner_hp, new_nm, new_torque):
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    console.print("================================")
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.yellow_to_red, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, '[!] Please use valid values.'))
                    sleep(2)
                    continue
            elif service == 28: # ANGLE
                print(Colorate.Horizontal(Colors.yellow_to_red, '[!] ENTER CAR DETALIS'))
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")
                print(Colorate.Horizontal(Colors.yellow_to_red, '[!] ENTER STEERING ANGLE'))
                custom = IntPrompt.ask("[red][?]﻿ENTER THE AMOUNT OF ANGLE YOU WANT[/red]")                
                console.print("[red][%] HACKING CAR ANGLE[/red]: ", end=None)
                if cpm.max_max1(car_id, custom):
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'ﺢﺟﺎﻧ'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("THANK YOU FOR USING OUR TOOL")
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue
            elif service == 29: # tire
                print(Colorate.Horizontal(Colors.yellow_to_red, '[!] ENTER CAR DETALIS'))
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")
                print(Colorate.Horizontal(Colors.yellow_to_red, '[!] ENTER PERCENTAGE'))
                custom = IntPrompt.ask("[pink][?]﻿ENTER PERCENTAGE TIRES U WANT[/pink]")                
                console.print("[red][%] Setting Percentage [/red]: ", end=None)
                if cpm.max_max2(car_id, custom):
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'ﺢﺟﺎﻧ'))
                    answ = Prompt.ask("[bold green][?] DO YOU WANT TO EXIT[/bold green] ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("THANK YOU FOR USING OUR TOOL")
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue
            elif service == 30: # Millage
                console.print("[bold]ENTER CAR DETAILS![/bold]")
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")
                console.print("[bold]ENTER NEW MILLAGE![/bold]")
                custom = IntPrompt.ask("[bold blue][?]﻿ENTER MILLAGE U WANT[/bold blue]")                
                console.print("[bold red][%] Setting Percentage [/bold red]: ", end=None)
                if cpm.millage_car(car_id, custom):
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    answ = Prompt.ask("[bold][?] DO YOU WANT TO EXIT[/bold] ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("THANK YOU FOR USING OUR TOOL")
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue
            elif service == 31: # Brake
                console.print("[bold]ENTER CAR DETAILS![/bold]")
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")
                console.print("[bold]ENTER NEW BRAKE![/bold]")
                custom = IntPrompt.ask("[bold blue][?]﻿ENTER BRAKE U WANT[/bold blue]")                
                console.print("[bold red][%] Setting BRAKE [/bold red]: ", end=None)
                if cpm.brake_car(car_id, custom):
                    console.print("[bold green]ﺢﺟﺎﻧ (✔)[/bold green]")
                    answ = Prompt.ask("[bold][?] DO YOU WANT TO EXIT[/bold] ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("THANK YOU FOR USING OUR TOOL")
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'FAILED'))
                    print(Colorate.Horizontal(Colors.yellow_to_red, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue
            else: continue
            break
        break
            
        
            
              
