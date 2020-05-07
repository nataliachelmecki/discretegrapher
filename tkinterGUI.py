import tkinter as tk

LARGE_FONT = ("Verdana, 12")


# main class for grapher application
class Grapher(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (startPage, pageOne):
            frame = F(container, self)

            self.frames[F] = frame

            """stretches from center to all sides"""
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(startPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class startPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(pageOne))
        button1.pack()


class pageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Back To Home",
                           command=lambda: controller.show_frame(startPage))
        button.pack()


app = Grapher()
app.mainloop()
