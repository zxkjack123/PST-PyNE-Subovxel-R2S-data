## Description
This folder contains geometry, material definition and input files for the demonstration problem of PyNE sub-voxel R2S.

- geomery: problem design and geometry/material inputs
  - demo\_collimator\_design.pdf: the design of the problem
  - demo_collimator.cub: the Trelis CAD file of the problem
  - geom.h5m: the material laden geometry file for DAG-MCNP5 transport
  - make_demo_collimator_mat.py: the python script to build PyNE material

- neutron_transport: input files for neutron transport
  - input: input file for neutron transport with DAG-MCNP5
  - wwinp1: the weight window input file

- r2s_run: files related to PyNE voxel/sub-voxel R2S workflow
  - ref: configure and parameters for REF case
  - def: configure and parameters for DEF case
  - sub: configure and parameters for SUB case

- photon_transport: files related to photon transport
  - input: input file for photon transport with DAG-MCNP5
