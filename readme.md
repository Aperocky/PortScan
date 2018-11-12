# PortScan

PortScan is a command line utility that allows user to conduct scanning over a range of IP addresses and port ranges.

Usage: `portscan 192.168.1.0/24 [-p 80-5000 [-t 100 [-e]]]`

`ip`: default and required argument, can parse single IP, list of IP, IP blocks:

    192.168.0.1 # single IP

    192.168.1.0/24 # A 24 block, from 192.168.1.0 to 192.168.1.255

    [192.168.1.0/24,8.8.8.8] # The aforementioned 24 block and 8.8.8.8.

    "[192.168.1.0/24, 8.8.8.8]" # if you want to use space in the command, wrap in quotes.

`-p`, `--port`: port range, default `22,23,80,5000,8000,8080`, use `,` without space, support port range (`22-100,5000`).

`-t`, `--threadnum`: thread numbers, default 100

`-e`, `--show_refused`: show connection errors other than timeouts.
