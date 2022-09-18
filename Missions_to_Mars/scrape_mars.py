from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd

def scrape():
    executable_path = {"executable_path": ChromeDriverManager().install()}
    browser = Browser("chrome", **executable_path, headless=False)

    # EMPTY DICTIONRARY FOR SCRAPED DATA FOR MONGO
    marsnews_dict = {}
    spaceimg_dict = {}
    marsfacts_dict = {}
    marshemis_dict = {}


    # URLS TO SCRAPE
    url_marsnews = "https://redplanetscience.com"
    url_spaceimage = "https://spaceimages-mars.com"
    url_marsfacts = "https://galaxyfacts-mars.com"
    url_marshemis = "https://marshemispheres.com"

    # SCRAPE MARS NEWS SITE
    browser.visit(url_marsnews)
    html = browser.html
    soup = bs(html, "html.parser")
    # print(soup.prettify())

    # SCRAPE FIRST NEWS TITLE FROM MARS NEWS SITE
    article = soup.find("div", class_="list_text")
    news_title = article.find("div", class_="content_title").text

    # SCRAPE RELATED PARAGRAPH FROM MARS NEWS SITE
    article = soup.find('div', class_="list_text")
    news_para = article.find('div', class_="article_teaser_body").text

    # SCRAPE SPACE IMAGE SITE
    browser.visit(url_spaceimage)
    html = browser.html
    soup = bs(html, "html.parser")
    # print(soup.prettify())

    # SCRAPE FOR THE URL OF THE FEATURED IMAGE
    space_img = soup.select("img", class_="fancybox-image")[1].get("src")

    # CREATE IMAGE URL
    space_img_url = url_spaceimage + "/" + space_img
    space_img_url

    # SCRAPE MARS FACTS SITE FOR MARS PLANET PROFILE TABLE
    browser.visit(url_marsfacts)
    html = browser.html
    soup = bs(html, "html.parser")
    # print(soup.prettify())

    # SCRAPE THE "MARS PLANET PROFILE" TABLE
    mars_facts = pd.read_html("https://galaxyfacts-mars.com")[1]
    mars_facts

    # SCRAPE MARS HEMISPHERES SITE
    browser.visit(url_marshemis)
    html = browser.html
    soup = bs(html, "html.parser")
    # print(soup.prettify())

    # EMPTY LIST TO HOLD IMAGES AND TITLES
    hemis_list = []

    # LOOP THROUGH SITE TO GET IMAGE URLs AND TITLES 
    for hemis in range(4):
        # EMPTY DICTIONARY FOR LOOP
        hemis_dict = {}
        
        # CLICK THROUGH PAGES / FIND IMAGE URL AND TITLE
        browser.find_by_css("a.product-item h3")[hemis].click()
        element = browser.find_link_by_text("Sample").first
        img_url = element["href"]
        title = browser.find_by_css("h2.title").text
        
        # DEFINE TITLE AND IMAGE URL VALUES FOR DICTIONRARY
        hemis_dict["title"] = title
        hemis_dict["img_url"] = img_url
        
        # APPEND TO EMPPYT LIST
        hemis_list.append(hemis_dict)
        browser.back()

    hemis_list

    # QUIT BROWSER
    browser.quit()

    # RETURN THE DICTIONARIES
    return marsnews_dict
    return spaceimg_dict
    return marsfacts_dict
    return marshemis_dict