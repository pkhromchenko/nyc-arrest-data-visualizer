import urllib.request
import json
import csv


def unique_values(k, lst):
    newlst = []
    for dict in lst:
        if dict[k] not in newlst:
            newlst.append(dict[k])
    return newlst


def filter_list(k, v, lst):
    newlst = []
    for dict in lst:
        if (k, v) in dict.items():
            newlst.append(dict)
    return newlst

# Create a new dict that pairs index positions with one another. Ie create new dict in which
# index 1 of the key list  is paired with its value (index 1 of the values list) & so on.


def dict_gen(keys, values):
    newdict = {}
    i = 0
    for item in keys:
        newdict[keys[i]] = values[i]
        i = i + 1
    return newdict


def get_values(keys, dic):
    newlst = []
    for searchkey in keys:
        newlst.append(dic.get(searchkey))
    return newlst

# Define a function named header_reader with one parameter:
# the parameter, called f_in in this description, is a string.
# The parameter specifies the name of the CSV file to be read.
# Your function will need to open f_in and read in the first row of the file. (The first row of the file contains the column headers).
# Your function must return a list containing the values in that header row.


def header_reader(f_in):
    newlst = []
    with open(f_in) as f:
        reader = csv.reader(f)
        header = next(reader)
        return header


def data_reader(f_in):
    newlst = []
    with open(f_in) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            newlst.append(row)
        return newlst


# Define a function named header_writer with two parameters:
# the 1st parameter, called lst in this description, is a list of strings
# the 2nd parameter, called f_out in this description, is a string.
# Your function will need to open f_out so that any existing contents will be erased.
# The contents of lst should be written to f_out as a row in a CSV file. Your function does not need to return anything.


def header_writer(lst, f_out):
    with open(f_out, "w") as f:
        writer = csv.writer(f)
        writer.writerow(lst)


# Define a function named data_writer with two parameters:
# the 1st parameter, called lst in this description, is a list of lists
# the 2nd parameter, called f_out in this description, is a string.
# Your function will need to open f_out so that its existing contents are preserved.
# Your function will need to write each entry in lst as a row in a CSV file at the end of f_out.
# The order of the added rows in f_out must match the order the entries appear in lst. Your function does not need to return anything.

def data_writer(lst, f_out):
    with open(f_out, "a") as f:
        writer = csv.writer(f)
        for entry in lst:
            writer.writerow(entry)


def clean_list(strx, listofdicts):
    newdict = []
    for lst in listofdicts:
        for entry in lst:
            if entry == strx:
                newdict.append(lst)
            else:
                continue
    return newdict


def cache_reader(f_in):
    newlst = []
    newdict = {}
    with open(f_in) as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            i = 0
            for entry in row:
                newdict[header[i]] = entry
                i += 1
            newlst.append(newdict)
        print(newlst)
        return newlst


def cache_writer(lst, f_out):
    with open(f_out, "w") as f:
        writer = csv.writer(f)
        headers = []
        i = 0
        for dict in lst:
            datalst = []
            for key in dict:
                if key not in headers:
                    headers.append(key)
            if i == 0:
                writer.writerow(headers)
                i += 1
            for value in dict.values():
                datalst.append(value)
            writer.writerow(datalst)


def retrieve_json(url):
    url2 = urllib.request.urlopen(url)
    text = url2.text
    data = json.loads(text)
    return data