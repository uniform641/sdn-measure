## create topology from mininet

A possible simple solution to solve ["loop switches"](https://github.com/mininet/mininet/wiki/FAQ#ethernet-loops) problem.
``` bash
$ sudo mn --custom ~/create_topo.py --topo mytopo --switch ovsbr,stp=1 --controller remote
```
And wait for STP to converge.
```bash
mininet> py net.waitConnected()
```
Then 'ping' is available.