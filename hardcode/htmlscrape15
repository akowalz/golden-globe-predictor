

import json
import re
from bs4 import BeautifulSoup





page1 = open('gg15.html')
soup = BeautifulSoup(page1)



awardCategories = soup.findAll("div",{"class":"views-field views-field-title"})
nomWinner = soup.findAll('td',{'class':'col views-field views-field-nominee-wrapper is-winner'})
nomOther = soup.findAll('div',{'class':'grey'})


# filters visible text
def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element)):
        return False
    return True

visible_texts = filter(visible, awardCategories)

# scrape award
def AwardScrape():

    awdata = [link.text for link in soup.find_all("div",{"class":"views-field views-field-title"})]

    for div_tag in soup.find_all("div",{"class":"views-field views-field-title"}):
        print div_tag.text, div_tag.next_sibling

    output = json.dumps(awdata)
    return output

#scrape Winner
def WinnerScrape():

    windata = [link.text for link in soup.find_all('td',{'class':'col views-field views-field-nominee-wrapper is-winner'})]

    for td_tag in soup.find_all('td',{'class':'col views-field views-field-nominee-wrapper is-winner'}):
        print td_tag.text, td_tag.next_sibling
    return windata


# nominee scrape
def NomineeScrape():

    nomdata = [link.text for link in soup.find_all('td',{'class':'col views-field views-field-nominee-wrapper'})]

    for td_tag in soup.find_all('td',{'class':'col views-field views-field-nominee-wrapper'}):
        print td_tag.text, td_tag.next_sibling
    return nomdata


# nominee scrape



# Soup Filter
adata = [link.text for link in soup.find_all("div",{"class":"views-field views-field-title"})]
viewcontent = [link.text for link in soup.find_all("div",{"class":"view-content"})]
wdata = [link.text for link in soup.find_all('td',{'class':'col views-field views-field-nominee-wrapper is-winner'})]
nomdata = [link.text for link in soup.find_all('td',{'class':'col views-field views-field-nominee-wrapper'})]




vct = viewcontent[0]
varray=[]

vct_string = "".join(vct)
vct_split = vct_string.split("\n\n\n\n\n\n\n\n\n")
vct_sp = vct_split[0:25]







adata_string = "".join(adata)

formt={}

with open("ggdump.json", "w") as outfile:

    for x in range(0, 25):
        varray[:] = vct_sp
        v_loop = vct_sp[x].split("\n\n\n")

        v_loop.pop(0)
        formt[x] = {
                        adata[x]: {
                        "Award": adata[x],
                        "Nominees": v_loop

                        }
        }



    json.dump(formt,outfile, indent=4)





































