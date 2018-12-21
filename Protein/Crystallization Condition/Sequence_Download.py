from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver_win32/chromedriver')
driver.implicitly_wait(3)

url_origin = 'http://www.rcsb.org/pdb/explore/remediatedSequence.do?structureId='
Name = [line.rstrip() for line in open('Name.txt')]
name_length = len(Name)

for i in range(0, name_length):
    print(Name[i])
    url = url_origin + Name[i]
    print(url)
    driver.get(url)
    elem = driver.find_element_by_link_text("Download FASTA File")
    print(elem.text)

    elem.click()

time.sleep(3)
driver.close()