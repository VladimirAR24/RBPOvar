from tkinter import *
from tkinter import ttk
from tkinter import filedialog

import os
import datetime
import time

import graph as graph
import parser
from header_format import header_structure
from add_data_format import add_data_structure

# import binascii

initial_date = datetime.datetime(2000, 1, 1, 12)
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 МБ

root = Tk()
root.title("Parser")
root.geometry("320x300")


def read_file_limited(file_path):
    with open(file_path, 'rb') as file_obj:
        file_bytes = file_obj.read(MAX_FILE_SIZE + 1)

    if len(file_bytes) > MAX_FILE_SIZE:
        raise ValueError("Файл слишком большой для безопасной обработки")

    return bytearray(file_bytes)


def consume_prefix(buffer, size, part_name):
    if not isinstance(size, int):
        raise ValueError(f"Некорректный размер {part_name}")

    if size <= 0:
        raise ValueError(f"Размер {part_name} должен быть больше нуля")

    if size > len(buffer):
        raise ValueError(f"Размер {part_name} превышает размер оставшегося буфера")

    chunk = buffer[:size]
    del buffer[:size]
    return chunk


def open_file():
    filepath = filedialog.askopenfilenames()
    global parsed_files
    parsed_files = []
    time0 = time.time()

    for file_path in filepath:
        if file_path.endswith('.evt'):
            ba = read_file_limited(file_path)
            i = 0

            while len(ba) > 0:
                parsed_header = parser.header_parser(header_structure, ba)

                header_size = parsed_header.get('dwHeaderSize')
                add_data_size = parsed_header.get('dwAddDataSize')
                hardware_id = parsed_header.get('wLngHardwareID')

                consume_prefix(ba, header_size, "заголовка")

                if hardware_id == 785:
                    if not isinstance(add_data_size, int) or add_data_size <= 0:
                        raise ValueError("Некорректный размер блока телеметрии")

                    if add_data_size > len(ba):
                        raise ValueError("Размер блока телеметрии превышает размер буфера")

                    parsed_data = parser.add_data_parser(add_data_structure, ba[:add_data_size])

                    print(
                        f'{i})',
                        initial_date + datetime.timedelta(
                            days=parsed_data['day'],
                            milliseconds=parsed_data['ms']
                        ),
                        # parsed_files[1][1]['day'],
                        # parsed_files[1][1]['ms'],
                        # parsed_files[1][1]['us'],
                        parsed_data['op_time'],
                        parsed_data['current'],
                        parsed_data['voltage'],
                        parsed_data['main_line_current[1]'],
                        parsed_data['main_line_voltage[1]'],
                        parsed_data['main_mcu_current[1]'],
                        parsed_data['main_mcu_voltage[1]'],
                        parsed_data['main_mcu_op_time[1]'],
                        parsed_data['main_line_temperature[1]'],
                        parsed_data['main_line_current[4]'],
                        parsed_data['main_line_voltage[4]'],
                        parsed_data['main_mcu_current[4]'],
                        parsed_data['main_mcu_voltage[4]'],
                        parsed_data['main_mcu_op_time[4]'],
                        parsed_data['main_line_temperature[4]']
                    )

                    i += 1
                    parsed_files.append((parsed_header, parsed_data))

                consume_prefix(ba, add_data_size, "блока телеметрии")

            time1 = time.time()
            parsing_time_label['text'] = str(time1 - time0)


def draw_graph():
    x = []
    y = []

    if combobox.get() == 'main_mcu_current[4]':
        for pair in parsed_files:
            x.append(datetime.datetime(
                pair[0]['wYear'],
                pair[0]['wMonth'],
                pair[0]['wDay'],
                pair[0]['wHour'],
                pair[0]['wMinute'],
                pair[0]['wSecond'],
                pair[0]['wMillisecond']
            ))
            y.append(pair[1]['main_mcu_current[4]'])
        graph.graph(x, y, 'main_mcu_current[4]')
        x.clear()
        y.clear()

    if combobox.get() == 'op_time':
        for pair in parsed_files:
            x.append(datetime.datetime(
                pair[0]['wYear'],
                pair[0]['wMonth'],
                pair[0]['wDay'],
                pair[0]['wHour'],
                pair[0]['wMinute'],
                pair[0]['wSecond'],
                pair[0]['wMillisecond']
            ))
            y.append(pair[1]['op_time'])
        graph.graph(x, y, 'op_time')
        x.clear()
        y.clear()

    if combobox.get() == 'umode':
        for pair in parsed_files:
            x.append(datetime.datetime(
                pair[0]['wYear'],
                pair[0]['wMonth'],
                pair[0]['wDay'],
                pair[0]['wHour'],
                pair[0]['wMinute'],
                pair[0]['wSecond'],
                pair[0]['wMillisecond']
            ))
            y.append(pair[1]['umode'])
        graph.graph(x, y, 'umode')
        x.clear()
        y.clear()


def open_directory():
    directorypath = filedialog.askdirectory()
    global parsed_files
    parsed_files = []
    time0 = time.time()

    for file_name in os.listdir(directorypath):
        if file_name.endswith('.txt'):
            full_path = os.path.join(directorypath, file_name)
            ba = read_file_limited(full_path)

            while len(ba) > 0:
                parsed_header = parser.header_parser(header_structure, ba)

                header_size = parsed_header.get('dwHeaderSize')
                add_data_size = parsed_header.get('dwAddDataSize')

                consume_prefix(ba, header_size, "заголовка")

                if not isinstance(add_data_size, int) or add_data_size <= 0:
                    raise ValueError("Некорректный размер блока телеметрии")

                if add_data_size > len(ba):
                    raise ValueError("Размер блока телеметрии превышает размер буфера")

                parsed_data = parser.add_data_parser(add_data_structure, ba[:add_data_size])
                parsed_files.append((parsed_header, parsed_data))

                consume_prefix(ba, add_data_size, "блока телеметрии")

            time1 = time.time()
            parsing_time_label['text'] = str(time1 - time0)


open_files = ttk.Button(text="Открыть файлы", command=open_file)
open_files.grid(column=1, row=0, columnspan=1)

# open_folder = ttk.Button(text="Выбрать папку", command=open_directory)
# open_folder.grid(column=6, row=0, columnspan=1)

parsing_time_label = Label()
parsing_time_label.grid(column=1, row=8, columnspan=1)

options = ['op_time', 'main_mcu_current[4]', 'umode']
combobox = ttk.Combobox(values=options)
combobox.grid(column=1, row=2, columnspan=2)

draw_graph_btn = ttk.Button(text="Построить график", command=draw_graph)
draw_graph_btn.grid(column=4, row=2, columnspan=1)

# сетка
for c in range(9):
    root.columnconfigure(index=c, weight=1)

for r in range(9):
    root.rowconfigure(index=r, weight=1)

root.mainloop()