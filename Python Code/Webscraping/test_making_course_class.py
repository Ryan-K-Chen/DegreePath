import requests
from bs4 import BeautifulSoup
from csv import writer
import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

def getSubjectHtml(index):
    ## must install selenium and put chrome webdriver in same folder as this file
    # global browser      # keeps browser open after program executes
    browser = webdriver.Chrome()
    browser.get('https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_dyn_ctlg')


    ## Select the term
    ### MUST CHANGE TERM VALUE TO UPDATE FOR NEW SEMESTER ####
    currentTerm = 'Fall 2020'
    term = Select(browser.find_element_by_name('cat_term_in'))
    term.select_by_visible_text(currentTerm)       ### change this for corresponding update
    browser.find_element_by_xpath("//input[@type='submit']").click()

    ## Select the subject
    subjects = Select(browser.find_element_by_id('subj_id'))
    subjects.select_by_index(index)
    browser.find_element_by_xpath("//input[@type='submit']").click()
    return browser.page_source

def get_Subject_Course_URLs():
    subject_html = getSubjectHtml(75)       # get subject at this index (Electrical Engineering)
    soup = BeautifulSoup(subject_html, 'html.parser')

    main_site = 'https://oscar.gatech.edu'  # declare the main url that will be added to hrefs
    courses = []                            # initialize empty matrix
    # create a matrix of all course urls in soup
    for course in soup.find_all(class_='nttitle'):
        url = course.find('a', href=True)
        courses.append(main_site + url['href'])

    return courses




def getPrereqs(url):
    response = requests.get(url)           
    soup = BeautifulSoup(response.text, 'html.parser')      #get the raw html from the url in text form

    #get the "Prerequisites" from the page
    body = soup.find(class_='ntdefault').text

    ########## make edge case if there are no prereqs like CRN 80087#################################################
    try: 
        rawPrereqs = body.lower().rsplit('prerequisites:')[1]
        ################ filter out excess text to return only course numbers ##########
        rawPrereqs = re.sub('\sminimum\sgrade\sof\s.','',rawPrereqs)
        # rawPrereqs = rawPrereqs.replace(' minimum grade of c', '').replace(' minimum grade of d', '').replace(' minimum grade of t', '')
        rawPrereqs = rawPrereqs.replace('undergraduate semester level  ','')
        rawPrereqs = re.sub('[\(\)]','', rawPrereqs)
        rawPrereqs = rawPrereqs.strip()
        prereqList = rawPrereqs.split(' and ')

        ### print list of each prerequisite 
        # print(prereqList)
        # print('')

        ### separate each prerequisite into a list with the prereq options 
        for req in range(len(prereqList)):
            prereqList[req]= prereqList[req].split(' or ')

        ## test by printing each requirement and each option
        # for req in range(len(prereqList)):
        #     print("Course " + str(req) + ":")
        #     for option in range(len(prereqList[req])):
        #         print(prereqList[req][option])
        #     print('')

        return prereqList
    except IndexError:
        prereqList = ['No prerequisites']
        return prereqList


class Course(object):
    def __init__(self, url=''):
        self.department = ''
        self.courseNumber = ''
        self.title = ''
        self.prereqMatrix = []
        self.url = url
        self.getInfo()
    
    def printInfo(self):
        print('Department: ' + self.department)
        print('Course Number: ' + self.courseNumber)
        print('Title: ' + self.title)
        print('')
        print('Prerequisities: ')
        print(self.prereqMatrix)

    def getInfo(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')      #get the raw html from the link in text form

        info = soup.find(class_='nttitle').text     #get the "Detailed Class Information" from the page


        ######## make an edge case for classes not offered anymore ECE 2030 based on All Section for this COurse###

        """  create a matrix of format, [Department, Course Number, Title]  """
        # print(info)
        tempMatrix = info.split(' - ')
        
        infoList = ['null', 'null', 'null']         # initialize matrix 
        # reorganize string into desired matrix format
        tempStr = tempMatrix[0] 
        self.title = tempMatrix[1]
        self.department = tempStr[:tempStr.find(' ')]
        self.courseNumber = tempStr[tempStr.find(' ')+1:len(tempStr)]




courseURLs = get_Subject_Course_URLs()
course1 = Course(courseURLs[5])
# course1.getInfo()
course1.printInfo()
# for url in range(len(courseURLs)):
    