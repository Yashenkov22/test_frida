import subprocess
import os
import time


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
        
        try:
            # Чтение вывода в цикле
            while True:
                # Получаем строку из stdout
                output = res.stdout.readline()
                if output:
                    print("STDOUT:", output.strip())
                
                # Проверяем завершение процесса
                if res.poll() is not None:
                    break

                # Можно добавить небольшую задержку, чтобы не нагружать CPU
                time.sleep(0.1)

        except KeyboardInterrupt:
            print("Завершение работы...")
            res.terminate()  # Завершаем процесс при прерывании
            res.wait()       # Ждем завершения процесса

        # Проверяем наличие ошибок
        stderr = res.stderr.read()
        if stderr:
            print("STDERR:", stderr.strip())

        
        # stdout, stderr = res.communicate()
        
        # print("Output:", res.stdout)  # Вывод будет строкой
        # print("Стандартный вывод:")
        # print(stdout)

        # if stderr:
        #     print("Ошибки:")
        #     print(stderr)
    else:
        print("Процессы в файле закончились, обновите proccess.txt")

    with open(file_path, 'w') as file:
        file.write(_file)