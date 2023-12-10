#Created by Vinny Pilone using Vectorworks Dialog Builder Tools
#DRAFT 11/13/22

import vs
import _main

# control IDs
kOK                   = 1
kCancel               = 2
ktitle                = 4
kincludeUni1          = 5
kinitialXtext         = 6
kinitialYtext         = 7
kcolumnLimitText      = 8
kboxWidthText         = 9
kinitialX             = 11
kinitialY             = 12
kcolumnLimit          = 13
kboxWidth             = 14

dialog = None
isFirstTime = False

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
        if ndx == 1001:			return 'Apply'
        elif ndx == 1002:		return 'Cancel'
        elif ndx == 1003:		return 'Settings Menu'
        elif ndx == 1004:		return 'Settings'
        elif ndx == 1005:		return 'Include Universe 1'
        elif ndx == 1006:		return 'Initial X (Inches):'
        elif ndx == 1007:		return 'Initial Y (Inches):'
        elif ndx == 1008:		return 'Column Limit:'
        elif ndx == 1009:		return 'Box Width (Inches):'
        elif ndx == 1011:		return ''
        elif ndx == 1012:		return ''
        elif ndx == 1013:		return ''
        elif ndx == 1014:		return ''
        # Help Text
        elif ndx == 2001:		return 'Accepts the dialog data.'
        elif ndx == 2002:		return 'Cancels the dialog data.'
        elif ndx == 2004:		return 'Help text.'
        elif ndx == 2005:		return 'Help text.'
        elif ndx == 2006:		return 'Help text.'
        elif ndx == 2007:		return 'Help text.'
        elif ndx == 2008:		return 'Help text.'
        elif ndx == 2009:		return 'Help text.'
        elif ndx == 2011:		return 'Help text.'
        elif ndx == 2012:		return 'Help text.'
        elif ndx == 2013:		return 'Help text.'
        elif ndx == 2014:		return 'Help text.'
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
    vs.CreateCenteredStaticText( dialog, ktitle, GetStr(ktitle), 16 )
    vs.CreateCheckBox( dialog, kincludeUni1, GetStr(kincludeUni1) )
    vs.CreateStaticText( dialog, kinitialXtext, GetStr(kinitialXtext), -1 )
    vs.CreateEditInteger( dialog, kinitialX, _main.initialX, 16 )
    vs.CreateStaticText( dialog, kinitialYtext, GetStr(kinitialYtext), -1 )
    vs.CreateEditInteger( dialog, kinitialY, _main.initialY, 16 )
    vs.CreateStaticText( dialog, kcolumnLimitText, GetStr(kcolumnLimitText), -1 )
    vs.CreateEditInteger( dialog, kcolumnLimit, _main.columnLimit, 16 )
    vs.CreateStaticText( dialog, kboxWidthText, GetStr(kboxWidthText), -1 )
    vs.CreateEditInteger( dialog, kboxWidth, _main.boxWidth, 16 )

    # set relations
    vs.SetFirstLayoutItem( dialog, ktitle )
    vs.SetBelowItem( dialog, ktitle, kincludeUni1, 0, 0 )
    vs.SetBelowItem( dialog, kincludeUni1, kinitialXtext, 0, 0 )
    vs.SetRightItem( dialog, kinitialXtext, kinitialX, 0, 0 )
    vs.SetBelowItem( dialog, kinitialXtext, kinitialYtext, 0, 0 )
    vs.SetRightItem( dialog, kinitialYtext, kinitialY, 0, 0 )
    vs.SetBelowItem( dialog, kinitialYtext, kcolumnLimitText, 0, 0 )
    vs.SetRightItem( dialog, kcolumnLimitText, kcolumnLimit, 0, 0 )
    vs.SetBelowItem( dialog, kcolumnLimitText, kboxWidthText, 0, 0 )
    vs.SetRightItem( dialog, kboxWidthText, kboxWidth, 0, 0 )

    # set alignments
    vs.AlignItemEdge( dialog, ktitle, kRight, 1, kResize );
    vs.AlignItemEdge( dialog, kinitialX, kRight, 1, kResize );

    # set help strings
    cnt = 1
    while ( cnt <= 14 ):
        vs.SetHelpText( dialog, cnt, GetHelpStr(cnt) )
        cnt += 1

    return dialog

