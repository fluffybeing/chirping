#!/usr/bin/env python
# coding=utf-8

class Robot(object):
    """Sophististicated class that moves a real robot"""
    # Don't wear down real robots by running tests!

    def fetch(self, tool):
        print('Physical Movement! Fetching')
    def move_forward(self, tool):
        print('Physical Movement! Moving Forward')
    def move_backward(self, tool):
        print('Physical Movement! Moving Backward')
    def replace(self, tool):
        print('Physical Movement! Replacing')

class CleaningRobot(Robot):
    """Custom robot that can clean with a given tool"""

    def clean(self, tool, times=10):
        super(CleaningRobot, self).fetch(tool)

        for i in range(times):
            super(CleaningRobot, self).move_forward(tool)
            super(CleaningRobot, self).move_backward(tool)
        super(CleaningRobot, self).replace(tool)

if __name__ == '__main__':
    t = CleaningRobot()
    t.clean('broom')

