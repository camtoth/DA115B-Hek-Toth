#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
from game import player


class TestPlayerClass(unittest.TestCase):
    def setUp(self):
        self.player = player.Player()

    def testDefaultObject(self):
        # Instantiate an object and check its properties
        self.assertIsInstance(self.player, player.Player)

        result = self.player.name
        expected = ""
        self.assertEqual(result, expected)

        result = self.player.playerType
        expected = 0
        self.assertEqual(result, expected)

    def testPlayerName(self):
        # Roll one die and check value is in bounds
        name = "Kalle"
        self.player.name = name
        self.assertEqual(self.player.name, name)

    def testPlayerType(self):
        playerType = "careful"
        self.player.playerType = playerType
        self.assertEqual(self.player.playerType, playerType)

    def testBehaviourPC(self):
        playerType = "careful"


if __name__ == "__main__":
    unittest.main()
