# NAO search path in V-REP
This project goal is to make NAO search a path in a simple labirinth in v-rep.
After control nao and v-rep simulation we created a labirinth problem where nao has to find the exit using his positioning and calculating the best path to the exit.
A big part of this was built upon [PierreJac]'s work. Please read his work as a start point for this.
In addition to v-rep we will use the Choregraphe suite and the Python NAOqi SDK from Aldebaran.
One video with this working is here [video]

### Requirements
- [v-rep] : A free simulation environment.
- [Python NAOqi-SDK] : Contain all the function you need to manipulate your NAO (virtual or not) using python.

### Quickstart
- After all prerequisites installed:

$ ./EnvironmentSetup/start_linux.sh

$ ./script/Labirinth.py

[PierreJac]:https://raw.githubusercontent.com/PierreJac/Project-NAO-Control
[v-rep]:http://www.coppeliarobotics.com/downloads.html
[Python NAOqi-SDK]:https://community.aldebaran.com/en/resources/software
[video]:https://www.youtube.com/watch?v=nk09YlGYX5E