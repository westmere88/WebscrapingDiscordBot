
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import random as rd

category = ['fiction','non-fiction']

fiction_subcategory = ['modern-and-contemporary-fiction','poetry-and-drama','romance','crime','classic-fiction','fantasy','adventure-fiction','science-fiction','historical-fiction','horror-and-paranormal-fiction','graphic-novels','young-adult','manga','dystopian','graphic-novels']

non_fiction_subcategory = ['history','reference','science-and-technology','social-sciences','religion-and-spirituality','business-and-finance','education','politics','biographies','art-and-architecture','craft-and-hobbies','computing','philosophy','self-help-and-motivation','entertainment','health-and-wellbeing','cooking','family-and-relationships','military','language','travel','sport-and-leisure','pets-and-nature','home-and-garden','humour','true-crime']



def getRandomBook(category):

  random_page_number = rd.randint(1,200)
  random_book_number = rd.randint(1,96)
  random_book_href = "https://www.dymocks.com.au/"
  
  if category != "":
    category+='/'
  
  url = 'https://www.dymocks.com.au/books/'+category+'page-'+str(random_page_number)+'/?npp=96'
  req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
  
  webpage = urlopen(req).read()
  page_soup = soup(webpage, "html.parser")
  books = page_soup.findAll("a","product-tile-img-container")
  
  i = 1
  for book in books:
    if i == random_book_number:
      random_book_href += book['href']
      break
    i+=1
  
  return random_book_href


def getUserBook(choice):
  valid = 1
  
  if choice == 'book':
    return getRandomBook("")

  if choice in category:
    return getRandomBook(choice)

  elif choice not in category:
      if choice in fiction_subcategory:
        choice = 'fiction/'+choice

      elif choice in non_fiction_subcategory:
        choice = 'non-fiction/'+choice
      
      else:
        valid =0

  if valid:
    return getRandomBook(choice)
  return False

 
 


