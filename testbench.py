from kivy.core.window import Window
from kivy.app import App
from kivy.uix.label import Label

window_size = str(Window.size)
print(type(window_size))

class MyApp(App):
	def build(self):
		return Label(text=window_size, font_size=72)


if __name__ == '__main__':
	MyApp().run()