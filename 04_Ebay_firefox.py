from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
import pickle

user_agent = 'Mozilla/5.0 (Linux; Android 5.1; Tesla Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.0.0 Mobile Safari/537.36 YaApp_Android/9.20/apad YaSearchBrowser/9.20'
# url = 'https://www.ebay.com/sch/i.html?_fsrp=1&_sop=10&_sacat=175672&LH_BIN=1&_from=R40&LH_TitleDesc=0&LH_ItemCondition=2000%7C1500%7C2500%7C3000&_udhi=450'
url = 'https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?LH_BIN=1&LH_ItemCondition=1000%7C1500%7C2000%7C2500%7C3000%7C10&rt=nc&_dcat=175672&_dmd=1&_fosrp=1&_from=R40%7CR40&_mPrRngCbx=1&_sop=10&_udhi=450'

# url = 'https://www.ebay.com/sch/i.html?_fsrp=1&_sop=10&_sacat=175672&LH_BIN=1&_from=R40&LH_TitleDesc=0&LH_ItemCondition=2000%7C1500%7C2500%7C3000&_udhi=450&LH_PrefLoc=4'
page_deep = 1

# if parsing by firefox, options:
# driver = webdriver.Firefox()
options = webdriver.FirefoxOptions()
options.set_preference("general.useragent.override", user_agent)
driver = webdriver.Firefox(options=options)

# if need to use chrome:
# options = webdriver.ChromeOptions()
# options.add_argument(f"user-agent={user_agent}")
# driver = webdriver.Chrome(options=options)

driver.get(url)

''' # save the cookies after login by hand
time.sleep(90)
pickle.dump(driver.get_cookies(), open('cookies/session', 'wb'))
driver.close()
'''

# load cookies
for cookie in pickle.load(open('cookies/session', 'rb')):
    driver.add_cookie(cookie)
print('loaded cookies')
time.sleep(2)

# get to the start page
driver.get(url)

'''# select shipping destination:
shipp_but = driver.find_element_by_id("shipto")
shipp_but.click()
time.sleep(2)
# xpath_us = "//div[@class='shipto__country-list']/span/div/div[1]/span/span[2]"  # version 2.0
xpath_us = "//div[@class='shipto__country-list']//span[text()='United States']" # version 3.0
country_buttons = driver.find_element_by_xpath(xpath_us)
country_buttons.click()
'''

# find links on the page:
item_arr = []

def get_specs_main():
    li_xpath = "//ul[@class='b-list__items_nofooter']/li"
    list_of_el = driver.find_elements_by_xpath(li_xpath)
    print(len(list_of_el))

    for i, k in enumerate(list_of_el):
        j = i + 1
        try:
            # link
            link = driver.find_element_by_xpath(li_xpath + f'[{j}]//a[@class="s-item__link"]').get_attribute('href')

            # title
            title = driver.find_element_by_xpath(li_xpath + f'[{j}]//h3').text

            # price
            price = driver.find_element_by_xpath(li_xpath + f'[{j}]//span[@class="s-item__price"]').text

            # shipp
            try:
                shipp = driver.find_element_by_xpath(li_xpath + f'[{j}]//span[@class="s-item__shipping s-item__logisticsCost"]').text
            except :
                print('error getting shipping', j, link)
                shipp = 'free'

            item_arr.append([link, title, price, shipp])

        except:
            print('error while getting lot details')

    return item_arr

m = get_specs_main()

print('array is:', m)










