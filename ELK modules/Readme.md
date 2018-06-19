# Introduction
This project is for fast checking whether ELK installation is complete and start the service. 
Moreover, it can also help you to apply your ELK modules. 

# Quick start
Step1. put this ELK-project folder under your server. 
Step2. operate `__init__.py` which is under this folder.  
Step3. Answer all of the questions. (More detailed introduction will be put below ) 
Step4. Finish.  

# Functions of this project
* Check the service status  
* Check the jvm 
* Check the firewall  
* Check the module  

# Check the service status
The default services should be started after ELK was installed are `Elasticsearch.service` and the `Kibana.service`. We will help you to start those two service by systemctl. 
If you need to check more services, such as Logstash.service, you could edit the `./__init__.py` and modify the parameter `service_list` directly or operate the check_service.py, which is in `./program/check_service.py` by this command `python check_service.py`

# Check the jvm


# Check the firewall 


# Check the module
