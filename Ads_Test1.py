#!/usr/bin/env python
# coding: utf-8

# # Connect to TwinCAT System

# In[98]:


import pyads
from ctypes import sizeof

ads_net_id='172.16.52.5.1.1'
plc=pyads.Connection(ads_net_id,pyads.PORT_TC3PLC1)

print('Connecting to TwinCAT PLC..')
plc.open()
print('Current connection status:',plc.is_open)
print('Current Status:',plc.read_state())

print('Closing the Connections..')
plc.close()
print('Current Status:',plc.is_open)


# # Reading Devices

# In[104]:


import pyads
from ctypes import sizeof

ads_net_id='172.16.52.5.1.1'
plc=pyads.Connection(ads_net_id,pyads.PORT_TC3PLC1)

print('Connecting to TwinCAT PLC..')
plc.open()
print('Current connection status:',plc.is_open)
print('Current Status:',plc.read_state())

print('Reading Devices..')
var=plc.read_by_name(data_name='GVL.i32',plc_datatype=pyads.PLCTYPE_DINT)
print('GVL.i32 is',var)

print('Closing the Connections..')
plc.close()
print('Current Status:',plc.is_open)


# # Get the Symbols

# In[107]:


import pyads
from ctypes import sizeof

ads_net_id='172.16.52.5.1.1'
plc=pyads.Connection(ads_net_id,pyads.PORT_TC3PLC1)

print('Connecting to TwinCAT PLC..')
plc.open()
print('Current connection status:',plc.is_open)
print('Current Status:',plc.read_state())

print('Reading Devices..')
var=plc.read_by_name(data_name='GVL.i32',plc_datatype=pyads.PLCTYPE_DINT)
print('GVL.i32 is',var)

symbols=plc.get_all_symbols()
print('Closing the Connections..')
plc.close()
print('Current Status:',plc.is_open)


# # Read the Devices as List

# In[132]:


import pyads
from ctypes import sizeof

ads_net_id='172.16.52.5.1.1'
plc=pyads.Connection(ads_net_id,pyads.PORT_TC3PLC1)

print('Connecting to TwinCAT PLC..')
plc.open()
print('Current connection status:',plc.is_open)
print('Current Status:',plc.read_state())

print('Reading Devices List..')
varList=['GVL.i32','GVL.var1','GVL.var2','GVL.var3']
vardata=plc.read_list_by_name(varList)
for k,v in vardata.items():
    print(k,':',v)

print('Closing the Connections..')
plc.close()
print('Current Status:',plc.is_open)



# #  Write Devices

# In[135]:


import pyads
from ctypes import sizeof

ads_net_id='172.16.52.5.1.1'
plc=pyads.Connection(ads_net_id,pyads.PORT_TC3PLC1)

print('Connecting to TwinCAT PLC..')
plc.open()
print('Current connection status:',plc.is_open)
print('Current Status:',plc.read_state())

plc.write_by_name(data_name='GVL.i32',value=100,plc_datatype=pyads.PLCTYPE_DINT)

print('Reading Devices List..')
varList=['GVL.i32','GVL.var1','GVL.var2','GVL.var3']
vardata=plc.read_list_by_name(varList)
for k,v in vardata.items():
    print(k,':',v)

print('Closing the Connections..')
plc.close()
print('Current Status:',plc.is_open)


# # Write Devices as List

# In[137]:


import pyads
from ctypes import sizeof

ads_net_id='172.16.52.5.1.1'
plc=pyads.Connection(ads_net_id,pyads.PORT_TC3PLC1)

print('Connecting to TwinCAT PLC..')
plc.open()
print('Current connection status:',plc.is_open)
print('Current Status:',plc.read_state())

varList=['GVL.i32','GVL.var1','GVL.var2','GVL.var3']
varWriteList={
    'GVL.i32':20
    ,'GVL.var1':99
    ,'GVL.var2':32
    ,'GVL.var3':88
}

plc.write_list_by_name(data_names_and_values=varWriteList)

print('Reading Devices List..')
varList=['GVL.i32','GVL.var1','GVL.var2','GVL.var3']
vardata=plc.read_list_by_name(varList)
for k,v in vardata.items():
    print(k,':',v)

print('Closing the Connections..')
plc.close()
print('Current Status:',plc.is_open)


# # Notifications

# In[191]:


import pyads
from ctypes import sizeof

ads_net_id='172.16.52.5.1.1'
plc=pyads.Connection(ads_net_id,pyads.PORT_TC3PLC1)

print('Connecting to TwinCAT PLC..')
plc.open()
print('Current connection status:',plc.is_open)
print('Current Status:',plc.read_state())

@plc.notification(pyads.PLCTYPE_DINT)
def callback(handle, name, timestamp, value):
    print('handle:',handle)
    print('name:',name)
    print('timestamp:',timestamp)
    print('value:',value)

attr = pyads.NotificationAttrib(sizeof(pyads.PLCTYPE_DINT))
handles = plc.add_device_notification('GVL.i32', attr, callback)

#do some things

plc.del_device_notification(*handles)
plc.close()


# In[ ]:




