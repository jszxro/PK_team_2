# 2) 어린이날

import datetime

def ChildrensDay(today):
    c_day = datetime.date(2025, 5, 5)
    k_day = c_day - today
    days = ['월', '화', '수', '목', '금', '토', '일']
    w_day = days[c_day.weekday()]
    return f'오늘은 {today.year}년 {today.month}월 {today.day}일입니다. 올해 어린이날까지 {k_day.days}일 남았습니다 이날은 {w_day}요일입니다.'

if __name__=="__main__" :
    today = datetime.datetime.now().date()
    print(ChildrensDay(today))