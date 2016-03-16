#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# users_LXPLUS                                                                 #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program collates LXPLUS users.                           #
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
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for     #
# more details.                                                                #
#                                                                              #
# For a copy of the GNU General Public License, see                            #
# <http://www.gnu.org/licenses/>.                                              #
#                                                                              #
################################################################################
"""

name    = "users_LXPLUS"
version = "2016-03-16T1333Z"

import os

import nodemaster

def main():

    commands = []
    for node_index in [str(index).zfill(4) for index in range(1, 200)]:
        command = "ssh -o StrictHostKeyChecking=no lxplus{index}.cern.ch \"echo \$HOSTNAME; users\"".format(
            index = node_index
        )
        commands.append(command)
    for command in commands:
        os.system(command)

if __name__ == "__main__":
    main()
