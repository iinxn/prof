import customtkinter
import requests

api_users = "http://127.0.0.1:8000/api/v1/users/"
api_personal = "http://127.0.0.1:8000/api/v1/personal/"
api_group = "http://127.0.0.1:8000/api/v1/group/"

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # design for application
        self.geometry("400x500")
        self.title("Терминал сотрудника общего доступа")

        # for grin methods
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        # entry for input
        self.entry_search = customtkinter.CTkEntry(master=self)
        self.entry_search.grid(row=1, column=0, columnspan=3, padx=20, pady=(20, 0), sticky="nsew")

        # update button
        self.button_update = customtkinter.CTkButton(master=self, text="Обновить", command=self.update)
        self.button_update.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # search button
        self.button_search = customtkinter.CTkButton(master=self, text="Поиск", command=self.search)
        self.button_search.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # filter button
        self.button_filter = customtkinter.CTkButton(master=self, text="Фильтрация")
        self.button_filter.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

        # frame for labels
        self.frame = customtkinter.CTkFrame(master=self, width=200, height=200)
        self.frame.grid(row=2, column=0, columnspan=3, padx=20, pady=(20, 0), sticky="nsew")

    #event for button search
    def search(self):
        id = int(self.entry_search.get())
        try:
            response = requests.get(f"{api_personal}{id}/")
            data = response.json()

            # clear the frame before adding new labels
            for widget in self.frame.winfo_children():
                widget.destroy()

            # add new labels to the frame
            for key, value in data.items():
                label = customtkinter.CTkLabel(master=self.frame, text=f"{key}: {value}")
                label.pack()
        except:
            for widget in self.frame.winfo_children():
                widget.destroy()
            label = customtkinter.CTkLabel(master=self.frame, text=f"Человека с такой кодом нет нет в списке заявок")
            label.pack()

    #event for button update
    def update(self):
      response = requests.get(f"{api_personal}")
      data = response.json()
      account = data["objects"]

      # clear the frame before adding new labels
      for widget in self.frame.winfo_children():
          widget.destroy()

      # add new labels to the frame
      for value in account:
        for key, values in value.items():
          if values == value["first_name"]:
            label = customtkinter.CTkLabel(master=self.frame, text=f"Имя: {values}")
            label.pack()

class SecurityApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Терминал сотрудника общего доступа")
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

    def button_event(self):
        username = self.entry_login.get()
        password = self.entry_password.get()

        try:
            response = requests.get(f"{api_users}?username={username}")  # &password={password}
            data = response.json()
            account = data["objects"][0]
            return ToplevelWindow()
        except:
            print("Ошибка авторизации")

if __name__ == "__main__":
    app = SecurityApp()
    app.mainloop()