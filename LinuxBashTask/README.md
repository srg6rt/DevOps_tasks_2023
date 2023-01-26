## Linux administration with bash. Home task

### A. Create a script that uses the following keys:

 A. Create a script that uses the following keys:
 1. When starting without parameters, it will display a list of possible keys and their description. 
 2. The --all key displays the IP addresses and symbolic names of all hosts in the current subnet 
 3. The --target key displays a list of open system TCP ports.The code that performs the functionality of each of the subtasks must be placed in a separate function

<img src="./docs/images/bash_code.png" />

<img src="./docs/images/my_script.png" />

B. Using Apache log example create a script to answer the following questions:

1. From which ip were the most requests? 
2. What is the most requested page? 
3. How many requests were there from each ip? 
4. What non-existent pages were clients referred to?  
5. What time did site get the most requests? 
6. What search bots have accessed the site? (UA + IP)

<img src="./docs/images/script.png" />

<img src="./docs/images/example_1.png" />

<img src="./docs/images/example_2.png" />

<img src="./docs/images/example_3.png" />

C. Create a data backup script that takes the following data as parameters:
1. Path to the syncing  directory.
2. The path to the directory where the copies of the files will be stored.

In case of adding new or deleting old files, the script must add a corresponding entry to the log file indicating the time, type of operation and file name. 
[The command to run the script must be added to crontab with a run frequency of one minute]

<em>Bash script synco.sh</em>

<img src="./docs/images/synco_script.png" />

<em>Copy, delete files in fotos directory, synchronously copy, deleting in a backup_fotos directory</em>

<img src="./docs/images/rsync_copy_del.png" />

<em>Log file with corresponding entry</em>

<img src="./docs/images/rsync_my_log.png" />

<em>Run synco.sh script in crontab with a run frequency of one minute</em>

<img src="./docs/images/cron.png" />