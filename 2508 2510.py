class Queue :   # Queue 정의
    def __init__(self) :
        self.items = []
    def enqueue(self,item) :
        self.items.insert(0,item) 
    def dequeue(self) :
        return self.items.pop()
    def isEmpty(self) :
        return self.items == []
    def size(self) :
        return len(self.items)
    
#지구를 구성하는 각 계의 탄소 소비량
g = Queue()
k = Queue()
b = Queue()
s = Queue()

for i in range(0,100):
    g.enqueue(1)
    k.enqueue(1)i
    b.enqueue(1)
    s.enqueue(1)
a1 = g.size() // 3
a2 = k.size() // 4
a3 = b.size() // 2
a4 = s.size() // 5
for i in range(a1) :
    g.dequeue()
for i in range(a2) :
    k.dequeue()
for i in range(a3) :
    b.dequeue()
for i in range(a4) :
    s.dequeue()
for i in range(a2) :
    g.enqueue(1)
for i in range(a3) :
    k.enqueue(1)
for i in range(a4) :
    b.enqueue(1)
for i in range(a1) :
    s.enqueue(1)
print(g.size())
print(k.size())
print(b.size())
print(s.size())


#q값에 따라 인류의 미래가 결정됨
q=True                                       #f= 수확량
wf=input('뭐 먹을래? 감자 보리 밀 쌀 인공 음식  콩   ')   # 무슨 음식을 먹을지 설정하는 코드 : 감자 보리 밀 쌀 인공 음식 콩
if wf=='감자' :
    f=292
elif wf=='보리' :
    f=176
elif wf=='밀' :
    f=248
elif wf=='쌀' :
    f=264
elif wf=='채소' :
    f=2
elif wf=='빵' :
    print('빵이 없으면 캐이크를 먹어-말이 안통하네트')
    q=False
elif wf=='인공 음식' :
    f=10000000
elif wf=='콩':
    f=1000
elif wf=='지구에는 먹을게 없어' :  #hidden ending : 살아남을 수 있는 단 하나의 코드
    print('당신은 지구에 식량난이 오기 전에 지구 탈출을 계획하여 탈출에 성공했습니다. 이제부터 우주를 개척하시면서 살아가면 됩니다. you alive')
    q=False    
else :
    print('그런 거 없다 반동분자야')   # 위 리스트에 없는 음식을 입력했을 경우
    q=False
a=10000
g=10000
h=70
at=[]
gt=[]
wt=[]
ht=[]
w=1000
y=2019
while q :
    b=int(input('편안함(편안함이 클수록 인류의 삶은 편해지지만 자원 소비량이 커집니다) : )'))
    for i in range(1,41):
        at.append(a)
        gt.append(g)
        wt.append(w)
        ht.append(h)
        y=y+1                         #해는 1년씩 늘어남
        nw=int(a*0.1)
        bh=int(b*h)
        bh1=int(bh*0.4)
        bh2=int(bh*0.1)
        f1=int(f*0.1)
        a=a+w-nw+h+bh2-f1            #1년 후 이산화탄소의 양
        g=g-bh+f-h                   #1년 후 화석 연료의 양
        w=nw
        dh=int(0.08*h)
        nh=int(0.02*bh)
        if a<3000 :                     #이산화탄소 농도가 너무 낮으면 호흡이 안되서 농사가 망함
            print('서기', end='')
            print(y, end='')
            print('년', end=' ')
            print(wf, end='')
            print('농사가 망했습니다 you die')
            at.append(a)
            q=False
            break
        elif f-h<0 :                #인구에 비해 수확량이 적으면 정부에 반기를 든 분노한 시민들이 폭동을 일으킵니다.
            print('서기', end='')
            print(y, end='')
            print('년', end=' ')
            print(wf, end='')
            print('수확량이 부족합니다 폭동이 일어났습니다 you die')
            q=False
            break
        elif g<0 :                  #화석 연료가 없어서 너는 굶어 죽습니다.
            print('서기', end='')
            print(y, end='')
            print('년', end=' ')
            print('화석 연료가 다 떨어졌습니다 가장 현실에 가깝습니다 you die')
            gt.append(g)
            q=False
            break
        elif a>30000:               #이산화탄소 농도가 너무 높으면 질식사합니다
            print('서기', end='')
            print(y, end='')
            print('년', end=' ')
            print('숨이 막혀 오는 것이 느껴집니다 you die')
            at.append(a)
            q=False
            break
        elif f-h>500 :             #수확량이 인구에 비해 너무 많으면 넘쳐나는 음식물 쓰레기를 주체할 수 없게 됩니다.
            print('서기', end='')
            print(y, end='')
            print('년', end=' ')
            print('음식물 쓰레기가 너무 많습니다 you die')
            q=False
            break
        else :
            h=h-dh+nh
    import matplotlib.pyplot as plt
    plt.figure(figsize = (5,3), dpi = 300) # 그래프 크기 및 해상도 조절

    plt.rc('font',family='Malgun Gothic') # 한글 폰트설정
    plt.plot(at, '.')
    plt.title('a') # 제목 넣기

    plt.xlim(0,len(at)+1) # x축 값 범위
    plt.ylim(1000,21000) # y축 값 범위

    plt.xlabel('x축') # x축 레이블
    plt.ylabel('y축') # y축 레이블

    plt.savefig('data.png') # 파일 저장

    plt.show() # 그래프 보여주기
    print(at)
    print(gt)
    print(wt)
    print(ht)
