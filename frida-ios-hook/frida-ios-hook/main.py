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
    try:
        file_path = './process.txt'
        first_line, _file = get_process_name_from_file(file_path)

        if first_line:

            test_command = 'ls -a'
            print(f'запускаю тестовый сабпроцесс на выполнение команды {test_command}')
            
            test_res = subprocess.Popen(test_command,
                                shell=True,
                                text=True,
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)

            output, error = test_res.communicate()

            # Выводим результат в терминал
            if output:
                print("Вывод:\n", output.strip())
            if error:
                print("Ошибка:\n", error.strip())

            test_frida_command = './ioshook --list-devices'
            print(f'запускаю тестовый сабпроцесс на выполнение команды {test_frida_command}')
            
            test_res = subprocess.Popen(test_frida_command,
                                shell=True,
                                text=True,
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)

            output, error = test_res.communicate()

            # Выводим результат в терминал
            if output:
                print("Вывод:\n", output.strip())
            if error:
                print("Ошибка:\n", error.strip())

            command = f'./ioshook -n {first_line} -m i-url-req'
            print(f'запускаю сабпроцесс на выполнение команды {command}')

            res = subprocess.Popen(command,
                                shell=True,
                                text=True,
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
            try:
            # Получаем вывод и ошибки
                output, error = res.communicate()

                # Выводим результат в терминал
                if output:
                    print("Вывод:\n", output.strip())
                if error:
                    print("Ошибка:\n", error.strip())
            except Exception:
                pass
            
            with open(file_path, 'w') as file:
                file.write(_file)
        else:
            print("Процессы в файле закончились, обновите proccess.txt")

            # res = subprocess.run(command,
            #                     shell=True,
            #                     text=True,
            #                     capture_output=True)
            
            # Ждем завершения процесса
            # res.wait()

            # Получаем код завершения
            # print('status code', res.returncode)
            
            # try:
            #     # Чтение вывода в цикле
            #     while True:
            #         # Получаем строку из stdout
            #         output = res.stdout.readline()
            #         if output:
            #             print("STDOUT:", output.strip())
                    
            #         # Проверяем завершение процесса
            #         if res.poll() is not None:
            #             break

            #         # Можно добавить небольшую задержку, чтобы не нагружать CPU
            #         time.sleep(0.1)

    except KeyboardInterrupt:
        print("Завершение работы...")
        try:
        # Получаем вывод и ошибки
            output, error = res.communicate()

            # Выводим результат в терминал
            if output:
                print("Вывод:\n", output.strip())
            if error:
                print("Ошибка:\n", error.strip())
        except Exception:
            pass
        finally:
            with open(file_path, 'w') as file:
                file.write(_file)
        # res.terminate()  # Завершаем процесс при прерывании
        # res.wait()       # Ждем завершения процесса

        # Проверяем наличие ошибок
        # stderr = res.stderr.read()
        # if stderr:
        #     print("STDERR:", stderr.strip())

        
        # stdout, stderr = res.communicate()
        
        # print("Output:", res.stdout)  # Вывод будет строкой
        # print("Стандартный вывод:")
        # print(stdout)

        # if stderr:
        #     print("Ошибки:")
        #     print(stderr)