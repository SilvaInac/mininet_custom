from mininet.topo import Topo

class MyTopo( Topo ):
    "3 host 2 switch 2 host custom topology"

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        leftHost1 = self.addHost( 'h1' )
        leftHost2=self.addHost('h2')
        middleHost1=self.addHost('h3')
        middleHost2=self.addHost('h4')
        rightHost1=self.addHost('h5')
        rightHost2=self.addHost('h6')
        rightHost3=self.addHost('h7')
        rightHost4=self.addHost('h8')
        rightHost1a=self.addHost('h9')
        leftHost1a=self.addHost('h10')

        leftSwitch = self.addSwitch('S1')
        middleSwitch = self.addSwitch('S2')
        rightSwitch = self.addSwitch('S3')
        leftSwitch1a = self.addSwitch('S4')
        rightSwitch1a = self.addSwitch('S5')

        # Add links
        self.addLink( leftHost1, leftSwitch )
        self.addLink( leftHost2, leftSwitch )
        self.addLink( middleHost1, middleSwitch )
        self.addLink( middleHost2, middleSwitch )
        self.addLink( rightHost1, rightSwitch )
        self.addLink( rightHost2, rightSwitch )
        self.addLink( rightHost3, rightSwitch )
        self.addLink( rightHost4, rightSwitch )
        self.addLink( rightHost1a, rightSwitch1a )
        self.addLink( leftHost1a, leftSwitch )
        self.addLink( rightHost1a, rightSwitch1a )
        self.addLink( leftHost1a, leftSwitch1a )
        
        self.addLink( leftSwitch1a, leftSwitch )
        self.addLink( leftSwitch, middleSwitch )
        self.addLink( middleSwitch, rightSwitch )
        self.addLink( rightSwitch, rightSwitch1a )

topos = { 'mytopo': ( lambda: MyTopo() ) }
