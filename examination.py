import datetime
from bs4 import BeautifulSoup

bg_color={'56-219':'a2b461','56-321':'bf9475','56-521':'bf758a','23-317':'9975bf','129-205':'64b0c4','56-322':'8fd175','56-522':'67947a'}

def get_a_day(date,room_number):

    date_wanted=datetime.datetime.strptime(date_from,"%Y-%m-%d")

    if(date_wanted.weekday()==6):
        print("There's no reservation on Sunday.")
        return 0

    today=datetime.date.today()

    url='http://phya.snu.ac.kr/php/time_table/'

    if(today-date_wanted<=datetime.timedelta(days=today.weekday()) || date_wanted-today<=datetime.timedelta(days=5-today.weekday())):
        url='http://phya.snu.ac.kr/php/time_table/list_seminar.php?room='+room_number+'&bg_color='+bg_color[room_number]
    elif(today-date_wanted>0):
        time_delta=datetime.timedelta(days=date_wanted.weekday()+2)
        next_date=(date_wanted-time_delta).strftime('%Y-%m-%d')
        url+='list_seminar_before_.php?before_date='+next_date
    else:
        time_delta=datetime.timedelta(days=date_wanted.weekday()+2)
        next_date=(date_wanted-time_delta).strftime('%Y-%m-%d')
        url+='list_seminar_next_.php?next_date='+next_date

    url+='&room='+room_number+'&bg_color'+bg_color[room_number]

    html=requests.get(url).text

    soup=BeautifulSoup(html,'html.parser')

    tr=soup.find_all('tr',{'align':'center'})
    #i번째 줄은 9시 + 30분*(i-1)을 의미

get_a_week():
    pass





def main():
    pass

if(__name__=="__main__"):
    main()
