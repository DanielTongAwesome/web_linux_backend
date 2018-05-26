'''
Date: May 26, 2018
Author: Daniel Tong, LF112
'''

import os

class executeCommand(object):
    path, filename = (None, None)
    # initialize param
    def __init__ (self):
        self.excommand = None
        pass
    
    # start to run and execute command
    def start(self):
        #check the command.txt assume the path start from current
        def checkCommandsFile(path, filename):
            des = path + filename
            readFile = open(des,'r')
            self.excommand = readFile.read()
            #print (self.excommand)
            return (self.excommand)

        def excute(command):
            os.system(command + ' > CmdResult.txt')
            #print (open('CmdResult.txt', 'r').read())
            result = open('CmdResult.txt', 'r').read()
        

        def emptyFile(path,filename):
            des = path + filename
            open(des, "w").close()



        while True:
            # empty CmdResult.txt --- clean result file
            emptyFile('./','CmdResult.txt')
            # read command
            excommand = checkCommandsFile('./','CmdRun.txt')
            # excute command
            excute(excommand)
            # clean CmdRun.txt --- clean input command file
            emptyFile('./', 'CmdRun.txt')
            break

if __name__ == '__main__':
    try:
        ex = executeCommand()
        ex.start()
    
    except Exception as ex:
        print(ex)

        