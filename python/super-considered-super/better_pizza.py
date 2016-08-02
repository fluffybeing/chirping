#!/usr/bin/env python
# coding=utf-8

from pizza1 import Pizza, DoughFactory

class OrganicDoughFactory(DoughFactory):

    def get_dough(self):
        return 'pure untreated wheat dough'

class OrganicPizza(Pizza, OrganicDoughFactory):
    pass

if __name__ == '__main__':
    OrganicPizza().order_pizza('Sausage', 'Mushroom')
    help(OrganicPizza)
