import subprocess


if __name__ == '__main__':
    # subprocess.call(['dir', '/a'], shell=True)
    popen = subprocess.Popen(['dir', '/a'], stdout=subprocess.PIPE,  shell=True)
    print popen.communicate()
    # popen1 = subprocess.Popen(['ping localhost'], stdout=subprocess.PIPE,  shell=True)
    # print popen1.stdout

    p1 = subprocess.Popen(['cat', 'subprocess-test.py'], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(['grep', 'main'], stdin=p1.stdout, stdout=subprocess.PIPE)
    p1.stdout.close()
    output = p2.communicate()
    print output