## This scripts run a full simulation set for a single parameter value
## First it has to create a configuration file for this run, 

import sys, os, glob
import shutil
import numpy as np

p_id = int(sys.argv[1])

if not os.path.exists('p_run%d' %p_id):
	os.makedirs('p_run%d' %p_id)


params = np.genfromtxt("latin_params.csv", delimiter=',', skip_header=2)
names = np.genfromtxt("latin_params.csv", delimiter=',', dtype='string')
names = names[0,:]
Params = dict(zip(names,params[p_id,:]))

shutil.copy('../src_master/sensitivity_analysis/configure_skeleton.py', 'p_run%d/configure.py' %p_id)

with open('p_run%d/configure.py' %p_id, 'a') as fi:
        fi.write('MUTUALISM = 0.5 \n')
        for k in Params.keys():
                fi.write(k + " = " + str(Params[k]) + '\n')

for file in glob.glob(r'../src_master/sensitivity_analysis/*.py'):
    #print file                                                                                                                                        
    shutil.copy(file, 'p_run%d' %p_id)
#shutil.copy('../src_master/sensitivity_analysis/*.py', 'p_run%d' %p_id)
os.chdir('p_run%d' %p_id)

os.system('nohup python main.py %d >> log.out &' %p_id)
