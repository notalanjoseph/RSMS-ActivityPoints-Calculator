from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import bs4
import time
import maskpass
from tabulate import tabulate

# ENTER YOUR CREDENTIALS
uid = ""
password = ""

TOTAL = 0

if uid == "":
    uid = str(input("Enter Uid: "))
if password == "":
    password = maskpass.askpass("Enter password: ")

# do something to reduce log info displayed in terminal

driver = webdriver.Edge()

# login
driver.get('https://www.rajagiritech.ac.in/stud/ktu/student/')
time.sleep(1)
driver.find_element("name", "Userid").send_keys(uid)
driver.find_element("name", "Password").send_keys(password)
driver.find_element("name", "Password").send_keys("\ue007")
time.sleep(1)

# navigating to activity page
activity_link = driver.find_element(By.LINK_TEXT, "Activity Point Form")
activity_link.click()
time.sleep(1)

def getActivities(driver, total):
    global TOTAL
    TOTAL = total
    table_sem = []
    for i in range(11,28):
        #activity = str(i)
        driver.find_element(By.XPATH, "//option[@value='"+str(i)+"']").click()
        #time.sleep(0.5)
        submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
        submit_button.click()
        time.sleep(1)
        soup = bs4.BeautifulSoup(driver.page_source, "lxml")
        table = soup.find('table', {'class': 'table table-striped'})
        if table != None:
            #print(i)
            columns = [1] # Activity Category at colm 1
            rows = [row for row in table.find_all('tr')]
            #for row in table.findAll('tr'):
            for row in rows:
                if len(row.find_all('td')) == 0: #empty row
                    continue
                elif row == rows[0]: #headings
                    cells = [cell for cell in row.find_all('td')]
                    j = 0
                    for cell in cells:
                        heading = str(cell.find("font").find("b").text)
                        if heading == "Name of the Course" or heading == "Name of event" or heading == "Name of the Conference/ event" or heading == "Name of the Company and Address" or heading == "Name of Exam" or heading == "Nameof company" or heading == "Name/ title of patent" or heading == "Name and Details of product/ innovation/idea":
                            columns.append(j)
                        elif heading == "Rating By Faculty":
                            columns.append(j)
                        elif heading == "Point Status":
                            columns.insert(2, j)
                        j += 1        
                else: #data 
                    cells = [cell for cell in row.find_all('td')]
                    table_row = []
                    for j in columns:
                        table_row.append((cells[j].text).replace('\n', ' ')[:50])
                        #print(cells[j].text, end = '\t')
                    if table_row[3] != '':
                        TOTAL += int(table_row[3])  
                    table_sem.append(table_row)

    print(tabulate(table_sem, headers=["Activity Category", "Name", "Status", "Rating"], tablefmt="github"))
    #print(TOTAL)


#for class in Class_Code
n = len(driver.find_element(By.ID, 'list1').find_elements(By.TAG_NAME, 'option'))#no.of sems
for x in range(n):
    sems = Select(driver.find_element(By.ID, 'list1'))
    sems.select_by_index(x)
    #time.sleep(0.5)
    print("\nSEMESTER ", n-x)
    getActivities(driver, TOTAL)

print("\n\nTOTAL ACTIVITY POINTS GAINED = ", TOTAL)

driver.quit()
time.sleep(1)
