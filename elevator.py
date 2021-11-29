import time


class Elevator(object):
    def __init__(self, f):
        self.floor = f
        self.now = self.floor
        self.next = 0

    def choice(self, n):
        print("您现在位于第%s" % self.now)
        print("------------------")
        print("----1     上升----")
        print("----2     下降----")
        print("----3     取消----")
        print("请输入您的选择：")

    def run(self, c):
        if c == 1:
            self.floor = int(input("请输入上升楼层："))
            if self.floor <= self.now:
                print("请选择上升楼层！")
                floor = int(input("请输入上升楼层："))
            if self.floor > 10 or c < 1:
                print("该楼层不存在！")
                floor = int(input("请输入上升楼层："))
            self.next = self.floor
            self.up(self.now, self.next)
        if c == 2:
            self.floor = int(input("请输入下降楼层："))
            if self.floor >= self.now:
                print("请选择下降楼层！")
                self.floor = int(input("请输入下降楼层："))
            if self.floor > 10 or c < 1:
                print("该楼层不存在！")
                self.floor = int(input("请输入下降楼层："))
            self.next = self.floor
        if c == 3:
            exit(0)
        else:
            print("请输入正确的指令！")
            self.choice(self.now)

    def up(self, now, n):
        self.next = n
        print("电梯运行中")
        for i in range(now, self.next + 1):
            time.sleep(1)
            print("----第%d层----" % i)
        print("您到第%d层了！" % self.next)
        self.now = self.next

    def down(self, now, n):
        self.next = n
        print("电梯运行中")
        for i in range(now, self.next + 1, -1):
            time.sleep(1)
            print("----第%d层----" % i)
        print("您到第%d层了！" % self.next)
        self.now = self.next


class Person:
    def __init__(self, start, aim, weigth):
        self.start = start
        self.aim = aim
        self.weigth = weigth


class AdvanceElevator(Elevator):
    def __init__(self, f=10):
        Elevator.__init__(self, f)
        self.stay = 0
        self.sw = 0
        self.n = 1

    def run(self):
        self.choice(self.n)
        self.c = int(input())
        self.getPerson(self.c)

    def getPerson(self, choice):
        if choice == 1:
            self.num = int(input('请输入本次乘坐的人数：'))
            plist = []
            inlist = []
            outlist = []
            for i in range(self.num):
                s, a, w = input('请输入第{0}位乘客所在楼层、目标楼层和体重：'.format(i + 1)).split()
                s=int(s)
                a=int(a)
                w=int(w)
                plist.append(Person(s, a, w))
                inlist.append(s)
                outlist.append(a)
            inlist.sort()
            outlist.sort()
            for i in range(self.num):
                if inlist[i] == self.n:
                    self.stay += 1
            j = 0
            k = 0
            for i in range(0,11):
                if (j<self.num and inlist[j] == i + 1):
                    if inlist[j] == self.n:
                        print('有%d位乘客上电梯了' % self.stay)
                        j += 1
                        for q in range(self.num):
                            if plist[q].start == self.n:
                                self.sw = self.sw + plist[q].weigth
                    else:
                        print('现在电梯内人数为：', self.stay)
                        self.up(self.n, i + 1)
                        for q in range(self.num):
                            if plist[q].start == self.n:
                                self.sw = self.sw + plist[q].weigth
                        if self.sw >= 200:
                            print('电梯已超载')
                            self.stay -= 1
                            k += 1
                            for q in range(self.num):
                                if plist[q].start == self.n:
                                    self.sw = self.sw - plist[q].weigth
                            print('有一位乘客下去了')
                        j += 1
                        self.stay += 1
                        self.n = i + 1
                if (k<self.num and outlist[k] == i + 1):
                    print('现在电梯内人数为：', self.stay)
                    self.up(self.n, i + 1)
                    for q in range(self.num):
                        if plist[q].start == self.n:
                            self.sw = self.sw - plist[q].weigth
                    k += 1
                    self.stay -= 1
                    self.n = i + 1
            self.choice(self.n)
            self.c = int(input())
            self.getPerson(self.c)
        if choice == 2:
            self.num = int(input('请输入本次乘坐的人数：'))
            plist = []
            inlist = []
            outlist = []
            for i in range(self.num):
                s, a, w = input('请输入第{0}位乘客所在楼层、目标楼层和体重：'.format(i + 1)).split()
                s=int(s)
                a=int(a)
                w=int(w)
                plist.append(Person(s, a, w))
                inlist.append(s)
                outlist.append(a)
            inlist.sort()
            outlist.sort()
            for i in range(self.num):
                if inlist[i] == self.n:
                    self.stay += 1
            j = self.num - 1
            k = self.num - 1
            for i in range(self.n, 0, -1):
                if (i == inlist[j]):
                    if inlist[i] == self.n:
                        print('有%d位乘客上电梯了' % self.stay)
                        j -= 1
                        for q in range(self.num):
                            if plist[q].start == self.n:
                                self.sw = self.sw + plist[q].weigth
                    else:
                        print('现在电梯内人数为：', self.stay)
                        self.dowm(self.n, i)
                        for q in range(self.num):
                            if plist[q].start == self.n:
                                self.sw = self.sw + plist[q].weigth
                        if self.sw >= 200:
                            print('电梯已超载')
                            self.stay -= 1
                            k -= 1
                            for q in range(self.num):
                                if plist[q].start == self.n:
                                    self.sw = self.sw - plist[q].weigth
                            print('有一位乘客下去了')
                        j -= 1
                        self.stay += 1
                        self.n = i
                if (outlist[k] == i + 1):
                    print('现在电梯内人数为：', self.stay)
                    self.down(self.n, i)
                    for q in range(self.num):
                        if plist[q].start == self.n:
                            self.sw = self.sw - plist[q].weigth
                    k -= 1
                    self.stay -= 1
                    self.n = i
            choice(self.n)
            self.c = int(input())
            self.getPerson(self.c)
        if choice == 3:
            exit(0)
        else:
            self.c = int(input('请输入正确的指令！'))
            self.getPerson(self.c)


print("您好,欢迎使用本电梯")
print("本电梯共10层，限重200公斤，请选择")
e = AdvanceElevator(1)
e.run()
