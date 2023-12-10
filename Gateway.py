# Created by Vinny Pilone
# DRAFT 11/13/22

import _main
import vs


# Class for gateways
class gateway:
    _name = "NAME"
    _ip = ""
    _universeList = []

    # Constructor requiring name, ip and universe
    def __init__(self, name, ip, universes):
        self._name = name
        self._ip = ip
        self._universeList = universes

    def getName(self):
        return self._name

    def getIP(self):
        return self._ip

    def getUniverseList(self):
        return self._universeList

    # Method to draw the gateways using xPos, yPos, boxWidth, boxHeight and lineColor
    def drawGateway(self, xPos, yPos, boxWidth, boxHeight, lineColor):
        boxWidth *= 1.5
        boxHeight *= 5 / 3
        vs.MoveTo(xPos, yPos)
        vs.RectangleN(xPos, yPos, 10, 0, boxWidth, -boxHeight)

        vs.MoveTo(xPos, yPos - (boxHeight / 5))
        vs.CreateText(self._name)
        vs.SetTextStyle(vs.LNewObj(), 0, len(self._name), 1)
        _main.centerObjX(vs.LNewObj(), boxWidth, xPos)

        vs.MoveTo(xPos, yPos - (boxHeight * 0.5))
        vs.CreateText("IP: " + self._ip)
        _main.centerObjX(vs.LNewObj(), boxWidth, xPos)

        # Top(1/4) Mid (0.6) Bottom (7/8)
        vs.MoveTo(xPos, yPos)
        counter = 0
        group = vs.BeginGroupN(None)
        for universe in self._universeList:
            vs.MoveTo(
                xPos + ((boxWidth / (len(self._universeList) + 1)) * counter),
                yPos - (boxHeight * 5 / 6),
            )
            vs.CreateText(format(counter + 1) + " - " + format(universe))
            counter += 1
        vs.EndGroup()
        _main.centerObjX(group, boxWidth, xPos)
        vs.HUngroup(group)
        vs.MoveTo(xPos, yPos)
        counter = 0
        group = vs.BeginGroupN(None)
        for universe in self._universeList:
            vs.MoveTo(
                xPos + ((boxWidth / (len(self._universeList) + 1)) * counter),
                yPos - (boxHeight),
            )
            vs.PenSize(21)
            vs.LineTo(
                xPos + ((boxWidth / (len(self._universeList) + 1)) * counter),
                yPos - boxHeight * 3 / 2,
            )
            vs.SetPenFore(vs.LNewObj(), lineColor)
            counter += 1
        vs.EndGroup()
        _main.centerObjX(group, boxWidth, xPos)
        vs.HUngroup(group)
