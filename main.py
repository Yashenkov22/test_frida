import subprocess
import os


# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# d = os.path.join(BASE_DIR, 'frida-ios-hook')

# print(d)

# if os.path.exists(d):
#     print(22)
# else:
#     print(11)

# print(BASE_DIR)


def get_process_name_from_file(file_path):
    with open(file_path, 'r') as file:
        first_line = file.readline()

        _file = file.read()

        return first_line.strip(), _file

file_path = 'process.txt'
first_line, _file = get_process_name_from_file(file_path)

if first_line:
    command = f'./frida-ios-hook/frida-ios-hook/ioshook -n {first_line} -m i-url-req'

    res = subprocess.Popen(command,
                        shell=True,
                        text=True,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    
    stdout, stderr = res.communicate()
    
    # print("Output:", res.stdout)  # Вывод будет строкой
    print("Стандартный вывод:")
    print(stdout)

    if stderr:
        print("Ошибки:")
    print(stderr)
else:
    print("Имя процесса не найдено или процессы в файле закончились")

with open(file_path, 'w') as file:
    file.write(_file)