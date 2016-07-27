# simple script to test out job array submission and file structure

# use a bash script to create the file structure, unique configuration files
# for each job, and copy all resources into the correct directories
import os
from configure import *


#if __name__=='_main___': ## Name does not equal main for job array submission!
if True:
    
    #job = os.environ['JOB_ID'];
    #task = os.environ['SGE_TASK_ID']; 
    id = os.environ['PBS_JOBID'];
    id = id[0:7]
    job = os.environ['PBS_ARRAYID'];
    print('Job ID = ' + id)
    print('Array ID = ' + job)
    
    output_dir = './' + id + '_' + job;
    #output_dir = './' + job;

    if not os.path.exists(output_dir):
    	os.makedirs(output_dir)
    os.chdir(output_dir)

    #if (os.path.isfile('./output/'+SRC_NET_FILE)):
    #    shutil.copy('./output/'+SRC_NET_FILE, output_dir)
    
    f = open('output.txt', 'w')
    f.write('HABITAT_LOSS = %d\n' %HABITAT_LOSS)
    f.write('MUTUALISM = %f\n' %MUTUALISM)
    f.write('JOBID = '+id+'\n')
    f.write('ARRAYID = '+job+'\n')
    f.close()
    

    os.chdir('..')


