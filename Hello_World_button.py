#created by Malcolm McCarthy
#created on sept 2017
#created for ICS3U
#this program is hello world, with a button

import ui

def  hello_world_touch_up_inside(sender):
		#print ('hello, world!')
		view['hello_world_label'].text = ("hello, world!")
	
		view = ui.load_view()
		view.present('sheet')
		
