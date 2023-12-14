#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Standard library modules
import subprocess
import os
from typing import NoReturn, Tuple, Union


class Start:
    def __init__(self, username: str, distribution: str) -> NoReturn:
        # Set device information
        self.username: str = username
        self.distribution: str = distribution

        # Set DNS port & Stransfer Port
        self.dnsPort: str = "9061"
        self.transferPort: str = "9051"

        # Set table & Network
        self.tables: Tuple[str, str] = ("nat", "filter")
        self.network: str = "10.66.0.0/255.255.0.0"

        # Set start TOR service command
        self.startTor: str = "systemctl start tor"


    def start_nipy(self) -> Union[bool, NoReturn]:
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
                self.startTor = "sv start tor > /dev/null"

            # Update Tor service start command if there is TOR init file in system
            if os.path.exists("/etc/init.d/tor"):
                self.startTor = "/etc/init.d/tor start > /dev/null"

            # Run tor with manual config file
            subprocess.run(f"tor -f .configs/$device{self.distribution}-torrc > /dev/null", shell=True);

            # Start tor service
            subprocess.run(f"{self.startTor}", shell=True)

            # Configures iptables rules for the specified tables, network, and ports. 
            for table in self.tables:

                # Set target
                target: str = "ACCEPT" if table == "nat" else "RETURN"
                
                # Execute Iptables commands
                subprocess.run(f"iptables -t {table} -F OUTPUT", shell=True)
                subprocess.run(f"iptables -t {table} -A OUTPUT -m state --state ESTABLISHED -j {target}", shell=True)
                subprocess.run(f"iptables -t {table} -A OUTPUT -m owner --uid {self.username} -j {target}", shell=True)

                # Set match DNS Port
                matchDnsPort: str = self.dnsPort
                if table == "nat":
                    target = f"REDIRECT --to-ports {self.dnsPort}"
                    matchDnsPort = "53"

                # Execute Iptables commands
                subprocess.run(f"iptables -t {table} -A OUTPUT -p udp --dport {matchDnsPort} -j {target}", shell=True)
                subprocess.run(f"iptables -t {table} -A OUTPUT -p tcp --dport {matchDnsPort} -j {target}", shell=True)

                # Update target
                if table == "nat":
                    target = f"REDIRECT --to-ports {self.transferPort}"

                # Execute Iptables commands
                subprocess.run(f"iptables -t {table} -A OUTPUT -d {self.network} -p tcp -j {target}", shell=True)

                # Update target
                if table == "nat":
                    target = "RETURN"

                # Execute Iptables commands
                subprocess.run(f"iptables -t {table} -A OUTPUT -d 127.0.0.1/8 -j {target}", shell=True)
                subprocess.run(f"iptables -t {table} -A OUTPUT -d 192.168.0.0/16 -j {target}", shell=True)
                subprocess.run(f"iptables -t {table} -A OUTPUT -d 172.16.0.0/12 -j {target}", shell=True)
                subprocess.run(f"iptables -t {table} -A OUTPUT -d 10.0.0.0/8 -j {target}", shell=True)

                # Update target
                if table == "nat":
                    target = f"REDIRECT --to-ports {self.transferPort}"

                # Execute Iptables commands
                subprocess.run(f"iptables -t {table} -A OUTPUT -p tcp -j {target}", shell=True)

            # Execute Iptables commands
            subprocess.run(f"iptables -t filter -A OUTPUT -p udp -j REJECT", shell=True)
            subprocess.run(f"iptables -t filter -A OUTPUT -p icmp -j REJECT", shell=True)

            # Execute SysCtl commands
            subprocess.run(f"sysctl -w net.ipv6.conf.all.disable_ipv6=1 >> /dev/null", shell=True)
            subprocess.run(f"sysctl -w net.ipv6.conf.default.disable_ipv6=1 >> /dev/null", shell=True)

            return True

        except Exception as ex:
            raise SystemExit(f"Error while starting NiPy!\n\nLog: {ex}")