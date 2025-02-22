import os
import datetime
import csv
import calendar

from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, tsv, timeline, is_platform_windows, media_to_html, kmlgen

def monthletter(month):
    monthdict = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
    return monthdict[month]

def get_snapchatConv(files_found, report_folder, seeker, wrap_text):

    for file_found in files_found:
        file_found = str(file_found)
        
        filename = os.path.basename(file_found)
        one = (os.path.split(file_found))
        username = (os.path.basename(one[0]).split('-')[0])
        
        if filename.startswith('geo_locations.csv'):
            data_list_geo =[]
            with open(file_found, 'r') as f:
                for i in range(4):
                    next(f)
                for line in f:
                    delimited = csv.reader(f, delimiter=',')
                    for item in delimited:
                        latitude = item[0].split(' ')
                        latitudemeters = latitude[2]
                        latitude = latitude[0]
                        
                        longitude = item[1].split(' ')
                        longitudemeters = longitude[2]
                        longitude = longitude[0]
                        
                        fecha = item[2]
                        timestamp = fecha.split(' ')
                        year = timestamp[5]
                        day = timestamp[2]
                        time = timestamp[3]
                        month = monthletter(timestamp[1])
                        timestampfinal = (f'{year}-{month}-{day} {time}')
                        
                        data_list_geo.append((timestampfinal, latitude, latitudemeters, longitude, longitudemeters))
    
            if data_list_geo:
                report = ArtifactHtmlReport(f'Snapchat - Geolocations')
                report.start_artifact_report(report_folder, f'Snapchat - Geolocations - {username}')
                report.add_script()
                data_headers = ('Timestamp','Latitude','Latitude +- Meters','Longitude','Longitude +- Meters')
                report.write_artifact_data_table(data_headers, data_list_geo, file_found, html_no_escape=['Media'])
                report.end_artifact_report()
                
                tsvname = f'Snapchat - Geolocations  - {username}'
                tsv(report_folder, data_headers, data_list_geo, tsvname)
                
                tlactivity = f'Snapchat - Geolocations  - {username}'
                timeline(report_folder, tlactivity, data_list_geo, data_headers)
                
                kmlactivity = f'Snapchat - Geolocations  - {username}'
                kmlgen(report_folder, kmlactivity, data_list_geo, data_headers)
            else:
                logfunc(f'No Snapchat - Geolocations  - {username}')
    
    
    
    for file_found in files_found:
        file_found = str(file_found)
    
        filename = os.path.basename(file_found)
        one = (os.path.split(file_found))
        username = (os.path.basename(one[0]).split('-')[0])
                    
        if filename.startswith('conversations.csv'):
            data_list_conversations =[]
            with open(file_found, 'r', errors='backslashreplace') as f:
                for i in range(20):
                    next(f)
                for line in f:
                    delimited = csv.reader(f, delimiter=',')
                    for item in delimited:
                        #print(item)
                        content_type = item[0]
                        message_type = item[1]
                        conversation_id = item[2]
                        message_id = item[3]
                        reply_to_message_id = item[4]
                        conversation_title = item[5]
                        sender_username = item[6]
                        sender_user_id = item[7]
                        recipient_username = item[8]
                        recipient_user_id = item[9]
                        text = item[10]
                        media = item[11]
                        if media == '':
                            agregator = ' '
                        else:
                            if ';' in media:
                                media = media.split(';')
                                agregator = '<table>'
                                counter = 0
                                for x in media:
                                    if counter == 0:
                                        agregator = agregator + ('<tr>')
                                    thumb = media_to_html(x, files_found, report_folder)        
                                
                                    counter = counter + 1
                                    agregator = agregator + f'<td>{thumb}</td>'
                                    #hacer uno que no tenga html
                                    if counter == 2:
                                        counter = 0
                                        agregator = agregator + ('</tr>')
                                if counter == 1:
                                    agregator = agregator + ('</tr>')
                                agregator = agregator + ('</table><br>')
                            else:
                                agregator = media_to_html(media, files_found, report_folder)
                        is_saved = item[12]
                        is_one_on_one = item[13] 
                        timestamp = item[14]
                        timestamp = timestamp.split(' ')
                        year = timestamp[5]
                        day = timestamp[2]
                        time = timestamp[3]
                        month = monthletter(timestamp[1])
                        timestampfinal = (f'{year}-{month}-{day} {time}')
                        data_list_conversations.append((timestampfinal,sender_username,recipient_username,text,is_saved,content_type,message_type,agregator,is_one_on_one,conversation_title,message_id,reply_to_message_id,sender_user_id,recipient_user_id))
                        
        
            if data_list_conversations:
                report = ArtifactHtmlReport(f'Snapchat - Conversations')
                report.start_artifact_report(report_folder, f'Snapchat - Conversations - {username}')
                report.add_script()
                data_headers = ('Timestamp','Sender Username','Recipient Username','Text','Is Saved','Content Type', 'Message Type','Media','Is One on One','Conversation Title','Message ID','Reply to Message ID','Sender User ID','Recipient User ID')
                report.write_artifact_data_table(data_headers, data_list_conversations, file_found, html_no_escape=['Media'])
                report.end_artifact_report()
                
                tsvname = f'Snapchat - Conversations - {username}'
                tsv(report_folder, data_headers, data_list_conversations, tsvname)
                
                tlactivity = f'Snapchat - Conversations - {username}'
                timeline(report_folder, tlactivity, data_list_conversations, data_headers)
            else:
                logfunc(f'No Snapchat - Conversations - {username}')
                
    for file_found in files_found:
        file_found = str(file_found)
        
        filename = os.path.basename(file_found)
        one = (os.path.split(file_found))
        username = (os.path.basename(one[0]).split('-')[0])
        
        if filename.startswith('chats.csv'):
            data_list_chats =[]
            with open(file_found, 'r') as f:
                #for i in range(1):
                #    next(f)
                for line in f:
                    delimited = csv.reader(f, delimiter=',')
                    for item in delimited:
                        #print(item)
                        #chatsid,from,to,body,href,media_id,saved,timestamp
                        chatsid = item[0]
                        fromc = item[1]
                        to = item[2]
                        body = item[3]
                        href = item[4]
                        media = item[5]
                        saved = item[6]
                        timestamp = item[7]
                        if media == '':
                            agregator = ' '
                        else:
                            if ';' in media:
                                media = media.split(';')
                                agregator = '<table>'
                                counter = 0
                                for x in media:
                                    if counter == 0:
                                        agregator = agregator + ('<tr>')
                                    thumb = media_to_html(x, files_found, report_folder)        
                                    
                                    counter = counter + 1
                                    agregator = agregator + f'<td>{thumb}</td>'
                                    #hacer uno que no tenga html
                                    if counter == 2:
                                        counter = 0
                                        agregator = agregator + ('</tr>')
                                if counter == 1:
                                    agregator = agregator + ('</tr>')
                                agregator = agregator + ('</table><br>')
                            else:
                                agregator = media_to_html(media, files_found, report_folder)
            
                        timestamp = timestamp.split(' ')
                        logfunc(str(timestamp))
                        year = timestamp[5]
                        day = timestamp[2]
                        time = timestamp[3]
                        month = monthletter(timestamp[1])
                        timestampfinal = (f'{year}-{month}-{day} {time}')
                        data_list_chats.append((timestampfinal,fromc,to,body,href,saved,agregator,))
                        
                        
            if data_list_chats:
                report = ArtifactHtmlReport(f'Snapchat - Chats')
                report.start_artifact_report(report_folder, f'Snapchat - Chats - {username}')
                report.add_script()
                data_headers = ('Timestamp','Sender Username','Recipient Username','Body','HREF','Is Saved','Media')
                report.write_artifact_data_table(data_headers, data_list_chats, file_found, html_no_escape=['Media'])
                report.end_artifact_report()
                
                tsvname = f'Snapchat - Chats - {username}'
                tsv(report_folder, data_headers, data_list_chats, tsvname)
                
                tlactivity = f'Snapchat - Chats - {username}'
                timeline(report_folder, tlactivity, data_list_chats, data_headers)
            else:
                logfunc(f'No Snapchat - Chats - {username}')
            
    userlist = []
    start_terms = ('memories','custom_sticker')
    for file_found in files_found:
        file_found = str(file_found)
    
        filename = os.path.basename(file_found)
        one = (os.path.split(file_found))
        username = (os.path.basename(one[0]).split('-')[0])
        if username not in userlist:
            userlist.append(username)
    

    for name in userlist:
        data_list_media = []
        for file_found in files_found:
            file_found = str(file_found)
            filename = os.path.basename(file_found)
            
            if filename.startswith(start_terms):
                metadata = filename.split('~')
                if name == metadata[3]:
                    typeoffile = metadata[0]
                    timestamp = metadata[2]
                    timestamp = timestamp.split('-')
                    org_string = timestamp[5]
                    mod_string = org_string[:-3]
                    timestamp = f'{timestamp[0]}-{timestamp[1]}-{timestamp[2]} {timestamp[3]}:{timestamp[4]}:{mod_string}'
                    usernamefile = metadata[3]
                    media = media_to_html(file_found, files_found, report_folder)
                    file_found_dir = os.path.dirname(file_found)
                    data_list_media.append((timestamp,media,filename,usernamefile,typeoffile,))
                    
        if data_list_media:
            report = ArtifactHtmlReport(f'Snapchat - Memories')
            report.start_artifact_report(report_folder, f'Snapchat - Memories - {name}')
            report.add_script()
            data_headers = ('Timestamp','Media','Filename','User','File Type')
            report.write_artifact_data_table(data_headers, data_list_media, file_found_dir, html_no_escape=['Media'])
            report.end_artifact_report()
            
            tsvname = f'Snapchat - Memories - {name}'
            tsv(report_folder, data_headers, data_list_media, tsvname)
            
            tlactivity = f'Snapchat - Memories- {name}'
            timeline(report_folder, tlactivity, data_list_media, data_headers)
        else:
            logfunc(f'No Snapchat - Memories - {name}')