from __future__ import print_function
# This must be the first statement before other statements.
# You may only put a quoted or triple quoted string,
# Python comments, other future statements, or blank lines before the __future__ line.

try:
    import __builtin__
except ImportError:
    # Python 3
    import __builtins__ as __builtin__
import super_std as sstd
print = sstd.super_print('output.txt')(__builtin__.print)
raw_input = sstd.super_raw_input('output.txt')(__builtin__.raw_input)





import os 
import sys

file_name = "/etc/rc.local"
modules_path = "../modules/"
def check_module_in_dir(module,modules_path):
    fname = "/usr/share/logstash/modules/%s" % module
    file_exist = os.path.exists(fname)
    if file_exist:
        print("\nHave already had a\033[1;33;40m %s\033[0;37;40m directory under the modules folder." % (module))
        return "Finish"
    else:
        print("\nThere is no\033[1;33;40m %s\033[0;37;40m directory under the modules folder." % (module))
        module_path = modules_path + module
        file_exist = os.path.exists(module_path)
        if file_exist:
            command = "cp -r %s /usr/share/logstash/modules/" % module_path
            os.popen(command)
            print("However,We have already helped you to move\033[1;33;40m %s\033[0;37;40m to the modules folder!" % (module))
            return "NeedSetting"
        else:
            return "Missing"

def check_command_line(module):
    command = "cat %s|grep %s" % (file_name,module)
    lines = os.popen(command).readlines()
    if len(lines) < 1:
        return False
    else:
        return True

def command_generate(input_port, elasticsearch_hosts, kibana_host, module):
    command = 'nohup /usr/share/logstash/bin/logstash --modules %s --setup ' % module
    command+= '-M "%s.var.input.port=%s" ' % (module, input_port)
    command+= '-M "%s.var.elasticsearch.hosts=%s" ' % (module,elasticsearch_hosts)
    command+= '-M "%s.var.elasticsearch.index=%s-%%{+YYYY.MM.dd}" ' % (module,module)
    command+= '-M "%s.var.kibana.host=%s" --path.data /tmp/%s ' % (module, kibana_host, module)
    command+= '> /var/log/logstash/module/%s.log ' % module
    command+= '2>&1 &\n'
    return command

def check_module(module,modules_path):
    is_in_dir = check_module_in_dir(module,modules_path);
    if is_in_dir == "Finish":
        is_in_rc = check_command_line(module)
        if is_in_rc == True:
            return True
    elif is_in_dir == "Missing":
        return False
    
    port = raw_input("Please enter the input port number: ")
    es_hosts = raw_input("Please enter the elasticsearch hosts: ")
    ki_host = raw_input("Please enter the kibana host: ")
    command = command_generate(input_port=port, elasticsearch_hosts=es_hosts, kibana_host=ki_host, module=module)
    with open(file_name,'at') as file:
        file.write(command)
        print("We have already helped you to set module\033[1;33;40m %s\033[0;37;40m automatically start when the server is rebooting." % (module))
    return True

def modules_info(modules,not_exist_module_list):
    success_modules = set(modules)
    
    if len(not_exist_module_list) == 0:
        print("\nAll of the modules will automatically start when the server is rebooting.")
    else:
        lose_modules = " ".join(not_exist_module_list)
        print("\nSorry, we cannot find those modules in %s:\033[1;33;40m %s\033[0;37;40m" % (file_name, lose_modules))
            
    success_modules = success_modules.symmetric_difference(set(not_exist_module_list))
    if (len(success_modules) > 0):
        dir = "/var/log/logstash/module"
        is_dir = os.path.isdir(dir)
        if(is_dir == False):
            os.popen("mkdir -p %s" % (dir))
        command = "%s" % file_name
        os.popen(command)
        print("We have alreay helped you start all of the modules:\033[1;33;40m %s\033[0;37;40m" % (" ".join(success_modules)))
    else:
        print("We did not start any modules since there is no modules been set newly at the rc.local")

def modules_generate(modules_list):
    modules = []
    for num, module in enumerate(modules_list):
        option = "Module%d: %s" % (num+1, module)
        print(option)
    response = raw_input("Please enter the number of modules you want to process and use space to split your options(eg.:1 2 4): ")
    response = response.split()
    for resp in response:
        if (resp.isdigit() == True):
            opt = int(resp)-1
            if(0 <= opt < len(modules_list)):
                modules.append(modules_list[opt])
            else:
                print("'%d' is out of the range of module list" % (opt+1))
        else:
            print("'%s' is not an illegal input format." % (resp))
    return modules
    


if __name__ == "__main__":
    modules_list = ["rsystem","winsystem"]
    missing_list = []
    modules_path = "../modules/"
    modules = modules_generate(modules_list)
    print("The modules you choose is : \033[1;33;40m%s\033[0;37;40m" % (" ".join(modules)))
    for module in modules:
        module_setting = check_module(module,modules_path)
        if module_setting == False:
            missing_list.append(module)
    modules_info(modules = modules, not_exist_module_list = missing_list)

