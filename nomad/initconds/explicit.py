"""
Sample a specific geometry or set of geometries.
"""
import numpy as np
import nomad.core.glbl as glbl
import nomad.core.trajectory as trajectory


def set_initial_coords(master):
    """Takes initial position and momentum from geometry specified in input"""
    coords = glbl.properties['init_coords']
    ndim   = coords.shape[-1]

    for coord in coords:
        itraj = trajectory.Trajectory(glbl.properties['n_states'], ndim,
                                      width=glbl.properties['crd_widths'],
                                      mass=glbl.properties['crd_masses'],
                                      parent=0, kecoef=glbl.kecoef)

        # set position and momentum
        itraj.update_x(np.array(coord[0]))
        itraj.update_p(np.array(coord[1]))

        # add a single trajectory specified by geometry.dat
        master.add_trajectory(itraj)
