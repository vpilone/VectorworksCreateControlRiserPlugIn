#Created by Vinny Pilone using Vectorworks Dialog Builder Tools
#DRAFT 11/13/22

import _main
import ui.settingsDlg
import vs

# control IDs
ktitle                = 4
kactivateButton       = 1
ksettings             = 8
khowTo                = 6
kquit                 = 2

def CreateDialog():
    # Alignment constants
    kRight                = 1
    kBottom               = 2
    kLeft                 = 3
    kColumn               = 4
    kResize               = 0
    kShift                = 1

    def GetPluginString(ndx):
        # Static Text
        if ndx == 1001:			return 'Create Control Riser Menu'
        elif ndx == 1002:		return 'Quit'
        elif ndx == 1003:		return 'Main Menu'
        elif ndx == 1004:		return 'Create Control Riser'
        elif ndx == 1005:		return 'Run Tool'
        elif ndx == 1006:		return 'How to Use'
        elif ndx == 1007:		return 'Quit'
        elif ndx == 1008:       return 'Settings'
        # Help Text
        elif ndx == 2001:		return 'Accepts the dialog data.'
        elif ndx == 2002:		return 'Cancels the dialog data.'
        elif ndx == 2004:		return 'Help text.'
        elif ndx == 2005:		return 'Help text.'
        elif ndx == 2006:		return 'Help text.'
        elif ndx == 2007:		return 'Help text.'
        elif ndx == 2008:		return 'Help text.'
        return ''

    def GetStr(ndx):
        result = GetPluginString( ndx + 1000 )
        return result

    def GetHelpStr(ndx):
        result = GetPluginString( ndx + 2000 )
        return result

    dialog = vs.CreateLayout( GetStr(3), False, '', '' )

    # create controls
    vs.CreateStaticText( dialog, ktitle, GetStr(ktitle), -1 )
    vs.SetStaticTextStyle( dialog, ktitle, 1 )
    vs.CreatePushButton( dialog, kactivateButton, GetStr(kactivateButton) )
    vs.CreatePushButton( dialog, ksettings, GetStr(ksettings) )
    vs.CreatePushButton( dialog, khowTo, GetStr(khowTo) )
    vs.CreatePushButton( dialog, kquit, GetStr(kquit) )

    # set relations
    vs.SetFirstLayoutItem( dialog, ktitle )
    vs.SetBelowItem( dialog, ktitle, kactivateButton, 0, 0 )
    vs.SetBelowItem( dialog, kactivateButton, ksettings, 0, 0 )
    vs.SetBelowItem( dialog, ksettings, khowTo, 0, 0 )
    vs.SetBelowItem( dialog, khowTo, kquit, 0, 0 )

    # set alignments
    vs.AlignItemEdge( dialog, ktitle, kRight, 1, kResize );
    vs.AlignItemEdge( dialog, kactivateButton, kRight, 1, kResize );
    vs.AlignItemEdge( dialog, ksettings, kRight, 1, kResize );
    vs.AlignItemEdge( dialog, khowTo, kRight, 1, kResize );
    vs.AlignItemEdge( dialog, kquit, kRight, 1, kResize );

    # set help strings
    cnt = 1
    while ( cnt <= 7 ):
        vs.SetHelpText( dialog, cnt, GetHelpStr(cnt) )
        cnt += 1

    return dialog

#Handler for the dialog
def DialogHandler(item, data):
    #Activates the program
    if item == kactivateButton:
        _main.execute()
    #Displays help file in an alert dialog
    elif item == khowTo:
        found, path = vs.FindFileInPluginFolder('InternalREADME.txt')
        if found:
            with open(path + 'InternalREADME.txt') as file:
                lines = ''
                for line in file:
                    lines += format(line)
                vs.AlrtDialog(format(lines))
        else:
            vs.AlrtDialog(format('Help file not found.'))
    #Displays the settings
    elif item == ksettings:
        ui.settingsDlg.isFirstTime = True
        vs.RunLayoutDialog(ui.settingsDlg.CreateDialog(), ui.settingsDlg.DialogHandler)
    #Quit is automatically handled
    return item

