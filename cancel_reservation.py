import sys
import datetime
import requests
from bs4 import BeautifulSoup

def main():

    if(sys.version_info[0]<3):
        print("Please use python3 instead.")
        return 0

    parser=optparse.OptionParser()
    parser.add_option("-d","--date",dest="date",help="Date to reserve. ex)2018-07-09")
    parser.add_option('-s',"--start",dest="start_time",help="Seminar starting time in 4 digit number. ex)1000(10 a.m.), 1400(2 p.m.)")
    parser.add_option('-r',"--room",dest="room_number",help="Seminar Room Number. ex)23-312,56-321")
    parser.add_option('-w',"--password",dest="password",help="Password needed for cancellation")


    options,args=parser.parse_args()

    date=options.date
    start_time=options.start_time
    room_nubmer=options.room_number
    password=options.password

    date2=datetime.datetime.strptime(date,"%Y-%m-%d")
    time_delta=datetime.timedelta(days=date2.weekday()+2)
    next_date=(date2-time_delta).strftime('%Y-%m-%d')

    bg_color={'56-219':'a2b461','56-321':'bf9475','56-521':'bf758a','23-317':'9975bf','129-205':'64b0c4','56-322':'8fd175','56-522':'67947a'}
    url='http://phya.snu.ac.kr/php/time_table/list_seminar.php?room='+room_number+'&bg_color='+bg_color[room_number]
    html=requests.get(url).text
    soup=BeautifulSoup(html,'html.parser')

    tr=soup.find_all('tr',{'align':'center'})

    index=int((int(start_time)-900)/50+1)
    if(int(start_time)%100==30):
        index+=1
    row=tr[index]

    [date2.weekday()]
    payloads={'form':password}
    post_action='http://phya.snu.ac.kr/php/time_table/action=delete_seminar.php?no=42857&bg_color=9975bf&date=2018-07-14&next_date='+next_date
    r=requests.post(post_action,data=payloads)
    print(r.text)


if(__name__=="__main__"):
    main()
