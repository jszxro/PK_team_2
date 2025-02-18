import datetime as da
def chu():
    days= ["월","화","수","목","금","토","일"]
    com = da.date(2025,7,25)
    ch = da.date(2025,10,6)
    week=ch.weekday() # 0, 월요일
    diff = ch-com # 73일
    return(f'수료후 추석까지 {diff.days}일 남았고, 추석은 {days[week]}요일 입니다.')

if __name__=="__main__" :
    print(chu())