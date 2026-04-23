NUMBER_PDU_CHANNELS = 10
SHORT_ERROR_LIST_SIZE = 10
NUMBER_MCUL_TYPE_LINES = 2

field_names = ['day', #2, Day part
               'ms', #4, Milliseconds of day
               'us', #2, Microseconds of milliseconds
               
               'umode', #1
               'uerrcounter', #1
               'reset_counter', #1
               'proto_version', #1
               'op_time', #4

               'temperature0', #1
               'temperature1', #1
               'temperature_flags', #1                       !!!!!!!!!!!!!
               'reserved0', #1

               'current', #2 mA
               'voltage', #2 mA
               'power', #2 mW/10
               'power_flags', #1                           !!!!!!!!!!!!
               'alert_flags', #1

               'last_st', #1
               'last_subst', #1
               'prev_st', #1
               'prev_subst', #1

               'role', #2 role of MCU: UNKNOWN: 0, MASTER: 1, SLAVE: 2
               'reserve', #2

               'channel_voltage[1]', #2 (in mA) 
               'channel_current[1]', #2 (in mV)
               'channel_voltage[2]', #2 (in mA) 
               'channel_current[2]', #2 (in mV)
               'channel_voltage[3]', #2 (in mA) 
               'channel_current[3]', #2 (in mV)
               'channel_voltage[4]', #2 (in mA) 
               'channel_current[4]', #2 (in mV)
               'channel_voltage[5]', #2 (in mA) 
               'channel_current[5]', #2 (in mV)
               'channel_voltage[6]', #2 (in mA) 
               'channel_current[6]', #2 (in mV)
               'channel_voltage[7]', #2 (in mA) 
               'channel_current[7]', #2 (in mV)
               'channel_voltage[8]', #2 (in mA) 
               'channel_current[8]', #2 (in mV)
               'channel_voltage[9]', #2 (in mA) 
               'channel_current[9]', #2 (in mV)
               'channel_voltage[10]', #2 (in mA) 
               'channel_current[10]', #2 (in mV)

               'lines_status', #4                         !!!!!!!!!!!!!!!!!!!!!!!!!!!!

               'lines_healthy', #4                          !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

               'ext_telemetry', #16*10

            #    'ext_day[SHORT_ERROR_LIST_SIZE]', #2, Day part                          РАЗОБРАТЬСЯ С РАСШИРЕННОЙ ТЕЛЕМЕТРИЕЙ
            #    'ext_ms[SHORT_ERROR_LIST_SIZE]', #4, Milliseconds of day
            #    'ext_us[SHORT_ERROR_LIST_SIZE]', #2, Microseconds of milliseconds

            #    'error_code[SHORT_ERROR_LIST_SIZE]', #2
            #    'params[SHORT_ERROR_LIST_SIZE]', #2                !!!!!!!!!!!!!!

            #    'service[SHORT_ERROR_LIST_SIZE]', #1
            #    'subservice[SHORT_ERROR_LIST_SIZE]', #1
            #    'data[SHORT_ERROR_LIST_SIZE][2]', #1*2
            #    'bytes[SHORT_ERROR_LIST_SIZE][4]', #1*4
            #    'halfword[SHORT_ERROR_LIST_SIZE][2]', #2*2
            #    'dword', #4

               'main_line_stm_err_code[1]', #2
               'main_line_temperature[1]', #1
               'main_line_flags[1]', #1
               'main_mcu_op_time[1]', #4
               'main_mcu_current[1]', #2 mA
               'main_mcu_voltage[1]', #2 mA
               'main_mcu_power[1]', #2 mW/10
               'main_mcu_power_flags[1]', #1                           !!!!!!!!!!!!
               'main_mcu_alert_flags[1]', #1 
               'main_line_key_voltage[1]', #2
               'main_line_limiter_imon[1]', #2  
               'main_line_current[1]', #2 mA
               'main_line_voltage[1]', #2 mA
               'main_line_power[1]', #2 mW/10
               'main_line_power_flags[1]', #1                           !!!!!!!!!!!!
               'main_line_alert_flags[1]', #1  

               'reserved_line_stm_err_code[1]', #2
               'reserved_line_temperature[1]', #1
               'reserved_line_flags[1]', #1
               'reserved_mcu_op_time[1]', #4
               'reserved_mcu_current[1]', #2 mA
               'reserved_mcu_voltage[1]', #2 mA
               'reserved_mcu_power[1]', #2 mW/10
               'reserved_mcu_power_flags[1]', #1                           !!!!!!!!!!!!
               'reserved_mcu_alert_flags[1]', #1 
               'reserved_line_key_voltage[1]', #2
               'reserved_line_limiter_imon[1]', #2  
               'reserved_line_current[1]', #2 mA
               'reserved_line_voltage[1]', #2 mA
               'reserved_line_power[1]', #2 mW/10
               'reserved_line_power_flags[1]', #1                           !!!!!!!!!!!!
               'reserved_line_alert_flags[1]', #1  
          
               'main_line_stm_err_code[2]', #2
               'main_line_temperature[2]', #1
               'main_line_flags[2]', #1
               'main_mcu_op_time[2]', #4
               'main_mcu_current[2]', #2 mA
               'main_mcu_voltage[2]', #2 mA
               'main_mcu_power[2]', #2 mW/10
               'main_mcu_power_flags[2]', #1                           !!!!!!!!!!!!
               'main_mcu_alert_flags[2]', #1 
               'main_line_key_voltage[2]', #2
               'main_line_limiter_imon[2]', #2  
               'main_line_current[2]', #2 mA
               'main_line_voltage[2]', #2 mA
               'main_line_power[2]', #2 mW/10
               'main_line_power_flags[2]', #1                           !!!!!!!!!!!!
               'main_line_alert_flags[2]', #1  

               'reserved_line_stm_err_code[2]', #2
               'reserved_line_temperature[2]', #1
               'reserved_line_flags[2]', #1
               'reserved_mcu_op_time[2]', #4
               'reserved_mcu_current[2]', #2 mA
               'reserved_mcu_voltage[2]', #2 mA
               'reserved_mcu_power[2]', #2 mW/10
               'reserved_mcu_power_flags[2]', #1                           !!!!!!!!!!!!
               'reserved_mcu_alert_flags[2]', #1 
               'reserved_line_key_voltage[2]', #2
               'reserved_line_limiter_imon[2]', #2  
               'reserved_line_current[2]', #2 mA
               'reserved_line_voltage[2]', #2 mA
               'reserved_line_power[2]', #2 mW/10
               'reserved_line_power_flags[2]', #1                           !!!!!!!!!!!!
               'reserved_line_alert_flags[2]',                                                            

               'main_line_stm_err_code[3]', #2
               'main_line_temperature[3]', #1
               'main_line_flags[3]', #1
               'main_mcu_op_time[3]', #4
               'main_mcu_current[3]', #2 mA
               'main_mcu_voltage[3]', #2 mA
               'main_mcu_power[3]', #2 mW/10
               'main_mcu_power_flags[3]', #1                           !!!!!!!!!!!!
               'main_mcu_alert_flags[3]', #1 
               'main_line_key_voltage[3]', #2
               'main_line_limiter_imon[3]', #2  
               'main_line_current[3]', #2 mA
               'main_line_voltage[3]', #2 mA
               'main_line_power[3]', #2 mW/10
               'main_line_power_flags[3]', #1                           !!!!!!!!!!!!
               'main_line_alert_flags[3]', #1  

               'reserved_line_stm_err_code[3]', #2
               'reserved_line_temperature[3]', #1
               'reserved_line_flags[3]', #1
               'reserved_mcu_op_time[3]', #4
               'reserved_mcu_current[3]', #2 mA
               'reserved_mcu_voltage[3]', #2 mA
               'reserved_mcu_power[3]', #2 mW/10
               'reserved_mcu_power_flags[3]', #1                           !!!!!!!!!!!!
               'reserved_mcu_alert_flags[3]', #1 
               'reserved_line_key_voltage[3]', #2
               'reserved_line_limiter_imon[3]', #2  
               'reserved_line_current[3]', #2 mA
               'reserved_line_voltage[3]', #2 mA
               'reserved_line_power[3]', #2 mW/10
               'reserved_line_power_flags[3]', #1                           !!!!!!!!!!!!
               'reserved_line_alert_flags[3]', #1   
               
               'main_line_stm_err_code[4]', #2
               'main_line_temperature[4]', #1
               'main_line_flags[4]', #1
               'main_mcu_op_time[4]', #4
               'main_mcu_current[4]', #2 mA
               'main_mcu_voltage[4]', #2 mA
               'main_mcu_power[4]', #2 mW/10
               'main_mcu_power_flags[4]', #1                           !!!!!!!!!!!!
               'main_mcu_alert_flags[4]', #1 
               'main_line_key_voltage[4]', #2
               'main_line_limiter_imon[4]', #2  
               'main_line_current[4]', #2 mA
               'main_line_voltage[4]', #2 mA
               'main_line_power[4]', #2 mW/10
               'main_line_power_flags[4]', #1                           !!!!!!!!!!!!
               'main_line_alert_flags[4]', #1  

               'reserved_line_stm_err_code[4]', #2
               'reserved_line_temperature[4]', #1
               'reserved_line_flags[4]', #1
               'reserved_mcu_op_time[4]', #4
               'reserved_mcu_current[4]', #2 mA
               'reserved_mcu_voltage[4]', #2 mA
               'reserved_mcu_power[4]', #2 mW/10
               'reserved_mcu_power_flags[4]', #1                           !!!!!!!!!!!!
               'reserved_mcu_alert_flags[4]', #1 
               'reserved_line_key_voltage[4]', #2
               'reserved_line_limiter_imon[4]', #2  
               'reserved_line_current[4]', #2 mA
               'reserved_line_voltage[4]', #2 mA
               'reserved_line_power[4]', #2 mW/10
               'reserved_line_power_flags[4]', #1                           !!!!!!!!!!!!
               'reserved_line_alert_flags[4]', #1        

               'main_line_stm_err_code[5]', #2
               'main_line_temperature[5]', #1
               'main_line_flags[5]', #1
               'main_mcu_op_time[5]', #4
               'main_mcu_current[5]', #2 mA
               'main_mcu_voltage[5]', #2 mA
               'main_mcu_power[5]', #2 mW/10
               'main_mcu_power_flags[5]', #1                           !!!!!!!!!!!!
               'main_mcu_alert_flags[5]', #1 
               'main_line_key_voltage[5]', #2
               'main_line_limiter_imon[5]', #2  
               'main_line_current[5]', #2 mA
               'main_line_voltage[5]', #2 mA
               'main_line_power[5]', #2 mW/10
               'main_line_power_flags[5]', #1                           !!!!!!!!!!!!
               'main_line_alert_flags[5]', #1  

               'reserved_line_stm_err_code[5]', #2
               'reserved_line_temperature[5]', #1
               'reserved_line_flags[5]', #1
               'reserved_mcu_op_time[5]', #4
               'reserved_mcu_current[5]', #2 mA
               'reserved_mcu_voltage[5]', #2 mA
               'reserved_mcu_power[5]', #2 mW/10
               'reserved_mcu_power_flags[5]', #1                           !!!!!!!!!!!!
               'reserved_mcu_alert_flags[5]', #1 
               'reserved_line_key_voltage[5]', #2
               'reserved_line_limiter_imon[5]', #2  
               'reserved_line_current[5]', #2 mA
               'reserved_line_voltage[5]', #2 mA
               'reserved_line_power[5]', #2 mW/10
               'reserved_line_power_flags[5]', #1                           !!!!!!!!!!!!
               'reserved_line_alert_flags[5]', #1 

               'main_line_stm_err_code[6]', #2
               'main_line_temperature[6]', #1
               'main_line_flags[6]', #1
               'main_mcu_op_time[6]', #4
               'main_mcu_current[6]', #2 mA
               'main_mcu_voltage[6]', #2 mA
               'main_mcu_power[6]', #2 mW/10
               'main_mcu_power_flags[6]', #1                           !!!!!!!!!!!!
               'main_mcu_alert_flags[6]', #1 
               'main_line_key_voltage[6]', #2
               'main_line_limiter_imon[6]', #2  
               'main_line_current[6]', #2 mA
               'main_line_voltage[6]', #2 mA
               'main_line_power[6]', #2 mW/10
               'main_line_power_flags[6]', #1                           !!!!!!!!!!!!
               'main_line_alert_flags[6]', #1  

               'reserved_line_stm_err_code[6]', #2
               'reserved_line_temperature[6]', #1
               'reserved_line_flags[6]', #1
               'reserved_mcu_op_time[6]', #4
               'reserved_mcu_current[6]', #2 mA
               'reserved_mcu_voltage[6]', #2 mA
               'reserved_mcu_power[6]', #2 mW/10
               'reserved_mcu_power_flags[6]', #1                           !!!!!!!!!!!!
               'reserved_mcu_alert_flags[6]', #1 
               'reserved_line_key_voltage[6]', #2
               'reserved_line_limiter_imon[6]', #2  
               'reserved_line_current[6]', #2 mA
               'reserved_line_voltage[6]', #2 mA
               'reserved_line_power[6]', #2 mW/10
               'reserved_line_power_flags[6]', #1                           !!!!!!!!!!!!
               'reserved_line_alert_flags[6]', #1 

               'main_line_stm_err_code[7]', #2
               'main_line_temperature[7]', #1
               'main_line_flags[7]', #1
               'main_mcu_op_time[7]', #4
               'main_mcu_current[7]', #2 mA
               'main_mcu_voltage[7]', #2 mA
               'main_mcu_power[7]', #2 mW/10
               'main_mcu_power_flags[7]', #1                           !!!!!!!!!!!!
               'main_mcu_alert_flags[7]', #1 
               'main_line_key_voltage[7]', #2
               'main_line_limiter_imon[7]', #2  
               'main_line_current[7]', #2 mA
               'main_line_voltage[7]', #2 mA
               'main_line_power[7]', #2 mW/10
               'main_line_power_flags[7]', #1                           !!!!!!!!!!!!
               'main_line_alert_flags[7]', #1  

               'reserved_line_stm_err_code[7]', #2
               'reserved_line_temperature[7]', #1
               'reserved_line_flags[7]', #1
               'reserved_mcu_op_time[7]', #4
               'reserved_mcu_current[7]', #2 mA
               'reserved_mcu_voltage[7]', #2 mA
               'reserved_mcu_power[7]', #2 mW/10
               'reserved_mcu_power_flags[7]', #1                           !!!!!!!!!!!!
               'reserved_mcu_alert_flags[7]', #1 
               'reserved_line_key_voltage[7]', #2
               'reserved_line_limiter_imon[7]', #2  
               'reserved_line_current[7]', #2 mA
               'reserved_line_voltage[7]', #2 mA
               'reserved_line_power[7]', #2 mW/10
               'reserved_line_power_flags[7]', #1                           !!!!!!!!!!!!
               'reserved_line_alert_flags[7]', #1 

               'main_line_stm_err_code[8]', #2
               'main_line_temperature[8]', #1
               'main_line_flags[8]', #1
               'main_mcu_op_time[8]', #4
               'main_mcu_current[8]', #2 mA
               'main_mcu_voltage[8]', #2 mA
               'main_mcu_power[8]', #2 mW/10
               'main_mcu_power_flags[8]', #1                           !!!!!!!!!!!!
               'main_mcu_alert_flags[8]', #1 
               'main_line_key_voltage[8]', #2
               'main_line_limiter_imon[8]', #2  
               'main_line_current[8]', #2 mA
               'main_line_voltage[8]', #2 mA
               'main_line_power[8]', #2 mW/10
               'main_line_power_flags[8]', #1                           !!!!!!!!!!!!
               'main_line_alert_flags[8]', #1  

               'reserved_line_stm_err_code[8]', #2
               'reserved_line_temperature[8]', #1
               'reserved_line_flags[8]', #1
               'reserved_mcu_op_time[8]', #4
               'reserved_mcu_current[8]', #2 mA
               'reserved_mcu_voltage[8]', #2 mA
               'reserved_mcu_power[8]', #2 mW/10
               'reserved_mcu_power_flags[8]', #1                           !!!!!!!!!!!!
               'reserved_mcu_alert_flags[8]', #1 
               'reserved_line_key_voltage[8]', #2
               'reserved_line_limiter_imon[8]', #2  
               'reserved_line_current[8]', #2 mA
               'reserved_line_voltage[8]', #2 mA
               'reserved_line_power[8]', #2 mW/10
               'reserved_line_power_flags[8]', #1                           !!!!!!!!!!!!
               'reserved_line_alert_flags[8]', #1 

               'main_line_stm_err_code[9]', #2
               'main_line_temperature[9]', #1
               'main_line_flags[9]', #1
               'main_mcu_op_time[9]', #4
               'main_mcu_current[9]', #2 mA
               'main_mcu_voltage[9]', #2 mA
               'main_mcu_power[9]', #2 mW/10
               'main_mcu_power_flags[9]', #1                           !!!!!!!!!!!!
               'main_mcu_alert_flags[9]', #1 
               'main_line_key_voltage[9]', #2
               'main_line_limiter_imon[9]', #2  
               'main_line_current[9]', #2 mA
               'main_line_voltage[9]', #2 mA
               'main_line_power[9]', #2 mW/10
               'main_line_power_flags[9]', #1                           !!!!!!!!!!!!
               'main_line_alert_flags[9]', #1  

               'reserved_line_stm_err_code[9]', #2
               'reserved_line_temperature[9]', #1
               'reserved_line_flags[9]', #1
               'reserved_mcu_op_time[9]', #4
               'reserved_mcu_current[9]', #2 mA
               'reserved_mcu_voltage[9]', #2 mA
               'reserved_mcu_power[9]', #2 mW/10
               'reserved_mcu_power_flags[9]', #1                           !!!!!!!!!!!!
               'reserved_mcu_alert_flags[9]', #1 
               'reserved_line_key_voltage[9]', #2
               'reserved_line_limiter_imon[9]', #2  
               'reserved_line_current[9]', #2 mA
               'reserved_line_voltage[9]', #2 mA
               'reserved_line_power[9]', #2 mW/10
               'reserved_line_power_flags[9]', #1                           !!!!!!!!!!!!
               'reserved_line_alert_flags[9]', #1 

               'main_line_stm_err_code[10]', #2
               'main_line_temperature[10]', #1
               'main_line_flags[10]', #1
               'main_mcu_op_time[10]', #4
               'main_mcu_current[10]', #2 mA
               'main_mcu_voltage[10]', #2 mA
               'main_mcu_power[10]', #2 mW/10
               'main_mcu_power_flags[10]', #1                           !!!!!!!!!!!!
               'main_mcu_alert_flags[10]', #1 
               'main_line_key_voltage[10]', #2
               'main_line_limiter_imon[10]', #2  
               'main_line_current[10]', #2 mA
               'main_line_voltage[10]', #2 mA
               'main_line_power[10]', #2 mW/10
               'main_line_power_flags[10]', #1                           !!!!!!!!!!!!
               'main_line_alert_flags[10]', #1  

               'reserved_line_stm_err_code[10]', #2
               'reserved_line_temperature[10]', #1
               'reserved_line_flags[10]', #1
               'reserved_mcu_op_time[10]', #4
               'reserved_mcu_current[10]', #2 mA
               'reserved_mcu_voltage[10]', #2 mA
               'reserved_mcu_power[10]', #2 mW/10
               'reserved_mcu_power_flags[10]', #1                           !!!!!!!!!!!!
               'reserved_mcu_alert_flags[10]', #1 
               'reserved_line_key_voltage[10]', #2
               'reserved_line_limiter_imon[10]', #2  
               'reserved_line_current[10]', #2 mA
               'reserved_line_voltage[10]', #2 mA
               'reserved_line_power[10]', #2 mW/10
               'reserved_line_power_flags[10]', #1                           !!!!!!!!!!!!
               'reserved_line_alert_flags[10]', #1          
]



