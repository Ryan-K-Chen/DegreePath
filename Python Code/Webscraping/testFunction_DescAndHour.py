import requests
from bs4 import BeautifulSoup
from csv import writer
import re
import json

from selenium import webdriver  # this version of chromedriver.exe supports Chrome v83
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

course_dict = {}



def build_SubjectCourseDict():

    url = 'https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&subj_code_in=ECE&crse_numb_in=3005'
    # print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')  # get the raw html from the link in text form
    # if soup.find("All Sections for this Course")=="None":
    #     continue

    title = soup.find(class_='nttitle').text  # get the title from the page
    course_key = dict_buildCourseAndTitle(title)

    body = soup.find(class_='ntdefault').text  # get the "Detailed Class Information" from the page
    dict_buildDescAndHours(body, course_key)

    dict_buildPrerequisites(body, course_key)
    course_dict[course_key]['url'] = url

    return course_dict

def dict_buildDescAndHours(body, course_key):
    global course_dict
    course_dict[course_key]['Hours'] = {}
    print(body)

    bodyMatrix = list(filter(None, body.splitlines()))


    for i in range(1,6):

        if 'hours' in bodyMatrix[i]:
            bodyMatrix[i] = re.sub('[ ]{2,}', ' ', bodyMatrix[i])
            bodyMatrix[i] = bodyMatrix[i].replace(' 0.000 OR ', '')
            print('bodyMatrix[i]' + bodyMatrix[i])
            hoursMatrix = bodyMatrix[i].split(' ')
            hoursMatrix = list(filter(None, hoursMatrix))
            print(hoursMatrix)
            course_dict[course_key]['Hours'][hoursMatrix[1]] = hoursMatrix[0]
    course_dict[course_key]['Description'] = bodyMatrix[0]




def dict_buildCourseAndTitle(title):
    ######## make an edge case for classes not offered anymore ECE 2030 based on All Section for this COurse###
    global course_dict
    """  create a matrix of format, [Department, Course Number, Title]  """
    # print(info)
    tempMatrix = title.split(' - ')

    infoList = ['null', 'null', 'null']  # initialize matrix
    # reorganize string into desired matrix format ['Department', 'Course Number', 'Course Title']
    tempStr = tempMatrix[0]
    department = tempStr[:tempStr.find(' ')]
    courseNumber = tempStr[tempStr.find(' ') + 1:len(tempStr)]
    courseTitle = tempMatrix[1]

    course_key = department + courseNumber

    course_dict[course_key] = {}
    course_dict[course_key]['Department'] = department
    course_dict[course_key]['Course Number'] = courseNumber
    course_dict[course_key]['Course Title'] = courseTitle

    return course_key




def dict_buildPrerequisites(body, course_key):
    # get the "Prerequisites" from the page
    global course_dict

    ########## make edge case if there are no prereqs like CRN 80087#################################################
    try:
        rawPrereqs = body.lower().rsplit('prerequisites:')[1]
        ################ filter out excess text to return only course numbers ##########
        rawPrereqs = re.sub('\sminimum\sgrade\sof\s.', '', rawPrereqs)
        # rawPrereqs = rawPrereqs.replace(' minimum grade of c', '').replace(' minimum grade of d', '').replace(' minimum grade of t', '')
        rawPrereqs = rawPrereqs.replace('undergraduate semester level  ', '')
        rawPrereqs = rawPrereqs.replace(' and ', ' && ')
        rawPrereqs = rawPrereqs.replace(' or ', ' || ')
        rawPrereqs = rawPrereqs.strip()
        course_dict[course_key]['Prerequisites'] = rawPrereqs

    except IndexError:
        prereqList = []  ## what is inputted when no prerequisite courses are required




courses = build_SubjectCourseDict()

print(json.dumps(courses,sort_keys=True, indent=4)) ## prints out each entry in the dictionary


## Exports the courses dictionary as a json file
with open('courses.json', 'w') as json_file:
    json.dump(courses, json_file)

# response = requests.get("https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_course_detail?cat_term_in=202008&subj_code_in=ECE&crse_numb_in=3084")
# soup = BeautifulSoup(response.text, 'html.parser')  # get the raw html from the link in text form
