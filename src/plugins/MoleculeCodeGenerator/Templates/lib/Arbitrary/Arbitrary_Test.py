
# -- ==arbitrary compound== --
import mbuild as mb


from Alkyl_Silane import Alkyl_Silane


class Arbitrary_Test(mb.Compound):
    """Generate all the instances of children based on the metaType they are.
    Connect all the instances based on the connections between each pair of them.
    Finally, describe a completed arbitrary compound. : P awesome!!!
    """
    def __init__(self):
        super(Arbitrary_Test, self).__init__()

        # Add all Compounds
    
        alkyl_silane = Alkyl_Silane()
        self.add(alkyl_silane, 'alkyl_silane')
        
        alkyl_silane = Alkyl_Silane()
        self.add(alkyl_silane, 'alkyl_silane')
        
        # Add Equivalence to connect Compounds
    
        mb.equivalence_transform(self['alkyl_silane'], self['alkyl_silane']['down'], self['alkyl_silane']['down'])
        
        # Hoist Port to be exposed.
    
        #alkane = Alkane(chain_length, cap_end=False)
        #self.add(alkane, 'alkane')
        #silane = Silane()
        #self.add(silane, 'silane')
        #mb.equivalence_transform(self['alkane'], self['alkane']['down'], self['silane']['up'])

        #self.add(silane['down'], 'down', containment=False)

# -- ==arbitrary compound== --
if __name__ == '__main__':
    arbitrary_test = Arbitrary_Test()
    tmpdir = arbitrary_test.visualize()
    print(tmpdir)
