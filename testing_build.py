import PySimpleGUI as sg
import images as img
from functions_body import OperationsBody as func
from interface import Interface as prog_face


# Создание окна
# window = sg.Window('Обрезатель первых строк в файлах', layout_folder)
window = sg.Window("LinesDeleter", prog_face.window_tabs)


# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == '-CLOSE-' or event == '-CLOSE_F-':
        break

    # Блок ввода "Количество удаляемых строк"
    if event == '-STRINGS-':
        try:
            strings = int(values['-STRINGS-']) - 1
            if strings == (-1):
                raise ValueError
        except:
            sg.Popup('Следует ввести число от 1', title='Ошибка', icon=img.warning_img)
            window['-STRINGS-']('')

    if event == '-STRINGS_F-':
        try:
            strings_file = int(values['-STRINGS_F-']) - 1
            if strings_file == (-1):
                raise ValueError
        except:
            sg.Popup('Следует ввести число от 1', title='Ошибка', icon=img.warning_img)
            window['-STRINGS_F-']('')

    state = window.Element('-CHECKBOX-').get()  # Переменная состояния чекбокса "Сменить расширение"

    if event == '-CHECKBOX-':
        if state is True:
            window.Element('-TOGGLE_AFTER-').Update(visible=True)
            window.Element('-FROM-').Update(visible=True)
            window.Element('-EXTENSION_1-').Update(visible=True)
            window.Element('-TO-').Update(visible=True)
            window.Element('-EXTENSION_2-').Update(visible=True)
            window.Element('-REMARK-').Update(visible=True)
            window.Element('-TOGGLE_TEXT-').Update(visible=True)
        else:
            window.Element('-TOGGLE_AFTER-').Update(visible=False)
            window.Element('-FROM-').Update(visible=False)
            window.Element('-EXTENSION_1-').Update(visible=False)
            window.Element('-TO-').Update(visible=False)
            window.Element('-EXTENSION_2-').Update(visible=False)
            window.Element('-REMARK-').Update(visible=False)
            window.Element('-TOGGLE_TEXT-').Update(visible=False)

    if '-CLEAR-' in event:
        window['-OLD_FOLDER-']('')
        window['-FILE-']('')
        window['-NEW_FOLDER-']('')
        window['-FOLDER_FOR_FILE-']('')
        window['-STRINGS-']('')
        window['-STRINGS_F-']('')
        if state == True:
            window['-EXTENSION_1-']('')
            window['-EXTENSION_2-']('')
            window['-EXTENSION_1F-']('')
            window['-EXTENSION_2F-']('')

    if event == '-TOGGLE_AFTER-':
        window['-TOGGLE_AFTER-'].metadata = not window['-TOGGLE_AFTER-'].metadata
        window['-TOGGLE_AFTER-'].update(
            image_data=img.toggle_btn_on if window['-TOGGLE_AFTER-'].metadata else img.toggle_btn_off)

    if event == '-TOGGLE_DELETE-':
        window['-TOGGLE_DELETE-'].metadata = not window['-TOGGLE_DELETE-'].metadata
        window['-TOGGLE_DELETE-'].update(
            image_data=img.toggle_btn_on if window['-TOGGLE_DELETE-'].metadata else img.toggle_btn_off)

    if event == '-TOGGLE-GRAPHIC-':
        window['-TOGGLE-GRAPHIC-'].metadata = not window['-TOGGLE-GRAPHIC-'].metadata
        window['-TOGGLE-GRAPHIC-'].update(image_data=img.toggle_btn_on if window['-TOGGLE-GRAPHIC-'].metadata else img.toggle_btn_off)
        if window['-TOGGLE-GRAPHIC-'].metadata is True:
            window.Element('-FROM_F-').Update(visible=True)
            window.Element('-EXTENSION_1F-').Update(visible=True)
            window.Element('-TO_F-').Update(visible=True)
            window.Element('-EXTENSION_2F-').Update(visible=True)
            window.Element('-REMARK_F-').Update(visible=True)
        else:
            window.Element('-FROM_F-').Update(visible=False)
            window.Element('-EXTENSION_1F-').Update(visible=False)
            window.Element('-TO_F-').Update(visible=False)
            window.Element('-EXTENSION_2F-').Update(visible=False)
            window.Element('-REMARK_F-').Update(visible=False)

    ex_1 = values['-EXTENSION_1-']
    ex_2 = values['-EXTENSION_2-']
    old_folder = values['-OLD_FOLDER-']
    new_folder = values['-NEW_FOLDER-']

# Блок работы со вкладкой "Папка"
    if event == '-FUNCTION-':

        # Изменение только расширения файлов в исходной или новой папках
        if state is True and values['-STRINGS-'] == '':
            try:
                func.extension_change_body(old_folder, ex_1, ex_2, new_folder)
            except:
                sg.PopupOK('Укажите корректный путь к папке и расширения!', title='Ошибка', icon=img.warning_img)

        # Удаление строк в файле с сохранением расширения
        if values['-STRINGS-'] != '' and window['-TOGGLE_AFTER-'].metadata is False:
            try:
                func.program_body(old_folder,new_folder, strings)
                func.extension_change_body(old_folder, ex_1, ex_2)
            except:
                sg.PopupOK('Проверьте корректность введенных данных!', title='Ошибка', icon=img.warning_img)

        # Удаление строк в файле с изменением расширения
        if values['-STRINGS-'] != '' and window['-TOGGLE_AFTER-'].metadata is True:
            try:
                func.program_body(old_folder, new_folder, strings)
                func.extension_change_body(new_folder, ex_1, ex_2)
            except:
                sg.PopupOK('Проверьте корректность введенных данных!', title='Ошибка', icon=img.warning_img)

    ex_1f = values['-EXTENSION_1F-']
    ex_2f = values['-EXTENSION_2F-']
    folder_for_file = values['-FOLDER_FOR_FILE-']
    file = values['-FILE-']

# Блок работы со вкладкой "Файл"
    if event == '-FUNCTION_FILE-':

        if values['-STRINGS_F-'] == '' and file != '' and window['-TOGGLE-GRAPHIC-'].metadata is True:
            try:
                func.extension_change_file(file, ex_1f, ex_2f, folder_for_file)
            except:
                sg.PopupOK('Укажите файл и расширение для изменения!', title='Ошибка', icon=img.warning_img)

        if values['-STRINGS_F-'] != '' and file != '':
            try:
                func.cut_lines_in_file(file, strings_file, folder_for_file)
                if window['-TOGGLE-GRAPHIC-'].metadata is True:
                    func.extension_change_file(file, ex_1f, ex_2f, folder_for_file)
            except:
                sg.PopupOK('Укажите корректный путь к файлу (папке)!', title='Ошибка', icon=img.warning_img)

window.close()
