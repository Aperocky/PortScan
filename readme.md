# PortScan

![PyPI version](http://img.shields.io/pypi/v/portscan.svg) &nbsp; ![Python 3.x](http://img.shields.io/badge/Python-3.x-green.svg) &nbsp; ![Python 2.x](http://img.shields.io/badge/Python-2.x-green.svg) &nbsp; ![PyPI license](https://img.shields.io/github/license/mashape/apistatus.svg) &nbsp; [![Downloads](https://pepy.tech/badge/portscan)](https://pepy.tech/project/portscan)

PortScan is a *light-weight* command line utility that allows user to conduct scanning over a range of IP addresses and port ranges with multi-threading.

Install: `pip install portscan`

Usage: `portscan 8.8.8.8 [-p 22,80 [-t 100 [-w 1 [-e]]]]`

![Simple Command](/images/Demo_0.png)

Use `-w [float]` to change timeout settings from default of `5` seconds: for LAN, this can be as low as `0.1`. `1` is usually good enough for continental level connection.

![Fast scanning](/images/Demo_2.png)
*Scanned 5000 ports in 4 seconds*

To show more potential connection, use `-e`, this will show you all ports that are not timed out.

![Show more potential connection](/images/Demo_1.png)

### Arguments

`ip`: default and required argument, can parse single IP, list of IP, IP blocks:

    192.168.1.0 # single IP

    192.168.1.0/24 # A 24 block, from 192.168.1.0 to 192.168.1.255

    [192.168.1.0/24,8.8.8.8] # The aforementioned 24 block and 8.8.8.8.

    "[192.168.1.0/24, 8.8.8.8]" # if you want to use space in the command, wrap in quotes.

Options:

`-p`, `--port`: port range, default `22,23,80,5000,8000,8080,8888`, use `,` as a delimiter without space, support port range (e.g. `22-100,5000`).

`-t`, `--threadnum`: thread numbers, default 100, as of now, thread number have been limited to 250 to avoid `errno 24`

`-e`, `--show_refused`: show connection errors other than timeouts, e.g. connection refused, permission denied with errno number as they happen.

`-w`, `--wait`: Wait time for socket to respond. If scanning LAN or relatively fast internet connection, this can be set to `1` or even `0.2` for faster scanning.
