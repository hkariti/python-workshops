import pytest
import mytool

@pytest.fixture(params=[0, 1, 5])
def total_pairs(request):
    return request.param

@pytest.fixture()
def expected_cis(total_pairs):
    if total_pairs == 0:
        return 0
    return 1

@pytest.fixture()
def pairs(total_pairs):
    if total_pairs == 0:
        return []
    if total_pairs == 1:
        return [(1, 2)]
    if total_pairs == 5:
        return [(1, 2), (4, 0), (2, 4), (1, 3), (0, 3)]

@pytest.fixture()
def chromosomes():
    return [1, 1, 1, 2, 3]

def test_count_cis(expected_cis, pairs, chromosomes):
    actual = mytool.count_cis(pairs, chromosomes)

    assert expected_cis == actual
