
import os
import subprocess
import codecs

#使用popen
def execmd(cmd):
    f=os.popen(cmd)
    text=f.read()
    f.close()
    return text

if __name__=='__main__':
    cmd="ipconfig/all"
    execmd(cmd)
    print (execmd(cmd))

#使用subprocess
input('press Enter to continue...')
app_package=subprocess.Popen('adb shell cd sdcard&&cd Android&&cd data&&ls', stdout=subprocess.PIPE, stderr=subprocess.PIPE)#自动执行adb shell以后的命令,获取app的package
print (app_package.stdout.read())
input("press Enter to continue...")

monkey=subprocess.Popen('adb shell monkey -s 200 -p prancent.project.rentalhouse.app --ignore-timeouts --ignore-crashes -v 400000 --throttle 500>/sdcard/monkey_log.txt',stdout=subprocess.PIPE, stderr=subprocess.PIPE)#运行monkey命令
print (monkey.stdout.read())

#类方法
import subprocess

class monkey(object):
    def __init__(self,appname,s,count,t,filename):
        self.pack=appname
        self.seed=s
        self.count=count
        self.time=t
        self.storage=filename

    def test(self):
        test_monkey=subprocess.Popen('adb shell monkey '+self.pack+' '+'-s '+self.seed+' --ignore-timeouts --ignore-crashes -v '+self.count+' '+self.time+' '+self.storage,stdout=subprocess.PIPE,stdin=subprocess.PIPE)
        return test_monkey.stdout.read()
        # return test_monkey

if __name__=="__main__":
    run=monkey('-p cn.rainbow.westore','200','300','--throttle 500','>/sdcard/monkey_log.txt')
    run.test()