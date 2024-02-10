#Create by Sn00ky89

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Pango
import webbrowser
import json
import os

class LauncherWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(350, 175)
        self.set_resizable(False)
        self.connect("destroy", Gtk.main_quit)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)  # Imposta uno spacing verticale di 10 pixel
        self.add(vbox)

        config_path = os.path.join(os.path.dirname(__file__), "bin", "config.json")
        with open(config_path) as f:
            config = json.load(f)

        # Imposta le dimensioni della finestra
        window_width = config.get("window_width", 350)
        window_height = config.get("window_height", 175)
        self.set_default_size(window_width, window_height)

        window_title = config.get("window_title", "Launcher")
        self.set_title(window_title)

        chat_url = config.get("url")

        button_text = config["button_text"]  # Ora non c'è un valore predefinito
        button_font_size = config.get("button_font_size", 12)

        # Imposta uno spacing di 10 pixel dai bordi laterali e dal bordo superiore per entrambi i pulsanti
        button = Gtk.Button.new_with_label(button_text)
        button.set_margin_start(10)
        button.set_margin_end(10)
        button.set_margin_top(10)
        font_desc = Pango.FontDescription()
        font_desc.set_size(int(button_font_size * Pango.SCALE))
        button.get_child().modify_font(font_desc)
        button.connect("clicked", self.open_chat_url)
        vbox.pack_start(button, True, True, 0)

        watermark_text = "© 2024 Sn00kY89, GNU GPL License"
        watermark_button = Gtk.Button.new_with_label(watermark_text)
        watermark_button.set_margin_start(10)
        watermark_button.set_margin_end(10)
        watermark_button.set_margin_top(10)
        watermark_button.connect("clicked", self.open_watermark_url)
        vbox.pack_end(watermark_button, False, False, 10)  # Imposta uno spacing di 10 pixel dal bordo inferiore

    def open_chat_url(self, widget):
        config_path = os.path.join(os.path.dirname(__file__), "bin", "config.json")
        with open(config_path) as f:
            config = json.load(f)
        chat_url = config.get("url")
        if chat_url:
            webbrowser.open_new(chat_url)

    def open_watermark_url(self, widget):
        watermark_url = "https://github.com/Sn00kY89"
        webbrowser.open_new(watermark_url)

win = LauncherWindow()
win.show_all()
Gtk.main()
