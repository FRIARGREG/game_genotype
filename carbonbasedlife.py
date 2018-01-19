# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 14:33:18 2018
@author: Friar Gregarious


"""

## new template for my code
import os
from dna import living_dna

class basic_exist_thing(object):
    """ the root of all things is existance """
    def __init__(self, **kwargs):
        """ the root of all things is existance """
        # =====================================================================
        # this is the parent for all objects in this world
        #      * all objects have physical attibutes and simple methods of
        #        behaviour like gravity and magnetics
        #      * to make things far simpler and to bite my thumb at the U.S.
        #        all measurements will be in metric. so there Mr. Trump.
        # =====================================================================
        self.mass = kwargs.get('mass', 0.0)

        self.height = kwargs.get('height', 0.0)
        self.length = kwargs.get('length', 0.0)
        self.width = kwargs.get('width', 0.0)

        self.volume = kwargs.get('volume', self.calc_volume())
        self.encumberance = kwargs.get('encumberance', self.calc_encumbrance())

    def calc_volume(self):
        """ volume is how much space a thing displaces """
        return self.height * self.width * self.length

    def calc_encumbrance(self):
        """ encumberance is how difficult a thing is carry. """
        return self.mass * self.volume * 2


class living_thing(basic_exist_thing):
    """ container for living_dna() this object contains the methods that all
    living creatures require which represent instincts """
    def __init__(self, **kwargs):
        """ initializing first heartbeat """
        basic_exist_thing.__init__(self)
        self.dna = kwargs.get('dna', living_dna())
        self.emotional_state = self.calc_emotional_state()

    def instinct_reproduce(self):
        """ all life feels a drive to reproduce """
        pass

    def instinct_survive(self):
        """ all life feels a drive to preserve their own existance. """
        pass

    def instinct_feed(self):
        """ all life feels hunger which also triggers survival. """
        # =====================================================================
        # this method will also handle thirst. no need to make things
        # too complicated. we're only dealing with a light simulation
        # =====================================================================
        pass

    def calc_emotional_state(self):
        """ this method constantly adjusts emotional state of the creature """
        # =====================================================================
        # all creatures have an emotional state of balance which can (and will)
        # be affected by their environment, their own actions/inactions and the
        # actions/inactions of the creatures/people around them.
        # =====================================================================
        pass

























# =============================================================================
# This section is simply for testing purposes. if this module is run directly
#  which only happens when I want to test it, then the test_my_classes() func
#  will instantiate the classes i've created here and test their output.
# =============================================================================

def test_my_classes():
    """ for testing purposes only """
    ## this is a great place to enter test code of my module that
    ## I don't want to run when I'm actually using the software.
    print("%s is being run as %s" % (__file__, __name__))

## this line forces the programmer no to name his files after
## the __main__ namespace. this can be troublesome when importing
assert os.path.basename(__file__) != '__main__.py'

## every file should have this
if __name__ == "__main__":
    ## this block will run if we are running this as a standalone
    ## god for calling test code like 'main()'
    test_my_classes()
else:
    ## this block will only run if this module is being imported
    ## by another module (usually the __main__ module.
    print("%s is being imported by __main__" % __name__)
