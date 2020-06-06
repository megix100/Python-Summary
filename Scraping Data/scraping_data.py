import requests #allowto download the data from the html
from bs4 import BeautifulSoup #Allow to use the data grabbed from the internet
import pprint #Make the printing function of HTML more organized

# https://pypi.org/project/beautifulsoup4/
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# SCRAPING VAST AMOUNTS OF DATA IN A WEBSITE: https://scrapy.org/

res=requests.get("https://news.ycombinator.com/")
print(res) #200 is good - communication stablished=> Right Click-> Inspect-> Network-> Headers-> Status Code: 200
soup= BeautifulSoup(res.text,"html.parser") #Separate the html from the text
print(soup) #Shows all the html code appears on that website
print(soup.body) #Just grab the body
print(soup.body.contents)#Grab the body in a format of a list
print(soup.find_all("div")) #Find all the word div you have in the website and get them in a list 
print(soup.find_all("a")) #Find all the Links you have in the website and get them in a list 
print(soup.find_all("title")) #Find all the titles you have in the website and get them in a list 
print(soup.a) #Find the first Link of the website
print(soup.find("a")) #Same as the previous one
print(soup.find(id="score_23240559")) #Search for this id in the website - Video 6:10 => https://www.udemy.com/course/complete-python-developer-zero-to-mastery/learn/lecture/16286200#bookmarks

# https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors
# https://www.w3schools.com/cssref/css_selectors.asp

#In the Hackernews website there is a class named score - Video 1:28 => https://www.udemy.com/course/complete-python-developer-zero-to-mastery/learn/lecture/16286204#bookmarks
#https://www.w3schools.com/cssref/css_selectors.asp
print(soup.select(".score")) #To search for a class, in this case the score class, just put a .score
print(soup.select("#score_23240559")) #To search for a ID, in this case the score ID, just put a # in the front of it
print(soup.select(".storylink")[0]) #To search for a class, in this case the storylink class, just put a .storylink. And [0] you are grabbing tphe first element
#Since the select command shows everything as a LIST, the list rules can be used
links=soup.select(".storylink") #This is going to grab the links
print(links[0]) #Same as print(soup.select("#score_23240559"))
votes=soup.select(".score")
print(votes[0].get("id")) #Get the first element of the Class Score and returns back its ID. The score_23240559 is the result



#--------------------PRACTICAL EXAMPLE SCRAPING THE DATA--------------------------------------------------------
#Getting just the links and the score
res1=requests.get("https://news.ycombinator.com/")
res2=requests.get("https://news.ycombinator.com/news?p=2") #Getting multiple pages to check the news
print(res1) #200 is good - communication stablished=> Right Click-> Inspect-> Network-> Headers-> Status Code: 200
soup1= BeautifulSoup(res1.text,"html.parser") #Separate the html from the text
soup2= BeautifulSoup(res2.text,"html.parser") #Separate the html from the text

links1=soup1.select(".storylink") #This is going to grab the links
links2=soup2.select(".storylink") #This is going to grab the links

links=links1+links2

# votes=soup.select(".score")
#Get the score for each topic - This can generate a problem since some items don't have a vote, so we have more items than votes
#So, instead of getting the score we can get the subtext which exists in each topic
subtext1=soup1.select(".subtext") #Select the class subtext
subtext2=soup2.select(".subtext") #Select the class subtext

subtext=subtext1+subtext2

def sort_stories_by_votes(hnlist):
	return sorted(hnlist,key=lambda k: k["votes"],reverse=True)
	#Since hn is a dictionary, you have to select the element which you want to search and you do this by using a lambda function
	#The third parameter is to reverse the order putting the highest votes at the top. Otherwise they would be in the bottom like in the expression below:
	#return sorted(hnlist,key=lambda k: k["votes"])

def create_custom_hn(links,subtext):
	hn=[]
	for idx, item in enumerate(links):
		title=links[idx].getText() #Grab the index or TITLE of each link - USE THIS ONE FOR SUBCLASSES
		href=links[idx].get("href",None) #The href is the link of the HackerNews Page and the None is just in case nothing is found  - USE THIS ONE FOR SUBCLASSES
		vote=subtext[idx].select(".score") #Due to the enumerate function this "SELECT" is going to create a list
		if len(vote):
			#The vote function is going to return a list. If the list has more the one element in other words it is not null we can grab the Title and Link
			#This solves the problem about having more titles and links then scores since some news were not read yet
			points=int(vote[0].getText().replace('points',''))  #The vote[idx] is not needed since we are already performing the function in the index of the loop order since the vote function comes from subtext[idx]
			#The vote[0] is used since the subtext[idx] select the whole score class,so we need to get the element we want from the list
			#The replace is used to remove the word "points" and convert into nothing, so
			#We can use the command int to convert everything into an integer
			#https://www.udemy.com/course/complete-python-developer-zero-to-mastery/learn/lecture/16286212#bookmarks
			if points>99: #Filtering the most popular news by getting the ones with more points
				hn.append({"title": title,"link":href, "votes":points})#Creating a dictionary
	return sort_stories_by_votes(hn)
pprint.pprint(create_custom_hn(links,subtext)) #THIS PPRINT IS A MODULE IMPORTED TO MAKE EVERYTHING MORE ORGANIZED