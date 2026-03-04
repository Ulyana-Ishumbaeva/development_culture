import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
#TODO make it with 'pip intall -e .'

from math_demo import (add, add_with_bug)

def test_addition():
    assert add(2,2) == 4, "Function did not return 4"
    print("Test BASIC ADDITION")

def test_addiction_with_bug():
    assert add_with_bug(2,2) == 4, "Function did not return 4"
    assert add_with_bug(0,0) == 0
    print("Test BUGGED ADDITION PASSED (does in mean code ok?)")
def test_addition_duplicated():
    #is it real good test(reties on absence of + int add())
    assert add(2,3) == 2+3

def test_addition_overcomlicated():
    #formally valid test but too slow
    for i in range(0,2**32):
        for j in range(0,2**32):
            assert add(i,j) == sum([i,j])
            assert add(-i,j) == sum([-i,j])
            assert add(i,-j) == sum([i,-j])
            assert add(-i,-j) == sum([-i,-j])
def test_addition_reasonable():
    assert add(2,2) == 4
    assert add(0,0) == 0
    assert add(6,7) == 13
    assert add(-6,-7) == -13
    assert add(6,-7) == -1
    assert add(-6,7) == 1
    assert add(-7,0) == -7
    assert add(7,0) == 0

if __name__ == "__main__":
    test_addition()
    test_addiction_with_bug()
    test_addition_duplicated()
    #test_addition_overcomlicated()