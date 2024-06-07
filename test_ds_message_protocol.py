'''
Test for format of ds_protocol
'''

# Kellan Yamamoto
# 28388886
# kellany@uci.edu

import pytest
from ds_protocol import format_for_json


def test_format_for_retrieve_new():
    '''
    pytest for formats
    '''
    result = format_for_json('2', '11010101010101010110')
    expected = {
        'token': '11010101010101010110',
        'directmessage': 'new'
    }
    assert result == expected, f"Expected {expected}, but got {result}"

def test_format_for_retrieve_all():
    '''
    pytest for formats
    '''
    result = format_for_json('3', '121212121212')
    expected = {
        'token': '121212121212',
        'directmessage': 'all'
    }
    assert result == expected, f"Expected {expected}, but got {result}"

if __name__ == "__main__":
    pytest.main()
