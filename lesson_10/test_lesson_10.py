import pytest


@pytest.mark.old
@pytest.mark.main
def test_1():
    assert True


@pytest.mark.new
def test_2():
    assert True


@pytest.mark.main
def test_3():
    assert True


@pytest.mark.old
def test_4():
    assert True


@pytest.mark.new
def test_5():
    assert True


@pytest.mark.main
def test_6():
    assert True


@pytest.mark.main
def test_7():
    assert True


@pytest.mark.old
def test_8():
    assert True


@pytest.mark.main
def test_9():
    assert True


@pytest.mark.new
def test_10():
    assert True


#  pytest -m "smoke or regression" -v     ранить і то і то
#  pytest -m "smoke and regression" -v    ранить коли збігається обидва
#  pytest -m "not smoke" -v               ранить всі окрім smoke