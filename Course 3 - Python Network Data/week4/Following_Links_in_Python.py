##Following Links in Python
##
##In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.
##
##We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment
##
##Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html 
##Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
##Sequence of names: Fikret Montgomery Mhairade Butchi Anayah 
##Last name in sequence: Anayah
##Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Mael.html 
##Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
##Hint: The first character of the name of the last page that you will load is: S
##Strategy
##The web pages tweak the height between the links and hide the page after a few seconds to make it difficult for you to do the assignment without writing a Python program. But frankly with a little effort and patience you can overcome these attempts to make it a little harder to complete the assignment without writing a Python program. But that is not the point. The point is to write a clever Python program to solve the program.
##
##Sample execution
##
##Here is a sample execution of a solution:
##
##$ python3 solution.py
##Enter URL: http://py4e-data.dr-chuck.net/known_by_Fikret.html
##Enter count: 4
##Enter position: 3
##Retrieving: http://py4e-data.dr-chuck.net/known_by_Fikret.html
##Retrieving: http://py4e-data.dr-chuck.net/known_by_Montgomery.html
##Retrieving: http://py4e-data.dr-chuck.net/known_by_Mhairade.html
##Retrieving: http://py4e-data.dr-chuck.net/known_by_Butchi.html
##Retrieving: http://py4e-data.dr-chuck.net/known_by_Anayah.html
##The answer to the assignment for this execution is "Anayah".

#print("\n\n\n\n It is a pleasure for me to take this course !!!\n\n")

# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
count_ranges = 0
target_count_ranges = 18 # 3 for http://py4e-data.dr-chuck.net/known_by_Fikret.html
count_times = 0
target_count_times = 7 # 4 for http://py4e-data.dr-chuck.net/known_by_Fikret.html
# the parameters 18 and 7 are for the link http://py4e-data.dr-chuck.net/known_by_Mael.html
# Retrieve all of the anchor tags
tags = soup('a')
while(count_times < target_count_times):
    print("new page ", count_times)
    for tag in tags:
        count_ranges += 1
        #print("trying ", count_ranges, tag.get('href', None))
        if(count_ranges == target_count_ranges):
            url = tag.get('href', None)
            print("matching ", url[39:len(url)-5])            
            html = urllib.request.urlopen(url, context=ctx).read()
            soup = BeautifulSoup(html, 'html.parser')
            tags = soup('a')
    count_times += 1
    count_ranges = 0