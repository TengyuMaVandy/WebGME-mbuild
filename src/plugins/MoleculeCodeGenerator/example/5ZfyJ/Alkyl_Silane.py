
# -- ==arbitrary compound== --
import mbuild as mb


from Silane import Silane
from Alkane import Alkane


class Alkyl_Silane(mb.Compound):
    """Generate all the instances of children based on the metaType they are.
    Connect all the instances based on the connections between each pair of them.
    Finally, describe a completed arbitrary compound. : P awesome!!!
    """
    def __init__(self):
        super(Alkyl_Silane, self).__init__()

        # Add all Compounds
    
        silane = Silane()
        self.add(silane, 'silane')
        
        alkane = Alkane()
        self.add(alkane, 'alkane')
        
        # Add Equivalence to connect Compounds
    
        mb.equivalence_transform(self['alkane'], self['alkane']['down'], self['silane']['up'])
        
        # Hoist Port to be exposed.
    
        self.add(silane['down'], 'down', containment=False)
        
        #alkane = Alkane(chain_length, cap_end=False)
        #self.add(alkane, 'alkane')
        #silane = Silane()
        #self.add(silane, 'silane')
        #mb.equivalence_transform(self['alkane'], self['alkane']['down'], self['silane']['up'])

        #self.add(silane['down'], 'down', containment=False)

# -- ==arbitrary compound== --
if __name__ == '__main__':
    alkyl_silane = Alkyl_Silane()
    tmpdir = alkyl_silane.visualize()
    print(tmpdir)
