# ---------------------------------------------------------------------
# Project "Track 3D-Objects Over Time"
# Copyright (C) 2020, Dr. Antje Muntzinger / Dr. Andreas Haja.
#
# Purpose of this file : Kalman filter class
#
# You should have received a copy of the Udacity license together with this program.
#
# https://www.udacity.com/course/self-driving-car-engineer-nanodegree--nd013
# ----------------------------------------------------------------------
#

# imports
import numpy as np

# add project directory to python path to enable relative imports
import os
import sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
import misc.params as params 

class Filter:
    '''Kalman filter class'''
    def __init__(self):
        pass

    def F(self):
        ############
        # TODO Step 1: implement and return system matrix F
        ############
        dt = params.dt
        F = np.eye((params.dim_state))
        F = np.asmatrix(F)
        F[0,3] = dt
        F[1,4] = dt
        F[2,5] = dt

        return F
        
        ############
        # END student code
        ############ 

    def Q(self):
        ############
        # TODO Step 1: implement and return process noise covariance Q
        ############
        dt2 = params.dt ** 2
        dt3 = params.dt ** 3
        
        q_11 = dt3 * params.q / 3.0
        q_13 = dt2 * params.q / 2.0
        q_33 = params.dt * params.q
        
        Q = np.matrix([[q_11, 0.0, 0.0, q_13, 0.0, 0.0],
                       [0.0, q_11, 0.0, 0.0, q_13, 0.0],
                       [0.0, 0.0, q_11, 0.0, 0.0, q_13],
                       [q_13, 0.0, 0.0, q_33, 0.0, 0.0],
                       [0.0, q_13, 0.0, 0.0, q_33, 0.0],
                       [0.0, 0.0, q_13, 0.0, 0.0, q_33],
                      ])
                    

        return Q
        
        ############
        # END student code
        ############ 

    def predict(self, track):
        ############
        # TODO Step 1: predict state x and estimation error covariance P to next timestep, save x and P in track
        ############

        F = self.F()
        Q = self.Q()
        P = track.P
        
        x =  F * track.x
        P = F*P*F.transpose() + Q
        
        track.set_x(x)
        track.set_P(P)
        
        ############
        # END student code
        ############ 

    def update(self, track, meas):
        ############
        # TODO Step 1: update state x and covariance P with associated measurement, save x and P in track
        ############
        x = track.x        
        H = meas.sensor.get_H(x)     
        gamma = self.gamma(track, meas)
        
        S = self.S(track, meas, H)
        P = track.P
        K = P*H.transpose()*np.linalg.inv(S)
        x = x + K*gamma
        I = np.identity(params.dim_state)
        P = (I - K*H) * P
        
        track.set_x(x)
        track.set_P(P)
        
        ############
        # END student code
        ############ 
        track.update_attributes(meas)
    
    def gamma(self, track, meas):
        ############
        # TODO Step 1: calculate and return residual gamma
        ############

        H = meas.sensor.get_hx(track.x)
        
        gamma = meas.z - H
        
        return gamma
        
        ############
        # END student code
        ############ 

    def S(self, track, meas, H):
        ############
        # TODO Step 1: calculate and return covariance of residual S
        ############

        S = H*track.P*H.transpose() + meas.R

        return S
        
        ############
        # END student code
        ############ 