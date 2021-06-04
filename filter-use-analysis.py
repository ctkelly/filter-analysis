#import csv -- could not figure out how to make this work

name = open("logs_chloe.csv", "r")
dataset = name.read()

datalist = dataset.split("\n")
#print(len(datalist)) check that the number of lines that are output is correct -- 1417

datalist2 = list()
for item in datalist:
    newitem = item.replace("GET ,/matcher/filter-providers/?", "")
    datalist2.append(newitem)
#print(datalist2)    

pairlist = list()
for item in datalist2:
    pairs = item.split("&")
    for pair in pairs:
        pairlist.append(pair)
# print(pairlist) 
       
filterlist = list()
for pair in pairlist:
    shortlist = pair.split("=")
    filterlist.append(shortlist[0])
#print(filterlist)

filtercounts = dict()
for item in filterlist:
    filtercounts[item] = filtercounts.get(item, 0) + 1
#print(filtercounts)

filtertups = list()
for key, value in filtercounts.items():
    filtertups.append( (value, key) )
#print(filtertups)    

sortedfilterlist = sorted(filtertups, reverse=True)
#print(sortedfilterlist)

for item in sortedfilterlist:
    print(item[0], item[1])

















