Introduction
============
This project is for fast checking whether ELK installation is complete and start the service. 
Moreover, it can also help you to apply your ELK modules quickly and you can realize the power of ELK without any experience on ELK.  


Environment
-----------
- Operating System: Centos 7.4
- Python version: 2.7
- Elasticsearch and Kibana version: 6.0.0
- Logstash version: 6.0.0
- Monitored environment: CentOS 7.4, Windows Server 2008


Quick start
-----------
Step1. put this ELK-project folder under your server.    
Step2. operate `__init__.py` which is under this folder.   
Step3. Answer all of the questions. (More detailed introductions will be put below )   
Step4. Congratulation!! It is all done!     


Functions of this project
-------------------------
* Check the service status  
* Check the jvm 
* Check the firewall  
* Check the module  


Check the service status
------------------------
The default services should be started after ELK was installed are `Elasticsearch.service` and the `Kibana.service`. We will help you to start those two service by systemctl.  

If you need to check more services, such as Logstash.service, you could edit the [__init__.py](./__init__.py) and modify the parameter [service_list](./program/check_service.py) directly or operate the check_service.py, which is in `./program/check_service.py`. The command for python2.7 would be: `python check_service.py`


Check the jvm
-------------
The official recommanded jvm( java virtual machine) size is 64g. If your jvm is not enough, we will pop out a message to notify you to resize the jvm size. Or, at least, we highly recommand you to set the jvm size more than the free size, so that we can make sure your elasticsearch service will run well.  

If you only want to check the jvm size, you can operate the [check_jvm.py](./program/check_service.py) directly, which is in `./program/check_service.py`. The command for python2.7 would be: `python check_service.py`  


Check the firewall
------------------
This will ask you the firewall ports' number you want to check. After typing the number, the program will tell you the conditions of the tcp and udp protocal of your port numbers.  
_*Note: Please remember that this program will only tell you the conditions of your port number and will not help you to start or stop them. Those demands should be realized and executed by yourselves since we think it is the network security problem and is better to do by you instead of us.*_

If you only want to check the jvm size, you can operate the [check_firewall.py](./program/check_firewall.py) directly, which is in `./program/check_firewall.py`. The command for python2.7 would be: `python check_firewall.py`

Check the module
----------------
ELK modularization has a strong function that it can transfer its configuration of elasticsearch, logstash and kibana from one server to another server quickly and set up all properties automatically. The official Elatic provides us the basic modules, Netflow and fb_apache, which is under the `logstash/modules/` folder and you can easily find them and operate them by this command: `logstash/bin/logstash --modules YourModuleName`. 

In this part, this program will ask you which module in the [modules_list.py](./modules_list.py) you want to set up and move them to the `logstash/modules/` folder so that the logstash can operate it . (You can edit the `modules_list.py` and add new modules into it if you create a new modules down the road. But, please remember to put your new modules into the `modules` folder.) Moreover, it will also write some commands in the `rc.local` file so that your modules will be restarted automatically after each time you reboot your system. This can help you to reduce the worries of the modules condition and do not need to think that question: *Is my modules still alive?*

Again, you can also run this function independently by [operate_module.py](./program/operate_module.py). The command for python2.7 would be: `python operate_module.py`


Note
----
All of my print function in python have already been replaced by my new super_print function. It is because of that this new function can help the users to record the process and all setting they did while they were running this program. They can check all of the setting they did by the `output.txt` after many days or even know the previous users' setting readily. Thus, no matter which function you operate, the `__init__.py` or each small functions directly, please remember to include the [super_stdio](./program/super_stdio.py) which is in `./program/super_stdio.py`    
If you find the output.txt is a little confusing when you use the `vim` command to read it, it is normal and is because of that the `vim` editing tool cannot realize the special word decorator. You can use the `cat output.txt` to review it and it will be more comfortable to read.
