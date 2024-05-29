# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 21:16:33 2024

@author: hibad
"""

import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt

mesh=o3d.io.read_triangle_mesh("../resource/Utah_teapot_(solid).stl")
mesh.compute_vertex_normals()
# mesh.transform(np.array([[0, 0, 1, 0],
#                          [0, 1, 0, 0],
#                          [1,0 ,0, 0 ],
#                          [0, 0 , 0 , 1]]))

R_init=mesh.get_rotation_matrix_from_xyz((np.random.rand() ,np.random.rand(),np.random.rand()))
mesh.rotate(R_init)
o3d.visualization.draw_geometries([mesh])
# vis = o3d.visualization.Visualizer()
# vis.create_window(visible=False) 
# vis.add_geometry(mesh)
# vis.update_geometry(mesh)
# vis.poll_events()
# vis.update_renderer()
# vis.capture_screen_image("../resource/test.png")
# vis.destroy_window()