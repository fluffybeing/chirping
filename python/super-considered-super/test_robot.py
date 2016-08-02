#!/usr/bin/env python
# coding=utf-8

from robot import Robot, CleaningRobot
import unittest

class MockBot(Robot):
    """Simulate a real robot by merely recording task"""

    def __init__(self):
        self.task = []

    def fetch(self, tool):
        self.task.append('fetching %s' % tool)
    def move_forward(self, tool):
        self.task.append('forward %s' % tool)
    def move_backward(self, tool):
        self.task.append('backward %s' % tool)
    def replace(self, tool):
        self.task.append('replace %s' % tool)

class MockedCleaningRobot(CleaningRobot, MockBot):
    """Inject a mock bot into the robot dependency"""

class TestCleaningRobot(unittest.TestCase):

    def test_client(self):
        t = MockedCleaningRobot()
        t.clean('mop')
        expected = (['fetching mop'] + ['forward mop', 'backward mop'] * 10 +
                   ['replace mop'])
        self.assertEqual(t.task, expected)

if __name__ == '__main__':
    unittest.main()


