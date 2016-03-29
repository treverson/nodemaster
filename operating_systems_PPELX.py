#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# operating_systems_PPELX                                                      #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program collates LXPLUS users.                                          #
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
version = "2016-03-29T1523Z"

import os

import nodemaster

def main():

    print("\nPPELX operating systems\n")
    print("find working nodes\n")
    working_nodes = nodemaster.working_nodes_PPELX(number = 8)
    commands = []
    for node in working_nodes:
        command = "ssh -o StrictHostKeyChecking=no {node} \"echo \$HOSTNAME; uname --all\"".format(
            node = node
        )
        commands.append(command)
    print("\nget operating systems on working nodes")
    for command in commands:
        print("")
        os.system(command)

if __name__ == "__main__":
    main()
