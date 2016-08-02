#!/usr/bin/env python
# coding=utf-8

from __future__ import print_function
from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    """Counter that remember the order elements are first seen"""
    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))

    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)


oc = OrderedCounter('abracadabra')
print(oc)
