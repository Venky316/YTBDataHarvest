-----------------------------------------------------------------------------------------------------------------------------------------------------------------
--
-- This file contains the workflow diagram, prerequisite softwares, packages used for the project
-- This file is subjected to copyrights.
--
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
--
-- List of Softwares
--
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
--
S.No	Software				Version				Bit				OS type
--
 1)		Python 					 3.12.0				64				Windows 10
 2)		Microsoft VS Code		 1.84.1				64				Windows 10
 3)		MongoDB Server			  7.0				64				Windows 10
 4)		MongoDB Data Tools		 100.9.4			64				Windows 10
 5)		Mongo Shell				 2.0.2				64				Windows 10
 6)		PostgreSQL				 16.1.1				64				Windows 10
 7)		PGAdmin					  7.8				64				Windows 10
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
--
-- List of VS Code Extensions
--
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
--
S.No	Addin					Version
--
 1)		Jupyter				v2023.11.1003402403	
 2)		Python				   v2023.22.1
 3)		Pylance				   v2023.12.1
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
--
-- List of Python Packages
--
----------------------------------------------------------------------------------------------------------------------------------------------------------------- 
--
S.No	Package
--
 1)		googleapiclient
 2)		pymongo
 3)		psycopg2
 4)		pandas
 5)		matplotlib
 6)		numpy
 7)		urllib
 8)		streamlit
 -----------------------------------------------------------------------------------------------------------------------------------------------------------------
--
-- Add the below paths to the Environmental Variable 'PATH' (both User and System)
-- Username VENKATESH is replaceable based on the respective machines on which the softwares are installed
-- The bin folder paths are replaceable based on the installation folder which is used during softwares installation 
--
----------------------------------------------------------------------------------------------------------------------------------------------------------------- 
--
 1) 	C:\Users\VENKATESH\AppData\Local\Programs\Python\Python312\
 2)		C:\Users\VENKATESH\AppData\Local\Programs\Python\Python312\Scripts\
 3)		C:\Users\VENKATESH\AppData\Local\Programs\Microsoft VS Code\bin\
 4)		C:\Program Files\MongoDB\MongoDB_Tools\bin\
 5)		C:\Users\VENKATESH\AppData\Local\Programs\mongosh\
 6)		C:\Program Files\PostgreSQL\16\bin\
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
--
-- Project Work Flow
-- Major Steps : 1) Data Collection (Youtube)
--				 2) Data Storage in NSQL DB (MongoDB)
--				 3) Data Transfer to SQL DB (PGAdmin)
--				 4) Data Processing (Python,Streamlit)
--				 5)	Data Display (Streamlit)
--
----------------------------------------------------------------------------------------------------------------------------------------------------------------- 
|
|
|--- 1) Data Collection (Youtube)
|		|
|		|
|		|--- 1) Create Google API project
|		|			|-- 1) Goto console.cloud.google.com
|		|			|-- 2) Select 'APIs & Services'
|		|			|-- 3) Click on 'NEW PROJECT' and provide a project name to create one
|		|			|-- 4) Click on 'ENABLE APIS AND SERVICES' and search for 'youtube data api v3'
|		|			|-- 5) An youtube icon will appear. Click on 'ENABLE' to link the project to Youtube API
|		|			|-- 6) From 'APIs & Services', select 'Credentials'.
|		|			|-- 7) In the new window, click on 'Credentials' and select 'CREATE CREDENTIALS'
|		|			|-- 8) Select 'API Key's'. A new API Key will be created.
|		|			|-- 9) Once created, click on the API Key and select 'Restrict Key'
|		|			|-- 10) Select 'Youtube Data API v3' from the filter and click save. Now this API key is ready to use
|		|
|		|	
|		|--- 2) Import the Google API Client module in python and extract the details of channels, playlists, videos and comments
|		|
|		|   
|		|--- 3) Save the extracted the details separately in json format
|		|
|		|
|
|
|--- 2) Data Storage in NSQL DB (MongoDB)
|		|
|		|
|		|--- 1) Import the pymongo module and connect to the MongoDB compass server as a localhost
|		|
|		|
|		|--- 2) Create Databases named ChannelDB, PlaylistDB, VideoDB, CommentsDB
|		|
|		|
|		|--- 3) Create Collections named Channel_List, Playlist_List, Video_List, Comments_List respectively
|		|
|		|
|		|--- 4) Import the json files and all the records into the collections respectively
|		|
|		|
|
|
|--- 3) Data Transfer to SQL DB (PGAdmin)  
|		|
|		|
|		|--- 1) Open Windows command line and change the current directory to the location where Mongo DB Data Tools bin folder is located
|       |       (In this case: C:\Program Files\MongoDB\MongoDB_Tools\bin\)
|       |
|       |
|       |--- 2) Run the mongoexport command to output the database collections from MongoDB to a csv file
|		|
|		|
|		|--- 3) Open PGAdmin and create the tables for Channels, Playlists, Videos and Comments
|		|
|		|
|		|--- 4) Import the csv files into the corresponding tables via SQL commands
|		|
|		|
|
|
|--- 4) Data Processing (Python,Streamlit)
|		|
|		|
|		|--- 1) Import the psycopg2 and streamlit module
|		|
|		|
|		|--- 2) Develop the python code for streamlit gui to display the details of channels, playlists, videos and comments
|		|
|		|
|
|
|--- 4) Data Display (Streamlit)
|		|
|		|
|		|--- 1) Save the python code as a .py file extension
|		|
|		|
|		|--- 2) In the terminal, run the streamlit application and call the above .py file
|		|
|		|
|		|--- 3) This will now display all the backend python code in the form of GUI using streamlit
|		|
|		|
|
|
----------------------------------------------------------------------------------------------------------------------------------------------------------------- 