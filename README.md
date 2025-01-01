## About
Full Stack Program to manage music audition scores using Python, tkinter, and mySQL

## Files
### auditionDatabase.sql
* mySQL file
* manage all data
* connected with the Python files

### auditionDb.py
* connect to mySQL
* different functions to manage student data
  * insert, delete, update, reading data, and connect/disconnect to mySQL
 
### auditionGui.py
* tkinter
* imports class 'AuditionDb' from auditionDb.py to access the data
* buttons to connect/disconnect with mySQL, navigate through the data
* CRUD operations

### auditionee2.png
* background of GUI
* called in auditionGui.py

### auditionMain.py
* defines main to run both auditionDb.py and auditionGui.py file
* run this file
