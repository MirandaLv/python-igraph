import unittest
from igraph.test import basic, games, foreign, structural, flow
from igraph import *

def suite():
    return unittest.TestSuite( \
        [basic.suite(),
	 games.suite(),
	 foreign.suite(),
	 structural.suite(),
	 flow.suite()] \
    )
    
def test():
    runner = unittest.TextTestRunner()
    runner.run(suite())
    
