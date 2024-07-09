import FreeSimpleGUI as sg
label =  sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
button = sg.Button("Add")
window = sg.Window('MY App to todo', layout=[[label], [input_box, button]])
window.read()
print('hello')
window.close()