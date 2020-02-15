import os
from tkinter import ttk, filedialog, IntVar, StringVar, Button, Checkbutton, Entry, Frame, Label, LabelFrame, OptionMenu, N, E, W, LEFT, RIGHT, X
import gui.widgets as widgets

def enemizer_page(parent,settings):
    # Enemizer
    self = ttk.Frame(parent)

    # Enemizer options
    self.widgets = {}

    # Pot Shuffle
    key = "potshuffle"
    self.widgets[key] = widgets.make_widget(
      self,
      "checkbox",
      self,
      "Pot Shuffle",
      None
    )
    self.widgets[key].pack(anchor=W)

    ## Enemizer CLI Path
    enemizerPathFrame = Frame(self)
    enemizerCLIlabel = Label(enemizerPathFrame, text="EnemizerCLI path: ")
    enemizerCLIlabel.pack(side=LEFT)
    self.enemizerCLIpathVar = StringVar(value=settings["enemizercli"])
    def saveEnemizerPath(caller,_,mode):
        settings["enemizercli"] = self.enemizerCLIpathVar.get()
    self.enemizerCLIpathVar.trace_add("write",saveEnemizerPath)
    enemizerCLIpathEntry = Entry(enemizerPathFrame, textvariable=self.enemizerCLIpathVar)
    enemizerCLIpathEntry.pack(side=LEFT, fill=X, expand=True)
    def EnemizerSelectPath():
        path = filedialog.askopenfilename(filetypes=[("EnemizerCLI executable", "*EnemizerCLI*")], initialdir=os.path.join("."))
        if path:
            self.enemizerCLIpathVar.set(path)
            settings["enemizercli"] = path
    enemizerCLIbrowseButton = Button(enemizerPathFrame, text='...', command=EnemizerSelectPath)
    enemizerCLIbrowseButton.pack(side=LEFT)
    enemizerPathFrame.pack(fill=X, expand=True)

    leftEnemizerFrame = Frame(self)
    rightEnemizerFrame = Frame(self)
    leftEnemizerFrame.pack(side=LEFT, anchor=N)
    rightEnemizerFrame.pack(side=RIGHT, anchor=N)

    ## Randomize Enemies
    key = "enemyshuffle"
    self.widgets[key] = widgets.make_widget(
      self,
      "selectbox",
      leftEnemizerFrame,
      "Enemy Shuffle",
      None,
      {"label": {"side": LEFT}, "selectbox": {"side": RIGHT}},
      {
        "Vanilla": "none",
        "Shuffled": "shuffled",
        "Chaos": "chaos"
      }
    )
    self.widgets[key].pack(anchor=E)

    ## Randomize Bosses
    key = "bossshuffle"
    self.widgets[key] = widgets.make_widget(
      self,
      "selectbox",
      leftEnemizerFrame,
      "Boss Shuffle",
      None,
      {"label": {"side": LEFT}, "selectbox": {"side": RIGHT}},
      {
        "Vanilla": "none",
        "Basic": "basic",
        "Normal": "normal",
        "Chaos": "chaos"
      }
    )
    self.widgets[key].pack(anchor=E)

    ## Enemy Damage
    key = "enemydamage"
    self.widgets[key] = widgets.make_widget(
      self,
      "selectbox",
      rightEnemizerFrame,
      "Enemy Damage",
      None,
      {"label": {"side": LEFT}, "selectbox": {"side": RIGHT}},
      {
        "Vanilla": "default",
        "Shuffled": "shuffled",
        "Chaos": "chaos"
      }
    )
    self.widgets[key].pack(anchor=E)

    ## Enemy Health
    key = "enemyhealth"
    self.widgets[key] = widgets.make_widget(
      self,
      "selectbox",
      rightEnemizerFrame,
      "Enemy Health",
      None,
      {"label": {"side": LEFT}, "selectbox": {"side": RIGHT}},
      {
        "Vanilla": "default",
        "Easy": "easy",
        "Normal": "normal",
        "Hard": "hard",
        "Expert": "expert"
      }
    )
    self.widgets[key].pack(anchor=E)

    return self,settings
