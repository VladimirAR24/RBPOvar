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

initial_date = datetime.datetime(2000,1,1,12)

root = Tk()
root.title("Parser")
root.geometry("320x300")
 

def open_file():
    filepath = filedialog.askopenfilenames()
    global parsed_files
    parsed_files = []
    time0 = time.time()
    for file in filepath:
        if file.endswith('.evt'):
            with open(file, 'rb') as  f:
                ba = bytearray(f.read())
                i=0
                while ba:
                    parsed_header = parser.header_parser(header_structure, ba)
                    ba = ba[parsed_header['dwHeaderSize']::]
                    if parsed_header['wLngHardwareID'] == 785:
                        parsed_data = parser.add_data_parser(add_data_structure, ba)
                        print(f'{i})',initial_date + datetime.timedelta(days = parsed_data['day'], milliseconds = parsed_data['ms']),
                        #   parsed_files[1][1]['day'], 
                        #   parsed_files[1][1]['ms'],
                        #   parsed_files[1][1]['us'],
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
                          parsed_data['main_line_temperature[4]'])
                        i+=1
                        parsed_files.append((parsed_header, parsed_data))
                    else:
                        pass
                    ba = ba[parsed_header['dwAddDataSize']::]     
                time1 = time.time()
                parsing_time_label['text'] = str(time1 - time0)
                

def draw_graph():
    x = []
    y = []
    if combobox.get() == 'main_mcu_current[4]':
        for pair in parsed_files:
            x.append(datetime.datetime(pair[0]['wYear'],pair[0]['wMonth'],pair[0]['wDay'],pair[0]['wHour'],pair[0]['wMinute'],pair[0]['wSecond'],pair[0]['wMillisecond']))
            y.append(pair[1]['main_mcu_current[4]']) # op_time, main_mcu_current[4], umode
        graph.graph(x,y,'main_mcu_current[4]')
        x.clear()
        y.clear()
    if combobox.get() == 'op_time':
        for pair in parsed_files:
            x.append(datetime.datetime(pair[0]['wYear'],pair[0]['wMonth'],pair[0]['wDay'],pair[0]['wHour'],pair[0]['wMinute'],pair[0]['wSecond'],pair[0]['wMillisecond']))
            y.append(pair[1]['op_time']) # op_time, main_mcu_current[4], umode
        graph.graph(x,y,'op_time')
        x.clear()
        y.clear()
    if combobox.get() == 'umode':
        for pair in parsed_files:
            x.append(datetime.datetime(pair[0]['wYear'],pair[0]['wMonth'],pair[0]['wDay'],pair[0]['wHour'],pair[0]['wMinute'],pair[0]['wSecond'],pair[0]['wMillisecond']))
            y.append(pair[1]['umode']) # op_time, main_mcu_current[4], umode
        graph.graph(x,y,'umode')
        x.clear()
        y.clear()           
    
 
def open_directory():
    directorypath = filedialog.askdirectory()
    filepath = os.listdir(directorypath)
    parsed_files = []
    time0 = time.time()
    for file in filepath:
        if file.endswith('.txt'):
            with open(file, 'rb') as  f:
                ba = bytearray(f.read())
                while ba:
                    parsed_header = parser.header_parser(header_structure, ba)
                    ba = ba[parsed_header['dwHeaderSize']::]
                    parsed_data = parser.add_data_parser(add_data_structure, ba)
                    ba = ba[parsed_header['dwAddDataSize']::]
                    parsed_files.append((parsed_header, parsed_data))
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
for c in range(9): root.columnconfigure(index=c, weight=1)
for r in range(9): root.rowconfigure(index=r, weight=1)

root.mainloop()