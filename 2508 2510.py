class Queue :
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
g = Queue()
k = Queue()
b = Queue()
s = Queue()
for i in range(0,100):
    g.enqueue(1)
    k.enqueue(1)
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



q=True
food=input('뭐 먹을래? 감자 보리 밀 쌀      ')
if food=='감자' :
    f=292
elif food=='보리' :
    f=176
elif food=='밀' :
    f=248
elif food=='쌀' :
    f=264
elif food=='채소' :
    f=2
elif food=='빵' :
    print('빵이 없으면 캐이크를 먹어')
    q=False
elif food=='인공 음식' :
    f=10000000
else :
    print('그런 거 없다 반동분자야')
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
    b=int(input('편안함'))
    for i in range(1,41):
        at.append(a)
        gt.append(g)
        wt.append(w)
        ht.append(h)
        y=y+1
        nw=int(a*0.1)
        bh=int(b*h)
        bh1=int(bh*0.4)
        bh2=int(bh*0.1)
        f1=int(f*0.1)
        a=a+w-nw+h+bh2-f1
        g=g-bh+f-h
        w=nw
        dh=int(0.08*h)
        nh=int(0.02*bh)
        if a<0 :
            print('서기', end='')
            print(y, end='')
            print('년', end=' ')
            print(food, end='')
            print('농사가 망했습니다 you die')
            at.append(a)
            q=False
            break
        elif f-h<0 :
            print('서기', end='')
            print(y, end='')
            print('년', end=' ')
            print(food, end='')
            print('수확량이 부족합니다 폭동이 일어났습니다 you die')
            q=False
            break
        elif g<0 :
            print('서기', end='')
            print(y, end='')
            print('년', end=' ')
            print('화석 연료가 다 떨어졌습니다 가장 현실에 가깝습니다 you die')
            gt.append(g)
            q=False
            break
        elif a>12000:
            print('서기', end='')
            print(y, end='')
            print('년', end=' ')
            print('숨이 막혀 오는 것이 느껴집니다 you die')
            at.append(a)
            q=False
            break
        elif f-h>240 :
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
    plt.ylim(8000,21000) # y축 값 범위

    plt.xlabel('x축') # x축 레이블
    plt.ylabel('y축') # y축 레이블

    plt.savefig('data.png') # 파일 저장

    plt.show() # 그래프 보여주기
    print(at)
    print(gt)
    print(wt)
    print(ht)
