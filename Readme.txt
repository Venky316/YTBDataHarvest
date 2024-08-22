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
 1)		Python 				3.12.0				64				Windows 10
 2)		Microsoft VS Code		 1.84.1				64				Windows 10
 3)		MongoDB Server			  7.0				64				Windows 10
 4)		MongoDB Data Tools		 100.9.4			64				Windows 10
 5)		Mongo Shell			  2.0.2				64				Windows 10
 6)		PostgreSQL			16.1.1				64				Windows 10
 7)		PGAdmin				7.8				64				Windows 10
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
-- Project Work Flow
-- Major Steps : 1) Data Collection (Youtube)
--				 2) Data Storage in NSQL DB (MongoDB)
--				 3) Data Transfer to SQL DB (PGAdmin)
--				 4) Data Processing (Python,Streamlit)
--				 5) Data Display (Streamlit)
--
------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
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
|
|--- 2) Data Storage in NSQL DB (MongoDB)
|		|
|		|
|		|--- 1) Establish connection to MongoDB using pymongo
|		|
|		|
|		|--- 2) Create Databases named ChannelDB, PlaylistDB, VideoDB, CommentsDB
|		|
|		|
|		|--- 3) Create Collections named Channel_List, Playlist_List, Video_List, Comments_List respectively
|		|
|		|
|		|--- 4) Insert all the records from the respective Lists
|		|
|		|
|
|--- 3) Data Transfer to SQL DB (PGAdmin)  
|		|
|		|
|		|--- 1) Establish connection to PGAdmin database using psycopg2
|		|
|		|
|		|--- 2) Create Tables named channtable, playlisttable, videotable, commenttable
|		|
|		|
|		|--- 3) Insert all the values from the respective Lists
|		|
|		|
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
----------------------------------------------------------------------------------------------------------------------------------------------------------------- 