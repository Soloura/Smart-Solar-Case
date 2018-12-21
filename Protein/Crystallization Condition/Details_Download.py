import requests
from bs4 import BeautifulSoup

print('Start!')
url_origin = 'http://www.rcsb.org/pdb/explore/materialsAndMethods.do?structureId='
name = [line.rstrip() for line in open('Name.txt')]
number = len(name)
Details_file = open('Details_old.txt', 'w')

for i in range(0, number):
    print(name[i])
    url = url_origin + name[i]
    # print(url)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'lxml')
    check = soup.find_all(text='Crystallization')

    if check:
        Details = soup.select('#maincontentcontainer > div > div.col-md-8 > div > table > tbody > tr > td')[-1].text
        print(Details)
        Details_file.write(Details + ', ' + '\n')
        # Details_file.write(name[i] + ', ' + Details + ', ' + '\n')
    else:
        print('pass!')
        Details_file.write('\n')
        # Details_file.write(name[i] + ', ' + '\n')

Details_file.close()
print('Done!')