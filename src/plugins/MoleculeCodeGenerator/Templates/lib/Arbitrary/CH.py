
# -- ==arbitrary compound== --
import mbuild as mb


from CH2_1 import CH2_1
from CH2_2 import CH2_2
from CH2_3 import CH2_3
from CH3 import CH3


class CH(mb.Compound):
    """Generate all the instances of children based on the metaType they are.
    Connect all the instances based on the connections between each pair of them.
    Finally, describe a completed arbitrary compound. : P awesome!!!
    """
    def __init__(self):
        super(CH, self).__init__()

        # Add all Compounds
    
        ch2_1 = CH2_1()
        self.add(ch2_1, 'ch2_1')
        
        ch2_2 = CH2_2()
        self.add(ch2_2, 'ch2_2')
        
        ch2_3 = CH2_3()
        self.add(ch2_3, 'ch2_3')
        
        ch3 = CH3()
        self.add(ch3, 'ch3')
        
        # Add Equivalence to connect Compounds
    
        mb.equivalence_transform(self['ch2_1'], self['ch2_1']['down'], self['ch2_2']['up'])
        
        mb.equivalence_transform(self['ch2_2'], self['ch2_2']['down'], self['ch2_3']['up'])
        
        mb.equivalence_transform(self['ch2_3'], self['ch2_3']['down'], self['ch3']['up'])
        
        # Hoist Port to be exposed.
    
        self.add(ch2_1['up'], 'up', containment=False)
        
        #alkane = Alkane(chain_length, cap_end=False)
        #self.add(alkane, 'alkane')
        #silane = Silane()
        #self.add(silane, 'silane')
        #mb.equivalence_transform(self['alkane'], self['alkane']['down'], self['silane']['up'])

        #self.add(silane['down'], 'down', containment=False)

# -- ==arbitrary compound== --
if __name__ == '__main__':
    ch = CH()
    tmpdir = ch.visualize()
    print(tmpdir)
