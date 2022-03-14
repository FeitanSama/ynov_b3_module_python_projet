import os
import re
import time
import string
import requests
import pandas as pd
# Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions

browser = webdriver.Chrome(os.getcwd() + "/chromedriver")

home = []
for ascii in list(string.ascii_lowercase)+['numeric']:
    browser.get('https://www.crunchyroll.com/fr/videos/anime/alpha?group='+ ascii)
    compt = 0
    active = True
    while active:
        compt = compt + 1
        try:
            
            title = browser.find_element_by_xpath('//*[@id="main_content"]/ul/li['+str(compt)+']/div/a/div/span[1]').text
            videos = int(re.findall('[0-9]+',browser.find_element_by_xpath('//*[@id="main_content"]/ul/li['+str(compt)+']/div/a/div/span[2]').text)[0])
            short_desc = browser.find_element_by_xpath('//*[@id="main_content"]/ul/li['+str(compt)+']/div/a/div/p').text
            url = str(browser.find_element_by_xpath('//*[@id="main_content"]/ul/li['+str(compt)+']/div/a').get_attribute('href'))

            home.append([
                title,
                videos,
                short_desc,
                url
                ])

        except exceptions.NoSuchElementException:
            active = False
            pass

final = []
anime_type = [
    'action',
    'adventure',
    'comedy',
    'drama',
    'fantasy',
    'harem',
    'historical',
    'idols',
    'isekai',
    'magical girls',
    'mecha',
    'music',
    'mystery',
    'post-apocalyptic',
    'romance',
    'sci-fi',
    'seinen',
    'shojo',
    'shonen',
    'slice of life',
    'sports',
    'supernatural',
    'thriller'
    ]

for page in home:

    # Previous data
    title = page[0]
    nb_videos = page[1]
    short_desc = page[2]
    url = page[3]

    # Connect
    browser.get(url)
    browser.find_element_by_xpath('//*[@id="main_tab_more"]').click()

    # Mean stars
    mean_stars = browser.find_element_by_xpath('//*[@id="showview_about_rate_widget"]')
    mean_stars = float(mean_stars.get_attribute('content'))

    # Other series
    other_series = browser.find_element_by_xpath('//*[@id="showview_content_videos"]/div/ul')
    
    # Stars
    try:
        five_stars = int(browser.find_element_by_xpath("//ul//li//ul//li[1]//div[3][contains(@class, 'left')]").text[1:-1])
        four_stars = int(browser.find_element_by_xpath("//ul//li//ul//li[2]//div[3][contains(@class, 'left')]").text[1:-1])
        three_stars = int(browser.find_element_by_xpath("//ul//li//ul//li[3]//div[3][contains(@class, 'left')]").text[1:-1])
        two_stars = int(browser.find_element_by_xpath("//ul//li//ul//li[4]//div[3][contains(@class, 'left')]").text[1:-1])
        one_star = int(browser.find_element_by_xpath("//ul//li//ul//li[5]//div[3][contains(@class, 'left')]").text[1:-1])
    except:
        five_stars,four_stars,three_stars,two_stars,one_star = 0,0,0,0,0

    # Editor
    try:
        editor = browser.find_element_by_xpath("//a[contains(@href, 'publisher')]").text
    except:
        pass
    
    # Keywords
    try:
        keywords_type = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        keywords = [i.text for i in browser.find_elements_by_xpath("//a[contains(@href, 'genres')]")]
        for word in keywords:
            if word in anime_type:
                index = anime_type.index(word)
                keywords_type[index] = 1

            action = keywords_type[0]
            adventure = keywords_type[1]
            comedy = keywords_type[2]
            drama = keywords_type[3]
            fantasy = keywords_type[4]
            harem = keywords_type[5]
            historical = keywords_type[6]
            idols = keywords_type[7]
            isekai = keywords_type[8]
            magical_girls = keywords_type[9]
            mecha = keywords_type[10]
            music = keywords_type[11]
            mystery = keywords_type[12]
            post_apocalyptic = keywords_type[13]
            romance = keywords_type[14]
            sci_fi = keywords_type[15]
            seinen = keywords_type[16]
            shojo = keywords_type[17]
            shonen = keywords_type[18]
            slice_of_life = keywords_type[19]
            sports = keywords_type[20]
            supernatural = keywords_type[21]
            thriller = keywords_type[22]

    except:
        pass
 
    final.append([
        title,
        nb_videos,
        short_desc,
        url,
        mean_stars,
        five_stars,
        four_stars,
        three_stars,
        two_stars,
        one_star,
        editor,
        action,
        adventure,
        comedy,
        drama,
        fantasy,
        harem,
        historical,
        idols,
        isekai,
        magical_girls,
        mecha,
        music,
        mystery,
        post_apocalyptic,
        romance,
        sci_fi,
        seinen,
        shojo,
        shonen,
        slice_of_life,
        sports,
        supernatural,
        thriller
        ])

browser.close()

df = pd.DataFrame(final, columns=[
    'title',
    'nb_videos',
    'short_desc',
    'url',
    'mean_stars',
    'five_stars',
    'four_stars',
    'three_stars',
    'two_stars',
    'one_star',
    'editor',
    'action',
    'adventure',
    'comedy',
    'drama',
    'fantasy',
    'harem',
    'historical',
    'idols',
    'isekai',
    'magical_girls',
    'mecha',
    'music',
    'mystery',
    'post_apocalyptic',
    'romance',
    'sci_fi',
    'seinen',
    'shojo',
    'shonen',
    'slice_of_life',
    'sports',
    'supernatural',
    'thriller'
    ])

df.to_csv(os.getcwd()+'/export_list.csv')