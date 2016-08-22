#!/usr/bin/env python2
from datetime import datetime



class Header:
    @staticmethod
    def toString():
        return """EESchema-LIBRARY Version 2.3 Date: %s
#encoding utf-8
""" % datetime.now().strftime("%d/%m/%Y %X")


class Symbols:
    def __init__(self, name, ref="U", pinoff = 40, show_pnum = 'Y', show_pname = 'Y', parts = 1,  locked = 'F', isPower = 'N' ):
        self.name = name
        self.ref  = ref
        self.pinoff = pinoff
        self.show_pnum = show_pnum
        self.show_pname = show_pname
        self.parts = parts
        self.locked = locked
        self.isPower = isPower
        self.setDefault()

    def setDefault(self):
        self.ref_hv = 'H'
        self.ref_iv = 'V'
        self.ref_hctrlb = 'C'
        self.ref_vctrlb = 'C'
        self.ref_in = 'N'
        self.ref_bn = 'N'
        self.ref_x = 0
        self.ref_y = -150
        self.ref_size = 60

        self.name_hv = 'H'
        self.name_iv = 'V'
        self.name_hctrlb = 'C'
        self.name_vctrlb = 'C'
        self.name_in = 'N'
        self.name_bn = 'N'
        self.name_x = 0
        self.name_y = 150
        self.name_size = 60

    def DEFString(self):
        return """\
DEF %s %s 0 %d %s %s %d %s %s
""" % (self.name, self.ref, self.pinoff, self.show_pnum, self.show_pname, self.parts, self.locked, self.isPower)
    
    def FNString(self):
        return """\
F0 "%s" %d %d %d %s %s %s %s%s%s
F1 "%s" %d %d %d %s %s %s %s%s%s
F2 "" 0 0 50 H I C C
F3 "" 0 0 50 H I C C
""" % ( self.ref, self.ref_x, self.ref_y, self.ref_size, self.ref_hv, self.ref_iv, self.ref_hctrlb, self.ref_vctrlb, self.ref_in, self.ref_bn, \
        self.name, self.name_x, self.name_y, self.name_size, self.name_hv, self.name_iv, self.name_hctrlb, self.name_vctrlb, self.name_in, self.name_bn \
       )
    
    def setPins(self, pins):
        self.pins = pins;
        self.pin_obj = DIPPin(len(pins))

    def PINString(self):
        p = self.pin_obj.getRect()
        s = """S %d %d %d %d 1 0 0 N\n""" % ( p[0], p[1], p[2], p[3] )
        for i in range(len(self.pins)) :
            p = self.pin_obj.getCoord(i+1)
            s += """\
X %s %d %d %d %d %s 50 50 %d %d %s
""" % ( self.pins[i][0], i, p[0], p[1], p[2], p[3], 50, 50, self.pins[i][1] )
        return s

class DIPPin():
    def __init__(self, num, size = 300):
        self.num = num
        self.width = 1500
        self.hgap = 100
        self.size = size
        self.base = ( num + 1 ) / 2
        self.base_y = ( ( self.base - 1 ) * self.hgap * - 1 ) / 2


    def getCoord(self, nth):
        if nth <= self.base :
            y = self.base - nth
            x = 1
            o = 'R'
        else :
            y = nth - self.base - 1
            x = -1
            o = 'L'
        return [self.width/2 * x, self.base_y + self.hgap * y, self.size, o]

    def getRect(self):
        x = self.width/2 - 300
        y = abs(self.base_y)  + 200
        return [-x, -y, x, y]



if __name__ == "__main__":
    print Header.toString()
    s = Symbols("ABC")
    print s.DEFString()
    print s.FNString()
    pins = [['VIN', 'W'], ['PPR', 'O'], ['CHG', 'O'], ['EN', 'I'], ['GND', 'W'], ['FAST', 'O'], ['ISET', 'O'], ['BAT', 'O']]
    s.setPins(pins)
    print s.PINString()

