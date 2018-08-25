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
