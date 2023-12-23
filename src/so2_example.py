# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 15:22:05 2023

@author: hibad
"""

import numpy as np
from numpy import sin, cos, tan, pi
import cv2
import imageio

def draw_robot(img, theta, color=(0,0,0)):
    cv2.circle(img, ((125,125)), radius=20, color=color, thickness = 2)
    cv2.line(img, (125,125), (int(125+40*cos(theta)), int(125+40*sin(theta))), color=color, thickness = 2)
    return img
#%% example 1
theta = 0
theta_ref = pi/2 
img = np.ones((250,250))*255
img = draw_robot(img, theta_ref, (127,0.5,0.5))
K=0.05
frames=[]

for i in range(150):
    u=K*(theta_ref-theta)
    theta = theta+u
    img_t=draw_robot(img.copy(), theta)
    img_t = cv2.flip(img_t, 0)
    frames.append(img_t)
    


imageio.mimsave('ex1.gif', frames, loop=0)
#%% example 2
theta = 0
theta_ref = 3/2*pi 
img = np.ones((250,250))*255
img = draw_robot(img, theta_ref, (127,0.5,0.5))
K=0.05
frames=[]

for i in range(150):
    u=K*(theta_ref-theta)
    theta = theta+u
    img_t=draw_robot(img.copy(), theta)
    img_t = cv2.flip(img_t, 0)
    frames.append(img_t)
    


imageio.mimsave('ex2.gif', frames, loop=0)

#%% example 2
theta = 0
theta_ref = 2*pi 
img = np.ones((250,250))*255
img = draw_robot(img, theta_ref, (127,0.5,0.5))
K=0.05
frames=[]

for i in range(150):
    u=K*(theta_ref-theta)
    theta = theta+u
    img_t=draw_robot(img.copy(), theta)
    img_t = cv2.flip(img_t, 0)
    frames.append(img_t)
    


imageio.mimsave('ex3.gif', frames, loop=0)

