cd ~/nao/sdk/naoqi-sdk/bin

./hal -s hal-ipc9559 -p HAL/Robot/Type:string=Nao -p HAL/Simulation:int=1 -p HAL/Time:int=0 -p HAL/CycleTime:int=0 -p DCM/Time:int=0 -p DCM/CycleTime:int=0 -p HAL/SimShmId:int=9559 -p HAL/Ack:int=0 -p HAL/Nack:int=0 -p HAL/Error:int=0 

./naoqi-bin -p 9559 --writable-path C:\Users\jp\AppData\Local\Temp\SimLauncher


cd ~/nao/V-REP
./vrep.sh ~/nao/workspace/scene/Labrinth.ttt
