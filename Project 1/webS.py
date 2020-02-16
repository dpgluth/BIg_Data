import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as Soup 
my_url = 'https://www.infoplease.com/homework-help/history/collected-state-union-addresses-us-presidents'
uClient = uReq(my_url)
page_html = uClient.read()
uClient = uReq(my_url)
uClient.close()
import csv


page_soup = Soup(page_html, "html.parser")

filename = "State of Union Address.csv"


headers = "President, Date, Link of Address, Filename_Address, TExt of Address\n"

containers = page_soup.findAll("span",{"class":"article"})	
data = list()
count = 0
for container in containers:
	President = container.a.text.split ('(')
	Date = container.a.text.split('(')

	#get the link
	link = container.a.get('href')
	full_link = "https://www.infoplease.com" + link
	link_page = uReq(full_link)
	link_html = link_page.read()
	#get the text of addres
	page_soup = Soup(link_html, "html.parser")
	#next line not woking

	Text_of_Address = page_soup.findAll("div",{"class":"article"})

	#print(len(Text_of_Address))
	if len(Text_of_Address) != 0:
		# text_a = Text_of_Address[0].p.unwrap()
		# print(text_a)
		text_a = Text_of_Address[0]
	else:
		print("skipping link, speechtext not found")
		continue

	#text = extract speech text(link)

	
	print("President: {}".format(' Date:'.join (President)))
	print("Link: https://www.infoplease.com" +link)
	#print("Text_of_Address: {}".format(text_a))

	#write the link to a text file
	count = count + 1
	file_name = "InfoUnionAddress_" + str(count) + ".txt"
	print("save to filenme " + file_name)

	#with open(file_name, "w") as file:
	#	file.write(str(text_a))
	# data.append({'President': President[0], 'Date': Date[1], 'Link': full_link, 'file_name': "C:\\Users\\DG-MS10\\Desktop\\" + file_name,  'Text_of_Address': text_a })
	data.append([President[0], Date[1], full_link,"C:\\Users\\DG-MS10\\Desktop\\" + file_name, text_a] )

with open('State of Union Address.csv', 'w') as csvfile:
	fieldnames = ['President', 'Date', 'Link', 'file_name', 'Text_of_Address']
	writer = csv.writer(csvfile)
	writer.writerow(fieldnames)
	for row in data:
		writer.writerow(row)