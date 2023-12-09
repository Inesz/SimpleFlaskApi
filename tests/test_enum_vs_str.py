from enum import Enum

from flaskr.timer_util import Timer


class En(Enum):
    a="abcd"
    b="bcde"
    c="cdef"

def test_ttt():
    val = "bcde"
    repeat = 10
    comp = 100000
    tm = Timer()

    for i in range(repeat):
        tm.start()
        for i in range(comp):
            if En(val) is En.b:
                a=1
        tm.stop()

        tm.start()
        for i in range(comp):
            if val.lower() == En.b.value:
                a=1
        tm.stop()

        tm.start()
        for i in range(comp):
            if En.b == En.b:
                a=1
        tm.stop()


    tm.print_all(3)
    tm.print_sum(3)
