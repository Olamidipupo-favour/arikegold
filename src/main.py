import os
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
sm=ScreenManager()
class Onboarding(MDScreen):
	pass
class Sign(MDScreen):
	pass
class Main(MDApp):
	data=os.getcwd()+'/data/'
	#change on production
	def build(self):
		global sm
		sm.add_widget(Onboarding(name="page0"))
		sm.add_widget(Sign(name="page1"))
		sm.current="page1"
if __name__=='__main__':
	Main().run()