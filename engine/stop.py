#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Standard library modules
import subprocess
import os
from typing import NoReturn, Tuple, Union


class Stop:
    def __init__(self, username: str, distribution: str) -> NoReturn:
        # Set device information
        self.username: str = username
        self.distribution: str = distribution

        # Set table & Network
        self.tables: Tuple[str, str] = ("nat", "filter")

        # Set start TOR service command
        self.stopTor: str = "systemctl stop tor"


    def stop_nipy(self) -> Union[bool, NoReturn]:
        """
        This method will start the tor service and make Tor default gateway

        Parameters:
            None

        Returns:
            On success (bool): True 
            On Failure (None): Error message will be raised 
        """
        try:
            # Update TOR service start command if distro is Void
            if self.distribution == "void":
                self.stopTor = "sv stop tor > /dev/null"

            # Configures iptables rules for the specified tables, network, and ports. 
            for table in self.tables:
                # Execute Iptables commands
                subprocess.run(f"iptables -t {table} -F OUTPUT", shell=True)
                subprocess.run(f"iptables -t {table} -F OUTPUT", shell=True)

            # Update Tor service stop command if there is TOR init file in system
            if os.path.exists("/etc/init.d/tor"):
                self.stopTor = "/etc/init.d/tor stop > /dev/null"

            # Stop tor service
            subprocess.run(f"{self.stopTor}", shell=True)

            return True

        except Exception as ex:
            raise SystemExit(f"Error while stopping NiPy!\n\nLog: {ex}")