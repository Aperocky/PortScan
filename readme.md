# PortScan

![PyPI version](http://img.shields.io/pypi/v/portscan.svg) &nbsp; ![Python 3.x](http://img.shields.io/badge/Python-3.x-green.svg) &nbsp; ![PyPI license](https://img.shields.io/github/license/mashape/apistatus.svg) &nbsp; [![Downloads](https://pepy.tech/badge/portscan)](https://pepy.tech/project/portscan)

PortScan is a *light-weight* command line utility that allows user to conduct scanning over a range of IP addresses and port ranges with multi-threading.

Install: `pip install portscan`

Upgrade: `pip install portscan --upgrade`

Usage: `portscan [192.168.1.0/24] [-p 22,80-200 [-t 100 [-w 1 [-e]]]]`

*New in version 0.2.1:*

![Simple Command](/images/Demo_3.png)

By default the command checks for your *Local Area Network* IP first, and then initiate a block wise search. specify IP if you want to search any other IP blocks. *Note: This is not available before 0.2.1, please update or specify IP if you're using 0.2.0 and older*

Use `-w [float]` to change timeout settings from default of `3` seconds: for LAN, this can be as low as `0.1`. `1` is usually good enough for continental level connection.

![Fast scanning](/images/Demo_2.png)
*Scanned 5000 ports in 2 seconds*

To show more potential connection, use `-e`, this will show you all ports that are not timed out.

![Show more potential connection](/images/Demo_1.png)

### Arguments

`ip`: default and optional *(since 0.2.1, required before 0.2.1)* argument, can parse single IP, list of IP, IP blocks:

    192.168.1.0 # single IP

    192.168.1.0/24 # A 24 block, from 192.168.1.0 to 192.168.1.255

    [192.168.1.0/24,8.8.8.8] # The aforementioned 24 block and 8.8.8.8.

    "[192.168.1.0/24, 8.8.8.8]" # if you want to use space in the command, wrap in quotes.

Options:

`-p`, `--port`: port range, default `22,23,80`, use `,` as a delimiter without space, support port range (e.g. `22-100,5000`).

`-t`, `--threadnum`: thread numbers, default 500, as of now, thread number have a hard cap of 2048. More thread will increase performance on large scale scans.

`-e`, `--show_refused`: show connection errors other than timeouts, e.g. connection refused, permission denied with errno number as they happen.

`-w`, `--wait`: Wait time for socket to respond. If scanning LAN or relatively fast internet connection, this can be set to `1` or even `0.2` for faster scanning. Default `3` seconds

`-s`, `--stop_after_open`: Number of open ports to be discovered after which scan would be gracefully stopped. Default `0` for not stopping.

## Python API
One can also use this portscan inside existing python scripts.  
Consider following example for finding out adb port for Android device in LAN with static IP:
```python
from portscan import PortScan
ip = '192.168.1.42'
port_range = '5555,37000-44000'
scanner = PortScan(ip, port_range, thread_num=500, show_refused=False, wait_time=1, stop_after_open=True)
open_port_discovered = scanner.run()  # <----- actual scan
# run returns a list of (ip, open_port) tuples
adb_port = int(open_port_discovered[0][1])

# Usecase specific part
from adb_shell.adb_device import AdbDeviceTcp, AdbDeviceUsb
device1 = AdbDeviceTcp(ip, adb_port, default_transport_timeout_s=9)
device1.connect(rsa_keys=[python_rsa_signer], auth_timeout_s=0.1)  # adb connect
# shell exec
notifications_dump = device1.shell('dumpsys notification').encode().decode('ascii','ignore')
device1.close()

print(notifications_dump)
```
## Acknowledgement

Jamieson Becker: For coming up with a way to find local IP on stackoverflow, which I used: https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
