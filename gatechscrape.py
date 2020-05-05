import requests
from bs4 import BeautifulSoup
from csv import writer
import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

""" code to keep browser open after program executes """
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)



def getSubjectHtml(index):
    ## must install selenium and put chrome webdriver in same folder as this file
    global browser
    browser = webdriver.Chrome()
    browser.get('https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_dyn_ctlg')


    ## Select the term
    ### MUST CHANGE TERM VALUE TO UPDATE FOR NEW SEMESTER ####
    term = Select(browser.find_element_by_name('cat_term_in'))
    term.select_by_visible_text('Fall 2020')       ### change this for corresponding update
    browser.find_element_by_xpath("//input[@type='submit']").click()
    
    ## Select the subject
    subjects = Select(browser.find_element_by_id('subj_id'))
    subjects.select_by_index(index)
    browser.find_element_by_xpath("//input[@type='submit']").click()
    return browser.page_source


def getInfo(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')      #get the raw html from the link in text form

    info = soup.find(class_='ddlabel').text     #get the "Detailed Class Information" from the page

    """  create a matrix of format, [Course, CRN, Department, Number]  """
    print(info)
    infoList = info.split(' - ')
    

    tempStr = infoList[2]
    infoList[2] = tempStr[:tempStr.find(' ')]
    infoList[3] = tempStr[tempStr.find(' ')+1:len(tempStr)]
    del infoList[4:]   
    return infoList

def getPrereqs(url):
    response = requests.get(url)           
    soup = BeautifulSoup(response.text, 'html.parser')      #get the raw html from the url in text form

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





# url='https://oscar.gatech.edu/pls/bprod/bwckschd.p_disp_detail_sched?term_in=202008&crn_in=90087'
# course1Info = getInfo(url)
# print(course1Info)

# course1Prereqs = getPrereqs(url)
# print(course1Prereqs)

subject_html = getSubjectHtml(0)
soup = BeautifulSoup(subject_html, 'html.parser')


main_site = 'https://oscar.gatech.edu'  # declare the main url that will be added to hrefs
courses = []                            # initialize empty matrix
# create a matrix of all course urls in soup
for course in soup.find_all(class_='nttitle'):
    url = course.find('a', href=True)
    courses.append(main_site + url['href'])

print('courses')
print(courses)

