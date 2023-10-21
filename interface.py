import PySimpleGUI as sg
import images as img


class Interface:

    sg.theme('DarkBlue14')

    text_multiline = [sg.T('Исходный фрагмент текста', size=(26, 1), justification="left top")]
    text_replace = [sg.T('Фрагмент текста на замену', size=(26, 1), justification="left top")]
    delete_toggle = [sg.Button(image_data=img.toggle_btn_off, key='-TOGGLE_DELETE-', enable_events=True,
                               button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0,
                               metadata=False), sg.T('Удалить', font='Calibri 9')]
    replace_toggle = [sg.Button(image_data=img.toggle_btn_off, key='-TOGGLE_REPLACE-', enable_events=True,
                                button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0,
                                metadata=False), sg.T('Заменить', font='Calibri 9')]
    text_case_toggle = [sg.Button(image_data=img.toggle_btn_off, key='-TOGGLE_TXT_CASE-', enable_events=True,
                                  button_color=(sg.theme_background_color(), sg.theme_background_color()),
                                  border_width=0, metadata=False),
                        sg.T('Игнорировать регистр', font='Calibri 9',
                             tooltip='Выполнить замену, игнорируя заглавные и строчные буквы')]
    replace_substring_toggle = [sg.Button(image_data=img.toggle_btn_off, key='-TOGGLE_SUBSTRING-', enable_events=True,
                                button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0,
                                metadata=False), sg.T('Выполнить замену подстрок', font='Calibri 9',
                                                      tooltip='Подстрока - часть текста входящая в слово, например: '
                                                              'поРУКА, РУКАв')]
    multiline_field = [sg.Multiline(size=(30, 4), key='-MULTILINE-')]
    replace_multiline = [sg.Multiline(size=(30, 4), key='-MULTILINE_REPLACE-')]
    multiline_field_f = [sg.Multiline(size=(30, 4), key='-MULTILINE_F-')]
    replace_multiline_f = [sg.Multiline(size=(30, 4), key='-MULTILINE_REPLACE_F-')]
    txt_multiline_f = [sg.T('Исходный фрагмент текста', size=(26, 1), justification="left top")]
    txt_replace_f = [sg.T('Фрагмент текста на замену', size=(26, 1), justification="left top")]
    txt_case_toggle_f = [sg.Button(image_data=img.toggle_btn_off, key='-TOGGLE_TXT_CASE_F-', enable_events=True,
                                  button_color=(sg.theme_background_color(), sg.theme_background_color()),
                                  border_width=0, metadata=False),
                         sg.T('Игнорировать регистр', font='Calibri 9',
                              tooltip='Выполнить замену, игнорируя заглавные и строчные буквы')]
    replace_substring_toggle_f = [sg.Button(image_data=img.toggle_btn_off, key='-TOGGLE_SUBSTRING_F-', enable_events=True,
                                            button_color=(sg.theme_background_color(), sg.theme_background_color()),
                                            border_width=0, metadata=False),
                                  sg.T('Выполнить замену подстрок', font='Calibri 9',
                                       tooltip='Подстрока - часть текста входящая в слово, например: поРУКА, РУКАв')]
    text_fragment_layout = [[sg.Column([text_multiline, multiline_field, text_case_toggle]),
                             sg.Button(image_data=img.change_texts, tooltip='Поменять текст местами',
                                       button_color=(sg.theme_background_color(), sg.theme_background_color()),
                                       border_width=0, key='-CHANGE_TXT-'),
                             sg.Column([text_replace, replace_multiline, replace_substring_toggle])]]
    txt_frame_layout_f = [[sg.Column([txt_multiline_f, multiline_field_f, txt_case_toggle_f]),
                           sg.Button(image_data=img.change_texts, tooltip='Поменять текст местами',
                                     button_color=(sg.theme_background_color(), sg.theme_background_color()),
                                     border_width=0, key='-CHANGE_TXT_F-'),
                           sg.Column([txt_replace_f, replace_multiline_f, replace_substring_toggle_f])]]
    delete_first_line_layout = [sg.Text('Удалить первые строки', font='Calibri 11', size=(20, 1),
                                        tooltip='Количество первых строк в файле для удаления'),
                                sg.InputText(size=(5, 1), enable_events=True, key='-STRINGS-')]
    lines_delete_frame_layout = [[sg.T('Удалить строки с', font='Calibri 11'),
                                  sg.InputText(size=(5, 1), enable_events=True, key='-STRINGS_FROM-',
                                               tooltip='номер строки с которой начать удаление'),
                                  sg.T('по', font='Calibri 11'),
                                  sg.InputText(size=(5, 1), enable_events=True, key='-STRINGS_TO-',
                                               tooltip='номер строки до которой следует удалить включительно')]]

    layout_folder = [
        [sg.Text('Папка с файлами для обработки', font='Calibri 11', size=(26, 1)),
         sg.Input(size=(34, 1), enable_events=True, key='-OLD_FOLDER-'),
         sg.FolderBrowse()],
        [sg.Text('Папка для обработанных файлов*', font='Calibri 11', size=(26, 1)),
         sg.Input(size=(34, 1), enable_events=True, key='-NEW_FOLDER-'),
         sg.FolderBrowse()],
        [sg.Text('*если необходимо', font='Calibri 9')],
        [sg.T('Удалить строки с', font='Calibri 11'),
         sg.InputText(size=(5, 1), enable_events=True, key='-STRINGS_FROM-',
                      tooltip='номер строки с которой начать удаление'),
         sg.T('по', font='Calibri 11'),
         sg.InputText(size=(5, 1), enable_events=True, key='-STRINGS_TO-',
                      tooltip='номер строки до которой следует удалить включительно')],
        [sg.T('', font='Calibri 11')],
        [sg.Frame('Работа с фрагментом текста', text_fragment_layout)],
        [sg.Checkbox('Сменить расширение файлов', enable_events=True, key='-CHECKBOX-')],
        [sg.pin(sg.Text('c', font='Calibri 11', visible=False, key='-FROM-')),
         sg.pin(sg.Input(size=(5, 1), enable_events=True, visible=False, key='-EXTENSION_1-')),
         sg.pin(sg.Text('на', font='Calibri 11', visible=False, key='-TO-')),
         sg.pin(sg.Input(size=(5, 1), enable_events=True, visible=False, key='-EXTENSION_2-'))],
        [sg.pin(sg.Text('*тип расширения вводить без точки (txt xml doc и т.д.)', font='Calibri 9', visible=False,
                        key='-REMARK-'))],
        [sg.Button('Выполнить', image_data=img.do_it_btn, button_color=('black', sg.theme_background_color()),
                   tooltip='Выполнить операцию', mouseover_colors=('white', sg.theme_background_color()),
                   border_width=0, enable_events=True, key='-FUNCTION-', font='Helvetica 10'),
         sg.Button('Сброс полей', image_data=img.clear_btn, tooltip='Очистить содержимое всех полей',
                   button_color=('white', sg.theme_background_color()),
                   mouseover_colors=('black', sg.theme_background_color()), border_width=0, font='Helvetica 10',
                   key='-CLEAR-'),
         sg.Button('Закрыть', key='-CLOSE-', button_color=('white', sg.theme_background_color()),
                   image_data=img.exit_btn, mouseover_colors=('black', sg.theme_background_color()), border_width=0,
                   font='Helvetica 10')]
    ]

    layout_files = [
        [sg.Text('Файл для обработки', font='Calibri 11', size=(26, 1)),
         sg.Input(size=(34, 1), enable_events=True, key='-FILE-'),
         sg.FileBrowse()],
        [sg.Text('Папка для обработанного файла*', font='Calibri 11', size=(26, 1)),
         sg.Input(size=(34, 1), enable_events=True, key='-FOLDER_FOR_FILE-'),
         sg.FolderBrowse()],
        [sg.Text('*если необходимо', font='Calibri 9')],
        [sg.T('Удалить строки с', font='Calibri 11'),
         sg.InputText(size=(5, 1), enable_events=True, key='-STRINGS_FROM_F-',
                      tooltip='номер строки с которой начать удаление'),
         sg.T('по', font='Calibri 11'),
         sg.InputText(size=(5, 1), enable_events=True, key='-STRINGS_TO_F-',
                      tooltip='номер строки до которой следует удалить включительно')],
        [sg.T('')],
        [sg.Frame('Работа с фрагментом текста', txt_frame_layout_f)],
        [sg.Text('Сменить расширение', font='Calibri 11'),
         sg.Button(image_data=img.toggle_btn_off, key='-TOGGLE-GRAPHIC-', enable_events=True,
                   button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0,
                   metadata=False)],
        [sg.pin(sg.Text('c', font='Calibri 11', visible=False, key='-FROM_F-')),
         sg.pin(sg.Input(size=(5, 1), enable_events=True, visible=False, disabled=True, key='-EXTENSION_1F-')),
         sg.pin(sg.Text('на', font='Calibri 11', visible=False, key='-TO_F-')),
         sg.pin(sg.Input(size=(5, 1), enable_events=True, visible=False, disabled=True, key='-EXTENSION_2F-'))],
        [sg.pin(sg.Text('*тип расширения вводить без точки (txt xml doc и т.д.)', font='Calibri 9',
                        visible=False, key='-REMARK_F-'))],
        [sg.Button('Выполнить', image_data=img.do_it_btn, button_color=('black', sg.theme_background_color()),
                   tooltip='Выполнить операцию', mouseover_colors=('white', sg.theme_background_color()),
                   border_width=0, enable_events=True, key='-FUNCTION_FILE-', font='Helvetica 10'),
         sg.Button('Сброс полей',  image_data=img.clear_btn, button_color=('white', sg.theme_background_color()),
                   tooltip='Очистить содержимое всех полей', mouseover_colors=('black', sg.theme_background_color()),
                   border_width=0, font='Helvetica 10', key='-CLEAR-'),
         sg.Button('Закрыть', key='-CLOSE_F-', image_data=img.exit_btn, button_color=('white', sg.theme_background_color()),
                   mouseover_colors=('black', sg.theme_background_color()), font='Helvetica 10', border_width=0,
                   tooltip='Закрыть программу')]
    ]

    layout_info = [[sg.Text('1. Программа предназначена для удаления и замены строк/текста в текстовых файлах\n'
                            'и изменения их расширения.\n'
                            '2. Работать можно как отдельно по каждой операции так и объединяя их.\n'
                            '3. Предусмотрена возможность работы как с одним файлом, так и с файлами в папке\n'
                            '4. Программа тестировалась на форматах txt, xml, doc, eml.\n'
                            '   За корректную работу с другими расширениями автор не ручается\n'
                            '5. Программа не является конвертером, а лишь меняет расширение файла(ов)\n'
                            '6. Для удаления фрагмента текста необходимо поле "Фрагмент текста на замену"\n'
                            'оставить пустым \n'
                            '7. При удалении слова/фрагмента текста на его месте остается пробел,\n'
                            'который следует удалить уже вручную\n'
                            '8. Программа не работает с файлами, в которых есть изображения внутри\n'
                            ' и выдаст оишбку.\n'
                            '9. Последовательность выполнения операций программой происходит согласно\n'                            
                            'интерфейса - сверху вниз\n'
                            '10. Не рекомендуется обрабатывать файлы с объемом более 10000 символов.\n'
                            'Возможны зависания ПК.\n\n'
                            'Открытый код и обновления: https://github.com/KoJIbaca/FirstStringCutter \n\n'
                            'Версия 1.5')]]

    window_tabs = [[sg.TabGroup([[sg.Tab('Папка', layout_folder),
                                  sg.Tab('Файл', layout_files),
                                  sg.Tab('Информация', layout_info)]], focus_color='white')]]
