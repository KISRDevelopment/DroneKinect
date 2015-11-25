Drone-Kinect Project
====================

There are two directories ``kinect_code`` and ``drone_code``. The ``kinect_code`` directory is a modification of one of the MS Kinect SDK example code. The ``drone_code`` is a Python code that realies on ``python_ardrone`` project. 

Implementation
--------------

The project is using server client architecture. The Python code has to run first to establish the server and the wait for a connection from the client code(Kinect Code). Once the connection is established the client code will send the position data back to the server(Python) applying normalization functions to the data. The Python code uses Regex to extract the data from the stream. The stream sends the data by using the following format ``binary 2Roll,Pitch,<Delta>binary 3``. 


Running code 
------------

Server
######

1. Getting the IP address of the Server by using ``ifconfig``
2. run ``python KinectDrone/drone_code/drone_control.py``


Client
######

1. Installing MS Visual Studio
2. Installing Kinect SDK
3. In ``sendkinectdata.h`` write the IP address of the server
4. Running the code inside ``kinect_code``
