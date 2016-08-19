RD C:\Users\jp\AppData\Local\Temp\SimLauncher /s /q

start cmd /k "C:\Users\jp\Desktop\NAO\SDKfolder\naoqi-sdk-2.4.3.28-win32-vs2010\bin/hal" -s hal-ipc9559 -p HAL/Robot/Type:string=Nao -p HAL/Simulation:int=1 -p HAL/Time:int=0 -p HAL/CycleTime:int=0 -p DCM/Time:int=0 -p DCM/CycleTime:int=0 -p HAL/SimShmId:int=9559 -p HAL/Ack:int=0 -p HAL/Nack:int=0 -p HAL/Error:int=0 

ping 127.0.0.1 -n 30 > nul

start cmd /k "C:\Users\jp\Desktop\NAO\SDKfolder\naoqi-sdk-2.4.3.28-win32-vs2010\bin/naoqi-bin.exe" -p 9559 --writable-path C:\Users\jp\AppData\Local\Temp\SimLauncher
