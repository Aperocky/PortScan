#!/usr/local/opt/python/bin/python3.7
import socket
import threading
import argparse
import re
import os
import time
try:
    from queue import Queue
except ImportError:
    from Queue import Queue

# A multithreading portscan module
class PortScan:

    # Regex Strings for parsing
    SINGLE_IP = r'^(?:\d{1,3}\.){3}\d{1,3}$'
    BLOCK_24 = r'^(?:\d{1,3}\.){3}0\/24$'
    GROUPED_IP = r'^\[.*\]$'

    def __init__(self, ip_str, port_str = None, thread_num = 100, show_refused=False, wait_time=5):
        # self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.sock.settimeout(10)
        self.ip_range = self.read_ip(ip_str)
        if port_str is None:
            self.ports = [22, 23, 80]
        else:
            self.ports = self.read_port(port_str)
        self.lock = threading.Lock()
        self.thread_num = thread_num
        if self.thread_num > 250:
            self.thread_num = 250
        self.q = Queue(maxsize=self.thread_num*2)
        self.gen = None # Generator instance to be instantiated later
        self.show_refused = show_refused
        self.wait_time = wait_time

    # Read in IP Address from string.
    def read_ip(self, ip_str):
        # Single IP address
        if re.match(PortScan.SINGLE_IP, ip_str):
            if all([x<256 for x in map(int, ip_str.split('.'))]):
                return [ip_str]
            raise ValueError('incorrect IP Address')
        # Block 24 IP address.
        if re.match(PortScan.BLOCK_24, ip_str):
            block_3 = list(map(int, ip_str.split('.')[:3]))
            if all([x<256 for x in block_3]):
                block_3s = '.'.join(map(str, block_3))
                return [block_3s+'.'+str(i) for i in range(256)]
            raise ValueError('incorrect IP Address')
        # List of IP Address
        if re.match(PortScan.GROUPED_IP, ip_str):
            ip_str = ip_str[1:-1]
            elements = [e.strip() for e in ip_str.split(',')]
            master = []
            for each in elements:
                try:
                    sub_list = self.read_ip(each)
                    master.extend(sub_list)
                except ValueError as e:
                    print("{} is not correctly formatted".format(each))
            return master
        raise ValueError('incorrect Match')

    # Read in port range from string delimited by ','
    def read_port(self, port_str):
        ports = port_str.split(',')
        port_list = []
        for port in ports:
            if re.match('^\d+$', port):
                port_list.append(int(port))
            elif re.match('^\d+-\d+$', port):
                p_start = int(port.split('-')[0])
                p_end = int(port.split('-')[1])
                p_range = list(range(p_start, p_end+1))
                port_list.extend(p_range)
            else:
                raise ValueError('incorrect Match')
        return port_list

    # Standalone thread for queue
    def fill_queue(self):
        while True:
            if not self.q.full():
                try:
                    self.q.put(next(self.gen))
                except StopIteration:
                    break
            else:
                time.sleep(0.05)
        return

    def run(self):
        # Generator that contains all ip:port pairs.
        self.gen = ((ip, port) for ip in self.ip_range for port in self.ports)
        queue_thread = threading.Thread(target=self.fill_queue)
        queue_thread.daemon = True
        queue_thread.start()
        for i in range(self.thread_num):
            t = threading.Thread(target=self.worker)
            t.daemon = True
            t.start()
        self.q.join()

    def worker(self):
        # Worker threads that take ports from queue and consume it
        while True: # never stop working!
            work = self.q.get()
            self.ping_port(*work)
            self.q.task_done()

    def ping_port(self, ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(self.wait_time)
        status = sock.connect_ex((ip, port))
        if status == 0:
            with self.lock:
                print('{}:{} OPEN'.format(ip, port))
        elif status not in [35, 64, 65] and self.show_refused:
            with self.lock:
                print('{}:{} ERRNO {}, {}'.format(ip, port, status, os.strerror(status)))
        return

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('ip')
    parser.add_argument('-p', '--port', action='store', dest='port')
    parser.add_argument('-t', '--threadnum', action='store', dest='threadnum', default=100, type=int)
    parser.add_argument('-e', '--show_refused', action='store_true', dest='show_refused', default=False)
    parser.add_argument('-w', '--wait', action='store', dest='wait_time', default=5, type=float)
    args = parser.parse_args()
    scanner = PortScan(ip_str=args.ip, port_str=args.port,
                       thread_num=args.threadnum, show_refused=args.show_refused,
                       wait_time=args.wait_time)
    scanner.run()

if __name__ == '__main__':
    main()
