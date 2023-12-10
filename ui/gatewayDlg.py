#Created by Vinny Pilone using Vectorworks Dialog Builder Tools
#DRAFT 11/13/22

import vs

# control IDs
kOK                   = 1
kCancel               = 2
ktitle                = 4
knameText             = 5
kname                 = 6
kipText               = 7
kip                   = 8
kuniText              = 9
kuniverses            = 10

dialog = None
nameData = None
ipData = None
universeData = None

def CreateDialog(gatewayNum):
    # Alignment constants
    kRight                = 1
    kBottom               = 2
    kLeft                 = 3
    kColumn               = 4
    kResize               = 0
    kShift                = 1

    def GetPluginString(ndx):
        # Static Text
        if ndx == 1001:			return 'OK'
        elif ndx == 1002:		return 'Cancel'
        elif ndx == 1003:		return 'Dialog'
        elif ndx == 1004:		return 'Gateway ' + format(gatewayNum) + ' Information'
        elif ndx == 1005:		return 'Name:'
        elif ndx == 1006:		return ''
        elif ndx == 1007:		return 'IP:'
        elif ndx == 1008:		return ''
        elif ndx == 1009:		return 'Enter universes seperated by a comma:'
        elif ndx == 1010:		return ''
        # Help Text
        elif ndx == 2001:		return 'Accepts the dialog data.'
        elif ndx == 2002:		return 'Cancels the dialog data.'
        elif ndx == 2004:		return 'Help text.'
        elif ndx == 2005:		return 'Help text.'
        elif ndx == 2006:		return 'Help text.'
        elif ndx == 2007:		return 'Help text.'
        elif ndx == 2008:		return 'Help text.'
        elif ndx == 2009:		return 'Help text.'
        elif ndx == 2010:		return ''
        return ''

    def GetStr(ndx):
        result = GetPluginString( ndx + 1000 )
        return result

    def GetHelpStr(ndx):
        result = GetPluginString( ndx + 2000 )
        return result

    global dialog
    dialog = vs.CreateLayout( GetStr(3), True, GetStr(kOK), GetStr(kCancel) )

    # create controls
    vs.CreateStaticText( dialog, ktitle, GetStr(ktitle), -1 )
    vs.SetStaticTextStyle( dialog, ktitle, 1 )
    vs.CreateStaticText( dialog, knameText, GetStr(knameText), -1 )
    vs.CreateEditText( dialog, kname, GetStr(kname), 32 )
    vs.CreateStaticText( dialog, kipText, GetStr(kipText), -1 )
    vs.CreateEditText( dialog, kip, GetStr(kip), 32 )
    vs.CreateStaticText( dialog, kuniText, GetStr(kuniText), -1 )
    vs.CreateEditText( dialog, kuniverses, GetStr(kuniverses), 32 )

    # set relations
    vs.SetFirstLayoutItem( dialog, ktitle )
    vs.SetBelowItem( dialog, ktitle, knameText, 0, 0 )
    vs.SetRightItem( dialog, knameText, kname, 0, 0 )
    vs.SetBelowItem( dialog, knameText, kipText, 0, 0 )
    vs.SetRightItem( dialog, kipText, kip, 0, 0 )
    vs.SetBelowItem( dialog, kipText, kuniText, 0, 0 )
    vs.SetBelowItem( dialog, kuniText, kuniverses, 2, 0 )

    # set alignments
    vs.AlignItemEdge( dialog, ktitle, kRight, 4, kResize )
    vs.AlignItemEdge( dialog, knameText, kLeft, 4, kShift )

    # set help strings
    cnt = 1
    while ( cnt <= 10 ):
        vs.SetHelpText( dialog, cnt, GetHelpStr(cnt) )
        cnt += 1

    return dialog

#Handler for dialog
def DialogHandler (item, data):
    #Accepts gateways data if provided
    if item == kOK:
        global nameData
        global ipData
        global universeData
        global dialog
        nameData = vs.GetItemText( dialog, kname)
        ipData = vs.GetItemText( dialog, kip)
        universeData = vs.GetItemText( dialog, kuniverses)
    return item

