import sys
import datetime
import requests
import optparse

assert sys.version_info[0]>=3

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

    parser=optparse.OptionParser()
    parser.add_option("-d","--date",dest="date",help="Date to reserve. ex)2018-07-09")
    parser.add_option("-n","--name",dest="name",help="name of the seminar")
    parser.add_option('-r',"--room",dest="room_number",help="Seminar Room Number. ex)23-312,56-321")
    parser.add_option('-s',"--start",dest="start_time",help="Seminar starting time in 4 digit number. ex)1000(10 a.m.), 1400(2 p.m.)")
    parser.add_option('-e',"--end",dest="end_time",help="Seminar ending time in 4 digit number. ex)1000(10 a.m.), 1400(2 p.m.)")
    parser.add_option('-p',"--prof",dest="professor",help="Name of the Professor")
    parser.add_option('-c',"--contact",dest="contact",help="Contact Information")
    parser.add_option('--pw',"--password",dest="password",default="alpine",help="Password needed for cancellation")

    options,args=parser.parse_args()

    date=options.date
    name=options.name
    room_number=options.room_number
    start_time=options.start_time
    end_time=options.end_time
    prof_name=options.professor
    contact=options.contact
    password=options.password

    room_list=['56-219','56-321','56-521','23-317','129-205','56-322','56-522']
    if(room_number not in room_list):
        print("There is no room numbered "+room_number)
        return 0

    if(int(end_time)<int(start_time)):
        print("you can't end something before you start.")
        return 0
    if(int(end_time)%30!=0||int(start_time)%30!=0):
        print("the time designation shall be done in 30-minute-units.")
        return 0

    date2=datetime.datetime.strptime(date,"%Y-%m-%d")
    time_delta=datetime.timedelta(days=date2.weekday()+2)
    next_date=(date2-time_delta).strftime('%Y-%m-%d')

    bg_color={'56-219':'a2b461','56-321':'bf9475','56-521':'bf758a','23-317':'9975bf','129-205':'64b0c4','56-322':'8fd175','56-522':'67947a'}
    url="http://phya.snu.ac.kr/php/time_table/input_seminar_d.php?date="+date+"&bg_color="+bg_color[room_number]+"&room="+room_number+"&p_first="+start_time+"&next_date="+next_date+"/post"
    payloads={'subject':name,'host':prof_name,'email':contact,'password':password,"p_end":end_time}
    r=requests.post(url,data=payloads)
    print(r.text)

if(__name__=="__main__"):
    main()
