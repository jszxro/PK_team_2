import sys
a= sys.argv[1:]
result =[]
class Woo:
    def __init__(self,word):
        self.result=[]
        self.word=word
    def check(self):
        for n in self.word : 
            if n[0]==n[-1]:
                self.result.append(n)
                print(f'{n}는 거꾸로 해도 같은 단어 입니다.')
        return self.result
b= Woo(a)
print(b.check())