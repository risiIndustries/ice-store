import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import subprocess
import urllib
import json

class window1(Gtk.Window):
	
	# The Window
	def __init__(self):

		# Generating Window
		Gtk.Window.__init__(self, title="Ice Store")
		self.set_default_size(360, 280)
		self.set_resizable(True)
		self.set_border_width(10)

		# Generates Tabs
		self.catagories = Gtk.Notebook()
		self.add(self.catagories) # Adds List to Window
		self.catagories.set_tab_pos(2)

		self.featuredList = Gtk.ListBox()
		self.featuredList.set_selection_mode(Gtk.SelectionMode.NONE)
		self.catagories.append_page(self.featuredList)
		self.catagories.set_tab_label_text(self.featuredList, "Featured")

		self.accessoriesList = Gtk.ListBox()
		self.accessoriesList.set_selection_mode(Gtk.SelectionMode.NONE)
		self.catagories.append_page(self.accessoriesList)
		self.catagories.set_tab_label_text(self.accessoriesList, "Accessories")

		self.gamesList = Gtk.ListBox()
		self.gamesList.set_selection_mode(Gtk.SelectionMode.NONE)
		self.catagories.append_page(self.gamesList)
		self.catagories.set_tab_label_text(self.gamesList, "Games")

		self.graphicsList = Gtk.ListBox()
		self.graphicsList.set_selection_mode(Gtk.SelectionMode.NONE)
		self.catagories.append_page(self.graphicsList)
		self.catagories.set_tab_label_text(self.graphicsList, "Graphics")

		self.internetList = Gtk.ListBox()
		self.internetList.set_selection_mode(Gtk.SelectionMode.NONE)
		self.catagories.append_page(self.internetList)
		self.catagories.set_tab_label_text(self.internetList, "Internet")

		self.multimediaList = Gtk.ListBox()
		self.multimediaList.set_selection_mode(Gtk.SelectionMode.NONE)
		self.catagories.append_page(self.multimediaList)
		self.catagories.set_tab_label_text(self.multimediaList, "Multimedia")

		self.officeList = Gtk.ListBox()
		self.officeList.set_selection_mode(Gtk.SelectionMode.NONE)
		self.catagories.append_page(self.officeList)
		self.catagories.set_tab_label_text(self.officeList, "Office")

		self.programmingList = Gtk.ListBox()
		self.programmingList.set_selection_mode(Gtk.SelectionMode.NONE)
		self.catagories.append_page(self.programmingList)
		self.catagories.set_tab_label_text(self.programmingList, "Programming")

		self.systemList = Gtk.ListBox()
		self.systemList.set_selection_mode(Gtk.SelectionMode.NONE)
		self.catagories.append_page(self.systemList)
		self.catagories.set_tab_label_text(self.systemList, "System")

		# test Json
		with open("repo.json") as icerepo:
			repo = json.load(icerepo)

		for ssb in repo["iceapps"]:
			exec("def " + ssb["id"] + """_clicked(self):
	subprocess.Popen(["ice", "--ssbname", \"""" + ssb["name"] +"\", \"--ssburl\", \"" + ssb["url"] + "\", \"--dialogmode\", \"True\"])")

			exec("self." + ssb["id"] + "Row = Gtk.ListBoxRow()")
			exec("self." + ssb["id"] + "Box = Gtk.Box()")
			exec("self." + ssb["id"] + "Grid = Gtk.Grid()")
			exec("self." + ssb["id"] + "Grid.set_row_spacing(3)")
			exec("self." + ssb["id"] + "Grid.set_column_spacing(20)")
			exec("self." + ssb["id"] + "Image = Gtk.Image()")
			exec("self." + ssb["id"] + "Image.set_from_icon_name(\"gedit\", Gtk.IconSize.DIALOG)")
			exec("self." + ssb["id"] + "Grid.attach(self." + ssb["id"] + "Image, 1, 3, 2, 2)")
			exec("self." + ssb["id"] + "NameLabel = Gtk.Label()")
			exec("self." + ssb["id"] + "NameLabel.set_markup(\"<b>\" + ssb[\"name\"] + \"</b>       <small><i>(\" + ssb[\"url\"] + \")</i></small>\")")
			exec("self." + ssb["id"] + "NameLabel.set_xalign(0.0)")
			exec("self." + ssb["id"] + "Grid.attach(self." + ssb["id"] + "NameLabel, 3, 3, 3, 1)")
			exec("self." + ssb["id"] + "DescriptionLabel = Gtk.Label()")
			exec("self." + ssb["id"] + "DescriptionLabel.set_label(ssb[\"description\"])")
			exec("self." + ssb["id"] + "DescriptionLabel.set_xalign(0.0)")
			exec("self." + ssb["id"] + "Grid.attach(self." + ssb["id"] + "DescriptionLabel, 3, 4, 3, 1)")
			exec("self." + ssb["id"] + "InstallBtn = Gtk.Button()")
			exec("self." + ssb["id"] + "InstallBtn.set_label(\"" + ssb["price"] + "\")")
			exec("self." + ssb["id"] + "InstallBtn.connect(\"clicked\", " + ssb["id"] + "_clicked)")
			# exec("self." + ssb["catagory"] + "ListBoxRow.connect(\"row_selected\", " + ssb["id"] + "_clicked)")
			# exec("self." + ssb["id"] + "Grid.attach(self." + ssb["id"] + "InstallBtn, 6, 3, 1, 1)")
			exec("self." + ssb["id"] + "Box.pack_start(self." + ssb["id"] + "Grid, True, True, 0)")
			exec("self." + ssb["id"] + "Box.pack_start(self." + ssb["id"] + "InstallBtn, False, False, 0)")
			exec("self." + ssb["id"] + "Row.add(self." + ssb["id"] + "Box)")
			exec("self." + ssb["catagory"] + "List.add(self." + ssb["id"] + "Row)")

mainWindow = window1()
mainWindow.connect("delete-event", Gtk.main_quit) # Makes the close button close the Window.
mainWindow.show_all()
Gtk.main()
