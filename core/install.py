#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Standard library modules
import subprocess
import os
from typing import NoReturn, Dict


class Install:
    def __init__(self, username: str, distribution: str) -> NoReturn:
        """
        This will install the Tor and Iptables for in system

        Parameters:
            username (str)     : Device's username (e.g. kali)
            distribution (str) : Device's distribution (e.g. debian)

        Returns:
            None (typing.NoReturn)
        """
        # Set username & Distribution for system
        self.username: str = username
        self.distribution: str = distribution

        # Initialize Tor service stop command
        self.stop_tor: str = "systemctl stop tor"

        # Initialize install jobs mapping
        # This will install 'tor' and 'iptables' for following distributions
        self.install_commands: Dict[str, str] = {
            "debian": "apt-get install -y tor iptables",
            "fedora": "dnf install -y tor iptables",
            "centos": "yum -y install epel-release tor iptables",
            "void": "xbps-install -y tor iptables",
            "arch": "pacman -S --noconfirm tor iptables"
        }
        
        # Update TOR service stop command if distro is Void
        if self.distribution == "void":
            self.stop_tor = "sv stop tor > /dev/null"

        # Update Tor service stop command if there is TOR init file in system
        if os.path.exists("/etc/init.d/tor"):
            self.stop_tor = "/etc/init.d/tor stop > /dev/null"


    def execute_installation(self) -> NoReturn:
        """
        This will execute installation process fro installing TOR
        and Iptables and also stop TOR service

        Parameters:
            None

        Returns:
            None
        """
        if (install_command:=self.install_commands.get(self.distribution, "")):
            subprocess.run(f"{install_command} && {self.stop_tor}", shell=True)
