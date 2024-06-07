This project implements a Python module for sending and receiving direct messages to another user on the DSP platform. It includes a 
graphical user interface (GUI) built with Tkinter that allows students to communicate with each other by knowing each other's usernames.

Project Structure:
ds_protocol.py: Extends the DSP protocol to support direct messaging commands.
ds_messenger.py: Implements the DirectMessenger class for sending and retrieving messages.
interface.py: Implements the GUI using Tkinter for user interaction.
test_ds_protocol.py: Contains tests for the ds_protocol module.
test_ds_messenger.py: Contains tests for the ds_messenger module.

Usage:
Run the GUI application: python gui.py
Use the interface to send and receive direct messages on the DSP platform.

Features:
Send direct messages to other users on the DSP platform.
Receive direct messages from other users.
Store messages locally for offline viewing.
GUI for easy and intuitive user interaction. 

Errors: 
The retreive_all() function needs some work