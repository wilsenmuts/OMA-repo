from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
import time
from kivy.config import Config
Config.set('graphics', 'fullscreen', '0')

class file_selector(BoxLayout):
    pass


def show_popup():
    show = file_selector()
    popupWindow = Popup(title="Select file of your choice", content= show, size_hint=(None, None), size=(800, 400))
    popupWindow.open()

class StuffBtnList(ListItemButton):
	pass

class MainScreen(Screen):
	name1 = ObjectProperty(None)
	pswd = ObjectProperty(None)

	def btnscp(self):
		print("name:", self.name1.text, "\npassword:", self.pswd.text)



class NewsFeed(Screen):
    def __init__(self, **kwargs):
        super(NewsFeed, self).__init__(**kwargs)

        def on_start(self):
            Clock.schedule_interval(self.write_time, 1)



    #Add member to the list
    def add_member(self, fstnm, srnm):
        entrant_name = self.ids.firstname.text + " " + self.ids.secondname.text
        if entrant_name != ' ':
            self.ids.member_name.adapter.data.extend([entrant_name])
            self.ids.member_name._trigger_reset_populate()
            self.ids.firstname.text = ''
            self.ids.secondname.text = ''
            self.ids.state.text= "State button"

        else:
            self.ids.state.text= "Null entry!!!"

    def btnX(self):
        show_popup()

    #replace member in the list
    def replace_member(self):
    	if self.ids.member_name.adapter.selection:
            selection = self.ids.member_name.adapter.selection[0].text
            self.ids.member_name.adapter.data.remove(selection)
            entrant_name = self.ids.firstname.text + " " + self.ids.secondname.text
            self.ids.member_name.adapter.data.extend([entrant_name])
            self.ids.member_name._trigger_reset_populate()
            self.ids.firstname.text = ''
            self.ids.secondname.text =''


    #remove member from the list
    def remove_member(self):
    	if self.ids.member_name.adapter.selection:
            selection = self.ids.member_name.adapter.selection[0].text
            self.ids.member_name.adapter.data.remove(selection)
            self.ids.member_name._trigger_reset_populate()

    def write_time(self, nap):
        localtime = time.strftime('%T')
        self.ids.timerX.text=str(localtime)
    #Event=Clock.schedule_interval(write_time, 1/60.)

    def on_start(self):
        Clock.schedule_interval(self.write_time, 1)

    #my calculator function
    def cal_addition(self, mycal):
    	
        try:
            calucation = eval(mycal)
            self.ids.mycal_input.text=str(calucation)
        except Exception as e:
            self.ids.mycal_input.text = "Error ecountered"

    #Working with the saving of minutes of a meeting
    def save_minutes(self):
        name= self.ids.meeting_name.text
        filen = ".".join([name, "txt"]) 
        myfile = open( filen, "a+")
        timer=time.strftime('%T %x')
        read1 = self.ids.minute_text.text
        myfile.write("\n\n"+timer+ "\n" + read1)
        myfile.close()
        self.ids.minute_text.text=''

class WindowManager(ScreenManager):
   pass

kv = Builder.load_file("my.kv")

class MyMainApp(App):
    def build(self):
        return kv

if __name__=="__main__":
	
	MyMainApp().run()