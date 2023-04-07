from kivy.app import App
from kivy.uix.screenmanager  import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
import requests

#api
api_users = "http://127.0.0.1:8000/api/v1/users/"
api_personal = "http://127.0.0.1:8000/api/v1/personal/"

#main screen
class Container(Screen):
  def login(self):
    try:
      id = int(self.ids.login.text)
      response = requests.get(f"{api_users}?id={id}")
      data = response.json()
      account = data["objects"][0]
      if account["id"] != id:
        print("Doesn't have this username")
      self.manager.current = "screen2"
    except:
      self.ids.login.text = "Пользователя под таким кодом нет!"
  
class Screen2(Screen):
  def search(self):
    try:
      id = int(self.ids.search.text)
      response = requests.get(f"{api_personal}{id}/")
      data = response.json()
      layout = self.ids.layout
      layout.clear_widgets()
      box_layout = BoxLayout(orientation="vertical", size_hint_y=None)
      box_layout.bind(minimum_height=box_layout.setter('height'))
      # add new labels to the frame
      for key, value in data.items():
        label = Label(text=f"{key.capitalize()}:{value}", size_hint_y=None, height=dp(40))
        box_layout.add_widget(label)
      layout.add_widget(box_layout)
    except:
      layout = self.ids.layout
      layout.clear_widgets()
      box_layout = BoxLayout(orientation="vertical", size_hint_y=None)
      box_layout.bind(minimum_height=box_layout.setter('height'))
      label = Label(text=f"Записи с таким кодом нет")
      box_layout.add_widget(label)
      layout.add_widget(box_layout)
  def access(self):
    self.manager.current = "screen3"

class Screen3(Screen):
  def back(self):
    self.manager.current = "screen2"

class MyApp(App):
  def build(self):
    sm = ScreenManager()
    sm.add_widget(Container(name = "container"))
    sm.add_widget(Screen2(name = "screen2"))
    sm.add_widget(Screen3(name = "screen3"))
    return sm

if __name__ == '__main__':
  MyApp().run()