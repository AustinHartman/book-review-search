from bs4 import BeautifulSoup
import requests
import re

# returns tuple (title with author(s), rating 0-5, number of reviews)
def getAmazonRatings(url):
    print("FUNC ENTERED")
    page = requests.get(url)
    print("made it here")
    soup = BeautifulSoup(page.content, 'html.parser')
    soup = BeautifulSoup(soup.prettify(), 'html.parser')

    ## TITLE ##
    title = soup.find('title')
    # clean text
    title = title.text
    title = re.sub(r'[^a-zA-Z\s,]', '', title)
    title = re.sub('Amazoncom', '', title)
    title = re.sub('Books', '', title)

    print(title)

    ## RATING ##
    rating = soup.find('span', attrs={'class', 'arp-rating-out-of-text'})
    rating = rating.text
    rating = rating.split()[0]

    print(rating)

    ## NUMBER OF REVIEWS ##
    num_reviews = soup.find('span', id='acrCustomerReviewText')
    num_reviews = num_reviews.text
    num_reviews = num_reviews.split()[0]

    return (title, rating, num_reviews)

# returns tuple (rating 0-5, number of reviews)
def getGoodreadsRatings(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")

    rating = soup.find('span', attrs={'itemprop': 'ratingValue'})
    rating = rating.text.strip()

    num_reviews = soup.find('span', attrs={'class', 'votes value-title'})
    num_reviews = num_reviews.text.strip()

    return (rating, num_reviews)