#Dialog Handler to update seetings
def DialogHandler(item, data):
    global isFirstTime
    if isFirstTime == True:
        isFirstTime = False
        vs.SetBooleanItem(dialog, kincludeUni1, _main.includeUni1)
    boolean = None
    if item == kOK:
        _main.includeUni1 = vs.GetBooleanItem(dialog, kincludeUni1)
        boolean, _main.initialX = vs.GetEditInteger(dialog, kinitialX)
        boolean, _main.initialY = vs.GetEditInteger(dialog, kinitialY)
        boolean, _main.columnLimit = vs.GetEditInteger(dialog, kcolumnLimit)
        boolean, _main.boxWidth = vs.GetEditInteger(dialog, kboxWidth)

# XML defintion of the layout
#
# <BEGIN_XML>
#<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
# <DialogBuilder>
# 
#   <LayoutData>
#     <Name>settingsDlg</Name>
#     <Title>Settings Menu</Title>
#     <OKText>Apply</OKText>
#     <OKHelpText>Accepts the dialog data.</OKHelpText>
#     <CancelText>Cancel</CancelText>
#     <CancelHelpText>Cancels the dialog data.</CancelHelpText>
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
#     <Control name="DialogBuilderControl" x="0" y="0">
#       <Parameter Name="__UUID">{42760D6B-BA92-4781-A1A8-D41C399B588C}</Parameter>
#       <Parameter Name="type">kCenteredStaticText</Parameter>
#       <Parameter Name="id">4</Parameter>
#       <Parameter Name="constName">title</Parameter>
#       <Parameter Name="label">Settings</Parameter>
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
#       <Parameter Name="ControlPoint00X">15mm</Parameter>
#       <Parameter Name="ControlPoint00Y">-2mm</Parameter>
#       <Parameter Name="ControlPoint01X">21mm</Parameter>
#       <Parameter Name="ControlPoint01Y">-12mm</Parameter>
#       <Parameter Name="ControlPoint02X">0mm</Parameter>
#       <Parameter Name="ControlPoint02Y">0mm</Parameter>
#       <Parameter Name="__BottomUUID">{503F593E-37BF-4BFF-BBE9-3B4B9A1C06EC}</Parameter>
#       <Parameter Name="__savedHandleRightX">15mm</Parameter>
#       <Parameter Name="__savedHandleRightY">-2mm</Parameter>
#       <Parameter Name="__savedHandleBottomX">21mm</Parameter>
#       <Parameter Name="__savedHandleBottomY">-12mm</Parameter>
#       <Parameter Name="__arrAlignments">1|0|0;</Parameter>
#       <Parameter Name="__fVisControlWidth">15</Parameter>
#       <Parameter Name="__fVisControlHeight">4</Parameter>
#     </Control>
#     <Control name="DialogBuilderControl" x="0" y="-12">
#       <Parameter Name="__UUID">{503F593E-37BF-4BFF-BBE9-3B4B9A1C06EC}</Parameter>
#       <Parameter Name="type">kCheckBox</Parameter>
#       <Parameter Name="id">5</Parameter>
#       <Parameter Name="constName">includeUni1</Parameter>
#       <Parameter Name="label">Include Universe 1</Parameter>
#       <Parameter Name="helpText">Help text.</Parameter>
#       <Parameter Name="bindLeft">kNone</Parameter>
#       <Parameter Name="bindRight">kNone</Parameter>
#       <Parameter Name="bindTop">kNone</Parameter>
#       <Parameter Name="bindBottom">kNone</Parameter>
#       <Parameter Name="realEditType"></Parameter>
#       <Parameter Name="renderMode">Wireframe</Parameter>
#       <Parameter Name="viewMode">Top/Plan</Parameter>
#       <Parameter Name="hasFrame">True</Parameter>
#       <Parameter Name="ControlPoint00X">42mm</Parameter>
#       <Parameter Name="ControlPoint00Y">-2mm</Parameter>
#       <Parameter Name="ControlPoint01X">15mm</Parameter>
#       <Parameter Name="ControlPoint01Y">-13mm</Parameter>
#       <Parameter Name="ControlPoint02X">0mm</Parameter>
#       <Parameter Name="ControlPoint02Y">0mm</Parameter>
#       <Parameter Name="__BottomUUID">{B5CC222B-040C-4B83-9AA7-F4AC1A4A3411}</Parameter>
#       <Parameter Name="__savedHandleRightX">42mm</Parameter>
#       <Parameter Name="__savedHandleRightY">-2mm</Parameter>
#       <Parameter Name="__savedHandleBottomX">15mm</Parameter>
#       <Parameter Name="__savedHandleBottomY">-13mm</Parameter>
#       <Parameter Name="__fVisControlWidth">42</Parameter>
#       <Parameter Name="__fVisControlHeight">4</Parameter>
#     </Control>
#     <Control name="DialogBuilderControl" x="0" y="-25">
#       <Parameter Name="__UUID">{B5CC222B-040C-4B83-9AA7-F4AC1A4A3411}</Parameter>
#       <Parameter Name="id">6</Parameter>
#       <Parameter Name="constName">initialXtext</Parameter>
#       <Parameter Name="label">Initial X (Inches):</Parameter>
#       <Parameter Name="helpText">Help text.</Parameter>
#       <Parameter Name="bindLeft">kNone</Parameter>
#       <Parameter Name="bindRight">kNone</Parameter>
#       <Parameter Name="bindTop">kNone</Parameter>
#       <Parameter Name="bindBottom">kNone</Parameter>
#       <Parameter Name="realEditType"></Parameter>
#       <Parameter Name="renderMode">Wireframe</Parameter>
#       <Parameter Name="viewMode">Top/Plan</Parameter>
#       <Parameter Name="hasFrame">True</Parameter>
#       <Parameter Name="ControlPoint00X">25mm</Parameter>
#       <Parameter Name="ControlPoint00Y">-2mm</Parameter>
#       <Parameter Name="ControlPoint01X">15mm</Parameter>
#       <Parameter Name="ControlPoint01Y">-13mm</Parameter>
#       <Parameter Name="ControlPoint02X">0mm</Parameter>
#       <Parameter Name="ControlPoint02Y">0mm</Parameter>
#       <Parameter Name="__RightUUID">{5EF6BCEA-16DA-454F-BD8F-AC54FD850DD9}</Parameter>
#       <Parameter Name="__BottomUUID">{6478253D-DE3E-4EA0-99AB-F64DBC3857BF}</Parameter>
#       <Parameter Name="__savedHandleRightX">25mm</Parameter>
#       <Parameter Name="__savedHandleRightY">-2mm</Parameter>
#       <Parameter Name="__savedHandleBottomX">15mm</Parameter>
#       <Parameter Name="__savedHandleBottomY">-13mm</Parameter>
#       <Parameter Name="__fVisControlWidth">32</Parameter>
#       <Parameter Name="__fVisControlHeight">4</Parameter>
#     </Control>
#     <Control name="DialogBuilderControl" x="0" y="-38">
#       <Parameter Name="__UUID">{6478253D-DE3E-4EA0-99AB-F64DBC3857BF}</Parameter>
#       <Parameter Name="id">7</Parameter>
#       <Parameter Name="constName">initialYtext</Parameter>
#       <Parameter Name="label">Initial Y (Inches):</Parameter>
#       <Parameter Name="helpText">Help text.</Parameter>
#       <Parameter Name="bindLeft">kNone</Parameter>
#       <Parameter Name="bindRight">kNone</Parameter>
#       <Parameter Name="bindTop">kNone</Parameter>
#       <Parameter Name="bindBottom">kNone</Parameter>
#       <Parameter Name="realEditType"></Parameter>
#       <Parameter Name="renderMode">Wireframe</Parameter>
#       <Parameter Name="viewMode">Top/Plan</Parameter>
#       <Parameter Name="hasFrame">True</Parameter>
#       <Parameter Name="ControlPoint00X">25mm</Parameter>
#       <Parameter Name="ControlPoint00Y">-2mm</Parameter>
#       <Parameter Name="ControlPoint01X">13mm</Parameter>
#       <Parameter Name="ControlPoint01Y">-12mm</Parameter>
#       <Parameter Name="ControlPoint02X">0mm</Parameter>
#       <Parameter Name="ControlPoint02Y">0mm</Parameter>
#       <Parameter Name="__RightUUID">{F3A010F0-B717-4BF6-8F8C-7DE7007E9175}</Parameter>
#       <Parameter Name="__BottomUUID">{7FB626C6-870C-4C7B-BB02-8CA9234E6628}</Parameter>
#       <Parameter Name="__savedHandleRightX">25mm</Parameter>
#       <Parameter Name="__savedHandleRightY">-2mm</Parameter>
#       <Parameter Name="__savedHandleBottomX">13mm</Parameter>
#       <Parameter Name="__savedHandleBottomY">-12mm</Parameter>
#       <Parameter Name="__fVisControlWidth">32</Parameter>
#       <Parameter Name="__fVisControlHeight">4</Parameter>
#     </Control>
#     <Control name="DialogBuilderControl" x="0" y="-50">
#       <Parameter Name="__UUID">{7FB626C6-870C-4C7B-BB02-8CA9234E6628}</Parameter>
#       <Parameter Name="id">8</Parameter>
#       <Parameter Name="constName">columnLimitText</Parameter>
#       <Parameter Name="label">Column Limit:</Parameter>
#       <Parameter Name="helpText">Help text.</Parameter>
#       <Parameter Name="bindLeft">kNone</Parameter>
#       <Parameter Name="bindRight">kNone</Parameter>
#       <Parameter Name="bindTop">kNone</Parameter>
#       <Parameter Name="bindBottom">kNone</Parameter>
#       <Parameter Name="realEditType"></Parameter>
#       <Parameter Name="renderMode">Wireframe</Parameter>
#       <Parameter Name="viewMode">Top/Plan</Parameter>
#       <Parameter Name="hasFrame">True</Parameter>
#       <Parameter Name="ControlPoint00X">31mm</Parameter>
#       <Parameter Name="ControlPoint00Y">-2mm</Parameter>
#       <Parameter Name="ControlPoint01X">18mm</Parameter>
#       <Parameter Name="ControlPoint01Y">-13mm</Parameter>
#       <Parameter Name="ControlPoint02X">0mm</Parameter>
#       <Parameter Name="ControlPoint02Y">0mm</Parameter>
#       <Parameter Name="__RightUUID">{5966CD92-9269-4D8D-9D4C-B0A9A0A1415D}</Parameter>
#       <Parameter Name="__BottomUUID">{2B35F8EF-551C-469E-A835-E8A6E2BC6B5D}</Parameter>
#       <Parameter Name="__savedHandleRightX">31mm</Parameter>
#       <Parameter Name="__savedHandleRightY">-2mm</Parameter>
#       <Parameter Name="__savedHandleBottomX">18mm</Parameter>
#       <Parameter Name="__savedHandleBottomY">-13mm</Parameter>
#       <Parameter Name="__fVisControlWidth">26</Parameter>
#       <Parameter Name="__fVisControlHeight">4</Parameter>
#     </Control>
#     <Control name="DialogBuilderControl" x="0" y="-63">
#       <Parameter Name="__UUID">{2B35F8EF-551C-469E-A835-E8A6E2BC6B5D}</Parameter>
#       <Parameter Name="id">9</Parameter>
#       <Parameter Name="constName">boxWidthText</Parameter>
#       <Parameter Name="label">Box Width (Inches):</Parameter>
#       <Parameter Name="helpText">Help text.</Parameter>
#       <Parameter Name="bindLeft">kNone</Parameter>
#       <Parameter Name="bindRight">kNone</Parameter>
#       <Parameter Name="bindTop">kNone</Parameter>
#       <Parameter Name="bindBottom">kNone</Parameter>
#       <Parameter Name="realEditType"></Parameter>
#       <Parameter Name="renderMode">Wireframe</Parameter>
#       <Parameter Name="viewMode">Top/Plan</Parameter>
#       <Parameter Name="hasFrame">True</Parameter>
#       <Parameter Name="ControlPoint00X">44mm</Parameter>
#       <Parameter Name="ControlPoint00Y">-2mm</Parameter>
#       <Parameter Name="ControlPoint01X">18mm</Parameter>
#       <Parameter Name="ControlPoint01Y">-4mm</Parameter>
#       <Parameter Name="ControlPoint02X">0mm</Parameter>
#       <Parameter Name="ControlPoint02Y">0mm</Parameter>
#       <Parameter Name="__RightUUID">{7E09CD64-FF82-4F5D-8989-344276AC01D0}</Parameter>
#       <Parameter Name="__savedHandleRightX">44mm</Parameter>
#       <Parameter Name="__savedHandleRightY">-2mm</Parameter>
#       <Parameter Name="__savedHandleBottomX">18mm</Parameter>
#       <Parameter Name="__savedHandleBottomY">-4mm</Parameter>
#       <Parameter Name="__fVisControlWidth">37</Parameter>
#       <Parameter Name="__fVisControlHeight">4</Parameter>
#     </Control>
#     <Control name="Dialog Builder Link" x="0" y="0">
#       <Parameter Name="ParentObj">{42760D6B-BA92-4781-A1A8-D41C399B588C}</Parameter>
#       <Parameter Name="RelatedObj">{503F593E-37BF-4BFF-BBE9-3B4B9A1C06EC}</Parameter>
#       <Parameter Name="ParentMode">1</Parameter>
#     </Control>
#     <Control name="Dialog Builder Link" x="0" y="0">
#       <Parameter Name="ParentObj">{503F593E-37BF-4BFF-BBE9-3B4B9A1C06EC}</Parameter>
#       <Parameter Name="RelatedObj">{B5CC222B-040C-4B83-9AA7-F4AC1A4A3411}</Parameter>
#       <Parameter Name="ParentMode">1</Parameter>
#     </Control>
#     <Control name="DialogBuilderControl" x="25" y="-25">
#       <Parameter Name="__UUID">{5EF6BCEA-16DA-454F-BD8F-AC54FD850DD9}</Parameter>
#       <Parameter Name="type">kEditIntegerBox</Parameter>
#       <Parameter Name="id">11</Parameter>
#       <Parameter Name="constName">initialX</Parameter>
#       <Parameter Name="value">0</Parameter>
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
#       <Parameter Name="ControlPoint00X">29mm</Parameter>
#       <Parameter Name="ControlPoint00Y">-2mm</Parameter>
#       <Parameter Name="ControlPoint01X">14mm</Parameter>
#       <Parameter Name="ControlPoint01Y">-4mm</Parameter>
#       <Parameter Name="ControlPoint02X">0mm</Parameter>
#       <Parameter Name="ControlPoint02Y">0mm</Parameter>
#       <Parameter Name="__savedHandleRightX">29mm</Parameter>
#       <Parameter Name="__savedHandleRightY">-2mm</Parameter>
#       <Parameter Name="__savedHandleBottomX">14mm</Parameter>
#       <Parameter Name="__savedHandleBottomY">-4mm</Parameter>
#       <Parameter Name="__arrAlignments">1|0|0;</Parameter>
#       <Parameter Name="__fVisControlWidth">29</Parameter>
#       <Parameter Name="__fVisControlHeight">4</Parameter>
#     </Control>
#     <Control name="Dialog Builder Link" x="0" y="0">
#       <Parameter Name="ParentObj">{B5CC222B-040C-4B83-9AA7-F4AC1A4A3411}</Parameter>
#       <Parameter Name="RelatedObj">{5EF6BCEA-16DA-454F-BD8F-AC54FD850DD9}</Parameter>
#       <Parameter Name="ParentMode">0</Parameter>
#     </Control>
#     <Control name="Dialog Builder Link" x="0" y="0">
#       <Parameter Name="ParentObj">{B5CC222B-040C-4B83-9AA7-F4AC1A4A3411}</Parameter>
#       <Parameter Name="RelatedObj">{6478253D-DE3E-4EA0-99AB-F64DBC3857BF}</Parameter>
#       <Parameter Name="ParentMode">1</Parameter>
#     </Control>
#     <Control name="Dialog Builder Link" x="0" y="0">
#       <Parameter Name="ParentObj">{6478253D-DE3E-4EA0-99AB-F64DBC3857BF}</Parameter>
#       <Parameter Name="RelatedObj">{7FB626C6-870C-4C7B-BB02-8CA9234E6628}</Parameter>
#       <Parameter Name="ParentMode">1</Parameter>
#     </Control>
#     <Control name="Dialog Builder Link" x="0" y="0">
#       <Parameter Name="ParentObj">{7FB626C6-870C-4C7B-BB02-8CA9234E6628}</Parameter>
#       <Parameter Name="RelatedObj">{2B35F8EF-551C-469E-A835-E8A6E2BC6B5D}</Parameter>
#       <Parameter Name="ParentMode">1</Parameter>
#     </Control>
#     <Control name="DialogBuilderControl" x="25" y="-38">
#       <Parameter Name="__UUID">{F3A010F0-B717-4BF6-8F8C-7DE7007E9175}</Parameter>
#       <Parameter Name="type">kEditIntegerBox</Parameter>
#       <Parameter Name="id">12</Parameter>
#       <Parameter Name="constName">Unnamed</Parameter>
#       <Parameter Name="value">0</Parameter>
#       <Parameter Name="helpText">Help text.</Parameter>
#       <Parameter Name="bindLeft">kNone</Parameter>
#       <Parameter Name="bindRight">kNone</Parameter>
#       <Parameter Name="bindTop">kNone</Parameter>
#       <Parameter Name="bindBottom">kNone</Parameter>
#       <Parameter Name="realEditType"></Parameter>
#       <Parameter Name="renderMode">Wireframe</Parameter>
#       <Parameter Name="viewMode">Top/Plan</Parameter>
#       <Parameter Name="hasFrame">True</Parameter>
#       <Parameter Name="ControlPoint00X">29mm</Parameter>
#       <Parameter Name="ControlPoint00Y">-2mm</Parameter>
#       <Parameter Name="ControlPoint01X">14mm</Parameter>
#       <Parameter Name="ControlPoint01Y">-4mm</Parameter>
#       <Parameter Name="ControlPoint02X">0mm</Parameter>
#       <Parameter Name="ControlPoint02Y">0mm</Parameter>
#       <Parameter Name="__savedHandleRightX">29mm</Parameter>
#       <Parameter Name="__savedHandleRightY">-2mm</Parameter>
#       <Parameter Name="__savedHandleBottomX">14mm</Parameter>
#       <Parameter Name="__savedHandleBottomY">-4mm</Parameter>
#       <Parameter Name="__fVisControlWidth">29</Parameter>
#       <Parameter Name="__fVisControlHeight">4</Parameter>
#     </Control>
#     <Control name="Dialog Builder Link" x="0" y="0">
#       <Parameter Name="ParentObj">{6478253D-DE3E-4EA0-99AB-F64DBC3857BF}</Parameter>
#       <Parameter Name="RelatedObj">{F3A010F0-B717-4BF6-8F8C-7DE7007E9175}</Parameter>
#       <Parameter Name="ParentMode">0</Parameter>
#     </Control>
#     <Control name="DialogBuilderControl" x="31" y="-50">
#       <Parameter Name="__UUID">{5966CD92-9269-4D8D-9D4C-B0A9A0A1415D}</Parameter>
#       <Parameter Name="type">kEditIntegerBox</Parameter>
#       <Parameter Name="id">13</Parameter>
#       <Parameter Name="constName">columnLimit</Parameter>
#       <Parameter Name="value">12</Parameter>
#       <Parameter Name="helpText">Help text.</Parameter>
#       <Parameter Name="bindLeft">kNone</Parameter>
#       <Parameter Name="bindRight">kNone</Parameter>
#       <Parameter Name="bindTop">kNone</Parameter>
#       <Parameter Name="bindBottom">kNone</Parameter>
#       <Parameter Name="realEditType"></Parameter>
#       <Parameter Name="renderMode">Wireframe</Parameter>
#       <Parameter Name="viewMode">Top/Plan</Parameter>
#       <Parameter Name="hasFrame">True</Parameter>
#       <Parameter Name="ControlPoint00X">29mm</Parameter>
#       <Parameter Name="ControlPoint00Y">-2mm</Parameter>
#       <Parameter Name="ControlPoint01X">14mm</Parameter>
#       <Parameter Name="ControlPoint01Y">-4mm</Parameter>
#       <Parameter Name="ControlPoint02X">0mm</Parameter>
#       <Parameter Name="ControlPoint02Y">0mm</Parameter>
#       <Parameter Name="__savedHandleRightX">29mm</Parameter>
#       <Parameter Name="__savedHandleRightY">-2mm</Parameter>
#       <Parameter Name="__savedHandleBottomX">14mm</Parameter>
#       <Parameter Name="__savedHandleBottomY">-4mm</Parameter>
#       <Parameter Name="__fVisControlWidth">29</Parameter>
#       <Parameter Name="__fVisControlHeight">4</Parameter>
#     </Control>
#     <Control name="Dialog Builder Link" x="0" y="0">
#       <Parameter Name="ParentObj">{7FB626C6-870C-4C7B-BB02-8CA9234E6628}</Parameter>
#       <Parameter Name="RelatedObj">{5966CD92-9269-4D8D-9D4C-B0A9A0A1415D}</Parameter>
#       <Parameter Name="ParentMode">0</Parameter>
#     </Control>
#     <Control name="DialogBuilderControl" x="44" y="-63">
#       <Parameter Name="__UUID">{7E09CD64-FF82-4F5D-8989-344276AC01D0}</Parameter>
#       <Parameter Name="type">kEditIntegerBox</Parameter>
#       <Parameter Name="id">14</Parameter>
#       <Parameter Name="constName">boxWidth</Parameter>
#       <Parameter Name="value">72</Parameter>
#       <Parameter Name="helpText">Help text.</Parameter>
#       <Parameter Name="bindLeft">kNone</Parameter>
#       <Parameter Name="bindRight">kNone</Parameter>
#       <Parameter Name="bindTop">kNone</Parameter>
#       <Parameter Name="bindBottom">kNone</Parameter>
#       <Parameter Name="realEditType"></Parameter>
#       <Parameter Name="renderMode">Wireframe</Parameter>
#       <Parameter Name="viewMode">Top/Plan</Parameter>
#       <Parameter Name="hasFrame">True</Parameter>
#       <Parameter Name="ControlPoint00X">29mm</Parameter>
#       <Parameter Name="ControlPoint00Y">-2mm</Parameter>
#       <Parameter Name="ControlPoint01X">14mm</Parameter>
#       <Parameter Name="ControlPoint01Y">-4mm</Parameter>
#       <Parameter Name="ControlPoint02X">0mm</Parameter>
#       <Parameter Name="ControlPoint02Y">0mm</Parameter>
#       <Parameter Name="__savedHandleRightX">29mm</Parameter>
#       <Parameter Name="__savedHandleRightY">-2mm</Parameter>
#       <Parameter Name="__savedHandleBottomX">14mm</Parameter>
#       <Parameter Name="__savedHandleBottomY">-4mm</Parameter>
#       <Parameter Name="__fVisControlWidth">29</Parameter>
#       <Parameter Name="__fVisControlHeight">4</Parameter>
#     </Control>
#     <Control name="Dialog Builder Link" x="0" y="0">
#       <Parameter Name="ParentObj">{2B35F8EF-551C-469E-A835-E8A6E2BC6B5D}</Parameter>
#       <Parameter Name="RelatedObj">{7E09CD64-FF82-4F5D-8989-344276AC01D0}</Parameter>
#       <Parameter Name="ParentMode">0</Parameter>
#     </Control>
#   </Controls>
# 
# </DialogBuilder>
# 
# <END_XML>

