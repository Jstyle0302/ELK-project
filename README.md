Introduction
============
This project is for fast checking whether ELK installation is complete and start the service. 
Moreover, it can also help you to apply your ELK modules. 


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

If you need to check more services, such as Logstash.service, you could edit the `./__init__.py` and modify the parameter `service_list` directly or operate the check_service.py, which is in `./program/check_service.py`. The command for python2.7 would be: `python check_service.py`


Check the jvm
-------------
The official recommanded jvm( java virtual machine) size is 64g. If your jvm is not enough, we will pop out a message to notify you to resize the jvm size. Or, at least, we highly recommand you to set the jvm size more than the free size, so that we can make sure your elasticsearch service will run well.  

If you only want to check the jvm size, you can operate the `check_jvm.py` directly, which is in `./program/check_service.py`. The command for python2.7 would be: `python check_service.py`  


Check the firewall
------------------
This will ask you the firewall ports' number you want to check. After typing the number, the program will tell you the conditions of the tcp and udp protocal of your port numbers.  
_*(Please remember that this program will only tell you the conditions of your port number and will not help you to start or stop them. Those demands should be realized and executed by yourselves since we think it is the network security problem and is better to do by you instead of us.)*_

If you only want to check the jvm size, you can operate the `check_firewall.py` directly, which is in `./program/check_firewall.py`. The command for python2.7 would be: `python check_firewall.py`

Check the module
----------------
