import os
import shutil
import PySimpleGUI as sg
import images as img
from functions_body import OperationsBody as func
from interface import Interface as prog_face


# Создание окна
window = sg.Window("LinesDeleter", prog_face.window_tabs)
toggle = toggle_in = True
checkbox_toggle = True

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == '-CLOSE-' or event == '-CLOSE_F-':
        break

    # Блок ввода "Количество удаляемых строк" вкладка "Папка"
    if event == '-STRINGS-':
        try:
            strings = int(values['-STRINGS-']) - 1
            if strings == (-1):
                raise ValueError
        except:
            sg.Popup('Следует ввести число от 1', title='Ошибка', icon=img.warning_img)
            window['-STRINGS-']('')

    if event == '-STRINGS_FROM-':
        try:
            strings_from = int(values['-STRINGS_FROM-']) - 1
            if strings_from == (-1):
                raise ValueError
        except:
            sg.Popup('Следует ввести число от 1', title='Ошибка', icon=img.warning_img)
            window['-STRINGS_FROM-']('')

    if event == '-STRINGS_TO-':
        try:
            strings_to = int(values['-STRINGS_TO-'])
        except:
            sg.Popup('Следует ввести число от 1', title='Ошибка', icon=img.warning_img)
            window['-STRINGS_TO-']('')

    # Блок проверки ввода числового значения в поля "с" и "по" на вкладке "Файл"
    if event == '-STRINGS_FROM_F-':
        try:
            strings_from_f = int(values['-STRINGS_FROM_F-']) - 1
            if strings_from_f == (-1):
                raise ValueError
        except:
            sg.Popup('Следует ввести число от 1', title='Ошибка', icon=img.warning_img)
            window['-STRINGS_FROM_F-']('')

    if event == '-STRINGS_TO_F-':
        try:
            strings_to_f = int(values['-STRINGS_TO_F-'])
        except:
            sg.Popup('Следует ввести число от 1', title='Ошибка', icon=img.warning_img)
            window['-STRINGS_TO_F-']('')

    state = window.Element('-CHECKBOX-').get()  # Переменная состояния чекбокса "Сменить расширение"

    if event == '-CHECKBOX-':
        if state is True:
            window['-FROM-'].update(visible=checkbox_toggle)
            window['-EXTENSION_1-'].update(visible=checkbox_toggle)
            window['-TO-'].update(visible=checkbox_toggle)
            window['-EXTENSION_2-'].update(visible=checkbox_toggle)
            window['-REMARK-'].update(visible=checkbox_toggle)
            checkbox_toggle = not checkbox_toggle
        else:
            window['-FROM-'].update(visible=not window['-FROM-'].visible)
            window['-EXTENSION_1-'].update(visible=not window['-EXTENSION_1-'].visible)
            window['-TO-'].update(visible=not window['-TO-'].visible)
            window['-EXTENSION_2-'].update(visible=not window['-EXTENSION_2-'].visible)
            window['-REMARK-'].update(visible=not window['-REMARK-'].visible)
            checkbox_toggle = not checkbox_toggle

    if '-CLEAR-' in event:
        window['-OLD_FOLDER-']('')
        window['-FILE-']('')
        window['-NEW_FOLDER-']('')
        window['-FOLDER_FOR_FILE-']('')
        window['-MULTILINE-']('')
        window['-MULTILINE_REPLACE-']('')
        window['-MULTILINE_F-']('')
        window['-MULTILINE_REPLACE_F-']('')
        window['-STRINGS_TO_F-']('')
        window['-STRINGS_FROM-']('')
        window['-STRINGS_FROM_F-']('')
        window['-STRINGS_TO-']('')
        if state is True:
            window['-EXTENSION_1-']('')
            window['-EXTENSION_2-']('')
        if window['-TOGGLE-GRAPHIC-'].metadata is True:
            window['-EXTENSION_1F-']('')
            window['-EXTENSION_2F-']('')

    if event == '-TOGGLE_AFTER-':
        window['-TOGGLE_AFTER-'].metadata = not window['-TOGGLE_AFTER-'].metadata
        window['-TOGGLE_AFTER-'].update(
            image_data=img.toggle_btn_on if window['-TOGGLE_AFTER-'].metadata else img.toggle_btn_off)

    if event == '-TOGGLE-GRAPHIC-':
        window['-TOGGLE-GRAPHIC-'].metadata = not window['-TOGGLE-GRAPHIC-'].metadata
        window['-TOGGLE-GRAPHIC-'].update(image_data=img.toggle_btn_on if window['-TOGGLE-GRAPHIC-'].metadata else img.toggle_btn_off)
        if window['-TOGGLE-GRAPHIC-'].metadata is True:
            window['-FROM_F-'].update(visible=toggle)
            window['-EXTENSION_1F-'].update(visible=toggle, disabled=False)
            window['-TO_F-'].update(visible=toggle)
            window['-EXTENSION_2F-'].update(visible=toggle, disabled=False)
            window['-REMARK_F-'].update(visible=toggle)
            toggle = not toggle
        else:
            window['-FROM_F-'].update(visible=not window['-FROM_F-'].visible)
            window['-EXTENSION_1F-'].update(visible=not window['-EXTENSION_1F-'].visible, disabled=True)
            window['-TO_F-'].update(visible=not window['-TO_F-'].visible)
            window['-EXTENSION_2F-'].update(visible=not window['-EXTENSION_2F-'].visible, disabled=True)
            window['-REMARK_F-'].update(visible=not window['-REMARK_F-'].visible)
            toggle = not toggle

    if event == '-TOGGLE_SUBSTRING-':
        window['-TOGGLE_SUBSTRING-'].metadata = not window['-TOGGLE_SUBSTRING-'].metadata
        window['-TOGGLE_SUBSTRING-'].update(image_data=img.toggle_btn_on if window['-TOGGLE_SUBSTRING-'].metadata else img.toggle_btn_off)

    if event == '-TOGGLE_SUBSTRING_F-':
        window['-TOGGLE_SUBSTRING_F-'].metadata = not window['-TOGGLE_SUBSTRING_F-'].metadata
        window['-TOGGLE_SUBSTRING_F-'].update(image_data=img.toggle_btn_on if window['-TOGGLE_SUBSTRING_F-'].metadata else img.toggle_btn_off)

    if event == '-TOGGLE_TXT_CASE-':
        window['-TOGGLE_TXT_CASE-'].metadata = not window['-TOGGLE_TXT_CASE-'].metadata
        window['-TOGGLE_TXT_CASE-'].update(image_data=img.toggle_btn_on if window['-TOGGLE_TXT_CASE-'].metadata else img.toggle_btn_off)

    if event == '-TOGGLE_TXT_CASE_F-':
        window['-TOGGLE_TXT_CASE_F-'].metadata = not window['-TOGGLE_TXT_CASE_F-'].metadata
        window['-TOGGLE_TXT_CASE_F-'].update(image_data=img.toggle_btn_on if window['-TOGGLE_TXT_CASE_F-'].metadata else img.toggle_btn_off)

    # Блок смены текста местами
    if event == '-CHANGE_TXT-':
        first_field = values['-MULTILINE-']
        second_field = values['-MULTILINE_REPLACE-']
        window['-MULTILINE-'].Update(value=second_field)
        window['-MULTILINE_REPLACE-'].Update(value=first_field)

    if event == '-CHANGE_TXT_F-':
        first_field = values['-MULTILINE_F-']
        second_field = values['-MULTILINE_REPLACE_F-']
        window['-MULTILINE_F-'].Update(value=second_field)
        window['-MULTILINE_REPLACE_F-'].Update(value=first_field)

    ex_1 = values['-EXTENSION_1-']
    ex_2 = values['-EXTENSION_2-']
    old_folder = values['-OLD_FOLDER-']
    new_folder = values['-NEW_FOLDER-']
    txt_fragment = (values['-MULTILINE-']).strip()
    replace_txt = values['-MULTILINE_REPLACE-']

