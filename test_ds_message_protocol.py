# Kellan Yamamoto
# 28388886
# kellany@uci.edu

from ds_protocol import format_for_json
'''
Module that tests ds_protocol
'''

format_for_send = format_for_json('1', "100101019101910")
print(format_for_send)

format_for_retreive_new = format_for_json('2', '11010101010101010110')
print(format_for_retreive_new)

format_for_retreive_all = format_for_json('3', '11010101010101010110')
print(format_for_retreive_all)