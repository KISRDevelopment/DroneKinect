#!/usr/bin/env python
# -*- coding: utf8 -*-

import socket


class Kinect_sock:

    def __init__(self, size=1024, host='', port=5050, backlog=5):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((host,port))
        sock.listen(backlog)
        self.sock = sock
