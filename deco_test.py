from enum import Enum

# なんとなくつくっただけ
class Answer(Enum):
    OfCourse = 1
    AbsolutelyNo = 0

def add(addition, is_want_add):
    """ 何を追加するかの関数と、列挙型Answerをもらって、デコレートする方法を決める """
    def _deco(f):
        def _wrap(*args, **kwargs):
            if is_want_add == Answer.OfCourse:
                print(addition(), end='')
            f(*args, **kwargs)
        return _wrap
    return _deco

def create_addition_furikake(kind_of_furikake):
    """ デコレータに渡す、あとで使う関数をつくる """

    furikake_dict = {
        "あおのり": "すばらしいおいしさを誇る",
        "しょうが": "しょうがない"
    }
    def addition_furikake():
        return furikake_dict[kind_of_furikake]

    return addition_furikake

@add(create_addition_furikake('あおのり'), Answer.OfCourse)
def takoyaki():
    print('たこやき')

takoyaki()
# -> すばらしいおいしさを誇るたこやき
