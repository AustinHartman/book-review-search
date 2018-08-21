from bs4 import BeautifulSoup
import requests

# returns tuple (rating 0-5, number of reviews)
def getAmazonRatings(url):
    ls = url.split('/')
    for i in range(len(ls)):
        if (ls[i] == 'dp'):
            asin = ls[i+1]
            break
    # to use this for scraping, first the asin key must be appended
    review_url = 'https://www.amazon.com/gp/customer-reviews/widgets/average-customer-review/popover/ref=dpx_acr_pop_?contextId=dpx&asin='
    review_url += asin

    page = requests.get(review_url)
    soup = BeautifulSoup(page.content, 'lxml')

    ## RATING ##
    rating = soup.find('span', attrs={'class': "a-size-base a-color-secondary"})
    rating = rating.text
    # example text: '4.0 starts out of five'
    rating = rating.split()[0]

    ## NUMBER OF REVIEWS ##
    num_reviews = soup.find('div', attrs={'class': "a-section a-spacing-none a-text-center"})
    num_reviews = num_reviews.text
    # example text: 'see all 31 reviews'
    num_reviews = num_reviews.split()[2]

    return (rating, num_reviews)

# returns tuple (rating 0-5, number of reviews, author (1st author if more than one))
def getGoodreadsRatings(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")

    rating = soup.find('span', attrs={'itemprop': 'ratingValue'})
    rating = rating.text.strip()

    num_reviews = soup.find('span', attrs={'class': 'votes value-title'})
    num_reviews = num_reviews.text.strip()

    author = soup.find('span', attrs={'itemprop': 'name'})
    author = author.text

    return (rating, num_reviews, author)
