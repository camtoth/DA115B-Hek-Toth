Creators: Cameron Toth & Stephan Hek (HKR students)

This document describes the working of the code in this Github repository.

INTRODUCTION
===============================================
The program runs a game of 'pig'. This is a dice game that can be played by two human players or a computer controlled player. 
User input and output is completely text-based.



BACKGROUND CODE
===============================================
The program code consists of a series of classes and a main script used to run the program.

- Menu Class:     this class creates the syntax for the menu of the game. Here the player can start a game or check the specific rules and other 
                  general settings/information.
- Game Class:     this class is the heart of the program and controls the flow of the game. This class has methods to process user input and 
                  give information during a game session.
- Player Class:   a seperate class is created for a player in the game. It contains the relevant player attributes and the decision process of 
                  an automated player
- Dice Class:     a class descibing a dice in the game. The game can be played with 1 or 2 dice which this class processes. It also has a method 
                  preforming a dice role with the defined number of dice. 


UNITTESTING
===============================================
Unittesting was used to determine if the program functions accordingly. For each class a seperate py-file is created (test_[classname].py) that contain a set of tests. The python module unittesting was used to perform these tests.


RUNNING THE PROGRAM IN A VIRTUAL ENVIRONMENT
===============================================
