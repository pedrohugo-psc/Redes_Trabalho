from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSSwitch, RemoteController
from mininet.cli import CLI

class CustomTopology(Topo):
        def build(self):
            h1 = self.addHost('h1', ip='10.0.1.1/8')
            h2 = self.addHost('h2', ip='10.0.2.2/8')
            h3 = self.addHost('h3', ip='11.0.3.1/8')
            h4 = self.addHost('h4', ip='11.0.4.2/8')
            h5 = self.addHost('h5', ip='12.0.5.1/8')
            h6 = self.addHost('h6', ip='12.0.6.2/8')
            h7 = self.addHost('h7', ip='13.0.7.1/8')
            h8 = self.addHost('h8', ip='14.0.8.1/8')

            s1 = self.addSwitch('s1')
            s2 = self.addSwitch('s2')
            s3 = self.addSwitch('s3')
            s4 = self.addSwitch('s4')
            s5 = self.addSwitch('s5')

            self.addLink(s1, s2)
            self.addLink(s2, s3)
            self.addLink(s3, s4)
            self.addLink(s4, s5)
            self.addLink(s5, s1)

            self.addLink(h1, s1)
            self.addLink(h2, s1)
            self.addLink(h3, s2)
            self.addLink(h4, s2)
            self.addLink(h5, s3)
            self.addLink(h6, s3)
            self.addLink(h7, s4)
            self.addLink(h8, s5)

def run_custom_topology():
    topo = CustomTopology()

    # Crie uma instância da rede Mininet
    net = Mininet(topo=topo, switch=OVSSwitch, controller=RemoteController)

    c0 = net.addController('c0', port=6633)

    c0.start()

    # Inicie a rede
    net.start()

    # Execute o CLI Mininet para interagir com a topologia
    CLI(net)

    # Pare a rede ao sair do CLI
    net.stop()

if __name__ == '__main__':
    run_custom_topology()

topos = {'customtopology': (lambda: CustomTopology())}
