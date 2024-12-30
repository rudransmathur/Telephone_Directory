# TELEPHONE DIRECTORY
## Table of Contents

|SL.NO|Topic|
|-|--|
|I|[System Specification At a Glance](https://github.com/rudransmathur/Telephone_Directory#i-system-specification-at-a-glance)|
|II|[Requirement Analysis](https://github.com/rudransmathur/Telephone_Directory#ii-requirement-analysis)|
|III|[System Specifications](https://github.com/rudransmathur/Telephone_Directory#iii-system-specifications)|
|IV|[Module](https://github.com/rudransmathur/Telephone_Directory#iv-modules)|
|V|[Table Design and Structures](https://github.com/rudransmathur/Telephone_Directory#v-table-design-and-structure)|
|VI|[Procedure / Function Description](https://github.com/rudransmathur/Telephone_Directory#vi-procedurefunction-description)|
|VII|[Future Enhancements](https://github.com/rudransmathur/Telephone_Directory#vii-future-enhancemets)|
|VIII[Bibliography](https://github.com/rudransmathur/Telephone_Directory#viii-bibliography)|
## I. SYSTEM SPECIFICATION AT A GLANCE
### AIM
The objective of our project is to computerize the telephone directory. Front end is developed using Python 3.7.7 software and back end is with MySQL 8.0. Thus, the entire project is based on Python-MySQL connectivity. The various modules included are:
<ol>
  <li>
    Login
  </li>
  <li>
    Add a record to the directory 
  </li>
  <li>
    Displaying all records 
  </li>
  <li>
    Search for a record using name 
  </li>
  <li>
    Search using city 
  </li>
  <li>
    Search using start alphabet 
  </li>
  <li>
    Modify a record
  </li>
  <li>
    Delete a record 
  </li>
  <li>
    Logout
  </li>
</ol>

### MODULES<br>
**Login**<br>
This is to provide a secured environment for the system. Software allows only the person with the correct username and password to enter into the software.

**Adding a record to the directory**<br>
In this module, software provides the interface to enter the details required to add the details of a person to directory. This includes directory number, person’s name, city, telephone number, address and occupation. 

**Displaying all records**<br>
Module lists all details of every person using tree view widget in Python’s tkinter module.

**Search for a record using name**<br>
Here name of the person is entered as input and all records are searched and it displays the record with the name entered as input

**Search using city**<br>
This module allows the administrator to search the details based on city. This displays the details of all persons of a city.

**Search using start alphabet**<br>
Here an alphabet is entered as input and the records with name starting with alphabet is displayed.

**Modify a record**<br>
Here we enter directory number as input and search and display that record. The administrator can modify all details except directory number and save.

**Delete a record**<br>
Here we enter directory number as input and search for that record and remove that record from our database.

**Logout**<br>
This module allows the administrator to come out from the software whenever he is moving out of his seat. So that unauthorized people cannot handle the things.

### DATABASE<br>
This project includes one database in MySQL named ‘Telephone’, having tables:
* **DIRECTORY** - which stores details like directory number (DNO), person’s name (NAME), person’s city (PHONE_NO), occupation (JOB) 
* **ADDRESS** - which stores Address ID (AID), House No (HNO), Area/Locality (Area), City (CITY), Pincode (PINCODE) and directory number (DNO).


## II. REQUIREMENT ANALYSIS

**HARDWARE REQUIREMENTS**

* **Processor**:Intel® CoreTM i3 CPU
* **CPU speed**:2.67 GHz
* **RAM**:4GB
* **Hard disk memory**:80GB
* **Cache**:512 KB

**SOFTWARE REQUIREMENTS**
* **Operating System**: Microsoft Windows 10
* **Software**: Python 3.8.5 and MySQL Server 8.0.21
* **Python Libraries**: tkinter, pyglet, mysql-connector, pillow.

## III. SYSTEM SPECIFICATIONS
**MySQL Database: Telephone**
**Table: DIRECTORY**

 ![image](https://github.com/user-attachments/assets/e8fc68e7-7cdd-454d-a8a9-61267485ec91)

**Description of data:** <br>
DNO: Directory number<br>
NAME: Name of the person<br>
PHONE_NO: Telephone number of the person<br>
JOB: Occupation of the person<br>

**Table: ADDRESS**

![image](https://github.com/user-attachments/assets/c7e417fc-c572-4304-b717-49de861e926b)

**Description of data:** <br>
AID: Address Id of the person<br>
HNO: House number where the person<br>
AREA: Locality in which the person lives<br>
CITY: City of the person<br>
PINCODE: Postal Address code where the person lives<br>
DNO: Directory number<br>

## IV. MODULES
Modules in our project along with their associated functions are as follows:
|Module Name|Puspose|Functions|
|-|-|-|
|mysql.connnector|To establish connection between Python and MySQL|connect( )<br>cursor( )<br>commit( )<br>execute( )<br>fetchone( )<br>fetchall( )<br>close( )
|tkinter|To create the GUI|Tk( )<br>title( )<br>geometry( )<br>configure( )<br>deiconify( )<br>Label( )<br>place( )<br>Entry( )<br>mainloop( )<br>Button( )<br>get( )<br>pack()<br>frame( )<br>scrollbar( )<br>destroy( ) <br>delete()<br>focus()<br>Toplevel()<br>grid_propogate()<br>resizeable()<br>withdraw()<br>winfo_screenwidth()<br>winfo_screenheight|
|tkinter’s  tkmessagebox|	To create intractable message boxes|showerror( )<br>showinfo( )|
|tkinter’s ttk|	To provide additional benefits to Tkinter like tables, font rendering, etc	|Treeview()<br>grid()<br>column()<br>heading()<br>insert()|
|pyglet|Easy to use Python library for developing games and other visually-rich applications|font.add_file()|
|pillow|lightweight image processing tools that aid in editing, creating and saving images|PhotoImage()|
|pickle|A module in python used for converting python datatypes into bytes and strings|open()<br>dump()<br>load()<br>close()|
|User defined functions|Deals with the SQL based operations|checking()<br>insertingdir()<br>insertingadd()<br>inserteddir()<br>insertedadd()<br>display()<br>display2()<br>searchname()<br>searchcity()<br>searchname1()<br>show1()<br>show2()<br>show3()<br>update()<br>hupdating()<br>updation()<br>deletion()<br>delete()<br>bi()|

## V. TABLE DESIGN AND STRUCTURE

|Sno.	|Field Name|	Type/Constraints|Purpose|
|-|-|-|-|
|1|	DNO|INT (5)(PRIMARY KEY, NOT NULL)|	It stores the directory id|
|2|NAME|VARCHAR(30)|	It stores the name of the person |
|3|PHONE_NO|VARCHAR (10)|	It stores the telephone number|
|4|JOB|VARCHAR (30)|	It stores the Occupation of the person|

|Sno.	|Field Name	|Type/Constraints	|Purpose|
|-|-|-|-|
|1|AID|	INT (5)(PRIMARY KEY, NOT NULL)|It stores the address id|
|2|HNO|VARCHAR(4)	|It stores the house number|
|3|AREA|	VARCHAR (30)|	It stores the area|
|4|CITY|VARCHAR (30)	|It stores the city|
|5|PINCODE|	INT (6)	|It stores the pincode|
|6|	DNO|INT (5)(FOREIGN KEY)|	It stores the directory id|

## VI. PROCEDURE/FUNCTION DESCRIPTION
|Sno|	Function|	Purpose|
|-|-|-|
|1|	checking()|	Checks the username and password 
|2	|insertingdir()|	For entering values for directory table
|3	|insertingadd()	|For entering values for address table
|4	|inserteddir()	|For inserting values in directory table
|5	|insertedadd()	|For inserting values in address table
|6	|display()	|For displaying all the records
|7	|searchname()|	For entering name to search
|8	|searchcity()	|For entering city to search
|9	|searchname1()	|For entering first letter of name to search
|10	|show1()	|For searching and displaying the records based on name  
|11	|show2()	|For displaying the records based on city
|12	|show3()	|For searching records with starting alphabet of name
|13	|update()	|For adding Entry and Button widget to window
|14	|updating()	|For retrieving data entered in the Entry and verify it|
|15	|updated()	|For making changes in directory|
|16	|deletion()	|For adding Entry and Button widget to window|
|17	|delete()	|For verifying data and deleting record in directory
|18	|bi()	|For displaying contact list
|19	|Canvases()	|To create a canvas for window

## VII FUTURE ENHANCEMETS

In the future designs, this program can be modified to not only store details but also the images of the people. Option for changing login details can be included.

## VIII. BIBLIOGRAPHY

<ul>
  <li>
    Computer Science with Python by Sumita Arora
  </li>
  <li>
    Tutorialspoint.com
  </li>
  <li>
    RealPython.com
  </li>
  <li>
    Python and Tkinter Programming by John
  </li>
  <li>
    Grayson
  </li>
  <li>
    Codemy.com
  </li>
  <li>
    Stackoverflow.com
  </li>
</ul>
