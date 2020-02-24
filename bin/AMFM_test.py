#!/usr/bin/env python

"""
Script to test the AMFM_decompy package.

Version 0.0
23/Feb/2020 Richard Hemphill - rhemphill2019@my.fit.edu
"""
import amfm_decompy_cuda
import amfm_decompy_cuda.pYAAPT as pyaapt
import amfm_decompy_cuda.pyQHM as pyqhm
import amfm_decompy_cuda.basic_tools as basic
import os.path

# Declare the variables.
file_name = os.path.dirname(amfm_decompy.__file__)+os.sep+"sample.wav"
window_duration = 0.015   # in seconds
nharm_max = 25
SNR = float('Inf')

# Create the signal object.
signal = basic.SignalObj(file_name)

# Create the window object.
window = pyqhm.SampleWindow(window_duration, signal.fs)

# Create the pitch object and calculate its attributes.
pitch = pyaapt.yaapt(signal)

# Set the number of modulated components.
signal.set_nharm(pitch.values, nharm_max)

# Check if gaussian noise has to be added.
if SNR != float('Inf'):
    signal.noiser(pitch.values, SNR)

# Perform the QHM extraction.
QHM = pyqhm.qhm(signal, pitch, window, 0.001, N_iter = 3, phase_tech = 'phase')

print ("QHM SRER: {}".format(QHM.SRER))

# Perform the aQHM extraction.
aQHM = pyqhm.aqhm(signal, QHM, pitch, window, 0.001, N_iter = 3, N_runs = 2,
            phase_tech = 'phase')

print ("aQHM SRER: {}".format(aQHM.SRER))

# Perform the eaQHM extraction.
eaQHM = pyqhm.eaqhm(signal, aQHM, pitch, window, 0.001, N_iter=3, N_runs=2,
              phase_tech = 'phase')

print ("eaQHM SRER: {}".format(eaQHM.SRER))

