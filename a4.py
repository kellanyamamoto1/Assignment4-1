"""
Main file that begins program which will run admin,
user, and trigger the UI
"""
# a4.py

# Starter code for assignment 4 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Kellan Yamamoto
# kellany@uci.edu
# 28388886


import admin
import ds_client
import ds_protocol
import ui as ui
import ds_messenger
import Profile as prof
import test_ds_messenger
import interface
import user

# PATH: C:\Users\kella\OneDrive\Desktop\ICS32Again\Assignment3
# E -usr "mark b" -pwd "password123" -bio "test bio"

if __name__ == "__main__":
    # token: 1269c913-8909-49ce-8f8f-f510140fcda9
    ds_client.send("168.235.86.101", 3021, "help", "mog", "fn")
    # ui.start()
    interface.begin()