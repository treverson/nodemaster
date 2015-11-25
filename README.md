# nodemaster

# introduction

This module provides various utilities that can be used for the control and diagnostics of a set of computing nodes. It could be used to check if a set of computers are accessible via SSH or could run a command on a set of computers accessible via SSH, for examples.

# launch commands in tmux

Commands can be sent to respective panes of tmux. The following example defines multiple commands, launches tmux, creates multiple panes in tmux and then runs each command in its respective tmux pane.

```Bash
import nodemaster
commands = [
    "ls",
    "ls",
    "ls",
    "ls"
}
nodemaster.launch_tmux(commands = commands)
```

The following example, for use on LXPLUS, illustrates how nodemaster can be used to send multiple commands out to multiple nodes and to observe the output in tmux.

```Bash
import nodemaster
commands = [
    "ssh -o StrictHostKeyChecking=no lxplus0000.cern.ch uptime",
    "ssh -o StrictHostKeyChecking=no lxplus0001.cern.ch uptime",
    "ssh -o StrictHostKeyChecking=no lxplus0002.cern.ch uptime",
    "ssh -o StrictHostKeyChecking=no lxplus0003.cern.ch uptime"
}
nodemaster.launch_tmux(commands = commands)
```
