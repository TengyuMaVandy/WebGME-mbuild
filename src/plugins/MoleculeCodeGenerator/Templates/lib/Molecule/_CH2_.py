
# -- ==ch2== --
import mbuild as mb


class CH2(mb.Compound):
    def __init__(self):
        super(CH2, self).__init__()

        mb.load('E:\\Users\TengyuMa\WebGME\WebGME-mbuild\src\plugins\MoleculeCodeGenerator\Templates\lib\moieties\ch2.pdb', compound=self, relative_to_module=self.__module__)
        mb.translate(self, -self[0].pos)  # Move carbon to origin.

        self.add(mb.Port(anchor=self[0]), 'up')
        self.add(mb.Port(anchor=self[0]), 'down')
        
        mb.translate(self['down'], [0,-0.07,0])
        mb.translate(self['up'], [0,0.07,0])

if __name__ == "__main__":
    ch2 = CH2()
    tempdir = ch2.visualize(show_ports=False)
    print(tempdir)
