import requests
from bs4 import BeautifulSoup
import sys
import re
import os.path
import wget

headers = {
    'Referer': 'https://www.data18.com/name/mike-adriano/scenes',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 OPR/87.0.4390.45',
}

save_path = 'trailers'

class Swallowed:

    def scrape_video(self):
        for n in range(100):
            n += 1
            params = {
                'page': '{}'.format(n),
            }

            response = requests.get('https://tour.swallowed.com/videos', params=params, headers=headers)

            soup = BeautifulSoup(response.text, 'html.parser')

            for i in soup.find_all("a", {"class": "main-img main-big-img"}):
                scene_url = i.get('href')
                title = scene_url.rsplit('/', 1)[-1]
                res = requests.get(scene_url, headers=headers)

                if os.path.exists('trailers/{}.mp4'.format(title)) == True:
                    pass
                else:
                    another_soup = BeautifulSoup(res.text, 'html.parser')

                    element = another_soup.find('a', {"class": "download-trailer"}).get('href')
                    last_res = requests.get(element, headers=headers)

                    completeName = os.path.join(save_path, title + ".mp4")

                    with open(completeName, 'wb') as f:
                        f.write(last_res.content)

                    print("'{}' was finished!".format(title))


    def scrape_all(self):
        wget.download(self.scrape_video())

if __name__ == '__main__':
    Swallowed().scrape_all()
