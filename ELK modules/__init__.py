from __future__ import print_function
# This must be the first statement before other statements.
# You may only put a quoted or triple quoted string,
# Python comments, other future statements, or blank lines before the __future__ line.

try:
    import __builtin__
except ImportError:
    # Python 3
    import __builtins__ as __builtin__

import sys
sys.path.append('program/')
import super_std as sstd
print = sstd.super_print('output.txt')(__builtin__.print)
raw_input = sstd.super_raw_input('output.txt')(__builtin__.raw_input)




import check_jvm as cj
import check_service as cs
import check_firewall as cf
import operate_module as om
import modules_list as ml

def main():
    service_list = ["kibana","elasticsearch"]
    modules_list = ml.modules_list
    modules_missing = []
    modules = []
    modules_path = "modules/"
    print("\n1) Check the service status")
    for service in service_list:
        
        cs.check_service(service)
    
    print("\n2) Check the jvm")
    cj.check_jvm_memory()
    
    print("\n3) Check the firewall")
    cf.check_firewall_port()
   
    print("\n4) Check the module")
    while True:
        modules = om.modules_generate(modules_list)
        print("The modules you choose is : \033[1;33;40m%s\033[0;37;40m" % (" ".join(modules)))
        for module in modules:
            module_setting = om.check_module(module = module,modules_path = modules_path)
            if module_setting == False:
                modules_missing.append(module)
        om.modules_info(modules = modules, not_exist_module_list = modules_missing)
        add_more = raw_input("Do you want to add more modules?If 'yes', please enter 'y' or 'yes': ")
        if (add_more != "y") and (add_more != "yes"):
            break

if __name__ == "__main__":
#    print = log.super_print('output.txt')(__builtin__.print)
    main()
