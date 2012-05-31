import urllib.request
import time


def send_to_twitter(msg):
        password_manager = urllib.request.HTTPPasswordMgr()
        password_manager.add_password("Twitter API",
                                      "http://twitter.com/statuses", "james_bent", "dbz@#naruto")
        http_handler = urllib.request.HTTPBasicAuthHandler(password_manager)
        page_opener = urllib.request.build_opener(http_handler)
        urllib.request.install_opener(page_opener)
        params = urllib.parse.urlencode( {'status': msg} )
        resp = urllib.request.urlopen("http://twitter.com/statuses/update.json",params)
        resp.read()
#-------------------------------------------------------------------------------------------------------------
def get_price():
        page = urllib.request.urlopen("http://beans.itcarlow.ie/prices.html")
        text = page.read().decode("utf8")
        where = text.find('>$')
        start_of_price = where + 2
        end_of_price = start_of_price + 4
        return float(text[start_of_price:end_of_price])

price_now=input("Do YOu want to see the price now(y/n)?")
if price_now=="y":
        send_to_twitter(get_price())
else:
        price=99.99
        while price>7.74:
            time.sleep(9)
            price=get_price()
        send_to_twitter("buy")
