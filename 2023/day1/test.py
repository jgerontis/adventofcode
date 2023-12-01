from main import value

def test_value():
    assert value('1abc2') == 12
    assert value('pqr3stu8vwx') == 38
    assert value('a1b2c3d4e5f') == 15
    assert value('treb7uchet') == 77
    assert value('two1nine') == 29
    assert value('eightwothree') == 83
    assert value('abcone2threexyz') == 13
    assert value('xtwone3four') == 24
    assert value('4nineeightseven2') == 42
    assert value('zoneight234') == 14
    assert value('7pqrstsixteen') == 76

test_value()