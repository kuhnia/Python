from application import *
import pytest

def getData():
    return [[5, 120],
[6, 720],
[1, 1],
[2, 2],
[3, 6],
[4, 24]]


@pytest.mark.parametrize("num, expected", getData())
def test_f3(num, expected):
    assert f3(num) == expected

@pytest.mark.parametrize("num, expected", getData())
def test_f4(num, expected):
    assert f4(num) == expected

def test_f5():
    assert f5(5) == {1: 1, 2: 4, 3: 9, 4: 16}
    assert f5(0) == {}

def test_f7():
    assert f7(" 1,2,3, 4 ,5,6,9 ") == (1,2,3,4,5,6,9)

def test_f8():
    assert f8("Hi,my,name,is,admin") == ["Hi", "admin", "is", "my", "name"]

def test_f10():
    assert f10("Hi my name is admin") == ["Hi", "admin", "is", "my", "name"]

def test_f11():
    assert f11("0001,0010,0011,0100,0101,0110,0111,1000,1001,1010,1011,1100,1101,1110,1111") == [5, 10, 15]

@pytest.mark.parametrize("num, expected", [[1, 1234],
[2, 2468],
[3, 3702]])
def test_f12(num, expected):
    assert f12(num) == expected

@pytest.mark.parametrize("pas, expected", [["1234567", "Пароль повинен містити хочаб одну маленьку літеру"],
["6346754ethh", "Пароль повинен містити хочаб одну велику літеру"],
["rdhtytytQ", "Пароль має містити хочаб одну цифру"],
["354dytytjQ", "Пароль має містити хочаб один з символів: $ # @"],
["354dytytjQ#", "Пароль відповідає правилам валідації"]])
def test_f13(pas, expected):
    assert f13(pas) == expected

def test_f14():
    assert f14([
        ("Mykola", 18, 9),
        ("Artem", 18, 8),
        ("Vika", 17, 9),
        ("Masha", 17, 7)
    ]) == [('Artem', 18, 8), ('Masha', 17, 7), ('Mykola', 18, 9), ('Vika', 17, 9)]

@pytest.mark.parametrize("steps, expected", [[["1 UP", "1 UP"], 2],
[["4 RIGHT", "4 RIGHT", "1 UP", "4 RIGHT", "3 DOWN"], 3]])
def test_f15(steps, expected):
    assert f15(steps) == expected

def test_f16():
    assert f16('''Вот дом,
Который построил Джек.
А это пшеница,
Которая в темном чулане хранится
В доме,
Который построил Джек.
А это веселая птица-синица,
Которая часто ворует пшеницу,
Которая в темном чулане хранится
В доме,
Который построил Джек.''') == {'А': 2, 'В': 3, 'Вот': 1, 'Джек.': 3, 'Которая': 3, 'Который': 3, 'в': 4, 'веселая': 1, 'ворует': 1, 'дом,': 1, 'доме,': 2, 'построил': 3, 'птица-синица,': 1, 'пшеница,': 1, 'пшеницу,': 1, 'темном': 2, 'хранится': 2, 'часто': 1, 'чулане': 2, 'это': 2}
