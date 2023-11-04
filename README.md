# RSMS-ActivityPoints-Tracker
![demo img](https://github.com/notalanjoseph/RSMS-ActivityPoints-Tracker/blob/main/demo.png)
![documentation](https://img.shields.io/readthedocs/gspread?logo=readthedocs)
![python version](https://img.shields.io/pypi/pyversions/gspread?style=pypi)

RSET students submit their certificates in RSMS website categorically for activity points. Finding out how much points one has accumulated so far is a hassle, as RSMS doesnt have a page that shows total points.  
This Python script solves the problem by automating login and scraping the RSMS website using Selenium & bs4 to calculate and display the total activity points gained by a student.  
Tracking of activity status is also incorporated- activities are displayed semester wise with status & points awarded for each activity.

## Prerequisites 🏁

- Python version 3.7 or higher.
- pip (any recent version).
- Microsoft Edge browser.
- Internet connection.

## How to use this 💻

- Clone this repository or download and extract the zip file.
- Open terminal from the folder RSMS-ActivityPoints-Tracker.
- Install the python dependencies using `pip` or `pip3`.
```bash
pip install -r requirements.txt
``` 
- Edit `msEdge.py` to enter your credentials OR enter credentials when prompted during runtime.
- Run the python code.
```bash
python msEdge.py
``` 
- That's it! The automated browser will open in your system and do the work. The program may take a few minutes to complete based on the no.of semesters. The result will be displayed in your terminal.