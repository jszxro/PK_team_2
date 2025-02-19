# 생일 입력받고 며칠 지났는지 계산하기, 무슨 요일인지
import datetime
def Birthday():
    days = ['월','화','수','목','금','토','일']
    birth = input("생일을 입력해주세요: (예:2024,11,7)")
    
    birth1 = birth.split(",")
    
    year = int(birth1[0])
    month = int(birth1[1])
    day = int(birth1[2])
    
    birth2 = datetime.date(year,month,day)
    
    diff = birth2 - datetime.datetime.now().date()
    
    return f"생일은 {abs(diff.days)}일 지났으며, 이날은 {days[birth2.weekday()]}요일 입니다."