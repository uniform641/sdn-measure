#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet


class MyTopo(Topo):
    def __init__(self):
        Topo.__init__(self)

        # Add hosts
        u1 = self.addHost('u1')
        u2 = self.addHost('u2')
        u3 = self.addHost('u3')
        u4 = self.addHost('u4')
        server = self.addHost('server')

        # Add switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')

        # Add links
        self.addLink(u1, s1)
        self.addLink(u2, s2)
        self.addLink(u3, s4)
        self.addLink(u4, s5)
        self.addLink(server, s6)

        self.addLink(s1, s2)
        self.addLink(s1, s3)
        self.addLink(s1, s4)
        self.addLink(s2, s3)
        self.addLink(s2, s5)
        self.addLink(s3, s4)
        self.addLink(s3, s5)
        self.addLink(s4, s5)
        self.addLink(s4, s6)
        self.addLink(s5, s6)


topos = {'mytopo':MyTopo}
