import os, shutil
import PySimpleGUI as sg
import images as img
#
# for file_name in os.listdir("C:\\Users\K-31\Desktop\\folder"):
#     with open(r"C:\Users\K-31\Desktop\folder\\" + file_name, encoding="utf8") as oldfile, open(r"C:\Users\K-31\Desktop\new\\" + file_name, 'w', encoding="utf8") as newfile:
#         for line in oldfile:
#             lines = oldfile.readlines()
#             newfile.writelines(lines[6:])

class OperationsBody:

    # Удаление строк в файлах папки
    def program_body(oldfiles_folder_path, newfiles_folder_path, x):
        try:
            for file_name in os.listdir(oldfiles_folder_path):
                with open(rf"{oldfiles_folder_path}" + "/" + file_name, encoding="utf8") as oldfile, \
                        open(rf"{newfiles_folder_path}" + "/" + file_name, 'w', encoding="utf8") as newfile:
                    for line in oldfile:
                        lines = oldfile.readlines()
                        newfile.writelines(lines[x:])
            sg.PopupOK('Удаление строк выполнено успешно!', title='Успешно', icon=img.accept_img)
        except FileNotFoundError:
            sg.PopupOK('Проверьте корректность указанного пути!', title='Ошибка', icon=img.warning_img)

    # Изменение расширения у файлов в папке
    def extension_change_body(folder_path, ex1, ex2, new_folder_path=''):
        try:
            for filename in os.listdir(folder_path):
                old_file_folder = os.path.join(folder_path, filename)
                if not os.path.isfile(old_file_folder): continue
                if new_folder_path == '':
                    newname = old_file_folder.replace(f'.{ex1}', f'.{ex2}')
                    os.rename(old_file_folder, newname)
                    sg.PopupOK('Расширение файлов в папке успешно изменено!', title='Успешно', icon=img.accept_img)
                else:
                    shutil.copy(old_file_folder, new_folder_path)
                    new_folder_files = os.path.join(new_folder_path, filename)
                    name = new_folder_files.replace(f'.{ex1}', f'.{ex2}')
                    os.rename(new_folder_files, name)
                    sg.PopupOK('Файлы в папке успешно перемещены с изменением расширения!', title='Успешно', icon=img.accept_img)
        except FileNotFoundError:
            sg.PopupOK('Проверьте корректность введенных данных!', title='Ошибка', icon=img.warning_img)

    # Удаление строк в файле
    def cut_lines_in_file(file_2, num, folder_path=''):
        try:
            with open(rf'{file_2}', encoding="utf8") as file_old:
                if folder_path == '':
                    lines = file_old.readlines()
                    with open(rf'{file_2}', "w", encoding="utf8") as file_new:
                        file_new.writelines(lines[num:])
                    sg.PopupOK('Удаление строк в файле успешно выполнено!', title='Успешно', icon=img.accept_img)
                else:
                    name_file = os.path.basename(file_2)
                    file_new_path = os.path.join(folder_path, name_file)
                    lines = file_old.readlines()
                    with open(rf"{file_new_path}", "w", encoding="utf8") as new_file_path:
                        new_file_path.writelines(lines[num:])
                    sg.PopupOK('Файл успешно перемещен с удалением в нем строк!', title='Успешно', icon=img.accept_img)
        except:
            sg.PopupOK('Укажите корректное расположение файла и количество строк для удаления!', title='Ошибка', icon=img.warning_img)

    # Изменение расширения файла
    def extension_change_file(file_path, ex1, ex2, new_folder_for_file=''):
        try:
            if new_folder_for_file == '':
                newfile = file_path.replace(f'.{ex1}', f'.{ex2}')
                os.rename(file_path, newfile)
                sg.PopupOK('Расширение файла успешно изменено!', title='Успешно', icon=img.accept_img)
            else:
                shutil.copy(file_path, new_folder_for_file)
                filename = os.path.basename(file_path)
                new_path = os.path.join(new_folder_for_file, filename)
                name = new_path.replace(f'.{ex1}', f'.{ex2}')
                os.rename(new_path, name)
                sg.PopupOK('Файл успешно перемещен с изменением его расширения!', title='Успешно', icon=img.accept_img)
        except:
            sg.PopupOK('Корректно укажите путь к файлу(папке)!', title='Ошибка', icon=img.warning_img)

