import datetime
def xms():
    days = ['월','화','수','목','금','토','일']
    day1 = datetime.datetime.now().date()
    day2 = datetime.date(2025,12,25)
    diff = day2 - day1
    return(f"오늘은 {day1} 입니다. 🎄크리스마스 까지 남은 기간은 {diff.days}일 이며, 🎅크리스마스는 {days[day2.weekday()]}요일 입니다!!")


if __name__=="__main__" :
    print(xms())