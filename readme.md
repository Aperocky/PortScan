# PortScan

PortScan is a command line utility that allows user to conduct scanning over a range of IP addresses and port ranges.

Usage: `portscan 192.168.1.0/24 [-p 80-5000 [-t 1000]]`

`-p`, `--port`: port range, default `22,23,80,5000,8000,8080`, use `,` without space, support port range (`22-100,5000`).

`-t`, `--threadnum`: thread numbers, default 100

`-e`, `--show_refused`: show connection errors other than timeouts.
