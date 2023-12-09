import io
import sys

from flaskr.timer_util import Timer


def test_print_all():
    timer_util = Timer()
    timer_util.starts = [2,3,4,5,6,7]
    timer_util.ends = [2,4,6,8,9,11]

    out = io.StringIO()
    sys.stdout = out
    timer_util.print_all(3)
    sys.stdout = sys.__stdout__
    assert out.getvalue() == "\n\n[0] |  [1] = [0] | [2] = [1] | [3] = [2] |\n[1] |  [1] = [3] | [2] = [3] | [3] = [4] |\n"


def test_print_sum():
    timer_util = Timer()
    timer_util.starts = [2,3,4,5,6,7]
    timer_util.ends = [2,4,6,8,9,11]

    out = io.StringIO()
    sys.stdout = out
    timer_util.print_sum(3)
    sys.stdout = sys.__stdout__
    print(out.getvalue())
    assert out.getvalue() == "\n[sum] |  [1] = [3] | [2] = [4] | [3] = [6] |\n"
