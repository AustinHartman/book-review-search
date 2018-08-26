#### INCOMPLETE ####

import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def inRecords(file, t):
    df = pd.read_csv(file)
    if (t in df.title.values):
        return True
    else:
        return False


def appendRecord(file, amazon_data, goodreads_data):
    data = [goodreads_data[3], goodreads_data[2], goodreads_data[0], goodreads_data[1], amazon_data[0], amazon_data[1]]

    # write data to file
    table = open(file, 'a')
    a = csv.writer(table)
    a.writerow(data)
    table.close()


def listBooksInLibrary(file):
    df = pd.read_csv(file)
    for t in df.title:
        print(t)


def bookComment(file):
    # user entered book name
    i = input("type the name of the book you would like to add a comment to: ")
    df = pd.read_csv(file)
    found_row = False

    for idx, row in df.iterrows():
        if (i.lower() in row['title'].lower()):
            found_row = True
            comment = input("Comment: ")
            df['user-comments'] = df['user-comments'].astype('str')
            if (df.iloc[idx]['user-comments'] == 'nan'):
                df.at[idx, 'user-comments'] = comment + ". "
            else:
                df.at[idx, 'user-comments'] += comment + ". "
            df.to_csv('books.csv', index=False)
            break

    if (found_row):
        print("Comment added")
    else:
        print("Unable to locate book")


def removeEntry(file):
    i = input("Name of book you would like to remove: ")
    df = pd. read_csv(file)
    found = False
    for idx, row in df.iterrows():
        if (i.lower() in row['title'].lower()):
            found = True
            verify = input("Is this the book you wish to remove: " + row['title'] + " (y/n): ")
            if (verify.lower() == 'y' or verify.lower() == 'yes'):
                df.drop(df.index[idx], inplace=True)
                print("Row was successfully dropped")
            else:
                print("Stopped row drop")

    if (not found):
        print("Book was not found")


def addHeaders(file):
    table = open(file, 'a')
    a = csv.writer(table)
    headers = ['title', 'author', 'goodreads-rating', 'goodreads-num-reviews', 'amazon-rating', 'amazon-num-reviews']
    a.writerow(headers)
    table.close()

# use with caution
def clear(file):
    table = open(file, 'w')
    table.close()
