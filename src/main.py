from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
sm=ScreenManager()
class Onboarding(MDScreen):
	pass
class Main(MDApp):
	def build(self):
		global sm
		sm.add_widget(Onboarding(name="page0"))
if __name__=='__main__':
	Main().run()