# XML defintion of the layout
#
# <BEGIN_XML>
#<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
# <DialogBuilder>
# 
#   <LayoutData>
#     <Name>mainDlg</Name>
#     <Title>Main Menu</Title>
#     <OKText>OK</OKText>
#     <OKHelpText>Accepts the dialog data.</OKHelpText>
#     <CancelText>Cancel</CancelText>
#     <CancelHelpText>Cancels the dialog data.</CancelHelpText>
#     <HasHelp>False</HasHelp>
#     <ResizableWidth>False</ResizableWidth>
#     <ResizableHeight>False</ResizableHeight>
#     <StringsStartID>0</StringsStartID>
#     <HelpStrStartID>1</HelpStrStartID>
#     <TablesAddToDlgRes>True</TablesAddToDlgRes>
#     <AltStringStartID>0</AltStringStartID>
#     <ResourceRoot>PluginModule_resource_file_vwr</ResourceRoot>
#   </LayoutData>
# 
#   <Controls>
#     <Control name="DialogBuilderControl" x="-107" y="69">
#       <Parameter Name="__UUID">{7D9843A7-7237-435D-A27E-3F3F998338C0}</Parameter>
#       <Parameter Name="id">4</Parameter>
#       <Parameter Name="constName">title</Parameter>
#       <Parameter Name="label">Create Control Riser Menu</Parameter>
#       <Parameter Name="staticTextStyle">kBoldStyle</Parameter>
#       <Parameter Name="helpText">Help text.</Parameter>
#       <Parameter Name="alignGroup">1</Parameter>
#       <Parameter Name="bindLeft">kNone</Parameter>
#       <Parameter Name="bindRight">kNone</Parameter>
#       <Parameter Name="bindTop">kNone</Parameter>
#       <Parameter Name="bindBottom">kNone</Parameter>
#       <Parameter Name="realEditType"></Parameter>
#       <Parameter Name="renderMode">Wireframe</Parameter>
#       <Parameter Name="viewMode">Top/Plan</Parameter>
#       <Parameter Name="hasFrame">True</Parameter>
#       <Parameter Name="ControlPoint00X">49mm</Parameter>
#       <Parameter Name="ControlPoint00Y">-2mm</Parameter>
#       <Parameter Name="ControlPoint01X">9mm</Parameter>
#       <Parameter Name="ControlPoint01Y">-12mm</Parameter>
#       <Parameter Name="ControlPoint02X">0mm</Parameter>
#       <Parameter Name="ControlPoint02Y">0mm</Parameter>
#       <Parameter Name="__BottomUUID">{70FE6FDF-2547-4DA1-A198-CA5028E7A6DA}</Parameter>
#       <Parameter Name="__savedHandleRightX">49mm</Parameter>
#       <Parameter Name="__savedHandleRightY">-2mm</Parameter>
#       <Parameter Name="__savedHandleBottomX">9mm</Parameter>
#       <Parameter Name="__savedHandleBottomY">-12mm</Parameter>
#       <Parameter Name="__arrAlignments">1|0|0;</Parameter>
#       <Parameter Name="__fVisControlWidth">49</Parameter>
#       <Parameter Name="__fVisControlHeight">4</Parameter>
#     </Control>
#     <Control name="DialogBuilderControl" x="-107" y="57">
#       <Parameter Name="__UUID">{70FE6FDF-2547-4DA1-A198-CA5028E7A6DA}</Parameter>
#       <Parameter Name="type">kPushButton</Parameter>
#       <Parameter Name="id">5</Parameter>
#       <Parameter Name="constName">activateButton</Parameter>
#       <Parameter Name="label">Run Tool</Parameter>
#       <Parameter Name="helpText">Help text.</Parameter>
#       <Parameter Name="alignGroup">1</Parameter>
#       <Parameter Name="bindLeft">kNone</Parameter>
#       <Parameter Name="bindRight">kNone</Parameter>
#       <Parameter Name="bindTop">kNone</Parameter>
#       <Parameter Name="bindBottom">kNone</Parameter>
#       <Parameter Name="realEditType"></Parameter>
#       <Parameter Name="renderMode">Wireframe</Parameter>
#       <Parameter Name="viewMode">Top/Plan</Parameter>
#       <Parameter Name="hasFrame">True</Parameter>
#       <Parameter Name="ControlPoint00X">17mm</Parameter>
#       <Parameter Name="ControlPoint00Y">-2mm</Parameter>
#       <Parameter Name="ControlPoint01X">12mm</Parameter>
#       <Parameter Name="ControlPoint01Y">-11mm</Parameter>
#       <Parameter Name="ControlPoint02X">0mm</Parameter>
#       <Parameter Name="ControlPoint02Y">0mm</Parameter>
#       <Parameter Name="__BottomUUID">{9C29AE5E-638A-429A-ADBD-AD2B73CD2509}</Parameter>
#       <Parameter Name="__savedHandleRightX">17mm</Parameter>
#       <Parameter Name="__savedHandleRightY">-2mm</Parameter>
#       <Parameter Name="__savedHandleBottomX">12mm</Parameter>
#       <Parameter Name="__savedHandleBottomY">-11mm</Parameter>
#       <Parameter Name="__arrAlignments">1|0|0;</Parameter>
#       <Parameter Name="__fVisControlWidth">17</Parameter>
#       <Parameter Name="__fVisControlHeight">4</Parameter>
#     </Control>
#     <Control name="DialogBuilderControl" x="-107" y="38">
#       <Parameter Name="__UUID">{C49936D7-4E5E-46EF-93D7-D6C6F097788B}</Parameter>
#       <Parameter Name="type">kPushButton</Parameter>
#       <Parameter Name="id">7</Parameter>
#       <Parameter Name="constName">quit</Parameter>
#       <Parameter Name="label">Quit</Parameter>
#       <Parameter Name="helpText">Help text.</Parameter>
#       <Parameter Name="alignGroup">1</Parameter>
#       <Parameter Name="bindLeft">kNone</Parameter>
#       <Parameter Name="bindRight">kNone</Parameter>
#       <Parameter Name="bindTop">kNone</Parameter>
#       <Parameter Name="bindBottom">kNone</Parameter>
#       <Parameter Name="realEditType"></Parameter>
#       <Parameter Name="renderMode">Wireframe</Parameter>
#       <Parameter Name="viewMode">Top/Plan</Parameter>
#       <Parameter Name="hasFrame">True</Parameter>
#       <Parameter Name="ControlPoint00X">10mm</Parameter>
#       <Parameter Name="ControlPoint00Y">-2mm</Parameter>
#       <Parameter Name="ControlPoint01X">5mm</Parameter>
#       <Parameter Name="ControlPoint01Y">-4mm</Parameter>
#       <Parameter Name="ControlPoint02X">0mm</Parameter>
#       <Parameter Name="ControlPoint02Y">0mm</Parameter>
#       <Parameter Name="__savedHandleRightX">10mm</Parameter>
#       <Parameter Name="__savedHandleRightY">-2mm</Parameter>
#       <Parameter Name="__savedHandleBottomX">5mm</Parameter>
#       <Parameter Name="__savedHandleBottomY">-4mm</Parameter>
#       <Parameter Name="__arrAlignments">1|0|0;</Parameter>
#       <Parameter Name="__fVisControlWidth">10</Parameter>
#       <Parameter Name="__fVisControlHeight">4</Parameter>
#     </Control>
#     <Control name="DialogBuilderControl" x="-107" y="46">
#       <Parameter Name="__UUID">{9C29AE5E-638A-429A-ADBD-AD2B73CD2509}</Parameter>
#       <Parameter Name="type">kPushButton</Parameter>
#       <Parameter Name="id">6</Parameter>
#       <Parameter Name="constName">howTo</Parameter>
#       <Parameter Name="label">How to Use</Parameter>
#       <Parameter Name="helpText">Help text.</Parameter>
#       <Parameter Name="alignGroup">1</Parameter>
#       <Parameter Name="bindLeft">kNone</Parameter>
#       <Parameter Name="bindRight">kNone</Parameter>
#       <Parameter Name="bindTop">kNone</Parameter>
#       <Parameter Name="bindBottom">kNone</Parameter>
#       <Parameter Name="realEditType"></Parameter>
#       <Parameter Name="renderMode">Wireframe</Parameter>
#       <Parameter Name="viewMode">Top/Plan</Parameter>
#       <Parameter Name="hasFrame">True</Parameter>
#       <Parameter Name="ControlPoint00X">23mm</Parameter>
#       <Parameter Name="ControlPoint00Y">-2mm</Parameter>
#       <Parameter Name="ControlPoint01X">5mm</Parameter>
#       <Parameter Name="ControlPoint01Y">-8mm</Parameter>
#       <Parameter Name="ControlPoint02X">0mm</Parameter>
#       <Parameter Name="ControlPoint02Y">0mm</Parameter>
#       <Parameter Name="__BottomUUID">{C49936D7-4E5E-46EF-93D7-D6C6F097788B}</Parameter>
#       <Parameter Name="__savedHandleRightX">23mm</Parameter>
#       <Parameter Name="__savedHandleRightY">-2mm</Parameter>
#       <Parameter Name="__savedHandleBottomX">5mm</Parameter>
#       <Parameter Name="__savedHandleBottomY">-8mm</Parameter>
#       <Parameter Name="__arrAlignments">1|0|0;</Parameter>
#       <Parameter Name="__fVisControlWidth">23</Parameter>
#       <Parameter Name="__fVisControlHeight">4</Parameter>
#     </Control>
#     <Control name="Dialog Builder Link" x="0" y="0">
#       <Parameter Name="ParentObj">{7D9843A7-7237-435D-A27E-3F3F998338C0}</Parameter>
#       <Parameter Name="RelatedObj">{70FE6FDF-2547-4DA1-A198-CA5028E7A6DA}</Parameter>
#       <Parameter Name="ParentMode">1</Parameter>
#     </Control>
#     <Control name="Dialog Builder Link" x="0" y="0">
#       <Parameter Name="ParentObj">{9C29AE5E-638A-429A-ADBD-AD2B73CD2509}</Parameter>
#       <Parameter Name="RelatedObj">{C49936D7-4E5E-46EF-93D7-D6C6F097788B}</Parameter>
#       <Parameter Name="ParentMode">1</Parameter>
#     </Control>
#     <Control name="Dialog Builder Link" x="0" y="0">
#       <Parameter Name="ParentObj">{70FE6FDF-2547-4DA1-A198-CA5028E7A6DA}</Parameter>
#       <Parameter Name="RelatedObj">{9C29AE5E-638A-429A-ADBD-AD2B73CD2509}</Parameter>
#       <Parameter Name="ParentMode">1</Parameter>
#     </Control>
#   </Controls>
# 
# </DialogBuilder>
# 
# <END_XML>

