from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
from win32com.client import Dispatch

speak = Dispatch('SAPI.SpVoice')
header = {'User-Agent': 'Mozilla'}
request = Request('https://www.worldometers.info/coronavirus/country/india/', headers = header)
html = urlopen(request)

soup = BeautifulSoup(html, 'lxml')
activeCases = soup.find_all('div', attrs={'class': 'maincounter-number'})[0].text
deaths = soup.find_all('div', attrs={'class': 'maincounter-number'})[1].text
recovered = soup.find_all('div', attrs={'class': 'maincounter-number'})[2].text
newCases = soup.find('li', {'class': 'news_li'}).strong.text.split()[0]
deathsToday = list(soup.find('li', {'class': 'news_li'}).strong.next_siblings)[1].text.split()[0]

toast = ToastNotifier()
if deathsToday == 'India':
    deathsToday = 0
message = f"New Cases-{newCases}\nNew Deaths-{deathsToday}"
mess = f"New Deaths-{deathsToday}"

toast.show_toast(title="COVID-19 Update", msg=message, duration=3, icon_path=r"icon.ico")
speak.Speak(message)
# toast.show_toast(title="COVID-19 Update", msg=mess, duration=3, icon_path=r"icon.ico")

# print(soup.find_all('div', attrs={'class': 'maincounter-number'}))
