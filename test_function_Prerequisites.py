import requests
from bs4 import BeautifulSoup
from csv import writer
import re

link = 'https://oscar.gatech.edu/pls/bprod/bwckschd.p_disp_detail_sched?term_in=202008&crn_in=90087'


response = requests.get(link)           
soup = BeautifulSoup(response.text, 'html.parser')      #get the raw html from the link in text form

#get the "Prerequisites" from the page
body = soup.find(class_='dddefault').text

##########make edge case if there are no prereqs like CRN 80087#################################################
# try: 
rawPrereqs = body.lower().rsplit('prerequisites:')[1]
# except:

################ filter out excess text to return only course numbers ##########
rawPrereqs = re.sub('\sminimum\sgrade\sof\s.','',rawPrereqs)
# rawPrereqs = rawPrereqs.replace(' minimum grade of c', '').replace(' minimum grade of d', '').replace(' minimum grade of t', '')
rawPrereqs = rawPrereqs.replace('undergraduate semester level  ','')
rawPrereqs = re.sub('[\(\)]','', rawPrereqs)
rawPrereqs = rawPrereqs.strip()
prereqList = rawPrereqs.split(' and ')

### print list of each prerequisite 
print(prereqList)
print('')

### separate each prerequisite into a list with the prereq options 
for req in range(len(prereqList)):
    prereqList[req]= prereqList[req].split(' or ')



for req in range(len(prereqList)):
    print("Course " + str(req) + ":")
    for option in range(len(prereqList[req])):
        print(prereqList[req][option])
    print('')
