#3)
import datetime

def parents():
    day1 = datetime.date(2025, 2, 18)
    day2 = datetime.date(2025, 5, 8)
    diff = day2 - day1
    print("어버이날까지 남은 기간:", diff.days, "일")
    days = ['월', '화', '수', '목', '금', '토', '일']
    print(f"어버이날은 {days[day2.weekday()]}요일 입니다")
parents()