## TODO
- [x] make our custom topology work with controller `Ryu`
- [x] classic routing
- [x] classic routing performance testing
- [x] SDN routing with varied strategies
- [x] SDN routing performance testing
- [ ] report
## Tutorial || Q&A
### create topology from mininet

A possible simple solution to solve ["loop switches"](https://github.com/mininet/mininet/wiki/FAQ#ethernet-loops) problem.
``` bash
$ sudo mn --custom ~/create_topo.py --topo mytopo --switch ovsbr,stp=1 --controller remote
```
And wait for STP to converge.
```bash
mininet> py net.waitConnected()
```
Then 'ping' is available.

### install Ryu
https://ernie55ernie.github.io/sdn/2019/03/25/install-mininet-and-ryu-controller.html
https://ryu.readthedocs.io/en/latest/getting_started.html

-----
### Linux Bridge & ovs
https://www.cnblogs.com/bakari/p/8097439.html

### ovsk vs ovsbr vs ovs vs user
https://mailman.stanford.edu/pipermail/mininet-discuss/2016-May/006876.html

Key contents
```
 1) ovsk and ovs are the same, they are ovs switches that run in kernel space.

 2) Ovsbr is a OVs switch in standalone/bridge mode.

 3) User is a OVs switch that runs in user space and therefore it is much slower than OVSK or  OVS.

 4) Then you also have LinuxBridge which is a normal linux br, the ones you can add doing : "brctl addbr name".

 To compare you should use LinuxBridge and OVS. Import the linux 
 bridge in the following way: from mininet.nodelib import LinuxBridge 
 if you use the python API. And then when you add switches to your 
 topology do
 that:

  self.addSwitch(name, cls=LinuxBridge)  To add a normal switch.
  self.addSwitch(name, cls=OVSKernelSwitch) To add a OVS switch
```

