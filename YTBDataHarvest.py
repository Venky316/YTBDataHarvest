#Import modules
import streamlit as st
import psycopg2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Set page title, heading and caption
st.set_page_config(
    page_title='Venky First App',layout='wide',initial_sidebar_state='auto',
)
gettitle = st.title(':red[Welcome to Youtube Data Harvesting]')
getcaption = st.caption(body='This app displays the details of various Youtube Channels such as Channel Details, Playlist Details, Video Details & Comment Sections.:thumbsup:')

#Select the channel genre
getgenre = st.radio(label='Select your Genre',options=['Foodie','Receipes','Content Reviewing','Devotional','Sports','All'],index = 2)

#Query SQL DB to retrieve the channels, playlists & videos table
conn = psycopg2.connect(host='localhost',database='postgres',user='postgres',password='Venky@24121993')
cur = conn.cursor()
cur.execute('select * from channtable')
row = cur.fetchall()
getchannpd = pd.DataFrame(row,columns=['Channel_ID','Channel_Name','Channel_Description','Channel_Views','Channel_Subscribers','Channel_Videos','Channel_Thumbnail','Channel_Genre'])
cur.execute('select * from channtable left join playlisttable on channtable.channel_id=playlisttable.channel_id')
row = cur.fetchall()
getplaylistpd = pd.DataFrame(row,columns=['Channel_ID','Channel_Name','Channel_Description','Channel_Views','Channel_Subscribers','Channel_Videos','Channel_Thumbnail','Channel_Genre','chann_id','Playlist_ID','Playlist_Name','Playlist_Videos'])
getdf = pd.unique(getplaylistpd['Channel_Name']).tolist()
cur.execute('select * from channtable join playlisttable on channtable.channel_id=playlisttable.channel_id join videotable on playlisttable.playlist_id=videotable.playlist_id')
row = cur.fetchall()
getvideospd = pd.DataFrame(row,columns=['Channel_ID','Channel_Name','Channel_Description','Channel_Views','Channel_Subscribers','Channel_Videos','Channel_Thumbnail','Channel_Genre','chann_id','Playlist_ID','Playlist_Name','Playlist_Videos','play_id','Video_ID','Video_Name','Video_Description','Published_Date','Published_Time','Duration','Caption','Views','Likes','Comments','Favorites'])

#Displays data for all the Channels when genre other than "All" is selected
if getgenre != 'All':
    if getgenre == 'Foodie':
        getchannloc = getchannpd.loc[getchannpd['Channel_Genre'].str.contains(getgenre)]
        getlist = getchannloc['Channel_Name'].values.tolist()
        getchannbox = st.selectbox(label='Channels',options=[getlist[0],getlist[1]],index=None)
    elif getgenre == 'Receipes':
        getchannloc = getchannpd.loc[getchannpd['Channel_Genre'].str.contains(getgenre)]
        getlist = getchannloc['Channel_Name'].values.tolist()       
        getchannbox = st.selectbox(label='Channels',options=[getlist[0],getlist[1]],index=None) 
    elif getgenre == 'Content Reviewing':
        getchannloc = getchannpd.loc[getchannpd['Channel_Genre'].str.contains(getgenre)]
        getlist = getchannloc['Channel_Name'].values.tolist()        
        getchannbox = st.selectbox(label='Channels',options=[getlist[0],getlist[1]],index=None)    
    elif getgenre == 'Devotional':
        getchannloc = getchannpd.loc[getchannpd['Channel_Genre'].str.contains(getgenre)]
        getlist = getchannloc['Channel_Name'].values.tolist()        
        getchannbox = st.selectbox(label='Channels',options=[getlist[0],getlist[1]],index=None)
    elif getgenre == 'Sports':
        getchannloc = getchannpd.loc[getchannpd['Channel_Genre'].str.contains(getgenre)]
        getlist = getchannloc['Channel_Name'].values.tolist()         
        getchannbox = st.selectbox(label='Channels',options=[getlist[0],getlist[1]],index=None)

    #Display channel name, description and no. of views, subscribers, playlists and videos along with thumbnail image
    if getchannbox:
        getchannvwcount = getchannpd.loc[getchannpd['Channel_Name'].str.contains(getchannbox),'Channel_Views'].values[0]
        getchannsubcount = getchannpd.loc[getchannpd['Channel_Name'].str.contains(getchannbox),'Channel_Subscribers'].values[0]
        getchannvidcount = getchannpd.loc[getchannpd['Channel_Name'].str.contains(getchannbox),'Channel_Videos'].values[0]
        getchanndesc = getchannpd.loc[getchannpd['Channel_Name'].str.contains(getchannbox),'Channel_Description'].values[0]
        getchannthumbnail = getchannpd.loc[getchannpd['Channel_Name'].str.contains(getchannbox),'Channel_Thumbnail'].values[0]
        st.write('Description')
        st.write(getchanndesc)
        st.write('#Channel Views : ',getchannvwcount)
        st.write('#Subscribers : ',getchannsubcount)
        st.write('#Videos : ',getchannvidcount)
        cur.execute('select * from channtable left join playlisttable on channtable.channel_id=playlisttable.channel_id')
        gettab = cur.fetchall()
        getpd = pd.DataFrame(gettab)
        getplid = getpd.loc[getpd[1].str.contains(getchannbox)].shape[0]
        st.write('#Playlists : ',getplid)
        import urllib.request
        from PIL import Image
        urllib.request.urlretrieve(getchannthumbnail,'getimage.png')
        img = Image.open('getimage.png')
        st.image(img)

