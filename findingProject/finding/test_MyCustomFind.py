from argparse import Namespace
import pytest
from MyCustomFind import *
import pytest_mock



def test_parse_args():
    input = ["-images", "D:\\"]
    expected = Namespace(duplicates=False, large=False, size=None, images=True, old=False, path='D:\\', o=None)
    assert parse_args(input) == expected

def test_getImages():
    input = ["file1.jpg", "file2.txt", "file3.png"]
    expected = ["file1.jpg", "file3.png"]
    assert getImages(input) == expected

def mock_cmp(one, two):
    return True

def test_getDuplicates(mocker):
    mocker.patch(
        'filecmp.cmp',
        mock_cmp
    )
    files = ["file1.jpg", "file2.txt", "file3.png"]
    path = "D:\\"
    expected = ["file1.jpg", "file2.txt", "file3.png"]
    assert expected == getDuplicates(files, path)

class temp:
    def __init__(self):
        self.st_size = 3519

def mock_stat(file_path):
    obj = temp()
    return obj

def test_file_size(mocker):
    mocker.patch(
        'os.stat',
        mock_stat
    )
    expected = 3519
    assert expected == file_size("D:\\f.png")

def test_getFileSize():
    assert getFileSize('10gb') == 10*1024*1024*1024

def test_getFileSizeInByte():
    assert 10*1024*1024*1024 == getFileSizeInByte(10, "gb")

def mock_file_size(file_path):
    obj = temp()
    return obj

def less(str):
    return 1

def more(str):
    return 1000000000

@pytest.mark.parametrize("mockk, expected", 
[
    [less, []],
    [more, ["file1.jpg", "file2.txt", "file3.png"]]
]
)
def test_getLarge(mockk, expected, mocker):
    mocker.patch(
        'MyCustomFind.file_size',
        mockk
    )
    files = ["file1.jpg", "file2.txt", "file3.png"]
    path = "D:\\"
    size = "1mb"
    assert expected == getLarge(files, path, size)


def smallTime(str):
    return 1

def bigTime(str):
    return 100000000000000

@pytest.mark.parametrize('mockk, expected',
[
    [smallTime, []],
    [bigTime, ["file1.jpg", "file2.txt", "file3.png"]]
]
)
def test_getOld(mockk, expected, mocker):
    mocker.patch(
        'os.path.getctime',
        mockk
    )
    files = ["file1.jpg", "file2.txt", "file3.png"]
    path = "D:\\"
    assert expected == getOld(files, path)

def test_getResult():
    files = ["file1.jpg", "file2.txt", "file3.png"]
    path = "D:\\"
    expected = "D:\\file1.jpg\nD:\\file2.txt\nD:\\file3.png\n"
    assert getResult(files, path) == expected
