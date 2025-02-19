# 06-1 구구단
def gugudan(n):
    result = []
    for i in range(1,10):
        num = n * i
        result.append(num)
    return f"{n}단: {result}"
    
#gugudan(7)   