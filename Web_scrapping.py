import requests
from bs4 import BeautifulSoup
import pandas as pd

name_=[]
price_=[]
img_url_=[]
short_des_=[]

url="https://www.web-scraping.dev/products"
response=requests.get(url)
soup=BeautifulSoup(response.text,"html.parser")

data=soup.find_all("div",class_="product")

"""           extracting name from the web page        """
for name in data:
    n=name.find("h3",class_="mb-0")
    name_.append(n.text.strip())

"""           extracting price from the web pafe        """    
for price in data:
    p=price.find ("div",class_="price") 
    price_.append(p.text.strip())  

"""           extracting description from the web page  """
for description in data :
    des=description.find("div",class_="short-description")   
    short_des_.append(des.text.strip())

"""           extracting image url from web page        """   
for image_ in data:
    images=image_.find("img")
    image=images['src'] 
    ful_link="https://www.web-scraping.dev/products"+image.replace("../","")
    img_url_.append(ful_link)

df=pd.DataFrame({"name":name_,
                 "price":price_,
                 "image_url":img_url_,
                 "description":short_des_,}
                )
print(df.to_excel("scraped_file.xlsx",index=True))
                
                

    




