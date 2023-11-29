# Titanic Dataset Project Overview 

This README file provides an outline of a project using the Titanic dataset. The project includes data cleaning, database creation, and a web application to visualize the data. 

## Dataset Information 

!['titanic'](https://wallpapers.com/images/hd/underwater-sunken-titanic-bat2e49s3bc1s45y.jpg)

The dataset used for this project can be found on Kaggle: [Titanic Dataset](https://www.kaggle.com/datasets/brendan45774/test-file). 

**Step 1: Data Cleaning**

1. Cabin Column Removed: 
Reason: Of the 418 rows, 327 contained null values in the 'Cabin' column. 
Action: The 'Cabin' column was deleted. 

2. Null values dropped: 
 Action: The dataset's remaining null values were eliminated. 

3. Made an updated CSV: 
 Name of the file: "new_titanic.csv" 

**Step 2: Database Creation** 

The cleaned data is read from 'new_titanic.csv' by the 'dataload.py' script, which then loads it into an SQLite database.  

 
**Step 3: Web Application** 

The Flask framework is used by the 'app.py' script to build a web application with two routes: 

note : about page is default page

path **/**: The 'about.html' page is rendered by this. Features a button to jump to the dataset. 

  

path **/data**: Opens the 'data.html' page with data that has been retrieved from the SQLite database ('titanic.db'). 

 

## HTML Pages 

**'about.html'** 

1 . Heading and Style: 

 - The main header of the website reads "Titanic Data."  

 - There's a "Jump on dataset" button that has a purple block-like design.  

2 . The Titanic Story: 

 - The article is a brief account of the Titanic's sinking, including the tragic part when not everyone was able to be salvaged.  

 - It briefly discusses chance and how certain social groups have higher survival rates. 

3. Dataset URL: 

 - There is a heading labelled "Dataset link." Below is a URL that can be clicked to access the Titanic dataset on Kaggle. 

4. Table of Data Description: 

 - Every item of data in the dataset, including PassengerId, Survived, Pclass, and so forth, is described in a table. 

 - It makes it easier for readers to comprehend the meaning of each dataset column. 

 

 

**'data.html'**  

1. Heading and Style: 

- The main header on the page reads "Data Viewer - Results." 

- There is a "Jump to description of data" button that has a purple block-like design. It is a convenient method to return to the story page. 

  

2 . Data Table:

- A large table takes up most of the page. In our collection, each row represents a line, and each column displays a distinct piece of data. 

- It's a clever method of viewing a portion of the Titanic dataset without being overtaken by data. 

 

## How to Experience the Journey 

 
1. Prepare Your Tools:  
- Verify that Python is installed on your computer.
- run the requirements.txt
   ```python
   pip install -r requirements.txt
   ```

3. Cleaning Data:  
Launch and operate the 'dataload.py' file. This will transfer the data into the 'titanic.db' database and clean it up. 

**Web Application:** 

- To access the directory containing "app.py," open a terminal or command prompt. 

- Execute this command: 
```python
python app.py
```

- You can launch the application by going to http://127.0.0.1:5000/ or http://localhost:5000/ in your web browser. 

**Note:** 

The 'database' directory is where 'titanic.db' is supposed to be, according to the SQLite database connection. If your configuration is different, please modify the connection details in 'app.py'. 
 

For demonstration purposes, the first 25 rows from the 'titanic_table' are retrieved via the '/data' route. To change the data that is presented, edit the SQL query in 'app.py'. 

 

Feel free to explore the web application, and don't hesitate to contact us if you have any questions or run into any problems! 
