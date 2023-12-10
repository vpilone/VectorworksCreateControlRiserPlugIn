CREATE CONTROL RISER PLUG-IN: How To Use
Created by Vinny Pilone

INSTALL
----------
1. Open Vectorworks
2. Navigate to Tools -> Plug-Ins -> Plug-In Manager...
3. Click "Third Party Plugins"
4. Click "Install..."
5. Navigate to ControlRiserPlug-In.zip and select
6. Navigate to Tools -> Workspaces -> Edit Current Workspace...
7. Select the "Create Control Riser" tool under Spotlight and add it to your workspace.


HOW TO USE
----------
Run the tool and click "Create Control Riser". 

There are three main parts of this tool: adding gateways, adding lights, and adding other.

Adding Gateways: If you wish to add gateways, press yes when prompted, then type in how many gateways you would like. You will be prompted for the name, the ip, and the universes of each gateway. For the universes, please type them in a a series of numbers separated by a comma (for example: 1, 3, 6, 11).

Adding Lights: If you wish to add lights, press yes when prompted, then select your .csv file that you have exported from Lightwright (Please see EXPORTING YOUR CSV FILE for details on how to do this). 

Adding Other: If you wish to add any other items to your control riser (such as dimmer racks, control consoles, etc.), press yes when prompted. You will be prompted to give each item a name optionally give each item an IP address. You can add unlimited items until you press "Done".
	NOTE: If you want an item to have an IP but don't know what it is, be sure to 
	type something into the IP field or the non-IP template will be used.


EXPORTING YOUR CSV FILE
----------
1. Open your Lightwright file in Lightwright.
2. Navigate to File -> Export Data -> Data
3. Ensure the following settings are selected:
	Export: All worksheet rows, not just the current view
	Export File Type: Comma Separated 
	Options: 
		Sort Exported Data by: Address
		Export field labels as the first record
		Strip Channel Parentheses
		Fill blank fields with: -
4. Press "Export the Data" and make sure to save it somewhere you can find it later.