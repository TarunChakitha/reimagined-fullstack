from solutions import *

def test_biggest():
    assert biggest([1,2,3]) == 3
    assert biggest([3]) == 3
    assert biggest([3,2,1]) == 3
    assert biggest([2,3,1]) == 3

def test_average():
    assert average([1,2,3]) == 2.0
    assert average([1,1,1]) == 1.0
    assert average([9,9,9]) == 9.0
    assert average(range(100)) == 49.5

def test_longest():
    assert longest(["python", "perl", "php"]) == "python"
    assert longest(["perl", "python", "php"]) == "python"
    assert longest(["perl", "php", "python"]) == "python"


def test_first_space():
    assert first_space(["php", "x y", "z"]) == "x y"
    assert first_space(["php", "x y", "z q"]) == "x y"
    assert first_space(["p p", "x y", "z q"]) == "p p"

def test_freq():
    s = "she sells sea shells on the sea shore"
    freq_s = {'s': 8, 'h': 4, 'e': 7, ' ': 7, 'l': 4, 'a': 2, 'o': 2, 'n': 1, 't': 1, 'r': 1}
    assert freq(s) == freq_s
    assert freq("abXba") == {"X" : 1, "a" : 2, "b" : 2}

def test_panagram():
    assert panagram("the quick brown fox jumps over the lazy dog")
    assert not panagram("the quick brown fox jumped over the lazy dog")
    
def test_abbreviate():
    assert abbreviate("Indian Institute of Sciences") == "IIS"
    assert abbreviate("All Indian Institute of Medical Sciences") == "AIIMS"


def test_split():
    d = [1000, 500, 100, 50, 20, 10, 5, 1]
    assert split(2246, d) == {1000: 2, 100: 2, 20: 2, 5: 1, 1: 1}
    assert split(1400, d) == {1000: 1, 100: 4}
    assert split(1670, d) == {1000: 1, 100: 1, 500:1, 50:1, 20:1}

if __name__ == '__main__':
    test_biggest()
    test_average()
    test_longest()
    test_first_space()
    test_freq()
    test_panagram()
    test_abbreviate()
    test_split()
    # unittest.main()
