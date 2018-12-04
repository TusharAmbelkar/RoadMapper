from bs4 import BeautifulSoup
import urllib2
import time
import requests

#insert link here
link = "https://www.cs.toronto.edu/~vmnih/data/mass_roads/train/map/index.html"

r  = requests.get(link)
data = r.text
soup = BeautifulSoup(data, features = "html.parser")
count = 0
for link in soup.find_all('a'):
	#start_time = time.time()
	response = urllib2.urlopen(link.get('href'))
	filename = (str(response.geturl()).split('/')[-1]).split('.')[0] + ".tif"
	files = open(filename,'w')
	files.write(response.read())
	files.close()
	#print(time.time() - start_time)
	count+=1
	#break
print(count)
