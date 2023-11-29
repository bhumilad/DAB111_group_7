# Titanic Dataset

## Team - 7

Titanic Dataset Project Overview 

This README file provides an outline of a project using the Titanic dataset. The project includes data cleaning, database creation, and a web application to visualize the data. 

Dataset Information 

The dataset used for this project can be found on Kaggle: Titanic Dataset. 

Step 1: Data Cleaning 

Cabin Column Removed: 
Reason: Of the 418 rows, 327 contained null values in the 'Cabin' column. 
Action: The 'Cabin' column was deleted. 

Null values dropped: 
Action: The dataset's remaining null values were eliminated. 

Made an updated CSV: 
Name of file: "new_titanic.csv" 

Step 2: Database Creation 

The cleaned data is read from 'new_titanic.csv' by the 'dataload.py' script, which then loads it into an SQLite database.  

 

Step 3: Web Application 

The Flask framework is used by the 'app.py' script to build a web application with two routes: 

  

/: The 'about.html' page is rendered by this. Features a button to jump to the dataset. 

  

/data: Opens the 'data.html' page with data that has been retrieved from the SQLite database ('titanic.db'). 

 

HTML Pages 

 

'about.html' 

Heading and Style: 

The main header of the website reads "Titanic Data."  

There's a "Jump on dataset" button that has a purple block-like design.  

The Titanic Story: 

The article is a brief account of the Titanic's sinking, including the tragic part when not everyone was able to be salvaged.  

It briefly discusses chance and how certain social groups have higher survival rates. 

Dataset URL: 

There is a heading labelled "Dataset link." Below is a URL that can be clicked to access the Titanic dataset on Kaggle. 

Table of Data Description: 

Every item of data in the dataset, including PassengerId, Survived, Pclass, and so forth, is described in a table. 

It makes it easier for readers to comprehend the meaning of each dataset column. 

 

 

'data.html'  

Heading and Style: 

The main header on the page reads "Data Viewer - Results." 

There is a "Jump to description of data" button that has a purple block-like design. It is a convenient method to return to the story page. 

  

Data Table: 

A large table takes up most of the page. In our collection, each row represents a line, and each column displays a distinct piece of data. 

It's a clever method of viewing a portion of the Titanic dataset without being overtaken by data. 

 

How to Experience the Journey 

 

Prepare Your Tools:  
Verify that Flask and Python are installed on your computer. 

Cleaning Data:  
Launch and operate the 'dataload.py' file. This will transfer the data into the 'titanic.db' database and clean it up. 

Web Application: 

To access the directory containing "app.py," open a terminal or command prompt. 

Execute this command: 
python app.py 

You can launch the application by going to http://127.0.0.1:5000/ or http://localhost:5000/ in your web browser. 

Note: 

The 'database' directory is where 'titanic.db' is supposed to be, according to the SQLite database connection. If your configuration is different, please modify the connection details in 'app.py'. 
 

For demonstration purposes, the first 25 rows from the 'titanic_table' are retrieved via the '/data' route. To change the data that is presented, edit the SQL query in 'app.py'. 

 

Feel free to explore the web application, and don't hesitate to contact us if you have any questions or run into any problems! 