import sys
import modules_list as ml

# Set the system path to get our code modules
sys.path.append('program/')
import check_jvm as cj
import check_service as cs
import check_firewall as cf
import operate_module as om
import super_stdio as super

def main():
    service_list = ["kibana","elasticsearch"] # Service you want to check
    modules_list = ml.modules_list # Modules you have
    modules_missing = []     # Use this list to save those missing modules
    modules = []             # Use this list to save those modules you want to process
    modules_path = "modules/"
 
    # Check whether your service is up; if not, help the user to open the service
    super.super_print("\n1) Check the service status")
    for service in service_list:
        
        cs.check_service(service)
    
    # Check whether the jvm size is enough; if not, send the warning message
    super.super_print("\n2) Check the jvm")
    cj.check_jvm_memory()
    
    # Check whether the firewall port number is open.
    super.super_print("\n3) Check the firewall")
    cf.check_firewall_port()
   
    # Check which module the user want to install, then help them to start up modules.
    super.super_print("\n4) Check the module")
    while True:
        modules = om.modules_generate(modules_list)
        super.super_print("The modules you choose is : \033[1;33;40m%s\033[0;37;40m" % (" ".join(modules)))
        for module in modules:
            module_setting = om.check_module(module = module,modules_path = modules_path)
            if module_setting == False:
                modules_missing.append(module)
        om.modules_info(modules = modules, not_exist_module_list = modules_missing)
        add_more = super.super_raw_input("Do you want to add more modules?If 'yes', please enter 'y' or 'yes': ")
        if (add_more != "y") and (add_more != "yes"):
            break

if __name__ == "__main__":
    main()
