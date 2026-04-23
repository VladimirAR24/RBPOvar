MAX_DEVICE_NAME_EX = 100
CMD_EMBEDDED_PARAM_LEN = 6

field_names = ["bVersion", #1
    "dwHeaderSize", #4
    "wYear", #2        TimeStamp (16)
    "wMonth", #2
    "wDayOfWeek", #2
    "wDay", #2
    "wHour", #2
    "wMinute", #2
    "wSecond", #2
    "wMillisecond", #2
    "dwStationID", #4
    "uComputerID", #4
    "wLngHardwareID", #2
    "bShtHardwareID", #1
    "bSubsystemID", #1
    "bDeviceID", #1
    "bDeviceItemID", #1
    "szDeviceItemName", #100
    "bModuleID", #1
    "nOpAppMode", #4
    "nAppStatus", #4
    "uCodeType", #4
    "dwCode", #4
    "dwCodeExtension", #4
    "dwAddDataSize", #4
    "dwAddDataChangedSize", #4
    "dwArrayOffset", #4
    "fBinaryData", #4
    "dwCrc", #4
    "szName", #100
    "wSpecialFlags", #2
    "wReceiverID", #2
    "wMyHardwareID", #2
    "bEmbeddedData", #6
    "bEmbeddedDataLen", #1
    "dwReserved1", #8
]

fields_lengths = (1,4,2,2,2,2,2,2,2,2,4,4,2,1,1,1,1,MAX_DEVICE_NAME_EX,
                  1,4,4,4,4,4,4,4,4,4,4,MAX_DEVICE_NAME_EX,
                  2,2,2,CMD_EMBEDDED_PARAM_LEN,1,8)



cur_beg_i = 0
header_structure = {}
for i in range(len(field_names)):
    header_structure[field_names[i]] = (cur_beg_i, fields_lengths[i])
    cur_beg_i = cur_beg_i + fields_lengths[i]



