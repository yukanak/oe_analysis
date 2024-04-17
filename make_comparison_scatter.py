import os,sys
import numpy as np
import pickle
import pylab as pl
import Lx_ModuleMapping as minfo
import triangle_mapping_Lx as tri
import histogram as hist
import shutil
import matplotlib.pyplot as plt

module = 'H10'
date = '20240416'
run = '%s_BA4_H10'%date
im = 1
date_sk = '20230822'
run_sk = '%s_SK_H10'%date
im_sk = 0
inpath = 'outputs/'
fn = 'dpdt_results.txt'
fn_sk = 'dpdt_results_sk.txt'

cmap = 'jet'
testbed = 'BA'
testbed_sk = 'SK'
infile = inpath + fn
infile_sk = inpath + fn_sk
d = pickle.load(open(infile,'rb'),encoding='latin1')
d_sk = pickle.load(open(infile_sk,'rb'),encoding='latin1')

outpath = inpath
rnti = np.array([[np.nan for i2 in range(41)] for i1 in range(24)])
dpdt = np.array([[np.nan for i2 in range(41)] for i1 in range(24)])
rnti_sk = np.array([[np.nan for i2 in range(41)] for i1 in range(24)])
dpdt_sk = np.array([[np.nan for i2 in range(41)] for i1 in range(24)])
detmap = np.array([[0 for i2 in range(41)] for i1 in range(24)])
detmap_sk = np.array([[0 for i2 in range(41)] for i1 in range(24)])
darkcolrow = [(13,0), (14,0), (1,0), (2,0), (11,2), (11,1), (5,0), (6,0)]

for col in range(16):
    for row in range(41):
        try:
            rnti[col, row] = d['rnti'][col+(im*16)][row]
            # subtraction in line below subtracts the mean dark value from the data 
            dpdt[col, row] = d['dpdt'][col+(im*16)][row] - 0.02 # correction for direct stimulation
            if (col,row) in darkcolrow:
                detmap[col,row] = -1
        except:
            continue

for col in range(16):
    for row in range(41):
        try:
            rnti_sk[col, row] = d_sk['rnti'][col+(im_sk*16)][row]
            # subtraction in line below subtracts the mean dark value from the data 
            dpdt_sk[col, row] = d_sk['dpdt'][col+(im_sk*16)][row] - 0.02 # correction for direct stimulation
            if (col,row) in darkcolrow:
                detmap_sk[col,row] = -1
        except:
            continue

np.roll(rnti_sk,1,axis=1)
np.roll(dpdt_sk,1,axis=1)

plt.scatter(dpdt_sk.flatten(), dpdt.flatten(), color='red', marker='x')
plt.axline((0, 0), slope=1, linestyle='--', color='k')
plt.xlabel('SK [pW/K]')
plt.ylabel('BA4 [pW/K]')
plt.title('dP/dT')
plt.xlim(0,0.5)
plt.ylim(0,0.5)
plt.show()

plt.scatter(rnti_sk.flatten(), rnti.flatten(), color='red', marker='x')
plt.axline((0, 0), slope=1, linestyle='--', color='k')
plt.xlabel('SK [mOhm]')
plt.ylabel('BA4 [mOhm]')
plt.title('$R_n$(Ti)')
plt.xlim(0,150)
plt.ylim(0,150)
plt.show()

