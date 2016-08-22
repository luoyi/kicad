#!/usr/bin/env python2

import unittest
from kilib import DIPPin

class TestDIPPin(unittest.TestCase):
    def test_base(self):
	dip = DIPPin(8)
        self.assertEqual(dip.base, 4);
        self.assertEqual(dip.base_y, -150);

	dip = DIPPin(7)
        self.assertEqual(dip.base, 4);
        self.assertEqual(dip.base_y, -150);

	dip = DIPPin(4)
        self.assertEqual(dip.base, 2);
        self.assertEqual(dip.base_y, -50);
        
	dip = DIPPin(5)
        self.assertEqual(dip.base, 3);
        self.assertEqual(dip.base_y, -100);

    def test_coord(self):
        dip = DIPPin(8)
        self.assertEqual(dip.getCoord(1), [750, 150, 300, 'R'])
        self.assertEqual(dip.getCoord(2), [750, 50, 300, 'R'])
        self.assertEqual(dip.getCoord(3), [750, -50, 300, 'R'])
        self.assertEqual(dip.getCoord(4), [750, -150, 300, 'R'])
        self.assertEqual(dip.getCoord(5), [-750, -150, 300, 'L'])
        self.assertEqual(dip.getCoord(6), [-750, -50, 300, 'L'])
        self.assertEqual(dip.getCoord(7), [-750, 50, 300, 'L'])
        self.assertEqual(dip.getCoord(8), [-750, 150, 300, 'L'])

        dip = DIPPin(7)
        self.assertEqual(dip.getCoord(1), [750, 150, 300, 'R'])
        self.assertEqual(dip.getCoord(2), [750, 50, 300, 'R'])
        self.assertEqual(dip.getCoord(3), [750, -50, 300, 'R'])
        self.assertEqual(dip.getCoord(4), [750, -150, 300, 'R'])
        self.assertEqual(dip.getCoord(5), [-750, -150, 300, 'L'])
        self.assertEqual(dip.getCoord(6), [-750, -50, 300, 'L'])
        self.assertEqual(dip.getCoord(7), [-750, 50, 300, 'L'])

        dip = DIPPin(4)
        self.assertEqual(dip.getCoord(1), [750, 50, 300, 'R'])
        self.assertEqual(dip.getCoord(2), [750, -50, 300, 'R'])
        self.assertEqual(dip.getCoord(3), [-750, -50, 300, 'L'])
        self.assertEqual(dip.getCoord(4), [-750, 50, 300, 'L'])

unittest.main()  
