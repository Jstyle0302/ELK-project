import os
import super_stdio as super

def check_jvm_memory():
    #The bytes mapping table
    bytes_mapping = {"t":1024**3,"g":1024**2,"m":1024**1,"k":1024**0}
    gbytes_mapping = {"t":1024**-1,"g":1024**0,"m":1024**1,"k":1024**2}

    #Search the jvm size
    str1 = os.popen("cat /etc/elasticsearch/jvm.options|grep Xms|grep -v '#'").read()
    size = str1[4:len(str1)-1]
    jvm_size_kbytes = int(''.join(map(str,size[:-1])))*bytes_mapping[size[-1].lower()]

    #Search the Memory size
    str2 = os.popen("cat /proc/meminfo |grep MemTotal").read()
    size2 = [word for word in str2 if word.isdigit() == True]
    free_size_kbytes = int(''.join(map(str,size2))) * bytes_mapping[str2[-3].lower()]
    free_size_gbytes = float(free_size_kbytes) / gbytes_mapping[str2[-3].lower()]

    #Show the jvm and memory size
    super.super_print("JVM size is " + str1[4:-1])
    super.super_print("Memory size is %3.2fg(%d %s)" % (free_size_gbytes,free_size_kbytes,str2[-3:-1]))

    # If the jvm size is not enough, super.super_print the warning message
    warning_message = ""
    official_recommand_size = 64
    if (jvm_size_kbytes < free_size_kbytes/2) or (jvm_size_kbytes < official_recommand_size * bytes_mapping["g"]):
        warning_message+= "\033[1;31;40mWarning:Your jvm size is not enough!"
        if (jvm_size_kbytes < free_size_kbytes/2):
            warning_message+= "\nPlease go to /etc/elasticsearch/jvm.options and set space more than %d kB." % (free_size_kbytes/2)
        if (jvm_size_kbytes < official_recommand_size * bytes_mapping["g"]):
            warning_message+= "\nThe official recommand size is %dg. We highly recommand you to enlarge your jvm space." % (official_recommand_size)
        warning_message += "\033[0;37;40m"
        super.super_print(warning_message)


if __name__ == "__main__":
    check_jvm_memory();