fields_lengths = (2,4,2,
                 1,1,1,1,4,
                 1,1,1,1,
                 2,2,2,1,1,
                 1,1,1,1,
                 2,2,
                 2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
                 4,
                 4,
                 16*SHORT_ERROR_LIST_SIZE,  #заглушка
                #  2*SHORT_ERROR_LIST_SIZE,4*SHORT_ERROR_LIST_SIZE,2*SHORT_ERROR_LIST_SIZE,
                #  2*SHORT_ERROR_LIST_SIZE,2*SHORT_ERROR_LIST_SIZE,
                #  1*SHORT_ERROR_LIST_SIZE,1*SHORT_ERROR_LIST_SIZE,
                #  1*2*SHORT_ERROR_LIST_SIZE,1*4*SHORT_ERROR_LIST_SIZE,
                #  2*2*SHORT_ERROR_LIST_SIZE,4*SHORT_ERROR_LIST_SIZE,
                 2,1,1,4,2,2,2,1,1,2,2,2,2,2,1,1,2,1,1,4,2,2,2,1,1,2,2,2,2,2,1,1,
                 2,1,1,4,2,2,2,1,1,2,2,2,2,2,1,1,2,1,1,4,2,2,2,1,1,2,2,2,2,2,1,1,
                 2,1,1,4,2,2,2,1,1,2,2,2,2,2,1,1,2,1,1,4,2,2,2,1,1,2,2,2,2,2,1,1,
                 2,1,1,4,2,2,2,1,1,2,2,2,2,2,1,1,2,1,1,4,2,2,2,1,1,2,2,2,2,2,1,1,
                 2,1,1,4,2,2,2,1,1,2,2,2,2,2,1,1,2,1,1,4,2,2,2,1,1,2,2,2,2,2,1,1,
                 2,1,1,4,2,2,2,1,1,2,2,2,2,2,1,1,2,1,1,4,2,2,2,1,1,2,2,2,2,2,1,1,
                 2,1,1,4,2,2,2,1,1,2,2,2,2,2,1,1,2,1,1,4,2,2,2,1,1,2,2,2,2,2,1,1,
                 2,1,1,4,2,2,2,1,1,2,2,2,2,2,1,1,2,1,1,4,2,2,2,1,1,2,2,2,2,2,1,1,
                 2,1,1,4,2,2,2,1,1,2,2,2,2,2,1,1,2,1,1,4,2,2,2,1,1,2,2,2,2,2,1,1,
                 2,1,1,4,2,2,2,1,1,2,2,2,2,2,1,1,2,1,1,4,2,2,2,1,1,2,2,2,2,2,1,1)


cur_beg_i = 0
add_data_structure = {}
for i in range(len(field_names)):
    add_data_structure[field_names[i]] = (cur_beg_i, fields_lengths[i])
    cur_beg_i = cur_beg_i + fields_lengths[i]