#Displays data for all the Channels when genre "All" is selected
else:
    #Lists out the channel details
    st.title(':blue[Channels List]')
    #st.dataframe(getchannpd,hide_index=True)
    st.data_editor(getchannpd,column_config={'Channel_Thumbnail':st.column_config.ImageColumn()},hide_index=True,column_order=('Channel_Thumbnail','Channel_Name','Channel_Genre','Channel_Description'))

    #Statistics of the channels, playlists, videos and comments
    st.title(':blue[Channels Stats]')
    getmaxvchann = getchannpd['Channel_Views'].idxmax()
    getmaxvchannloc = getchannpd.loc[getmaxvchann]
    getmaxsubchann = getchannpd['Channel_Subscribers'].idxmax()
    getmaxsubchannloc = getchannpd.loc[getmaxsubchann]
    getmaxvdchann = getchannpd['Channel_Videos'].idxmax()
    getmaxvdchannloc = getchannpd.loc[getmaxvdchann]
    getmaxlikchann = getvideospd['Likes'].idxmax()
    getmaxlikchannloc = getvideospd.loc[getmaxlikchann]
    getmaxcommchann = getvideospd['Comments'].idxmax()
    getmaxcommchannloc = getvideospd.loc[getmaxcommchann]
    #Loop to get playlists count based on channel name
    getpd = getplaylistpd['Channel_Name'].value_counts()
    getnewpd = pd.DataFrame({'Channel_Name':getpd.index,'Playlists':getpd.values})
    getmax = getnewpd['Playlists'].max().item()
    getarr = np.where(getnewpd['Playlists'] == getmax)
    getlist = list()
    for i in getarr[0]:
        getlist.append(getnewpd.loc[i].Channel_Name)
    getstr = ' '.join(str(i) for i in getlist)

    st.write(':green[Top Viewed Channel] :sunglasses::sunglasses: :', getmaxvchannloc.Channel_Name, '(', getmaxvchannloc.Channel_Views, 'viewers )')
    st.write(':green[Top Subscribed Channel] :pray::pray: :', getmaxsubchannloc.Channel_Name, '(', getmaxsubchannloc.Channel_Subscribers, 'subscribers )')
    st.write(':green[Channel with most playlists] :open_hands::open_hands: :', getstr, '(', getmax, 'Playlists )')
    st.write(':green[Channel with most videos] :crossed_fingers::crossed_fingers: :', getmaxvdchannloc.Channel_Name, '(', getmaxvdchannloc.Channel_Videos, 'videos )') 
    st.write(':green[Channel with most likes] :thumbsup::thumbsup: :', getmaxlikchannloc.Channel_Name, '(', int(getmaxlikchannloc.Likes), 'likes )')
    st.write(':green[Channel with most comments] :speech_balloon::speech_balloon: :', getmaxcommchannloc.Channel_Name, '(', int(getmaxcommchannloc.Comments), 'comments )')  

    #Bar chart display of the Views, Subscribers, Playlists and Videos Statistics
    st.write('\n')
    st.write('\n')
    st.markdown("<h1 style='text-align: center; color: green; '>Viewers Stats</h1>", unsafe_allow_html=True)       
    st.bar_chart(data=getchannpd,x='Channel_Name',y='Channel_Views')
    st.write('\n')
    st.write('\n')
    st.markdown("<h1 style='text-align: center; color: green; '>Subscribers Stats</h1>", unsafe_allow_html=True)       
    st.bar_chart(data=getchannpd,x='Channel_Name',y='Channel_Subscribers')
    st.write('\n')
    st.write('\n')
    st.markdown("<h1 style='text-align: center; color: green; '>Playlists Stats</h1>", unsafe_allow_html=True)       
    st.bar_chart(data=getnewpd,x='Channel_Name',y='Playlists')    
    st.write('\n')
    st.write('\n')
    st.markdown("<h1 style='text-align: center; color: green; '>Videos Stats</h1>", unsafe_allow_html=True)       
    st.bar_chart(data=getchannpd,x='Channel_Name',y='Channel_Videos')

    #Questions
    st.title(':blue[Questionnaire]')
        #1st question
    st.write('1. What are the names of all the videos and their corresponding channels?')
    getonebut = st.button('Ans', key='but1')
    if(getonebut):
        getonebutdf = pd.DataFrame([getvideospd['Channel_Name'],getvideospd['Video_Name']]).T
        st.dataframe(getonebutdf)

        #2nd question
    st.write('2. Which channels have the most number of videos, and how many videos do they have?')
    gettwobut = st.button('Ans', key='but2')
    if(gettwobut):
        st.write(getmaxvdchannloc.Channel_Name, '(', getmaxvdchannloc.Channel_Videos, 'videos )')
    
        #3rd question   
    st.write('3. What are the top 10 most viewed videos and their respective channels?')
    getthreebut = st.button('Ans', key='but3')
    if(getthreebut):
        getthreebutdf = pd.DataFrame([getvideospd['Channel_Name'],getvideospd['Video_Name'],getvideospd['Views']]).T
        newpd = getthreebutdf.sort_values(by=['Views'],ascending=False,ignore_index=True)
        st.write(newpd.head(10))
    
        #4th question    
    st.write('4. How many comments were made on each video, and what are their corresponding video names?')
    getfourbut = st.button('Ans', key='but4')
    if(getfourbut):
        getfourbutdf = pd.DataFrame([getvideospd['Video_Name'],getvideospd['Comments']]).T
        st.dataframe(getfourbutdf)
    
        #5th question    
    st.write('5. Which videos have the highest number of likes, and what are their corresponding channel names?')
    getfivebut = st.button('Ans', key = 'but5')
    if(getfivebut):
        getfivbutdf = pd.DataFrame([getvideospd['Channel_Name'],getvideospd['Video_Name'],getvideospd['Likes']]).T
        getchannlist = getchannpd['Channel_Name'].values.tolist()
        getlist = list()
        for i in getchannlist:
            getnewdf = getvideospd[getvideospd['Channel_Name'].str.contains(i)]
            getfiltdf = getnewdf.replace(np.nan,0)
            getmax = getfiltdf['Likes'].idxmax()
            getlist.append([getfiltdf.loc[getmax].Channel_Name,getfiltdf.loc[getmax].Video_Name,getfiltdf.loc[getmax].Likes])
        getdf = pd.DataFrame(getlist,columns=['Channel_Name','Video_Name','Likes'])
        st.dataframe(getdf)

        #6th question
    st.write('6. What is the total number of likes for each video, and what are their corresponding video names?')
    getsixbut = st.button('Ans', key = 'but6')
    if(getsixbut):
        getsixbutdf = pd.DataFrame([getvideospd['Video_Name'],getvideospd['Likes']]).T
        st.dataframe(getsixbutdf)
    
        #7th question    
    st.write('7. What is the total number of views for each channel, and what are their corresponding channel names?')
    getsevenbut = st.button('Ans', key = 'but7')
    if(getsevenbut):
        getsevenbutdf = pd.DataFrame([getchannpd['Channel_Name'],getchannpd['Channel_Views']]).T
        st.dataframe(getsevenbutdf)
    
        #8th question    
    st.write('8. What are the names of all the channels that have published videos in the year 2022?')
    geteightbut = st.button('Ans', key = 'but8')
    if(geteightbut):
        getrecentchann = getvideospd.loc[getvideospd['Published_Date'].str.contains('2022')]
        getchann = getrecentchann['Channel_Name'].unique()
        getchanndf = pd.DataFrame(getchann,columns=['Channel Name'])
        st.dataframe(getchanndf)
    
        #9th question    
    st.write('9. What is the average duration of all videos in each channel, and what are their corresponding channel names?')
    getninebut = st.button('Ans', key='but9')

        #10th question
    st.write('10. Which videos have the highest number of comments, and what are their corresponding channel names?')
    gettenbut = st.button('Ans', key='but10')
    if(gettenbut):
        gettenbutdf = pd.DataFrame([getvideospd['Channel_Name'],getvideospd['Video_Name'],getvideospd['Comments']]).T
        getchannlist = getchannpd['Channel_Name'].values.tolist()
        getlist = list()
        for i in getchannlist:
            getnewdf = getvideospd[getvideospd['Channel_Name'].str.contains(i)]
            getfiltdf = getnewdf.replace(np.nan,0)
            getmax = getfiltdf['Comments'].idxmax()
            getlist.append([getfiltdf.loc[getmax].Channel_Name,getfiltdf.loc[getmax].Video_Name,getfiltdf.loc[getmax].Comments])
        getdf = pd.DataFrame(getlist,columns=['Channel_Name','Video_Name','Comments'])
        st.dataframe(getdf)

    #Feedback about the favourite channel       
    st.title(':blue[Rate your favourite Channel]')
    ratchann = st.multiselect(label ='Select Channels',options = getchannpd['Channel_Name'])
    getresponse = st.radio(label='Rating',options= ['Poor','Average','Good','Very Good','Excellent'],index=None)
    if(ratchann and getresponse):
        st.subheader('Thanks for submitting your response...!!')