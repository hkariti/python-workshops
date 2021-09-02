import pytest
import mytool

def test_count_cis():
    pairs = [(1, 2), (4, 0)]
    chromosomes = [1, 1, 1, 2, 3]

    expected = 1
    actual = mytool.count_cis(pairs, chromosomes)

    assert expected == actual

def test_verify_list_correct():
    correct_input = [0,1,2,3]
    mytool.verify_non_negative(correct_input)

def test_verify_list_bad():
    bad_input = [0,1,-2,3]
    with pytest.raises(ValueError):
        mytool.verify_non_negative(bad_input)
