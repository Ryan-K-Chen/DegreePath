from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


## must install selenium and put chrome webdriver in same folder as this file
browser = webdriver.Chrome()
browser.get('https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_dyn_ctlg')


## Select the term
### MUST CHANGE TERM VALUE TO UPDATE FOR NEW SEMESTER ####
term = Select(browser.find_element_by_name('cat_term_in'))
term.select_by_visible_text('Fall 2020')       ### change this for corresponding update
browser.find_element_by_xpath("//input[@type='submit']").click()


index = 1

## Select the subject
subjects = Select(browser.find_element_by_id('subj_id'))
subjects.select_by_index(index)
browser.find_element_by_xpath("//input[@type='submit']").click()
print(browser.page_source)