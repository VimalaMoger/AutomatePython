import FreeSimpleGUI as sg
import length

label1 = sg.Text("Enter a task: ")
input_box1 = sg.InputText(tooltip='text', key='keyValue1')

choose_button = sg.Button("Add")

list_box = sg.Listbox(values=length.get_data(), key="todos",
                      enable_events=True, size=[30, 10])

edit_button = sg.Button("Edit")
window = sg.Window("Converter",
                   layout=[[label1], [[input_box1, choose_button]], [list_box, edit_button]],
                   font=('Helvetica', 10))
#event = window.read()
#print(event)
# event, values = window.read()
# print(event)
# print(values)
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case 'Add':
            data = length.get_data()
            print(data)
            newData = values['keyValue1'] + "\n"
            data.append(newData)
            length.write_todos(data)
            window['todos'].update(values=data)
        case 'Edit':
            to_edit = values['todos'][0]
            newData = values['keyValue1']
            todos = length.get_data()
            index = todos.index(to_edit)
            todos[index] = newData
            length.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['keyValue1'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()
