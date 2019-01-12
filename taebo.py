import datetime
import queue
import copy
from functools import partial


MONTH = 30

class Stomach():
    force = False


class Movement():
    def __enter__(self):
        print('조혜련의 동작과', end=' ')
        return True

    def __exit__(self, type, value, traceback):
        return True

class Ment():
    def __enter__(self):
        print('멘트를 들으시면서')
        return True

    def __exit__(self, type, value, traceback):
        return True

class Human():
    def __init__(self, name):
        self.name = name
        self.stomach = Stomach()
        self.__movement = Movement()
        self.ment = Ment()

    def yell(self, text):
        print(text)

    def do(self, movement):
        print(f'{self.name}아줌마! {movement()}')

    @property
    def movement(self):
        return self.__movement

    @movement.setter
    def movement(self, value):
        print("따라만하세요! 따라만하세요!")
        self.__movement = value

    @property
    def body_shape(self):
        return self.__body_shape

    @body_shape.setter
    def body_shape(self, value):
        self.__body_shape = value
        print(f'{self.name}이 지금 이렇게 {self.__body_shape}한 몸매가 되었습니다.')

    @property
    def movement_score(self):
        return self.__movement_score

    @movement_score.setter
    def movement_score(self, value):
        self.__movement_score = value
        if self.__movement_score == 100:
            print("아, 정말 동작 제대로 나옵니다.")

    def ment(self):
        pass

class Dancer(Human):
    pass

class Japanese(Human):
    pass

class Taekwondo():
    movements = "우리나라의 태권도"

class Boxing():
    movements = "복싱"

class Treadmill():
    def efficacy(self, minute):
        print(f"러닝머신 한시간!")

class Taebo():
    def __init__(self, greeting):
        self.instance = []
        print(greeting)

    @property
    def popularity(self):
        return self.__popularity

    @popularity.setter
    def popularity(self, value):
        self.__popularity = value
        print(f'태보는 지금 {self.__popularity}으로 선풍적인 인기를 끌고있는데요')

    def set_movements(self, movelist):
        print(f'태보란 {"와 ".join(movelist)}을 접목한 운동입니다.')

    @property
    def sleep(self):
        return self.__sleep

    @sleep.setter
    def sleep(self, value):
        self.__sleep = value
        print(f'이게 인제, 태보에선 쉬는겁니다.')

    def do_taebo(self, instance, month):
        print(f'{month}달동안 태보를 했더니')

    def pelvic_twist(self):
        return "골반 트위스트!"

    def push_instance(self, instance, minute=None):
        if minute:
            self.instance.append(instance)
            print(f"여러분도 하루에 {minute}분만!")
            print(f"태보의 세계로 들어가봅시다!")
        else:
            print("지금부터 태보의 세계로 들어가봅시다!")

    def set_duration(self, minute=20):
        print(f'{minute}분만 하세요!')
        return True

    def enque(self, instance, minute=25):
        print(f"하루에 {minute}분만 투자하자구!")
        raise RuntimeError

    def efficacy(self, minute):
        print(f"태보를 하루 {minute}분만 투자한다면")

    def jab(self):
        print("JAB JAB JAB")

    def punch(self):
        print("PUNCH")

    def hook(self):
        print("HOOK")

    def side_kick(self):
        print("SIDE KICK")

    def cross(self):
        print("CROSS")

    def jump(self):
        print("JUMP")

class DayQueue():
    def __init__(self):
        self.__queue = []

    def push(self, value):
        self.__queue.append(value)
        if len(self.__queue) == 1:
            print("내일 또 보고", end=' ')
        elif len(self.__queue) > 1:
            print("모레 또보자!")

day_queue = DayQueue()

you = Human("여러분")
miJa = Dancer("미자")
wooJiIn = Dancer("우지인")
joHyeRyun = Japanese("조혜련")
treadmill = Treadmill()

# == 가사 시작 ==
taebo = Taebo("안녕하세요!!")
taebo.popularity = "전세계적"

taebo.set_movements([Taekwondo.movements, Boxing.movements])

taebo.do_taebo(joHyeRyun, month=2)
joHyeRyun.body_shape = "완벽"

joHyeRyun.yell("와!")

taebo.efficacy(25) == treadmill.efficacy(60)
taebo.push_instance(you, minute=25)
joHyeRyun.yell("WA!")

for idx in range(3):
    taebo.jab()
    taebo.punch()
    taebo.hook()

you.movement = copy.copy(joHyeRyun.movement)

for idx in range(2):
    taebo.jab()
    taebo.punch()
    taebo.hook()
joHyeRyun.yell("POWER!")

taebo.set_duration(minute=20)
joHyeRyun.yell("SEVEN, EIGHT!")

miJa.do(taebo.pelvic_twist)
try:
    assert(miJa.stomach.force)
except AssertionError:
    joHyeRyun.yell("배에 힘 안줬다!!!")

# 2절
wooJiIn.movement_score = 100

# 조혜련의 동작과 멘트를 들으시면서
with joHyeRyun.movement as _, joHyeRyun.ment as _:
    taebo.push_instance(you)

taebo.set_movements([Taekwondo.movements, Boxing.movements])
taebo.do_taebo(joHyeRyun, month=2)
joHyeRyun.body_shape = "완벽"

wooJiIn.yell("그렇죠!")

taebo.efficacy(25) == treadmill.efficacy(60)
taebo.push_instance(you, minute=25)

for idx in range(3):
    taebo.side_kick()
    taebo.cross()
    taebo.jump()

taebo.sleep = False

for idx in range(2):
    taebo.side_kick()
    taebo.cross()
    taebo.jump()

try:
    taebo.enque(you, minute=25)
except:
    print("오늘만 보고 끄지말고!")
    day_queue.push(partial(taebo.push_instance, you, minute=25))
    day_queue.push(partial(taebo.push_instance, you, minute=25))

