# MiW-MBuild in WebGME
A domain specific modeling environment for complex molecular systems
## Team
Sallai Janos, Tengyu Ma
## mbuild
mBuild does hierarchical modeling, using the Composite pattern. The leaves of the hierarchy are particles (atoms). Atoms can be composed into Components, and Components can be composed into more complex components. In mBuild, Ports define the geometric constraints of the composition.
### MBuild in WebGME
1. Metamodel to describe the whole hierarchy in the chemistry field like Atom, Polymer, Monolayer.
2. Higher level examples such as Alkane, Beta_Cristobalite, Alkane_Monolayer.
3. Plug-in to generate python file based on the model.
4. Visualize dynamically for the model inside of the WebGME.
5. Easily get a visualization for the example you build.
