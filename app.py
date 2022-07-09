from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd

my_url = 'https://www.newegg.com/p/pl?d=graphics+card'

# opening up connection, grabbing the page

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# parse the html because the html is a big block of text
# tell is how to parse it

page_soup = soup(page_html,"html.parser")
#print(page_soup.h1)

#print(page_soup.p)
#print(page_soup.body.span)

# grabs each products

containers = page_soup.findAll("div",{"class":"item-cell"})
#print(len(containers))
#print(containers[0])

filename = "products.csv"
f = open(filename,"w")
headers = "brand, product_name, shipping\n"
f.write(headers)

for container in containers:
    title = container.div.a.img['title'.strip()]
    print(title)
    brand_ = title.split()[0]
    print(brand_)

    f.write(brand_ + "," + title.replace(",","|"))
f.close()    