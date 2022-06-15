import pathlib
import pyglet
import tkinter as tk
from screeninfo import get_monitors


class Form(tk.Tk):

    def __init__(self):
        super().__init__()

        primary_monitor = next(x for x in get_monitors() if x.is_primary)

        self.fullscreen = tk.StringVar(self)
        self.fullscreen.set("0")

        icon_path = pathlib.Path("resources/icon.ico")
        self.iconbitmap(str(icon_path))

        self.resolution = tk.StringVar(self)
        if round(primary_monitor.width / primary_monitor.height, 2) == round(16/9, 2):
            self.resolution.set(f"{primary_monitor.width}x{primary_monitor.height}")
        else:
            self.resolution.set(f"426x240")
        self.title("JDU - Resolución")

        path = pathlib.Path("resources/fonts/Liminality-Regular.ttf")
        pyglet.font.add_file(str(path))
        self.font = ('Liminality', 15)
        self.bg_color = "#FFB5FD"
        self.configure(background=self.bg_color)
        self.configure_widgets()

        self.good_close = False

    def configure_widgets(self):
        lbl = tk.Label(self, text="Elija una resolución", font=self.font,background=self.bg_color,
                       foreground="white")
        lbl.grid(row=0, column=0, padx=10)

        res_menu = tk.OptionMenu(self, self.resolution, "720x480", "960x540", "1280x720",
                                 "1366x768", "1600x900", "1920x1080", "2560x1440", "3200x1800",
                                 "3840x2160", "5120x2880", "7680x4320", "15630x8640")
        for i in range(12):
            res_menu.children['menu'].entryconfig(i,foreground='white')
        res_menu.configure(background=self.bg_color, font=self.font, foreground="white",
                           activebackground=self.bg_color)
        res_menu["menu"].configure(background=self.bg_color, font=self.font)
        res_menu.grid(row=0, column=1, padx=10)

        otherlbl = tk.Label(self,
                            text="¿Pantalla completa?",
                            font=self.font,
                            background=self.bg_color,
                            foreground="white")
        otherlbl.grid(row=1, column=0)

        fullscreen = tk.Checkbutton(self, font=self.font,
                                    background=self.bg_color,
                                    selectcolor=self.bg_color,
                                    variable=self.fullscreen,
                                    activebackground=self.bg_color)
        fullscreen.grid(row=1, column=1)

        accept = tk.Button(self, text="Confirmar",
                           font=self.font,
                           background=self.bg_color,
                           foreground="white",
                           activebackground=self.bg_color,
                           command=self.close_window)
        accept.grid(row=2, column=0, columnspan=2, pady=10)

    def close_window(self):
        self.good_close = True
        self.destroy()

    def get_data(self):
        res = self.resolution.get()
        width, height = res.split("x")
        width = int(width)
        height = int(height)
        fullscreen = self.fullscreen.get() == "1"
        return {"width": width, "height": height, "fullscreen": bool(fullscreen)}
