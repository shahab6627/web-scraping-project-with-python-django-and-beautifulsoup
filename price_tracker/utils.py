import requests

from bs4 import BeautifulSoup 

import lxml
# url = "https://www.flipkart.com/zunbella-3d-super-transparent-car-toy-toy-kids-360-degree-rotation-gear-simulation-mechanical-car-concept-racing-sound-light-toys-boys-girls/p/itm972194f147a13?pid=RCTGY239WTDWJCQQ&lid=LSTRCTGY239WTDWJCQQZCDOBS&marketplace=FLIPKART&store=tng%2F56a%2Ffq8&spotlightTagId=BestsellerId_mgl%2F56m&srno=b_1_5&otracker=nmenu_sub_Baby%20%26%20Kids_0_Remote%20Control%20Toys&fm=organic&iid=31bdbd72-f0fe-4446-8b01-2755c8f8e19b.RCTGY239WTDWJCQQ.SEARCH&ppt=browse&ppn=browse&ssid=d2oj3wccds0000001690974290236"

def getFlipkartItems(url):
    headers = {
            "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "Accept-Language":"en"
        }

    try:
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "lxml")

        title = soup.find('span', attrs={'class':'B_NuCI'}).getText()

        item_price = soup.find('div', class_='_30jeq3').getText()
        price = format(item_price).replace(',', '')
        price = float(price[1:])
        image = soup.find('img', attrs={'class':'_396cs4'})

        image_url = image.get('src')

        return [title, price, image_url]
    except Exception as e:
        return e
        
        

# a = getFlipkartItems(url)