# XML defintion of the layout
#
# <BEGIN_XML>
#<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
# <DialogBuilder>
# 
#   <LayoutData>
#     <Name>dlg</Name>
#     <Title>Dialog</Title>
#     <OKText>OK</OKText>
#     <OKHelpText>Accepts the dialog data.</OKHelpText>
#     <CancelText>Cancel</CancelText>
#     <CancelHelpText>Cancels the dialog data.</CancelHelpText>
#     <ResizableWidth>False</ResizableWidth>
#     <ResizableHeight>False</ResizableHeight>
#     <StringsStartID>0</StringsStartID>
#     <HelpStrStartID>0</HelpStrStartID>
#     <TablesAddToDlgRes>True</TablesAddToDlgRes>
#     <AltStringStartID>0</AltStringStartID>
#     <ResourceRoot>PluginModule_resource_file_vwr</ResourceRoot>
#   </LayoutData>
# 
#   <Controls>
#     <Control name="DialogBuilderControl" x="0" y="-14">
#       <Parameter Name="__UUID">{53E9AFC2-C8A0-4624-909D-63C315554079}</Parameter>
#       <Parameter Name="id">5</Parameter>
#       <Parameter Name="constName">nameText</Parameter>
#       <Parameter Name="label">Name:</Parameter>
#       <Parameter Name="helpText">Help text.</Parameter>
#       <Parameter Name="alignGroup">4</Parameter>
#       <Parameter Name="alignEdge">kLeft</Parameter>
#       <Parameter Name="alignMode">kShift</Parameter>
#       <Parameter Name="bindLeft">kNone</Parameter>
#       <Parameter Name="bindRight">kNone</Parameter>
#       <Parameter Name="bindTop">kNone</Parameter>
#       <Parameter Name="bindBottom">kNone</Parameter>
#       <Parameter Name="realEditType"></Parameter>
#       <Parameter Name="renderMode">Wireframe</Parameter>
#       <Parameter Name="viewMode">Top/Plan</Parameter>
#       <Parameter Name="hasFrame">True</Parameter>
#       <Parameter Name="ControlPoint00X">22mm</Parameter>
#       <Parameter Name="ControlPoint00Y">-2mm</Parameter>
#       <Parameter Name="ControlPoint01X">3mm</Parameter>
#       <Parameter Name="ControlPoint01Y">-14mm</Parameter>
#       <Parameter Name="ControlPoint02X">0mm</Parameter>
#       <Parameter Name="ControlPoint02Y">0mm</Parameter>
#       <Parameter Name="__RightUUID">{BD9BC4C6-A5C9-4E8D-BDCF-65E2DEC57BA7}</Parameter>
#       <Parameter Name="__BottomUUID">{1D50958B-A87E-45C3-AAC4-FC5DE4848B2D}</Parameter>
#       <Parameter Name="__savedHandleRightX">22mm</Parameter>
#       <Parameter Name="__savedHandleRightY">-2mm</Parameter>
#       <Parameter Name="__savedHandleBottomX">3mm</Parameter>
#       <Parameter Name="__savedHandleBottomY">-14mm</Parameter>
#       <Parameter Name="__arrAlignments">4|2|1;</Parameter>
#       <Parameter Name="__fVisControlWidth">12</Parameter>
#       <Parameter Name="__fVisControlHeight">4</Parameter>
#     </Control>
#     <Control name="DialogBuilderControl" x="22" y="-14">
#       <Parameter Name="__UUID">{BD9BC4C6-A5C9-4E8D-BDCF-65E2DEC57BA7}</Parameter>
#       <Parameter Name="type">kEditTextBox</Parameter>
#       <Parameter Name="id">6</Parameter>
#       <Parameter Name="constName">name</Parameter>
#       <Parameter Name="helpText">Help text.</Parameter>
#       <Parameter Name="bindLeft">kNone</Parameter>
#       <Parameter Name="bindRight">kNone</Parameter>
#       <Parameter Name="bindTop">kNone</Parameter>
#       <Parameter Name="bindBottom">kNone</Parameter>
#       <Parameter Name="ctrlWidth">32</Parameter>
#       <Parameter Name="realEditType"></Parameter>
#       <Parameter Name="renderMode">Wireframe</Parameter>
#       <Parameter Name="viewMode">Top/Plan</Parameter>
#       <Parameter Name="hasFrame">True</Parameter>
#       <Parameter Name="ControlPoint00X">24mm</Parameter>
#       <Parameter Name="ControlPoint00Y">-2mm</Parameter>
#       <Parameter Name="ControlPoint01X">12mm</Parameter>
#       <Parameter Name="ControlPoint01Y">-4mm</Parameter>
#       <Parameter Name="ControlPoint02X">0mm</Parameter>
#       <Parameter Name="ControlPoint02Y">0mm</Parameter>
#       <Parameter Name="__savedHandleRightX">24mm</Parameter>
#       <Parameter Name="__savedHandleRightY">-2mm</Parameter>
#       <Parameter Name="__savedHandleBottomX">12mm</Parameter>
#       <Parameter Name="__savedHandleBottomY">-4mm</Parameter>
#       <Parameter Name="__fVisControlWidth">24</Parameter>
#       <Parameter Name="__fVisControlHeight">4</Parameter>
#     </Control>
#     <Control name="DialogBuilderControl" x="0" y="-28">
#       <Parameter Name="__UUID">{1D50958B-A87E-45C3-AAC4-FC5DE4848B2D}</Parameter>
#       <Parameter Name="id">7</Parameter>
#       <Parameter Name="constName">ipText</Parameter>
#       <Parameter Name="label">IP:</Parameter>
#       <Parameter Name="helpText">Help text.</Parameter>
#       <Parameter Name="bindLeft">kNone</Parameter>
#       <Parameter Name="bindRight">kNone</Parameter>
#       <Parameter Name="bindTop">kNone</Parameter>
#       <Parameter Name="bindBottom">kNone</Parameter>
#       <Parameter Name="realEditType"></Parameter>
#       <Parameter Name="renderMode">Wireframe</Parameter>
#       <Parameter Name="viewMode">Top/Plan</Parameter>
#       <Parameter Name="hasFrame">True</Parameter>
#       <Parameter Name="ControlPoint00X">15mm</Parameter>
#       <Parameter Name="ControlPoint00Y">-2mm</Parameter>
#       <Parameter Name="ControlPoint01X">37mm</Parameter>
#       <Parameter Name="ControlPoint01Y">-14mm</Parameter>
#       <Parameter Name="ControlPoint02X">0mm</Parameter>
#       <Parameter Name="ControlPoint02Y">0mm</Parameter>
#       <Parameter Name="__RightUUID">{28D1FF6D-5920-41BF-989C-D08B83C62E21}</Parameter>
#       <Parameter Name="__BottomUUID">{7010B845-46AE-4C76-A978-DD10974AAAAE}</Parameter>
#       <Parameter Name="__savedHandleRightX">15mm</Parameter>
#       <Parameter Name="__savedHandleRightY">-2mm</Parameter>
#       <Parameter Name="__savedHandleBottomX">37mm</Parameter>
#       <Parameter Name="__savedHandleBottomY">-14mm</Parameter>
#       <Parameter Name="__fVisControlWidth">5</Parameter>
#       <Parameter Name="__fVisControlHeight">4</Parameter>
#     </Control>
#     <Control name="DialogBuilderControl" x="15" y="-28">
#       <Parameter Name="__UUID">{28D1FF6D-5920-41BF-989C-D08B83C62E21}</Parameter>
#       <Parameter Name="type">kEditTextBox</Parameter>
#       <Parameter Name="id">8</Parameter>
#       <Parameter Name="constName">ip</Parameter>
#       <Parameter Name="helpText">Help text.</Parameter>
#       <Parameter Name="bindLeft">kNone</Parameter>
#       <Parameter Name="bindRight">kNone</Parameter>
#       <Parameter Name="bindTop">kNone</Parameter>
#       <Parameter Name="bindBottom">kNone</Parameter>
#       <Parameter Name="ctrlWidth">32</Parameter>
#       <Parameter Name="realEditType"></Parameter>
#       <Parameter Name="renderMode">Wireframe</Parameter>
#       <Parameter Name="viewMode">Top/Plan</Parameter>
#       <Parameter Name="hasFrame">True</Parameter>
#       <Parameter Name="ControlPoint00X">24mm</Parameter>
#       <Parameter Name="ControlPoint00Y">-2mm</Parameter>
#       <Parameter Name="ControlPoint01X">12mm</Parameter>
#       <Parameter Name="ControlPoint01Y">-4mm</Parameter>
#       <Parameter Name="ControlPoint02X">0mm</Parameter>
#       <Parameter Name="ControlPoint02Y">0mm</Parameter>
#       <Parameter Name="__savedHandleRightX">24mm</Parameter>
#       <Parameter Name="__savedHandleRightY">-2mm</Parameter>
#       <Parameter Name="__savedHandleBottomX">12mm</Parameter>
#       <Parameter Name="__savedHandleBottomY">-4mm</Parameter>
#       <Parameter Name="__fVisControlWidth">24</Parameter>
#       <Parameter Name="__fVisControlHeight">4</Parameter>
#     </Control>
#     <Control name="DialogBuilderControl" x="0" y="-42">
#       <Parameter Name="__UUID">{7010B845-46AE-4C76-A978-DD10974AAAAE}</Parameter>
#       <Parameter Name="id">9</Parameter>
#       <Parameter Name="constName">uniText</Parameter>
#       <Parameter Name="label">Enter universes seperated by a comma:</Parameter>
#       <Parameter Name="helpText">Help text.</Parameter>
#       <Parameter Name="bindLeft">kNone</Parameter>
#       <Parameter Name="bindRight">kNone</Parameter>
#       <Parameter Name="bindTop">kNone</Parameter>
#       <Parameter Name="bindBottom">kNone</Parameter>
#       <Parameter Name="realEditType"></Parameter>
#       <Parameter Name="renderMode">Wireframe</Parameter>
#       <Parameter Name="viewMode">Top/Plan</Parameter>
#       <Parameter Name="hasFrame">True</Parameter>
#       <Parameter Name="ControlPoint00X">74mm</Parameter>
#       <Parameter Name="ControlPoint00Y">-2mm</Parameter>
#       <Parameter Name="ControlPoint01X">12mm</Parameter>
#       <Parameter Name="ControlPoint01Y">-14mm</Parameter>
#       <Parameter Name="ControlPoint02X">0mm</Parameter>
#       <Parameter Name="ControlPoint02Y">0mm</Parameter>
#       <Parameter Name="__BottomUUID">{4E6329B9-62EA-459F-BAA7-D5308E666F2B}</Parameter>
#       <Parameter Name="__savedHandleRightX">74mm</Parameter>
#       <Parameter Name="__savedHandleRightY">-2mm</Parameter>
#       <Parameter Name="__savedHandleBottomX">12mm</Parameter>
#       <Parameter Name="__savedHandleBottomY">-14mm</Parameter>
#       <Parameter Name="__fVisControlWidth">74</Parameter>
#       <Parameter Name="__fVisControlHeight">4</Parameter>
#     </Control>
#     <Control name="Dialog Builder Link" x="0" y="0">
#       <Parameter Name="ParentObj">{53E9AFC2-C8A0-4624-909D-63C315554079}</Parameter>
#       <Parameter Name="RelatedObj">{BD9BC4C6-A5C9-4E8D-BDCF-65E2DEC57BA7}</Parameter>
#       <Parameter Name="ParentMode">0</Parameter>
#     </Control>
#     <Control name="Dialog Builder Link" x="0" y="0">
#       <Parameter Name="ParentObj">{53E9AFC2-C8A0-4624-909D-63C315554079}</Parameter>
#       <Parameter Name="RelatedObj">{1D50958B-A87E-45C3-AAC4-FC5DE4848B2D}</Parameter>
#       <Parameter Name="ParentMode">1</Parameter>
#     </Control>
#     <Control name="Dialog Builder Link" x="0" y="0">
#       <Parameter Name="ParentObj">{1D50958B-A87E-45C3-AAC4-FC5DE4848B2D}</Parameter>
#       <Parameter Name="RelatedObj">{7010B845-46AE-4C76-A978-DD10974AAAAE}</Parameter>
#       <Parameter Name="ParentMode">1</Parameter>
#     </Control>
#     <Control name="DialogBuilderControl" x="0" y="0">
#       <Parameter Name="__UUID">{831ABAE6-6E6A-47C4-BAE7-CF9BE5A2F176}</Parameter>
#       <Parameter Name="id">4</Parameter>
#       <Parameter Name="constName">title</Parameter>
#       <Parameter Name="label">Gateway X Information</Parameter>
#       <Parameter Name="staticTextStyle">kBoldStyle</Parameter>
#       <Parameter Name="helpText">Help text.</Parameter>
#       <Parameter Name="alignGroup">4</Parameter>
#       <Parameter Name="bindLeft">kNone</Parameter>
#       <Parameter Name="bindRight">kNone</Parameter>
#       <Parameter Name="bindTop">kNone</Parameter>
#       <Parameter Name="bindBottom">kNone</Parameter>
#       <Parameter Name="realEditType"></Parameter>
#       <Parameter Name="renderMode">Wireframe</Parameter>
#       <Parameter Name="viewMode">Top/Plan</Parameter>
#       <Parameter Name="hasFrame">True</Parameter>
#       <Parameter Name="ControlPoint00X">43mm</Parameter>
#       <Parameter Name="ControlPoint00Y">-2mm</Parameter>
#       <Parameter Name="ControlPoint01X">6mm</Parameter>
#       <Parameter Name="ControlPoint01Y">-14mm</Parameter>
#       <Parameter Name="ControlPoint02X">0mm</Parameter>
#       <Parameter Name="ControlPoint02Y">0mm</Parameter>
#       <Parameter Name="__BottomUUID">{53E9AFC2-C8A0-4624-909D-63C315554079}</Parameter>
#       <Parameter Name="__savedHandleRightX">43mm</Parameter>
#       <Parameter Name="__savedHandleRightY">-2mm</Parameter>
#       <Parameter Name="__savedHandleBottomX">6mm</Parameter>
#       <Parameter Name="__savedHandleBottomY">-14mm</Parameter>
#       <Parameter Name="__arrAlignments">4|3|1;</Parameter>
#       <Parameter Name="__fVisControlWidth">43</Parameter>
#       <Parameter Name="__fVisControlHeight">4</Parameter>
#     </Control>
#     <Control name="Dialog Builder Link" x="0" y="0">
#       <Parameter Name="ParentObj">{831ABAE6-6E6A-47C4-BAE7-CF9BE5A2F176}</Parameter>
#       <Parameter Name="RelatedObj">{53E9AFC2-C8A0-4624-909D-63C315554079}</Parameter>
#       <Parameter Name="ParentMode">1</Parameter>
#     </Control>
#     <Control name="Dialog Builder Link" x="0" y="0">
#       <Parameter Name="ParentObj">{1D50958B-A87E-45C3-AAC4-FC5DE4848B2D}</Parameter>
#       <Parameter Name="RelatedObj">{28D1FF6D-5920-41BF-989C-D08B83C62E21}</Parameter>
#       <Parameter Name="ParentMode">0</Parameter>
#     </Control>
#     <Control name="DialogBuilderControl" x="0" y="-56">
#       <Parameter Name="__UUID">{4E6329B9-62EA-459F-BAA7-D5308E666F2B}</Parameter>
#       <Parameter Name="type">kEditTextBox</Parameter>
#       <Parameter Name="id">10</Parameter>
#       <Parameter Name="constName">universes</Parameter>
#       <Parameter Name="horzOffset">2</Parameter>
#       <Parameter Name="bindLeft">kNone</Parameter>
#       <Parameter Name="bindRight">kNone</Parameter>
#       <Parameter Name="bindTop">kNone</Parameter>
#       <Parameter Name="bindBottom">kNone</Parameter>
#       <Parameter Name="ctrlWidth">32</Parameter>
#       <Parameter Name="realEditType"></Parameter>
#       <Parameter Name="renderMode">Wireframe</Parameter>
#       <Parameter Name="viewMode">Top/Plan</Parameter>
#       <Parameter Name="hasFrame">True</Parameter>
#       <Parameter Name="ControlPoint00X">24mm</Parameter>
#       <Parameter Name="ControlPoint00Y">-2mm</Parameter>
#       <Parameter Name="ControlPoint01X">12mm</Parameter>
#       <Parameter Name="ControlPoint01Y">-4mm</Parameter>
#       <Parameter Name="ControlPoint02X">0mm</Parameter>
#       <Parameter Name="ControlPoint02Y">0mm</Parameter>
#       <Parameter Name="__savedHandleRightX">24mm</Parameter>
#       <Parameter Name="__savedHandleRightY">-2mm</Parameter>
#       <Parameter Name="__savedHandleBottomX">12mm</Parameter>
#       <Parameter Name="__savedHandleBottomY">-4mm</Parameter>
#       <Parameter Name="__fVisControlWidth">24</Parameter>
#       <Parameter Name="__fVisControlHeight">4</Parameter>
#     </Control>
#     <Control name="Dialog Builder Link" x="0" y="0">
#       <Parameter Name="ParentObj">{7010B845-46AE-4C76-A978-DD10974AAAAE}</Parameter>
#       <Parameter Name="RelatedObj">{4E6329B9-62EA-459F-BAA7-D5308E666F2B}</Parameter>
#       <Parameter Name="ParentMode">1</Parameter>
#     </Control>
#     <Control name="Dialog Builder Link" x="0" y="0">
#       <Parameter Name="ParentObj">{831ABAE6-6E6A-47C4-BAE7-CF9BE5A2F176}</Parameter>
#       <Parameter Name="RelatedObj">{BD9BC4C6-A5C9-4E8D-BDCF-65E2DEC57BA7}</Parameter>
#       <Parameter Name="ParentMode">1</Parameter>
#     </Control>
#   </Controls>
# 
# </DialogBuilder>
# 
# <END_XML>

