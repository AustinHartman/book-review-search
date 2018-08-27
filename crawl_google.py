from googlesearch import search
import requests
import sys
import os

import scrape
import book_records

gr_found = False
az_found = False
amazon_data = ()
goodreads_data = ()

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


def saveBook(gr_found, az_found, goodreads_data, amazon_data):
    if (az_found and gr_found):
        if (not book_records.inRecords('books.csv', goodreads_data[3])):
            book_records.appendRecord('books.csv', amazon_data, goodreads_data)
            print("Book was saved successfully")
        else:
            print("Book is already in your library")
    else:
        print("There is no book data to save")


def helpMenu():
    print("'search book'    - search a new book")
    print("'save book'      - save book")
    print("'quit'           - leave app")
    print("'help'           - display help menu")
    print("'show library'   - display title of all saved books")
    print("'add comment'    - add a comment to a book in saved books")
    print("'remove book'    - remove a book from saved books")


def getAction():
    action = input("Type an action (type help for list of actions): ")
    commands = ['search book', 'save book', 'help', 'quit', 'show library', 'add comment', 'remove book']
    while (action not in commands):
        print("Invalid input")
        action = input("Type an action (type help for list of actions): ")
    return action


def handleAction(gr_found, az_found, goodreads_data, amazon_data):
    action = getAction()
    if (action == 'quit'):
        quit()
    elif (action == 'search book'):
        gr_found, az_found, goodreads_data, amazon_data = searchBookData(gr_found, az_found, goodreads_data, amazon_data)
    elif (action == 'save book'):
        saveBook(gr_found, az_found, goodreads_data, amazon_data)
    elif (action == 'help'):
        helpMenu()
    elif (action == 'show library'):
        book_records.listBooksInLibrary('books.csv')
    elif (action == 'add comment'):
        book_records.bookComment('books.csv')
    elif (action == 'remove book'):
        book_records.removeEntry('books.csv')

    return (gr_found, az_found, goodreads_data, amazon_data)


def searchBookData(gr_found, az_found, goodreads_data, amazon_data):
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
            print("Title:", goodreads_data[3])
            print("Author:", goodreads_data[2])
            print("Description:", goodreads_data[4])
            print("\n")
            print("GOODREADS")
            print("Rating:", goodreads_data[0])
            print("Number of Reviews:", goodreads_data[1])
        except:
            gr_found = False
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
            az_found = False
            print("\n")
            print("Sorry, something went wrong with the Amazon scraping")

    return (gr_found, az_found, goodreads_data, amazon_data)


def displayTitle():
    os.system('clear')
    print("Book Search App")


while (True):
    # displayTitle()
    gr_found, az_found, goodreads_data, amazon_data = handleAction(gr_found, az_found, goodreads_data, amazon_data)
    print("\n")
