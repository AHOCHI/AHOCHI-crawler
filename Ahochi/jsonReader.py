#code attempt 1

import json
from pprint import pprint
file = open('output5.json')
json_file = file.read()
json_data = json.loads(json_file)

#initalizes arrays
arrayKeyword= []
arrayUrl= []
arrayPageTitle= []
arrayMatch = []
arrayMatch.append([])

#looks for a keywords in the json and stores them, urls, and pagetitles
#in a temporary arrays
height= 0
while height < len(json_data):
    if json_data[height]["keyword"] != "nothing":
        arrayUrl.append(json_data[height]["url"])
        arrayKeyword.append(json_data[height]["keyword"])
        arrayPageTitle.append(json_data[height]["page_title"])
    height+= 1

#todo
#Scans for repeating urls in the temporary array and combines their
#keywords into the first url in the match
#todo: after combining, remove one/all of the duplicate(s) url,keyword, pagetitle
#k=0
#for i in arrayUrl:
#    if arrayUrl.count(i) > 1:
#        j= k + 1
#        while j < len(arrayUrl):
#            if arrayUrl[j] == arrayUrl[k]:
#                arrayKeyword[k]= arrayKeyword[k] + ", " + arrayKeyword[j]
#            j= j+1
#    k= k + 1

#looks for zipcodes in the json and stores them and their urls,keywords, and pagetitles
#then stores them into a final array
counter1=0
height=0
while height < len(json_data):
    value= json_data[height]
    #Continues if the element doesn't store "nothing"
    if json_data[height]["zip"] != "nothing":
        zipcode= json_data[height]["zip"]
        url= json_data[height]["url"]
        #continues only if the url has already been stored with a keyword
        if arrayUrl.count(url) > 0:
            index= arrayUrl.index(url)
            keyword= arrayKeyword[index]
            pageTitle= arrayPageTitle[index]
            length= len(arrayMatch)
            #Adds the new zipcode with an already stored keyword
            #Todo: get this to work
            if arrayMatch.count(zipcode) > 0:
                arrayMatch[index].append(zipcode)
                print "zip code is being added"
                print arrayMatch[index]
                print "Zip code was added"
            #Stores data into array without making an array
            elif counter1 == 0:
                arrayMatch[0].append(keyword)
                arrayMatch[0].append(url)
                arrayMatch[0].append(pageTitle)
                arrayMatch[0].append(zipcode)
                counter1 = counter1 + 1
                print "The first array has been stored"
            #creates an array in that index and then the data
            else:
                arrayMatch.append([])
                arrayMatch[length].append(keyword)
                arrayMatch[length].append(url)
                arrayMatch[length].append(pageTitle)
                arrayMatch[length].append(zipcode)
                print "A new array was created"
    height+= 1

json_data = open('TriStateFile').read()
data = json.loads(json_data)

finalArray=[]

userZip= 41073
i=0
while i < len(data[userZip]):
    x=0
    while x < len(arrayMatch):
        if arrayMatch[x][3] == data[userZip][i]:
            finalArray.append([])
            finalArray.append(arrayMatch[x][0])
            finalArray.append(arrayMatch[x][1])
            finalArray.append(arrayMatch[x][2])
            finalArray.append(arrayMatch[x][3])
            print "It was swapped"
        x= x+1  
    i= i+1

print(data[41074])



#Prints the final array
print "The final array is being printed"
print finalArray
print "The final array was printed"

