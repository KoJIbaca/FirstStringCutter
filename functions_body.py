import os, shutil
import PySimpleGUI as sg
import images as img
import chardet
import re


def decode_func(file):
    rawdata = file.read()
    result = chardet.detect(rawdata)
    charenc = result['encoding']
    return charenc


class OperationsBody:

    # Изменение расширения у файлов в папке
    def extension_change_body(folder_path, ex1, ex2, new_folder_path=''):
        try:
            for filename in os.listdir(folder_path):
                old_file_folder = os.path.join(folder_path, filename)
                if not os.path.isfile(old_file_folder): continue
                if new_folder_path == '':
                    newname = old_file_folder.replace(f'.{ex1}', f'.{ex2}')
                    os.rename(old_file_folder, newname)
                else:
                    shutil.copy(old_file_folder, new_folder_path)
                    new_folder_files = os.path.join(new_folder_path, filename)
                    name = new_folder_files.replace(f'.{ex1}', f'.{ex2}')
                    os.rename(new_folder_files, name)
        except FileNotFoundError:
            sg.PopupOK('Проверьте корректность введенных данных!', title='Ошибка', icon=img.warning_img)
        except UnicodeDecodeError:
            sg.PopupOK('Проблема с декодированием файлов!', title='Ошибка', icon=img.warning_img)
        except:
            sg.PopupOK(f'Что-то пошло не так!', title='Ошибка', icon=img.warning_img)
        sg.PopupOK('Расширение файлов в папке успешно изменено!', title='Успешно', icon=img.accept_img)

    # Удаление определенных строк
    def delete_line_or_lines(folder_path, line_from, line_to, new_folder=''):
        try:
            for files in os.listdir(folder_path):
                with open(rf'{folder_path}' + '/' + files, 'rb') as file_to_replace:
                    rawdata = file_to_replace.read()
                    result = chardet.detect(rawdata)
                    charenc = result['encoding']
                    file_to_replace.close()
                    with open(f'{folder_path}' + '/' + files, 'r', encoding=charenc) as file_to_edit:
                        lines = file_to_edit.readlines()
                        if line_from == -1:
                            first_str_var = lines[line_to:]
                        elif line_from == line_to:
                            first_str_var = lines[line_from]
                        else:
                            lines_1 = lines[:line_from]
                            lines_2 = lines[line_to:]
                            first_str_var = lines_1 + lines_2
                        with open(f'{folder_path}' + '/' + files, 'w', encoding=charenc) as old_file:
                            old_file.writelines(first_str_var)
        except FileNotFoundError:
            sg.PopupOK('Укажите корректный путь к файлам/папке!', title='Ошибка', icon=img.warning_img)
        except UnicodeDecodeError:
            sg.PopupOK('Проблема с декодированием файлов!', title='Ошибка', icon=img.warning_img)
        except:
            sg.PopupOK(f'Что-то пошло не так!', title='Ошибка', icon=img.warning_img)

    def sub_and_case_body(sub, case, txt_fragment, replace_text, file_text):
        if sub == 0 and case == 1:
            new_data = re.sub(rf'\b{txt_fragment}\b', replace_text, file_text, flags=re.I)
        elif sub == 1 and case == 1:
            new_data = re.sub(txt_fragment, replace_text, file_text, flags=re.I)
        elif sub == 0 and case == 0:
            new_data = re.sub(rf'\b{txt_fragment}\b', replace_text, file_text)
        else:
            new_data = file_text.replace(txt_fragment, replace_text)
        return new_data

    # Замена(удаление) текста из файлов папки
    def replace_or_delete_text_in_files(folder_path, txt_fragment, sub, case, replace_text='', new_file_folder=''):
        try:
            for files in os.listdir(fr'{folder_path}'):
                file_to_replace = open(f'{folder_path}' + '/' + files, 'rb')
                rawdata = file_to_replace.read()
                result = chardet.detect(rawdata)
                charenc = result['encoding']
                file_to_replace.close()
                with open(f'{folder_path}' + '/' + files, 'r+', encoding=charenc) as encoding_file:
                    read_file = encoding_file.read()
                    if new_file_folder != '':
                        with open(fr'{new_file_folder}' + '/' + files, 'w', encoding=charenc) as new_file:
                            new_data = OperationsBody.sub_and_case_body(sub, case, txt_fragment, replace_text,
                                                                        read_file)
                            new_file.write(new_data)
                    else:
                        with open(f'{folder_path}' + '/' + files, 'w') as old_new_file:
                            new_text = OperationsBody.sub_and_case_body(sub, case, txt_fragment, replace_text,
                                                                        read_file)
                            old_new_file.write(new_text)
            sg.PopupOK('Текст успешно обработан!', title='Успешно', icon=img.accept_img)
        except FileNotFoundError:
            sg.PopupOK('Укажите корректный путь к файлам/папке!', title='Ошибка', icon=img.warning_img)
        except UnicodeDecodeError:
            sg.PopupOK('Проблема с декодированием файлов!', title='Ошибка', icon=img.warning_img)
        except:
            sg.PopupOK(f'Что-то пошло не так!', title='Ошибка', icon=img.warning_img)

    # Удаление строк в файлах папки
    def delete_line_or_lines_in_file(file_path, line_from, line_to, new_folder=''):
        try:
            with open(rf'{file_path}', 'rb') as file_to_replace:
                rawdata = file_to_replace.read()
                result = chardet.detect(rawdata)
                charenc = result['encoding']
                file_to_replace.close()
                with open(f'{file_path}', 'r', encoding=charenc) as file_to_edit:
                    lines = file_to_edit.readlines()
                    if line_from == -1:
                        first_str_var = lines[line_to:]
                    elif line_from == line_to:
                        first_str_var = lines[line_from]
                    else:
                        lines_1 = lines[:line_from]
                        lines_2 = lines[line_to:]
                        first_str_var = lines_1 + lines_2
                    with open(f'{file_path}', 'w', encoding=charenc) as old_file_write:
                        old_file_write.writelines(first_str_var)
        except FileNotFoundError:
            sg.PopupOK('Укажите корректный путь к файлам/папке!', title='Ошибка', icon=img.warning_img)
        except UnicodeDecodeError:
            sg.PopupOK('Проблема с декодированием файлов!', title='Ошибка', icon=img.warning_img)
        except:
            sg.PopupOK(f'Что-то пошло не так!', title='Ошибка', icon=img.warning_img)

    # Замена(удаление) текста в файле
    def replace_or_delete_txt_in_file(file, txt_fragment, sub, case, replace_text='', folder_for_file=''):
        try:
            file_to_replace = open(f'{file}', 'rb')
            rawdata = file_to_replace.read()
            result = chardet.detect(rawdata)
            charenc = result['encoding']
            file_to_replace.close()
            with open(f'{file}', 'r', encoding=charenc) as encoding_file:
                read_file = encoding_file.read()
                with open(f'{file}', 'w', encoding=charenc) as old_file:
                    new_text = OperationsBody.sub_and_case_body(sub, case, txt_fragment, replace_text, read_file)
                    old_file.write(new_text)
            sg.PopupOK('Текст успешно обработан!', title='Успешно', icon=img.accept_img)
        except FileNotFoundError:
            sg.PopupOK('Укажите корректный путь к файлам/папке!', title='Ошибка', icon=img.warning_img)
        except UnicodeDecodeError:
            sg.PopupOK('Проблема с декодированием файлов!', title='Ошибка', icon=img.warning_img)
        except:
            sg.PopupOK(f'Что-то пошло не так!', title='Ошибка', icon=img.warning_img)

    # Изменение расширения файла
    def extension_change_file(file_path, ex1, ex2, new_folder_for_file=''):
        try:
            newfile = file_path.replace(f'.{ex1}', f'.{ex2}')
            os.rename(file_path, newfile)
            sg.PopupOK('Расширение файла успешно изменено!', title='Успешно', icon=img.accept_img)
        except FileNotFoundError:
            sg.PopupOK('Укажите корректный путь к файлам/папке!', title='Ошибка', icon=img.warning_img)
        except UnicodeDecodeError:
            sg.PopupOK('Проблема с декодированием файлов!', title='Ошибка', icon=img.warning_img)
        except:
            sg.PopupOK(f'Что-то пошло не так!', title='Ошибка', icon=img.warning_img)
