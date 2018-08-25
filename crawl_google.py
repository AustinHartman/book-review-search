from googlesearch import search
import requests
import scrape
import sys


def getSearch():
    s = input("Book title: ")
    return str(s)


def getURL(query, site):
    # variables store addresses to scrape from
    site_query = query + " " + site
    site_url = ""

    for url in search(site_query, stop=3):
        if (site in url):
            site_url = url
            break

    return site_url


def checkFound(url, site):
    if (len(url) > 0):
        print("+ " + site + " URL found")
        return True
    else:
        print("- " + site + " URL not found")
        return False


s = getSearch()

print("\nFetching data...\n")

goodreads_url = getURL(s, "goodreads")
amazon_url = getURL(s, "amazon")

gr_found = checkFound(goodreads_url, "Goodreads")
az_found = checkFound(amazon_url, "Amazon")

### NOW SCRAPE DATA FROM WEBSITES IF LINKS FOUND ####
if (gr_found):
    try:
        goodreads_data = scrape.getGoodreadsRatings(goodreads_url)
        print("\n")
        print("Author:", goodreads_data[2])
        print("\n")
        print("GOODREADS")
        print("Rating:", goodreads_data[0])
        print("Number of Reviews:", goodreads_data[1])
    except:
        print("\n")
        print("Sorry, something went wrong with the goodreads scraping")

if (az_found):
    try:
        amazon_data = scrape.getAmazonRatings(amazon_url)
        print("\n")
        print("AMAZON")
        print("Rating:", amazon_data[0])
        print("Number of Reviews:", amazon_data[1])
    except:
        print("\n")
        print("Sorry, something went wrong with the Amazon scraping")