# Блок работы со вкладкой "Папка"
    if event == '-FUNCTION-':

        if old_folder != '' and new_folder != '':
            try:
                if os.path.isdir(new_folder) is True and os.path.isdir(old_folder) is True:
                    for filename in os.listdir(old_folder):
                        old_file_folder = os.path.join(old_folder, filename)
                        shutil.copy(old_file_folder, new_folder)
                        new_folder_files = os.path.join(new_folder, filename)

                    # Удаление строк в папке файла
                    if values['-STRINGS_FROM-'] != '' and values['-STRINGS_TO-'] != '':
                        strings_from = int(values['-STRINGS_FROM-'] or -1)
                        strings_to = int(values['-STRINGS_TO-'] or -1)
                        try:
                            if values['-STRINGS_FROM-'] <= values['-STRINGS_TO-']:
                                func.delete_line_or_lines(new_folder, (strings_from-1), strings_to)
                            else:
                                raise ArithmeticError
                        except ArithmeticError:
                            sg.PopupOK('Значение в поле "с" должно быть меньше или равно значению в поле "по"!',
                                       title='Ошибка', icon=img.warning_img)
                        # else:
                        #     func.delete_line_or_lines(old_folder, (strings_from-1), strings_to, new_folder)
                        sg.PopupOK(f'Строки в файлах успешно обработаны!', title='Успешно', icon=img.accept_img)

                    # Удаление/замена фрагмента текста файлов в папке
                    if txt_fragment != '':
                        case, sub = 0, 0
                        if window['-TOGGLE_TXT_CASE-'].metadata is True:
                            case = 1
                        if window['-TOGGLE_SUBSTRING-'].metadata is True:
                            sub = 1
                        func.replace_or_delete_text_in_files(new_folder, txt_fragment, sub, case, replace_txt)

                    # Изменение только расширения файлов в исходной или новой папках
                    if state is True:
                        func.extension_change_body(new_folder, ex_1, ex_2)
                else:
                    raise FileNotFoundError
            except FileNotFoundError:
                sg.PopupOK('Укажите верный путь к папке!', title='Ошибка', icon='img.warning_img')

        else:

            # Удаление строк в папке файла
            if values['-STRINGS_FROM-'] != '' or values['-STRINGS_TO-'] != '':
                strings_from = int(values['-STRINGS_FROM-'] or -1)
                strings_to = int(values['-STRINGS_TO-'] or -1)
                if values['-STRINGS_FROM-'] != '' and values['-STRINGS_TO-'] != '':
                    try:
                        if values['-STRINGS_FROM-'] <= values['-STRINGS_TO-']:
                            func.delete_line_or_lines(old_folder, (strings_from - 1), strings_to)
                        else:
                            raise ArithmeticError
                    except:
                        sg.PopupOK('Значение в поле "с" должно быть меньше или равно значению в поле "по"!',
                                   title='Ошибка', icon=img.warning_img)
                else:
                    func.delete_line_or_lines(old_folder, (strings_from - 1), strings_to)
                sg.PopupOK(f'Строки в файлах успешно обработаны!', title='Успешно', icon=img.accept_img)

            # Удаление/замена фрагмента текста файлов в папке
            if txt_fragment != '' and old_folder != '':
                case, sub = 0, 0
                if window['-TOGGLE_TXT_CASE-'].metadata is True:
                    case = 1
                if window['-TOGGLE_SUBSTRING-'].metadata is True:
                    sub = 1
                func.replace_or_delete_text_in_files(old_folder, txt_fragment, sub, case, replace_txt)

            # Изменение только расширения файлов в исходной или новой папках
            if state is True and old_folder != '':
                try:
                    func.extension_change_body(old_folder, ex_1, ex_2)
                except:
                    sg.PopupOK('Укажите корректный путь к папке и расширения!', title='Ошибка', icon=img.warning_img)

    # Переменные вкладки "Файл"
    ex_1f = values['-EXTENSION_1F-']
    ex_2f = values['-EXTENSION_2F-']
    folder_for_file = values['-FOLDER_FOR_FILE-']
    file = values['-FILE-']
    txt_fragment_f = (values['-MULTILINE_F-']).strip()
    replace_txt_f = values['-MULTILINE_REPLACE_F-']

    # Блок работы со вкладкой "Файл"
    if event == '-FUNCTION_FILE-':

        if file != '' and folder_for_file != '':
            try:
                if os.path.isdir(folder_for_file) is True:
                    shutil.copy(file, folder_for_file)
                    filename = os.path.basename(file)
                    new_file = os.path.join(folder_for_file, filename)

                    if values['-STRINGS_FROM_F-'] or values['-STRINGS_TO_F-']:
                        strings_from_f = int(values['-STRINGS_FROM_F-'] or -1)
                        strings_to_f = int(values['-STRINGS_TO_F-'] or -1)
                        try:
                            if strings_from_f <= strings_to_f:
                                func.delete_line_or_lines_in_file(new_file, (strings_from_f - 1), strings_to_f)
                            else:
                                raise ArithmeticError
                        except ArithmeticError:
                            sg.PopupOK('Значение в поле "с" должно быть меньше или равно значению в поле "по"!',
                                       title='Ошибка', icon=img.warning_img)
                        sg.PopupOK(f'Строки в файлах успешно обработаны!', title='Успешно', icon=img.accept_img)

                    if values['-MULTILINE_F-'] != '':
                        case_f, sub_f = 0, 0
                        if window['-TOGGLE_TXT_CASE_F-'].metadata is True:
                            case_f = 1
                        if window['-TOGGLE_SUBSTRING_F-'].metadata is True:
                            sub_f = 1
                        func.replace_or_delete_txt_in_file(new_file, txt_fragment_f, sub_f, case_f, replace_txt_f)

                    if window['-TOGGLE-GRAPHIC-'].metadata is True and ex_1f != '' and ex_2f != '':
                        try:
                            func.extension_change_file(new_file, ex_1f, ex_2f)
                        except:
                            sg.PopupOK('Проверьте правильность введенных данных!', title='Ошибка', icon=img.warning_img)
                else:
                    raise FileNotFoundError
            except FileNotFoundError:
                sg.PopupOK('Укажите верный путь к папке!', title='Ошибка', icon=img.warning_img)

        else:

            # Блок удаления строк в файле
            if file != '' and (values['-STRINGS_FROM_F-'] or values['-STRINGS_TO_F-']):
                strings_from_f = int(values['-STRINGS_FROM_F-'] or -1)
                strings_to_f = int(values['-STRINGS_TO_F-'] or -1)
                if values['-STRINGS_FROM_F-'] != '' and values['-STRINGS_TO_F-'] != '':
                    try:
                        if strings_from_f <= strings_to_f:
                            func.delete_line_or_lines_in_file(file, (strings_from_f-1), strings_to_f)
                        else:
                            raise ArithmeticError
                    except ArithmeticError:
                        sg.PopupOK('Значение в поле "с" должно быть меньше или равно значению в поле "по"!',
                                   title='Ошибка', icon=img.warning_img)
                else:
                    func.delete_line_or_lines_in_file(file, (strings_from_f-1), strings_to_f)
                sg.PopupOK(f'Строки в файлах успешно обработаны!', title='Успешно', icon=img.accept_img)

            # Блок работы с фрагментом текста в файле
            if values['-MULTILINE_F-'] != '' and file != '':
                case_f, sub_f = 0, 0
                if window['-TOGGLE_TXT_CASE_F-'].metadata is True:
                    case_f = 1
                if window['-TOGGLE_SUBSTRING_F-'].metadata is True:
                    sub_f = 1
                func.replace_or_delete_txt_in_file(file, txt_fragment_f, sub_f, case_f, replace_txt_f)

            # Изменение расширения файла
            if window['-TOGGLE-GRAPHIC-'].metadata is True and ex_1f != '' and ex_2f != '' and file != '':
                try:
                    func.extension_change_file(file, ex_1f, ex_2f)
                except:
                    sg.PopupOK('Проверьте правильность введенных данных!', title='Ошибка', icon=img.warning_img)

window.close()
