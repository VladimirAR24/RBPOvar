# import struct
# bVersion, dwHeaderSize, SystemTime = struct.unpack('s4s16s', file.read)
# print(bVersion, dwHeaderSize, SystemTime)
from header_format import header_structure
from add_data_format import add_data_structure
#import binascii



def header_parser(header_structure, byte_array):

    """header_structure - словарь, ключами которого являются названия полей, 
       значениями - количество байт, занимаемых полем и номер первого байта, занимаемого полем
       byte_array - байтовое предстваление заголовка, который нужно распорсить в соответствии с header_structure"""

    parsed_header = {}
    field_first_byte_index = 0
    field_size = 0
    for field in header_structure:
        field_first_byte_index = header_structure[field][0]
        field_size = header_structure[field][1]
        if len(byte_array) < (field_size + field_first_byte_index):
            raise IndexError('byte_array не соответствует данной структуре заголовка')
        cur_field_value = byte_array[field_first_byte_index:(field_size + field_first_byte_index)]
        # parsed_header[field] = int(cur_field_value[::-1].hex(), 16) #hex()- для строки или binascii.hexlify(cur_field_value) - для байтового хекса
        parsed_header[field] = int.from_bytes(cur_field_value, 'little')
    
    return (parsed_header) #int.from_bytes(cur_field_value, 'little') -> в десятичную
       


    
def add_data_parser(add_data_structure, byte_array):
    parsed_data = {}
    field_first_byte_index = 0
    field_size = 0
    for field in add_data_structure:
        field_first_byte_index = add_data_structure[field][0]
        field_size = add_data_structure[field][1]
        if len(byte_array) < (field_size + field_first_byte_index):
            raise IndexError('byte_array не соответствует данной структуре заголовка')
        cur_field_value = byte_array[field_first_byte_index:(field_size + field_first_byte_index)]
        parsed_data[field] = int.from_bytes(cur_field_value, 'big')
    
    return (parsed_data)






