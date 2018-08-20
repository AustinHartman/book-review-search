from googlesearch import search
import requests
import bs4_functions
import sys

# to search
query = input("Book title: ")

# variables store addresses to scrape from
amazon_query = query + " amazon"
goodreads_query = query + " goodreads"
amazon_url = ""
goodreads_url = ""

print("\nFetching data...\n")

for url in search(amazon_query, stop=3):
    if ("amazon" in url):
        amazon_url = url
        break

for url in search(goodreads_query, stop=3):
    if ("goodreads" in url):
        goodreads_url = url
        break

if (len(amazon_url)>0):
    print("+ Amazon URL found")
if (len(goodreads_url)>0):
    print("+ Goodreads URL found")
if (len(amazon_url)<1 and len(goodreads_url)<1):
    print("Sorry, no ratings were found.")


### NOW SCRAPE DATA FROM WEBSITES IF LINKS FOUND ####
if (len(amazon_url)>0):
    try:
        amazon_data = bs4_functions.getAmazonRatings(amazon_url)
        print("\n")
        print("AMAZON")
        print("Rating:", amazon_data[0])
        print("Number of Reviews:", amazon_data[1])
    except:
        print("Sorry, something went wront with the Amazon scraping")

if (len(goodreads_url)>0):
    try:
        goodreads_data = bs4_functions.getGoodreadsRatings(goodreads_url)
        print("\n")
        print("GOODREADS")
        print("Rating:", goodreads_data[0])
        print("Number of Reviews:", goodreads_data[1])
    except:
        print("Sorry, something went wrong with the goodreads scraping")
