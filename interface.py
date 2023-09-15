import PySimpleGUI as sg
import images as img

class Interface:

    sg.theme('DarkBlue14')

    layout_folder = [[sg.Text('Папка с файлами для обработки', font='Calibri 11', size=(26, 1)),
                        sg.Input(size=(25, 1), enable_events=True, key='-OLD_FOLDER-'),
                        sg.FolderBrowse()],
                [sg.Text('Папка для обработанных файлов', font='Calibri 11', size=(26, 1)),
                 sg.Input(size=(25, 1), enable_events=True, key='-NEW_FOLDER-'),
                 sg.FolderBrowse()],
                [sg.Text('Количество удаляемых строк', font='Calibri 11', size=(26, 1)),
                 sg.InputText(size=(10, 1), enable_events=True, key='-STRINGS-')],
                [sg.Checkbox('Сменить расширение файлов', enable_events=True, key='-CHECKBOX-')],
                [sg.Button(image_data=img.toggle_btn_off, key='-TOGGLE_AFTER-', visible=False, enable_events=True, button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0, metadata=False),
                sg.Text('после обработки', font='Calibri 9', visible=False, key='-TOGGLE_TEXT-')],
                [sg.Text('c', font='Calibri 11', visible=False, key='-FROM-'),
                 sg.Input(size=(5, 1), enable_events=True, visible=False, key='-EXTENSION_1-'),
                 sg.Text('на', font='Calibri 11', visible=False, key='-TO-'),
                 sg.Input(size=(5, 1), enable_events=True, visible=False, key='-EXTENSION_2-')],
                [sg.Text('*тип расширения вводить без точки (txt xml doc и т.д.)', font='Calibri 9', visible=False, key='-REMARK-')],
                [sg.Button('Выполнить', image_data=img.do_it_btn, button_color=('black', sg.theme_background_color()), tooltip = 'Выполнить операцию', mouseover_colors=('white', sg.theme_background_color()), border_width=0, enable_events=True, key='-FUNCTION-', font='Helvetica 10'),
                 sg.Button('Сброс полей', image_data=img.clear_btn, button_color=('white', sg.theme_background_color()), tooltip = 'Очистить содержимое всех полей', mouseover_colors=('black', sg.theme_background_color()), border_width=0, font='Helvetica 10', key='-CLEAR-'),
                 sg.Button('Закрыть', key ='-CLOSE-', image_data=img.exit_btn, button_color=('white', sg.theme_background_color()), mouseover_colors=('black', sg.theme_background_color()), border_width=0, font='Helvetica 10')]]

    layout_files = [  [sg.Text('Файл для обработки', font='Calibri 11', size=(26, 1)),
                       sg.Input(size=(25, 1), enable_events=True, key='-FILE-'),
                       sg.FileBrowse()],
                [sg.Text('Папка для обработанного файла*', font='Calibri 11', size=(26, 1)),
                 sg.Input(size=(25, 1), enable_events=True, key='-FOLDER_FOR_FILE-'),
                 sg.FolderBrowse()],
                [sg.Text('*если необходимо', font='Calibri 9')],
                [sg.Text('Количество удаляемых строк', font='Calibri 11', size=(26,1)),
                 sg.InputText(size=(10, 1), enable_events=True, key='-STRINGS_F-')],
                [sg.Text('Сменить расширение', font='Calibri 11'),
                 sg.Button(image_data=img.toggle_btn_off, key='-TOGGLE-GRAPHIC-', enable_events=True, button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0, metadata=False)],
                [sg.Text('c', font='Calibri 11', visible=False, key='-FROM_F-'),
                 sg.Input(size=(5, 1), enable_events=True, visible=False, key='-EXTENSION_1F-'),
                 sg.Text('на', font='Calibri 11', visible=False, key='-TO_F-'),
                 sg.Input(size=(5, 1), enable_events=True, visible=False, key='-EXTENSION_2F-')],
                [sg.Text('*тип расширения вводить без точки (txt xml doc и т.д.)', font='Calibri 9', visible=False, key='-REMARK_F-')],
                [sg.Button('Выполнить', image_data=img.do_it_btn, button_color=('black', sg.theme_background_color()), tooltip = 'Выполнить операцию', mouseover_colors=('white', sg.theme_background_color()), border_width=0, enable_events=True, key='-FUNCTION_FILE-', font='Helvetica 10'),
                 sg.Button('Сброс полей',  image_data=img.clear_btn, button_color=('white', sg.theme_background_color()), tooltip = 'Очистить содержимое всех полей', mouseover_colors=('black', sg.theme_background_color()), border_width=0, font='Helvetica 10', key='-CLEAR-'),
                 sg.Button('Закрыть', key='-CLOSE_F-', image_data=img.exit_btn, button_color=('white', sg.theme_background_color()), mouseover_colors=('black', sg.theme_background_color()), font='Helvetica 10', border_width=0, tooltip = 'Закрыть программу')] ]

    layout_info = [[sg.Text('1. Программа предназначена для удаления первых строк в текстовых файлах и\n'
                            'изменения их расширения.\n'
                            '2. Работать можно как отдельно по каждой операции так и объединяя их.\n'
                            '3. Предусмотрена возможность работы как с одним файлом, так и с папкой\n'
                            '4. Программа тестировалась на форматах txt, xml, doc, eml.\n'
                            '   За корректную работу с другими расширениями автор не ручается\n\n'
                            'Открытый код и обновления: https://github.com/KoJIbaca/FirstStringCutter \n\n'
                            'Версия 1.0')]]

    window_tabs = [[sg.TabGroup([[sg.Tab('Папка', layout_folder, tooltip='Обрезать строки в файлах папки'),
                        sg.Tab('Файл', layout_files, tooltip='Обрезать строки в файле'),
                        sg.Tab('Информация', layout_info, tooltip='Информация по работе')]])]]