# Created by Vinny Pilone
# DRAFT 11/13/22

import vs
import ui.gatewayDlg
import ui.settingsDlg
import ui.otherDlg
import ui.mainDlg
import Gateway
import OtherSystems

# Adjustable Vars (in inches)
includeUni1 = True
initialX = 0
initialY = 0
columnLimit = 12
boxWidth = 72
lineColor = (56797, 7453, 7453)


# Called method to open the main dialog
def runProgram():
    vs.RunLayoutDialog(ui.mainDlg.CreateDialog(), ui.mainDlg.DialogHandler)


# Run Program
def execute():
    # Constructor
    universe = 0
    counter = 0
    boxHeight = boxWidth / 3
    universeSeperation = boxWidth / 2
    boxSeperation = boxHeight / 2
    xPos = initialX
    yPos = initialY
    vs.MoveTo(xPos, yPos)
    vs.TextFont(vs.GetFontID("Trebuchet MS"))
    vs.TextSize(boxWidth * 14 / 3)
    typeIndex = -1
    unitIndex = -1
    channelIndex = -1
    addressIndex = -1
    groupRef = None
    gatewayList = []
    gatewayCounter = 1
    otherItem = None

    # Loop to Create Gateways
    if vs.YNDialog("Would you like to add gateways?"):
        vs.TextSize(boxWidth * 24 / 3)
        numGateways = vs.IntDialog("How many gateways would you like to add?", 0)
        # Asks for gateway info and adds them to Gateway List
        while numGateways >= gatewayCounter:
            dialog = ui.gatewayDlg.CreateDialog(gatewayCounter)
            if (
                vs.RunLayoutDialog(dialog, ui.gatewayDlg.DialogHandler)
                == ui.gatewayDlg.kOK
            ):
                gatewayList.append(
                    Gateway.gateway(
                        ui.gatewayDlg.nameData,
                        ui.gatewayDlg.ipData,
                        ui.gatewayDlg.universeData.strip().split(","),
                    )
                )
            gatewayCounter += 1
        # Draws each gateway
        gatewayCounter = 0
        while gatewayCounter < numGateways:
            gatewayList[gatewayCounter].drawGateway(
                xPos, yPos, boxWidth, boxHeight, lineColor
            )
            xPos += boxWidth * 1.5 + universeSeperation * 1.5
            gatewayCounter += 1

    # Read and draw fixtures from csv file
    yPos += -(boxHeight * 2.5)
    xPos = initialX - (boxWidth + universeSeperation)
    if vs.YNDialog("Would you like to add fixtures?"):
        vs.TextSize(boxWidth * 14 / 3)
        vs.AlrtDialog("Please select your .csv file.")
        found, filePath = vs.GetFileN("Select your CSV file", "/", "")
        if found:
            vs.AlrtDialog("You selected " + filePath)
            # Reads in first lines, then finds appropriate data fields
            with open(filePath, encoding="utf8") as csvDoc:
                for line in csvDoc:
                    line = line.strip()
                    tempList = line.split(",")
                    listCounter = 0
                    for item in tempList:
                        if item == "Instrument Type":
                            typeIndex = listCounter
                        elif item == "Unit#":
                            unitIndex = listCounter
                        elif item == "Channel":
                            channelIndex = listCounter
                        elif item == "Address":
                            addressIndex = listCounter
                        listCounter += 1
                    if (
                        typeIndex
                        == -1 | unitIndex
                        == -1 | channelIndex
                        == -1 | addressIndex
                        == -1
                    ):
                        vs.AlrtDialog("Invalid file, please try again.")
                        exit()
                    break
                # Draws a fixture for each unique intrument line in the csv file
                for line in csvDoc:
                    line = line.strip()
                    data = line.split(",")
                    nextUniverse = (data[3].split("/"))[0]
                    if nextUniverse.isnumeric() == False:
                        continue
                    if universe != nextUniverse:
                        counter = 0
                        xPos += boxWidth + universeSeperation
                        yPos = initialY - (boxHeight * 4)
                        universe = nextUniverse
                        if universe != "-":
                            vs.MoveTo(xPos + boxWidth / 2, yPos + boxSeperation)
                            vs.PenSize(21)
                            vs.LineTo(xPos + boxWidth / 2, yPos + boxSeperation * 2)
                            vs.SetPenFore(vs.LNewObj(), lineColor)
                    elif counter >= columnLimit:
                        counter = 0
                        xPos += boxWidth + boxSeperation
                        yPos = initialY - (boxHeight * 4)
                        if universe != "-":
                            vs.PenSize(21)
                            vs.MoveTo(xPos + boxWidth / 2, yPos + boxSeperation)
                            vs.LineTo(
                                xPos - (boxWidth / 2 + boxSeperation),
                                yPos + boxSeperation,
                            )
                            vs.SetPenFore(vs.LNewObj(), lineColor)

                    # Replace Common Long Light Names
                    data[typeIndex] = data[typeIndex].replace(
                        "ETC ColorSource", "C.S.", 1
                    )
                    data[typeIndex] = data[typeIndex].replace("High End", "H.E.", 1)

                    if universe != "-":
                        vs.MoveTo(xPos + boxWidth / 2, yPos)
                        vs.PenSize(21)
                        vs.LineTo(xPos + boxWidth / 2, yPos + boxSeperation)
                        vs.SetPenFore(vs.LNewObj(), lineColor)

                    vs.PenSize(13)

                    vs.RectangleN(xPos, yPos, 10, 0, boxWidth, -boxHeight)

                    vs.MoveTo(xPos, yPos - (boxHeight / 3))
                    vs.CreateText(data[typeIndex])
                    vs.SetTextStyle(vs.LNewObj(), 0, len(data[typeIndex]), 1)
                    centerObjX(vs.LNewObj(), boxWidth, xPos)

                    groupRef = vs.BeginGroupN(None)
                    vs.MoveTo(xPos, yPos - (boxHeight * 3 / 4))
                    vs.CreateText("U#: " + data[unitIndex])

                    vs.MoveTo(xPos + (boxWidth / 4), yPos - (boxHeight * 3 / 4))
                    vs.CreateText("C: " + data[channelIndex])

                    vs.MoveTo(xPos + (boxWidth * 1 / 2), yPos - (boxHeight * 3 / 4))
                    vs.CreateText("A: " + data[addressIndex])
                    vs.EndGroup()

                    centerObjX(groupRef, boxWidth, xPos)
                    vs.HUngroup(groupRef)

                    yPos += -(boxHeight + boxSeperation)
                    counter += 1

    yPos = initialY + (boxHeight * 21 / 6)
    xPos = initialX

    # Loops asking for a name and IP of any other items and draws them until the user selects done
    if vs.YNDialog("Would you like to add any other items?"):
        vs.TextSize(boxWidth * 10)
        while True:
            dialog = ui.otherDlg.CreateDialog()
            if vs.RunLayoutDialog(dialog, ui.otherDlg.DialogHandler) == ui.otherDlg.kOK:
                if ui.otherDlg.ipData == "":
                    if ui.otherDlg.nameData == "":
                        continue
                    else:
                        otherItem = OtherSystems.controlItem(ui.otherDlg.nameData, None)
                else:
                    otherItem = OtherSystems.controlItem(
                        ui.otherDlg.nameData, ui.otherDlg.ipData
                    )
                otherItem.drawControlItem(xPos, yPos, boxWidth, boxHeight, lineColor)
                xPos += boxWidth * 5 / 3 + universeSeperation * 5 / 3
            else:
                break


# method to center an object horizontally in a box
def centerObjX(object, boxWidth, xPos):
    vs.HMove(object, (abs(boxWidth / 2 - abs(vs.HCenter(object)[0] - xPos))), 0)
