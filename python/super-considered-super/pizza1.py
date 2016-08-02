#!/usr/bin/env python
# coding=utf-8

class DoughFactory(object):

    def get_dough(self):
        return 'insectide treated wheat dough'

class Pizza(DoughFactory):

    def order_pizza(self, *toppings):
        print('Getting dough')
        # use super to avoid hard written Doughfactory twice
        dough = super(Pizza, self).get_dough()
        print('Making pie with %s' % dough)

        for topping in toppings:
            print('Adding: %s' % topping)

if __name__ == '__main__':
    Pizza().order_pizza('Pepperoni', 'Bell Pepper')


