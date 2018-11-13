# PortScan

PortScan is a command line utility that allows user to conduct scanning over a range of IP addresses and port ranges.

Install: `pip install portscan`

Usage: `portscan 8.8.8.8 [-p 22,80 [-t 100 [-e]]]`

![Simple Command](/Demo_0.png)

![Show more potential connection](/Demo_1.png)

`ip`: default and required argument, can parse single IP, list of IP, IP blocks:

    192.168.1.0 # single IP

    192.168.1.0/24 # A 24 block, from 192.168.1.0 to 192.168.1.255

    [192.168.1.0/24,8.8.8.8] # The aforementioned 24 block and 8.8.8.8.

    "[192.168.1.0/24, 8.8.8.8]" # if you want to use space in the command, wrap in quotes.

Options:

`-p`, `--port`: port range, default `22,23,80,5000,8000,8080,8888`, use `,` as a delimiter without space, support port range (e.g. `22-100,5000`).

`-t`, `--threadnum`: thread numbers, default 100

`-e`, `--show_refused`: show connection errors other than timeouts, e.g. connection refused, permission denied with errno number as they happen.

---

![PyPI version](http://img.shields.io/pypi/v/termdown.svg) &nbsp; ![Python 3.x](http://img.shields.io/badge/Python-3.x-green.svg) &nbsp; ![PyPI license](https://img.shields.io/github/license/mashape/apistatus.svg)
