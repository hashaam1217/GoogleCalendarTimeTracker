import sys
import gi

gi.require_version("Gtk", "4.0")
from gi.repository import GLib, Gtk


class GCTT(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.example.MyGtkApplication")
        GLib.set_application_name('Google Calendar Time Tracker')

    def do_activate(self):
        window = Gtk.ApplicationWindow(application=self, title="Google Calendar Time Tracker")
        button1 = Gtk.Button(label="1Click me!")
        button2 = Gtk.Button(label="2Click me!")

        def on_button_clicked1(widget):
            print("Button clicked!1")
        def on_button_clicked2(widget):
            print("Button clicked!2")

        button1.connect("clicked", on_button_clicked1)
        button2.connect("clicked", on_button_clicked2)
        window.set_child(button1)
        window.set_child(button2)
        window.present()

app = GCTT()
exit_status = app.run(sys.argv)
sys.exit(exit_status)

