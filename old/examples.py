#!/usr/bin/env python

import nodemaster

def main():

    computers = [
    "gks-167.scc.kit.edu",
    "gks-168.scc.kit.edu",
    "gks-169.scc.kit.edu",
    "gks-170.scc.kit.edu",
    "gks-171.scc.kit.edu",
    "gks-173.scc.kit.edu",
    "gks-174.scc.kit.edu",
    "gks-175.scc.kit.edu",
    "gks-176.scc.kit.edu",
    "gks-177.scc.kit.edu",
    "gks-178.scc.kit.edu",
    "gks-179.scc.kit.edu",
    "gks-180.scc.kit.edu",
    "gks-185.scc.kit.edu",
    "gks-186.scc.kit.edu",
    "gks-187.scc.kit.edu",
    "gks-188.scc.kit.edu",
    "gks-189.scc.kit.edu",
    "gks-190.scc.kit.edu",
    "gks-191.scc.kit.edu",
    "gks-192.scc.kit.edu",
    "gks-193.scc.kit.edu",
    "gks-194.scc.kit.edu",
    "gks-195.scc.kit.edu"
    ]

    nodemaster.checkServersForSSHAccess(
        userName = "mtuser",
        computers = computers
    )

if __name__ == '__main__':
    main()
