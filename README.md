Creators: Cameron Toth & Stephan Hek (HKR students)

This document describes the working of the code in this Github repository.


INTRODUCTION
===============================================
The program runs a game of 'pig'. This is a dice game that can be played by two human players or a computer controlled player. 
User input and output is completely text-based.


RUNNING THE GAME
===============================================
One can run the game by executing the main.py file in the game directory. In the terminal one can type "python3 main.py". 


BACKGROUND CODE
===============================================
The program code consists of a series of classes and a main script used to run the program.

Menu Class
this class creates the syntax for the menu of the game. Here the player can start a game or check the specific rules 
and other general settings/information.

Game Class
this class is the heart of the program and controls the flow of the game. 
This class has methods to process user input and give information during a game session.

Player Class 
a seperate class is created for a player in the game. It contains the relevant player attributes 
and the decision process of an automated player
Dice Class
a class descibing a dice in the game. The game can be played with 1 or 2 dice which this class processes.
It also has a method preforming a dice role with the defined number of dice. 

Leaderboard Class
This class contains the leaderboard with player scores of previous sessions. This data is stored in a pickle file.

For more documentation one can run the "make pydoc" command. This generates html files of each python file with documentation.


UNITTESTING
===============================================
Unittesting was used to determine if the program functions accordingly. For each class a seperate py-file is created (test_[classname].py) that contain a set of tests. The python module unittesting was used to perform these tests.

Run unittesting using the "make unittest"  command


CHECK CODE FORMATTING
===============================================
The code was programmed using the flake8 syntax. One can check if the structure is correct and possibly contains errors
by typing "make flake8". A list of formatting errors will be printed if present.


RUNNING THE PROGRAM IN A VIRTUAL ENVIRONMENT
===============================================
Use the make command to setup a virtual environment. Use the "make venv" command. 

After this setup one can install the required packagers using "make install". Type "make installed" to view which modules were installed.

When done, one can clean up the environment using "make clean-all".




