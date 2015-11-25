import re
import sys
import time
import socket
import python_ardrone.libardrone as libardrone
from kinect_socket import Kinect_sock

SIZE = 256
SLEEP_TIME = 4e-6

def main():
    regex = re.compile(r'\x02(-?\d+.\d+),(-?\d+.\d+),<(-?\d+.\d+)>\x03')
    deltax = 0
    drone = libardrone.ARDrone()
    drone.speed = 0.1
    try:
        sock = Kinect_sock()
        print('Waiting for someone to connect')
    except:
        sys.exit(-1)
    client,_ = sock.sock.accept()
    print('Launching')
    drone.takeoff()
    drone.hover()
    while 1: # running:
        try:
            """Set the pitch, roll, and yaw"""
            data = client.recv(SIZE)
            par_data = [(float(i[0]),float(i[1]),float(i[2])) for i in regex.findall(data)]
            _,roll, delta = par_data[-1]

            if deltax == 0:
                print('deltax = {}'.format(delta))
                deltax = delta

            if delta < 0:
                raise KeyboardInterrupt
                print('LAND')
                break

            if roll > 0.4:
               drone.move_right()
               print('Turn_right')
            elif roll < -.4:
               drone.move_left()
               print('Turn_left')

            if delta > deltax*1.3:
                deltax = delta
                drone.move_forward()
                print("Forward")
            elif delta < deltax*.7:
                deltax = delta
                drone.move_backward()
                print("Backwords")

            time.sleep(SLEEP_TIME)

        except (KeyboardInterrupt, socket.error):
            drone.land()
            drone.halt()
            print("SOCK Error")
            break
        except IndexError:
            continue

if __name__ == '__main__':
    main()
