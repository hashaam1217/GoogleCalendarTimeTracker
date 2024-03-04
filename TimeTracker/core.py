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

        # Create a grid container
        grid = Gtk.Grid(column_spacing=6, row_spacing=6)

        # Create buttons and add them to the grid
        for row in range(3):
            for col in range(2):
                button = Gtk.Button(label=f"Button {row+1}-{col+1}")
                button.set_hexpand(True)  # Allow horizontal expansion
                button.set_vexpand(True)  # Allow vertical expansion
                grid.attach(button, col, row, 1, 1)

        # Set the grid as the child of the window
        window.set_child(grid)

        window.present()

app = GCTT()
exit_status = app.run(sys.argv)
sys.exit(exit_status)

