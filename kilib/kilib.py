#!/usr/bin/env python2
from datetime import datetime
import json
import sys



class Header:
    @staticmethod
    def HeadString():
        return """EESchema-LIBRARY Version 2.3 Date: %s
#encoding utf-8
""" % datetime.now().strftime("%d/%m/%Y %X")

    @staticmethod
    def TailString():
        return "#End Library\n"


class Symbol:
    def __init__(self, prop_dict):
        self.name = prop_dict["name"]
        self.ref  =  prop_dict["ref"] if ("ref" in prop_dict) else "U"
        self.pinoff  =  prop_dict["pinoff"] if ("pinoff" in prop_dict) else 40
        self.show_pnum  =  prop_dict["show_pnum"] if ("show_pnum" in prop_dict) else "Y"
        self.show_pname  =  prop_dict["show_pname"] if ("show_pname" in prop_dict) else "Y"
        self.parts  =  prop_dict["parts"] if ("parts" in prop_dict) else 1
        self.locked  =  prop_dict["locked"] if ("locked" in prop_dict) else "F"
        self.isPower  =  prop_dict["isPower"] if ("isPower" in prop_dict) else "N"
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
""" % ( self.pins[i][0], i, p[0], p[1], p[2], p[3], 1, 1, self.pins[i][1] )
        return s

    def AllString(self):
        s = self.DEFString()
        s += self.FNString()
        s += "DRAW\n"
        s += self.PINString()
        s += "ENDDRAW\nENDDEF\n"
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
            x = -1
            o = 'R'
        else :
            y = nth - self.base - 1
            x = 1
            o = 'L'
        return [self.width/2 * x, self.base_y + self.hgap * y, self.size, o]

    def getRect(self):
        x = self.width/2 - 300
        y = abs(self.base_y)  + 200
        return [-x, -y, x, y]

def SymFromJson(jstr):
    js = json.loads(jstr)
    rs  = []
    for j in js:
        s = Symbol(j)
        s.setPins(j["pins"])
        rs.append(s)
    return rs


if __name__ == "__main__":
    print Header.HeadString()
    for s in SymFromJson(sys.stdin.read()):
        print s.AllString()
    print Header.TailString()

