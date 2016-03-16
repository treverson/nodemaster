#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# nodemaster                                                                   #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program provides node control utilities.                                #
#                                                                              #
# 2014 Will Breaden Madden, w.bm@cern.ch                                       #
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

name    = "nodemaster"
version = "2016-03-16T1338Z"

import os
import subprocess

def launch_tmux(
    commands = None
    ):
    configuration =\
    """
    set -g set-remain-on-exit on
    new -s "nodemaster"
    set-option -g prefix C-a
    unbind C-b
    bind - split-window -v
    bind | split-window -h
    ## colours
    set-option -g window-status-current-bg yellow
    set-option -g pane-active-border-fg yellow
    set -g status-fg black
    set -g status-bg '#FEFE0A'
    set -g message-fg black
    set -g message-bg '#FEFE0A'
    set -g message-command-fg black
    set -g message-command-bg '#FEFE0A'
    set-option -g mode-keys vi
    set -g history-limit 5000
    ## mouse mode
    set -g mode-mouse on
    set -g mouse-select-pane on
    set -g mouse-select-window on
    set -g mouse-resize-pane on # resize panes with mouse (drag borders)
    ## status
    set-option -g status-interval 1
    set-option -g status-left-length 20
    set-option -g status-left ''
    set-option -g status-right '%Y-%m-%dT%H%M%S '
    """
    for command in range(1, len(commands)):
        configuration += "\nsplit-window -v\nselect-layout even-vertical"
    for index, command in enumerate(commands):
        configuration += "\nselect-pane -t {index}".format(
            index = index
        )
        configuration += "\nsend-keys '{command}' Enter".format(
            command = command
        )
    configuration += "\nset -g set-remain-on-exit off"
    command = \
        "configurationtmux=\"$(mktemp)\" && { echo \"" +\
        configuration                                  +\
        "\" > \"${configurationtmux}\"; "              +\
        "tmux"                                         +\
        " -f \"${configurationtmux}\" attach; "        +\
        "unlink \"${configurationtmux}\"; }"
    os.system(command)

def working_nodes_LXPLUS(
    number = None
    ):
    nodes = [
        #"lxplus0000.cern.ch",
        "lxplus0001.cern.ch",
        #"lxplus0002.cern.ch",
        #"lxplus0003.cern.ch",
        "lxplus0004.cern.ch",
        #"lxplus0005.cern.ch",
        #"lxplus0006.cern.ch",
        #"lxplus0007.cern.ch",
        "lxplus0008.cern.ch",
        "lxplus0009.cern.ch",
        "lxplus0010.cern.ch",
        "lxplus0011.cern.ch",
        "lxplus0012.cern.ch",
        "lxplus0013.cern.ch",
        "lxplus0014.cern.ch",
        "lxplus0015.cern.ch",
        "lxplus0016.cern.ch",
        "lxplus0017.cern.ch",
        "lxplus0018.cern.ch",
        "lxplus0019.cern.ch",
        "lxplus0020.cern.ch",
        "lxplus0021.cern.ch",
        "lxplus0022.cern.ch",
        "lxplus0023.cern.ch",
        "lxplus0024.cern.ch",
        "lxplus0025.cern.ch",
        "lxplus0026.cern.ch",
        "lxplus0027.cern.ch",
        "lxplus0028.cern.ch",
        "lxplus0029.cern.ch",
        "lxplus0030.cern.ch",
        "lxplus0031.cern.ch",
        "lxplus0032.cern.ch",
        "lxplus0033.cern.ch",
        "lxplus0034.cern.ch",
        "lxplus0035.cern.ch",
        "lxplus0036.cern.ch",
        "lxplus0037.cern.ch",
        "lxplus0038.cern.ch",
        "lxplus0039.cern.ch",
        "lxplus0040.cern.ch",
        "lxplus0041.cern.ch",
        "lxplus0042.cern.ch",
        "lxplus0043.cern.ch",
        "lxplus0044.cern.ch",
        "lxplus0045.cern.ch",
        "lxplus0046.cern.ch",
        "lxplus0047.cern.ch",
        "lxplus0048.cern.ch",
        "lxplus0049.cern.ch",
        "lxplus0050.cern.ch",
        "lxplus0051.cern.ch",
        "lxplus0052.cern.ch",
        "lxplus0053.cern.ch",
        "lxplus0054.cern.ch",
        "lxplus0055.cern.ch",
        "lxplus0056.cern.ch",
        "lxplus0057.cern.ch",
        "lxplus0058.cern.ch",
        "lxplus0059.cern.ch",
        "lxplus0060.cern.ch",
        "lxplus0061.cern.ch",
        "lxplus0062.cern.ch",
        "lxplus0063.cern.ch",
        "lxplus0064.cern.ch",
        "lxplus0065.cern.ch",
        "lxplus0066.cern.ch",
        "lxplus0067.cern.ch",
        "lxplus0068.cern.ch",
        "lxplus0069.cern.ch",
        "lxplus0070.cern.ch",
        "lxplus0072.cern.ch",
        "lxplus0073.cern.ch",
        "lxplus0074.cern.ch",
        "lxplus0075.cern.ch",
        "lxplus0076.cern.ch",
        "lxplus0077.cern.ch",
        "lxplus0078.cern.ch",
        "lxplus0079.cern.ch",
        "lxplus0080.cern.ch",
        "lxplus0081.cern.ch",
        "lxplus0082.cern.ch",
        "lxplus0083.cern.ch",
        "lxplus0084.cern.ch",
        "lxplus0085.cern.ch",
        "lxplus0086.cern.ch",
        "lxplus0087.cern.ch",
        "lxplus0088.cern.ch",
        "lxplus0089.cern.ch",
        "lxplus0090.cern.ch",
        "lxplus0091.cern.ch",
        "lxplus0092.cern.ch",
        "lxplus0093.cern.ch",
        "lxplus0094.cern.ch",
        "lxplus0095.cern.ch",
        "lxplus0096.cern.ch",
        "lxplus0097.cern.ch",
        "lxplus0098.cern.ch",
        "lxplus0099.cern.ch",
        "lxplus0100.cern.ch",
        "lxplus0101.cern.ch",
        "lxplus0102.cern.ch",
        "lxplus0103.cern.ch",
        "lxplus0103.cern.ch",
        "lxplus0104.cern.ch",
        "lxplus0105.cern.ch",
        "lxplus0106.cern.ch",
        "lxplus0107.cern.ch",
        "lxplus0108.cern.ch",
        "lxplus0109.cern.ch",
        "lxplus0110.cern.ch",
        "lxplus0111.cern.ch",
        "lxplus0112.cern.ch",
        "lxplus0113.cern.ch",
        "lxplus0114.cern.ch",
        "lxplus0141.cern.ch",
        "lxplus0148.cern.ch",
        "lxplus0159.cern.ch",
        "lxplus0233.cern.ch"
    ]
    working_nodes = []
    for node in nodes:
        #log.debug("check node {node}".format(node = node))
        return_code = subprocess.call([
            "ssh",
            "-o",
            "StrictHostKeyChecking=no",
            node,
            "uptime"
        ])
        #log.debug("return code: {return_code}".format(
        #    return_code = return_code
        #))
        if return_code == 0:
            working_nodes.append(node)
        if len(working_nodes) == number:
            return working_nodes
    return working_nodes
