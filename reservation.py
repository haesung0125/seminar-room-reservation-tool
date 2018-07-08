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

    url="http://phya.snu.ac.kr/php/time_table/inputform_seminar_d.php?date="+date+"&bg_color="+bg_color[room_number]+"&room="+room_number+"&p_first="+start_time+"&next_date="+next_date

    name="asdfadsfdsf" #name of the meeting
    prof_name="" #name of the professor

    duration="120" #in minutes.
    Contact="010-1234-5678" #your contact information
    Password="alpine" #password needed for cancellation

if(__name__=="__main__"):
    main()
