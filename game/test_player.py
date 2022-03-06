# unittesting of player class
import unittest
import player


class TestPlayerClass(unittest.TestCase):
    def setUp(self):
        self.player = player.Player()

    def test_01_DefaultObject(self):
        # Instantiate an object and check its properties
        self.assertIsInstance(self.player, player.Player)

        result = self.player.name
        expected = ""
        self.assertEqual(result, expected)

        result = self.player.playerType
        expected = 0
        self.assertEqual(result, expected)

    def test_02_PlayerName(self):
        # test player name
        name = "Kalle"
        self.player.name = name
        self.assertEqual(self.player.name, name)

    def test_03_PlayerType(self):
        # test playertype
        playerType = "careful"
        self.player.playerType = playerType
        self.assertEqual(self.player.playerType, playerType)

    def test_04_BehaviourPC1(self):
        number_rolls = 1
        number_decision = 1000

        # loop through behaviour types
        for i, pt in enumerate(self.player.behaviourTypes):
            self.player.playerType = i + 1
            y = pt[1]
            n = pt[2]
            prob = y / (y + n * number_rolls)

            # determine boundaries for confidence level 5-sigma event
            mean = number_decision * prob
            variance = number_decision * prob * (1 - prob)
            sd = variance**(0.5)
            lowBoundary = mean - sd * 5
            highBoundary = mean + sd * 5

            # run decision multiple times
            result = 0
            for i in range(0, number_decision):
                decision = self.player.makeDecision(number_rolls)

                if decision == "y":
                    result += 1

            self.assertGreaterEqual(result, lowBoundary)
            self.assertLessEqual(result, highBoundary)

    def test_05_BehaviourPC2(self):
        number_rolls = 2
        number_decision = 1000

        # loop through behaviour types
        for i, pt in enumerate(self.player.behaviourTypes):
            self.player.playerType = i + 1
            y = pt[1]
            n = pt[2]
            prob = y / (y + n * number_rolls)

            # determine boundaries for confidence level 5-sigma event
            mean = number_decision * prob
            variance = number_decision * prob * (1 - prob)
            sd = variance**(0.5)
            lowBoundary = mean - sd * 5
            highBoundary = mean + sd * 5

            # run decision multiple times
            result = 0
            for i in range(0, number_decision):
                decision = self.player.makeDecision(number_rolls)

                if decision == "y":
                    result += 1

            self.assertGreaterEqual(result, lowBoundary)
            self.assertLessEqual(result, highBoundary)

    def test_06_BehaviourPC3(self):
        number_rolls = 3
        number_decision = 1000

        # loop through behaviour types
        for i, pt in enumerate(self.player.behaviourTypes):
            self.player.playerType = i + 1
            y = pt[1]
            n = pt[2]
            prob = y / (y + n * number_rolls)

            # determine boundaries for confidence level 5-sigma event
            mean = number_decision * prob
            variance = number_decision * prob * (1 - prob)
            sd = variance**(0.5)
            lowBoundary = mean - sd * 5
            highBoundary = mean + sd * 5

            # run decision multiple times
            result = 0
            for i in range(0, number_decision):
                decision = self.player.makeDecision(number_rolls)

                if decision == "y":
                    result += 1

            self.assertGreaterEqual(result, lowBoundary)
            self.assertLessEqual(result, highBoundary)


if __name__ == "__main__":
    unittest.main()
