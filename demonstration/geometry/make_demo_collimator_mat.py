#!/usr/bin/python
#
from pyne.material import Material,MaterialLibrary
print "Welcome!"
mat_lib=MaterialLibrary()
#
lead = Material({'Pb':1},density=11.35)
lead = lead.expand_elements()

# define a simple water since O-18 not in mcnp xs libs
watervec={10010:2,80160:1} # simple water
water = Material()
water.density = 1.0
water.from_atom_frac(watervec)

# Air
air = Material({'C':0.000124, 'N':0.755268, 'O':0.231781, 'Ar':0.012827},
               density=0.001205)
air = air.expand_elements()

# Put materials in the mat_lib
mat_lib["Lead"] = lead
mat_lib["Air"] = air
mat_lib["Water"] = water

#
mat_lib.write_hdf5("demo_collimator_mat_lib.h5")
#
print "All done!"
