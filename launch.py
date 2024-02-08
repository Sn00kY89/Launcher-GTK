#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import webbrowser
import json
import os

class LauncherWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(350, 175)
        self.set_resizable(False)
        self.connect("destroy", Gtk.main_quit)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
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

        # Calcola le dimensioni del pulsante in base alla finestra
        button_width_ratio = config.get("button_width_ratio", 0.3)
        button_height_ratio = config.get("button_height_ratio", 0.1)
        button_width = int(window_width * button_width_ratio)
        button_height = int(window_height * button_height_ratio)

        button_text = config.get("button_text", "Apri Chat GPT")
        button = Gtk.Button.new_with_label(button_text)
        button.connect("clicked", self.open_chat_url)
        vbox.pack_start(button, True, True, 0)
        button.set_size_request(button_width, button_height)

        # Watermark fisso
        watermark_text = "© 2024 Sn00kY89, GNU GPL License"
        watermark_button = Gtk.Button.new_with_label(watermark_text)
        watermark_button.connect("clicked", self.open_watermark_url)
        vbox.pack_end(watermark_button, False, False, 0)

    def open_chat_url(self, widget):
        config_path = os.path.join(os.path.dirname(__file__), "bin", "config.json")
        with open(config_path) as f:
            config = json.load(f)
        chat_url = config.get("url")
        if chat_url:
            webbrowser.open_new(chat_url)

    def open_watermark_url(self, widget):
        config_path = os.path.join(os.path.dirname(__file__), "bin", "config.json")
        with open(config_path) as f:
            config = json.load(f)
        watermark_url = config.get("watermark_url")
        if watermark_url:
            webbrowser.open_new(watermark_url)

win = LauncherWindow()
win.show_all()
Gtk.main()