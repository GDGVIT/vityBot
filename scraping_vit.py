# -- Web scraping of clubs and chapters data from VIT University website ("http://vit.ac.in/")

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup as soup
import re
import unicodedata
import json

def clean(string) :
	string = re.sub('\s+',' ',string)
	return(unicodedata.normalize('NFKD',string).encode('ascii', 'ignore'))

#All urls
dic = {'studentclubs' : ['arts','literature','technology','outreach','awareness'],'studentchapters' : ['ieee','indian','international','university','american']}

#Scraping
collection=[]

#Text file
f = open("clubs_and_chapters.txt","w")

for i in dic :
	for j in dic[i] :
		url = "http://vit.ac.in/campus/"+str(i)+"/"+str(j)

		#Opening web driver and loading page
		wd = webdriver.Chrome("C:\Python27\selenium\chromedriver.exe")
		wd.get(url)
		WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "page-footer")))
		page_html = wd.page_source
		wd.quit()

		#Scraping
		page_soup = soup(page_html,"html.parser")
		containers = page_soup.findAll("div",{"class":"l12"})
		for container in containers[1:len(containers)-2] :

			clubs="false"

			#Name
			name = clean(container.h5.text.strip())

			#About
			all_about = container.findAll("div",{"class":"col l8 m8 s12"})
			if not(len(all_about)>0) :
				all_about = container.findAll("div",{"class":"col l8 m8 s12 left"})
			about = clean(all_about[0].text.strip())

			#Facebook
			fac = container.findAll("div",{"class":"col l1 m1 s3 right"})
			if len(fac)>0 :
				facebook = fac[0].a["href"]
			else :
				facebook = ""

			f.write(str(name)+"\n"+str(about)+"\n"+str(facebook)+"\n\n")

f.close()
