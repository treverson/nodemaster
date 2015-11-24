################################################################################
#                                                                              #
# nodemaster                                                                   #
#                                                                              #
################################################################################
#                                                                              #
# version: 2014-08-28T1736                                                     #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program provides node control utilities.                                #
#                                                                              #
# copyright (C) 2014 William Breaden Madden                                    #
#                                                                              #
# This software is released under the terms of the GNU General Public License  #
# version 3 (GPLv3).                                                           #
#                                                                              #
# This program is free software: you can redistribute it and/or modify it      #
# under the terms of the GNU General Public License as published by the Free   #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# This program is distributed in the hope that it will be useful, but WITHOUT  #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or        #
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for    #
# more details.                                                                #
#                                                                              #
# For a copy of the GNU General Public License, see                            #
# <http://www.gnu.org/licenses/>.                                              #
#                                                                              #
################################################################################

import subprocess

def printLine(character = '-'):
    terminalWidth = int(subprocess.Popen(['tput', 'cols'], stdout = subprocess.PIPE).communicate()[0].strip('\n'))
    line = ""
    for column in range(0, terminalWidth):
        line += character
    print(line)

def checkServersForSSHAccess(
    computers = None,
    userName = None,
    passcode = None
    ):
    if passcode == None:
        passcode = raw_input("enter passcode: ")
    if userName == None:
        userName = raw_input("enter passcode: ")
    problemComputers = []
    printLine()
    for computer in computers:
        print("checking computer {computer}".format(computer = computer))
        returnCode = subprocess.call([
            "sshpass",
            "-p",
            passcode,
            "ssh",
            "-o",
            "StrictHostKeyChecking=no",
            "-p",
            "24",
            userName + "@" + computer,
            "uptime"
        ])
        print("return code: {returnCode}".format(
            returnCode = returnCode
        ))
        if returnCode != 0:
            problemComputers.append(computer)
        printLine()
    if problemComputers:
        print("list of problem computers:\n{problemComputers}".format(
            problemComputers = problemComputers
        ))
    else:
        print("no problem computers found")
