# unit tests

# functions are the same in Linux.py, MacOS.py and Windows.py

from Linux import extensions_checker


def test_extensions_checker_valid_extension():
    extensions_list = [".pdf", ".txt", ".md", ".jpg"]
    assert extensions_checker("test.txt", extensions_list)


def test_extensions_checker_invalid_extension():
    extensions_list = [".pdf", ".txt", ".md", ".jpg"]
    assert not extensions_checker("program.py", extensions_list)
