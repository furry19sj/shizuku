import subprocess
import time
import os

package_name = 'moe.shizuku.privileged.api'
apk_file = 'shizuku.apk'

def is_package_installed(package_name):
    result = subprocess.run(['adb', 'shell', 'pm', 'list', 'packages'], stdout=subprocess.PIPE, text=True)
    return package_name in result.stdout

def install_apk():
    subprocess.run(['adb', 'install', apk_file])

def launch_app(package_name):
    subprocess.run(['adb', 'shell', 'am', 'start', '-n', f'{package_name}/moe.shizuku.manager.MainActivity'])
    
if is_package_installed(package_name):
    cmd1 = 'adb tcpip 5555'
    subprocess.run(['cmd', '/c', cmd1])
    time.sleep(2)
    cmd2 = 'adb shell sh /storage/emulated/0/Android/data/moe.shizuku.privileged.api/start.sh'
    subprocess.run(['cmd', '/c', cmd2])
    
else:
    install_apk()
    launch_app(package_name)
    cmd1 = 'adb tcpip 5555'
    subprocess.run(['cmd', '/c', cmd1])
    time.sleep(2)
    cmd2 = 'adb shell sh /storage/emulated/0/Android/data/moe.shizuku.privileged.api/start.sh'
    subprocess.run(['cmd', '/c', cmd2])
    time.sleep(1)
