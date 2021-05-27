from selenium import webdriver
import selenium.common.exceptions as sce
import time
from selenium.webdriver.support.select import Select
import pickle

user_agent = 'Mozilla/5.0 (Linux; Android 5.1; Tesla Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.0.0 Mobile Safari/537.36 YaApp_Android/9.20/apad YaSearchBrowser/9.20'
url = 'https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?LH_BIN=1&LH_ItemCondition=1000%7C1500%7C2000%7C2500%7C3000%7C10&rt=nc&_dcat=175672&_dmd=1&_fosrp=1&_from=R40%7CR40&_mPrRngCbx=1&_sop=10&_udhi=450'

page_deep = 2

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
time.sleep(1)

# get to the start page
driver.get(url)

'''# select shipping destination (if no account or cookies been added):
shipp_but = driver.find_element_by_id("shipto")
shipp_but.click()
time.sleep(2)
# xpath_us = "//div[@class='shipto__country-list']/span/div/div[1]/span/span[2]"  # version 2.0
xpath_us = "//div[@class='shipto__country-list']//span[text()='United States']" # version 3.0
country_buttons = driver.find_element_by_xpath(xpath_us)
country_buttons.click()
'''

# --------------------------  find array of links, titles, prices  ----------------------------------
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
            except sce.NoSuchElementException as exc:
                print(exc, link)
                # print('error getting shipping', j, link)
                shipp = '0'

            item_arr.append([link, title, price, shipp])

        except sce.NoSuchElementException as exc_el:
            print(exc_el)
        except sce.NoSuchAttributeException as exc_attr:
            print(exc_attr)

# m = get_specs_main()
# print('array is:', m)


# check_other_page
def iterate_pages(page_deep):
    i = 0
    # for i in range(page_deep):
    while i < page_deep:
        get_specs_main()
        time.sleep(2)
        print(f'page #{i + 1} was done creating links')
        i = i + 1
        try:
            next_page_sel = 'ebayui-image-chevron-light-right'
            next_page_but = driver.find_element_by_class_name(next_page_sel)
            next_page_but.click()
        except sce.NoSuchElementException as exc:
            print(f'no such button: next_page, {i+2}')
            print(exc)
        time.sleep(3)
    print(len(item_arr))
    return item_arr

try:
    list_of_el = iterate_pages(page_deep)
    print(list_of_el)
except:
    print('error iterating by page')



#         -----------------        Find description           -------------------

for el in list_of_el:
    print(el)
    print(el[0])
    # define the product link
    try:
        link = el[0]
        driver.get(link)
    except:
        print('can not get prod_url')

    # open description page:
    try:
        # show_more_btn = driver.find_element_by_class_name("app-item-description__body--readmore")
        show_more_btn = driver.find_element_by_class_name("app-item-description__wrapper")
        show_more_btn.click()
    except:
        print('cant find/click show/more')

    #get description:
    try:
        body_id = "ds_div"
        body = driver.find_element_by_css_selector("div[id='ds_div']")
    except:
        print('cant find body selector')
        body = 'error'
    try:
        desc = body.text.lower()
        el.append(desc)
    except:
        print('error reading description')

print(list_of_el)










