name = open("logs_chloe.csv", "r")
dataset = name.read()

datalist = dataset.split("\n")
# print(len(datalist)) to check that the number of lines that are output is correct -- 1417

# get rid of un-needed part of strings and append new strings to a list
datalist2 = list()
for item in datalist:
    newitem = item.replace("GET ,/matcher/filter-providers/?", "")
    datalist2.append(newitem)

# split string on the "&" and append filter pairs to a list
pairlist = list()
for item in datalist2:
    pairs = item.split("&")
    for pair in pairs:
        pairlist.append(pair)

# split filter pairs on the "=" and append the items at [0] to a list       
filterlist = list()
for pair in pairlist:
    shortlist = pair.split("=")
    filterlist.append(shortlist[0])

# count how many of each type of filter
filtercounts = dict()
for item in filterlist:
    filtercounts[item] = filtercounts.get(item, 0) + 1

# create tuples with value first and key second
filtertups = list()
for key, value in filtercounts.items():
    filtertups.append( (value, key) )

# sort in descending order
sortedfilterlist = sorted(filtertups, reverse=True)

for item in sortedfilterlist:
    print(item[0], item[1])

















