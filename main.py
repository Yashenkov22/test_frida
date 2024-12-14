import subprocess
import os


def get_process_name_from_file(file_path):
    with open(file_path, 'r') as file:
        first_line = file.readline()

        _file = file.read()

        return first_line.strip(), _file

# file_path = 'process.txt'
# first_line, _file = get_process_name_from_file(file_path)

# if first_line:
#     command = f'./frida-ios-hook/frida-ios-hook/ioshook -n {first_line} -m i-url-req'

#     print('запускаю процесс на выполнение')

#     res = subprocess.Popen(command,
#                         shell=True,
#                         text=True,
#                         stdout=subprocess.PIPE,
#                         stderr=subprocess.PIPE)
    
#     stdout, stderr = res.communicate()
    
#     # print("Output:", res.stdout)  # Вывод будет строкой
#     print("Стандартный вывод:")
#     print(stdout)

#     if stderr:
#         print("Ошибки:")
#     print(stderr)
# else:
#     print("Имя процесса не найдено или процессы в файле закончились")

# with open(file_path, 'w') as file:
#     file.write(_file)


if __name__ == '__main__':
    file_path = 'process.txt'
    first_line, _file = get_process_name_from_file(file_path)

    if first_line:
        command = f'./frida-ios-hook/frida-ios-hook/ioshook -n {first_line} -m i-url-req'

        print(f'запускаю процесс на выполнение команды {command}')

        res = subprocess.Popen(command,
                            shell=True,
                            text=True,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
        # res = subprocess.run(command,
        #                     shell=True,
        #                     text=True,
        #                     capture_output=True)
        
        # Ждем завершения процесса
        # res.wait()

        # Получаем код завершения
        # print('status code', res.returncode)
        
        stdout, stderr = res.communicate()
        
        print("Output:", res.stdout)  # Вывод будет строкой
        print("Стандартный вывод:")
        print(stdout)

        if stderr:
            print("Ошибки:")
        print(stderr)
    else:
        print("Имя процесса не найдено или процессы в файле закончились")

    with open(file_path, 'w') as file:
        file.write(_file)