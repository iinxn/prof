import customtkinter
import requests

#api
api_users = "http://127.0.0.1:8000/api/v1/users/"
api_personal = "http://127.0.0.1:8000/api/v1/personal/"
api_group = "http://127.0.0.1:8000/api/v1/group/"

#Second form for all stuff
class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # design for application
        self.geometry("800x600")
        self.title("Терминал сотрудника охраны")

        # for grin methods
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)

        # entry for input
        self.entry_search = customtkinter.CTkEntry(master=self)
        self.entry_search.grid(row=1, column=0, columnspan=4, padx=20, pady=(20, 0), sticky="nsew")

        # search button for first_name
        self.button_search_first = customtkinter.CTkButton(master=self, text="Поиск по имени", command=self.search_first)
        self.button_search_first.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # search button for last_name
        self.button_search_last = customtkinter.CTkButton(master=self, text="Поиск по фамилии", command=self.search_last)
        self.button_search_last.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # search button for midle_name(sur_name)
        self.button_search_sur = customtkinter.CTkButton(master=self, text="Поиск по отчеству", command=self.search_sur)
        self.button_search_sur.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

        # search button for pasport numbers
        self.button_search_number = customtkinter.CTkButton(master=self, text="Поиск по номеру паспорта", command=self.search_numbers)
        self.button_search_number.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")

        # frame for labels
        self.frame = customtkinter.CTkFrame(master=self, width=200, height=200)
        self.frame.grid(row=2, column=0, columnspan=4, padx=20, pady=(20, 0), sticky="nsew")

    #event for button search_last(last_name)
    def search_last(self):
        last_name = self.entry_search.get()
        try:
            response = requests.get(f"{api_personal}?last_name={last_name}")  
            data = response.json()
            account = data["objects"][0]
            if account['last_name'] != last_name:
              print("failed to login")
            else:
              for widget in self.frame.winfo_children():
                widget.destroy()
                
              for key, value in account.items():
                label = customtkinter.CTkLabel(master=self.frame, text=f"{key}: {value}")
                label.pack()
        except:
          for widget in self.frame.winfo_children():
                widget.destroy()
          label = customtkinter.CTkLabel(master=self.frame, text=f"Человека с такой фамилией нет в списке заявок")
          label.pack()

    #event for button search_first(first_name)
    def search_first(self):
      first_name = self.entry_search.get()
      try:
          response = requests.get(f"{api_personal}?first_name={first_name}")  
          data = response.json()
          account = data["objects"][0]
          if account['first_name'] != first_name:
            print("failed to login")
          else:
            for widget in self.frame.winfo_children():
              widget.destroy()
              
            for key, value in account.items():
              label = customtkinter.CTkLabel(master=self.frame, text=f"{key}: {value}")
              label.pack()
      except:
        for widget in self.frame.winfo_children():
              widget.destroy()
        label = customtkinter.CTkLabel(master=self.frame, text=f"Человека с таким именем нет в списке заявок")
        label.pack()

    #event for button search_sur(sur_name)
    def search_sur(self):
      sur_name = self.entry_search.get()
      try:
          response = requests.get(f"{api_personal}?sur_name={sur_name}")  
          data = response.json()
          account = data["objects"][0]
          if account['sur_name'] != sur_name:
            print("failed to login")
          else:
            for widget in self.frame.winfo_children():
              widget.destroy()
              
            for key, value in account.items():
              label = customtkinter.CTkLabel(master=self.frame, text=f"{key}: {value}")
              label.pack()
      except:
        for widget in self.frame.winfo_children():
              widget.destroy()
        label = customtkinter.CTkLabel(master=self.frame, text=f"Человека с таким отчеством нет в списке заявок")
        label.pack()

    def search_numbers(self):
      number = int(self.entry_search.get())
      try:
          response = requests.get(f"{api_personal}?number={number}")  
          data = response.json()
          account = data["objects"][0]
          if account['number'] != number:
            print("failed to login")
          else:
            for widget in self.frame.winfo_children():
              widget.destroy()
              
            for key, value in account.items():
              label = customtkinter.CTkLabel(master=self.frame, text=f"{key}: {value}")
              label.pack()
      except:
        for widget in self.frame.winfo_children():
              widget.destroy()
        label = customtkinter.CTkLabel(master=self.frame, text=f"Человека с таким номером паспорта нет в списке заявок")
        label.pack()

#Authorization form
class SecurityApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Терминал сотрудника охраны")
        self.geometry("400x300")
        self.minsize(400, 300)

        self.grid_rowconfigure((1, 2, 3), weight=1)
        self.grid_columnconfigure((0), weight=1)

        self.entry_login = customtkinter.CTkEntry(master=self)
        self.entry_login.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")

        self.entry_password = customtkinter.CTkEntry(master=self, height=20)
        self.entry_password.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

        self.button = customtkinter.CTkButton(master=self, text='Login', anchor="center", command=self.button_event)
        self.button.grid(row=3, column=0, padx=20, pady=10, sticky="nsew")

    #event for  button(auth)
    def button_event(self):
        username = self.entry_login.get()
        password = self.entry_password.get()

        try:
            response = requests.get(f"{api_users}?username={username}") # &password={password}
            data = response.json()
            account = data["objects"][0]
            return ToplevelWindow()
        except:
            print("Ошибка авторизации")


if __name__ == "__main__":
    app = SecurityApp()
    app.mainloop()