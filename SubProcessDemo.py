import os
import subprocess

import codecs

# class Adb(object):
#     @staticmethod
#     def adb_devices():
#         cmd = "adb devices"
#         c_line = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()[0]
#         if c_line.find("List of devices attached") < 0: # adb is not working
#             return None
#         return c_line.split("\t")[0].split("\r\n")[-1] # This line may have different format
#     @staticmethod
#     def pull_sd_dcim(device, target_dir='E:/files'):
#         """ Pull DCIM files from device """
#         print ("Pulling files")
#         des_path = os.path.join(target_dir, device)
#         if not os.path.exists(des_path):
#             os.makedirs(des_path)
#         print(des_path)
#         cmd = "adb pull /sdcard/DCIM/ " + des_path
#         result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
#         print(result)
#         print("Finish!")
#         return des_path
#     @staticmethod
#     def some_adb_cmd():
#         p = subprocess.Popen('adb shell cd sdcard&&ls&&cd ../sys&&ls',stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#         return_code = p.poll()
#         while return_code is None:
#             line = p.stdout.readline()
#             return_code = p.poll()
#             line = line.strip()
#             if line:
#                 print(line)
#         print("Done")

# 使用popen
def execmd(cmd):
    f = os.popen(cmd)
    text = f.read()
    f.close()
    return text

if __name__=='__main__':
    cmd = input("请输入：")
    execmd(cmd)
    print(execmd(cmd))

# 使用subprocess
input('press Enter to continue...')
app_package=subprocess.Popen('adb shell cd sdcard&&cd Android&&cd data&&ls', stdout=subprocess.PIPE, stderr=subprocess.PIPE)#自动执行adb shell以后的命令,获取app的package
print (app_package.stdout.read())
input("press Enter to continue...")


monkey=subprocess.Popen('adb shell monkey -s 200 -p prancent.project.rentalhouse.app --ignore-timeouts --ignore-crashes -v 400000 --throttle 500>/sdcard/monkey_log.txt',stdout=subprocess.PIPE, stderr=subprocess.PIPE)#运行monkey命令
print (monkey.stdout.read())

