# Created by Vinny Pilone
# DRAFT 11/13/22

import vs
import _main


# Class for other control items
class controlItem:
    name = "name"
    ip = None

    # Constructor requiring name and ip
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip

    # Method to draw each item using xPos, yPos, boxWidth, boxHeight, and lineColor
    def drawControlItem(self, xPos, yPos, boxWidth, boxHeight, lineColor):
        boxWidth *= 5 / 3
        boxHeight *= 2
        vs.MoveTo(xPos, yPos)
        vs.RectangleN(xPos, yPos, 10, 0, boxWidth, -boxHeight)

        # Has version for an included IP and no IP
        if self.ip != None:
            vs.MoveTo(xPos, yPos - (boxHeight / 3))
            vs.CreateText(self.name)
            vs.SetTextStyle(vs.LNewObj(), 0, len(self.name), 1)
            _main.centerObjX(vs.LNewObj(), boxWidth, xPos)

            vs.MoveTo(xPos, yPos - (boxHeight * 2 / 3))
            vs.CreateText("IP: " + self.ip)
            _main.centerObjX(vs.LNewObj(), boxWidth, xPos)

        else:
            vs.MoveTo(xPos, yPos - (boxHeight / 2))
            vs.CreateText(self.name)
            vs.SetTextStyle(vs.LNewObj(), 0, len(self.name), 1)
            _main.centerObjX(vs.LNewObj(), boxWidth, xPos)

        vs.MoveTo(xPos + boxWidth / 2, yPos - boxHeight)
        vs.PenSize(21)
        vs.LineTo(xPos + boxWidth / 2, yPos - boxHeight * 3 / 2)
        vs.SetPenFore(vs.LNewObj(), lineColor)
