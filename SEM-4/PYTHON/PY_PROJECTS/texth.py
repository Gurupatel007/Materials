import pywhatkit as pw
# import cv2 
text=''' 
NAME:GURU PATEL
EN.NO:21012011074


1). What is the role of Tkinter in python?
Tkinter is a Python binding to the Tk GUI toolkit. It is the standard Python interface to the Tk GUI toolkit, 
and is Python’s de facto standard GUI. Tkinter is included with standard Linux, Microsoft Windows and 
macOS installs of Python1
.
Tkinter provides several standard GUI widgets such as buttons, labels, text boxes, etc. that can be used 
to create graphical user interfaces2
. It also provides several other features such as event handling, 
geometry management, etc
2. Explain Tkinter Widgets: Button, Label, Entry, Radio button, Check button, Scale, Scroll bar, Listbox, 
Combo box, Frame, Message, Toplevel, Spinbox, Menubutton and Menu
→ Tkinter is a Python library for creating graphical user interfaces (GUIs). It provides a wide range of 
widgets that can be used to create buttons, labels, text entry boxes, radio buttons, checkboxes, scales, 
scrollbars, listboxes, combo boxes, frames, messages, toplevel windows, spinboxes, menubuttons, and 
menus.
Here is a brief explanation of each of these widgets:
1. Button: A button is a rectangular widget that can be clicked to trigger a specific action.
2. Label: A label is a widget that displays text or an image. It is used to provide information to the 
user.
3. Entry: An entry widget is used to allow the user to enter or edit a single line of text.
4. Radio button: A radio button is a widget that allows the user to select one option from a group 
of options.
5. Check button: A check button is a widget that allows the user to select one or more options 
from a group of options.
6. Scale: A scale widget is used to select a value from a range of values.
7. Scroll bar: A scroll bar is a widget that allows the user to scroll through a long list or text box.
8. Listbox: A listbox is a widget that displays a list of items from which the user can select one or 
more.
9. Combo box: A combo box is a widget that combines the functionality of an entry widget and a 
listbox. It allows the user to select an option from a list or enter a new option.
10. Frame: A frame is a widget that provides a container for other widgets. It is used to group 
related widgets together.
'''

pw.text_to_handwriting(text,save_to='demo1.jpeg')
print(" END ")