import datetime
import requests

'''
Information needed to reserve a seminar room

1. Name of the meeting
2. Room number
3. Name of the professor
4. Date
5. starting time
5. duration of the meeting
6. Contact Information
7. Password
'''

def main():
    date="2018-07-14"
    date2=datetime.datetime.strptime(date,"%Y-%m-%d")
    time_delta=datetime.timedelta(days=date2.weekday()+2)
    next_date=(date2-time_delta).strftime('%Y-%m-%d')

    bg_color={'56-219':'a2b461','56-321':'bf9475','56-521':'bf758a','23-317':'9975bf','129-205':'64b0c4'}
    room_number="23-317"
    start_time="1000"

    url="http://phya.snu.ac.kr/php/time_table/inputform_seminar_d.php?date="+date+"&bg_color="+bg_color[room_number]+"&room="+room_number+"&p_first="+start_time+"&next_date="+next_date+"/post"

    name="asdfadsfdsf" #name of the meeting
    prof_name="" #name of the professor
    duration="120" #in minutes.

    start_time2=int(start_time)
    duration2=int(duration)
    end2=start_time2+100*(duration/60)
    if(duration==30):
        end2+=30
    else:
        print("Reservation can be done only in 30-minute unit")
        return 0
    end=str(end2)
    contact="010-1234-5678" #your contact information
    password="alpine" #password needed for cancellation

    payloads={'subject':name,'host':prof_name,'email':contact,'password':password,"p_end":end}
    r=requests.post(url,data=payloads)

if(__name__=="__main__"):
    main()
