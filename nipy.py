#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# NiPy - [Nipe] re-coded in Python
# An engine to make Tor network your default gateway
# Nipe: https://github.com/htrgouvea/nipe


# Standard library imports
import os
import sys
import platform
from typing import NoReturn, Tuple

# Local application/library specific imports
from core.install import Install
from core.device import Device
from core.status import Status
from engine.start import Start
from engine.stop import Stop


# NiPy Class
class NiPy:
    def __init__(self, argument: str) -> NoReturn:
        """
        This method will handle argument and do specific process
        based on given argument

        Parameters:
            argument (str): argument to be processed. one of:
                            - install
                            - start
                            - stop
                            - restart
                            - status
                            - help

        Returns:
            None (typing.NoReturn)
        """
        # Set the argument
        self.argument: str = argument.strip().lower()
        
        # Initialize device info variables
        self.username: str = ""
        self.distribution: str = ""

        # Initialize colors for pretty printing
        self.red: str = "\33[1;31m"
        self.green: str = "\33[1;32m"
        self.blue: str = "\33[1;34m"
        self.reset: str = "\33[m"


    def process(self) -> NoReturn:
        """
        Process method to do process with given argument

        Parameters:
            None

        Returns:
            None (typing.NoReturn)
        """
        # Get argument
        argument: str = self.argument

        # Print Device info (will update self.username & self.distribution)
        info: Tuple[str, str] = Device().get_device_info()
        if info:
            self.argument, self.distribution = info
        else:
            raise SystemExit(f"[x] {self.red}Could not get system information!{self.reset}")
        
        # Process [status] argument
        if argument == "install":
            print(f"\n  [*] {self.blue}Installing NiPy... Be patient.{self.reset}\n")
            Install(self.username,self.distribution).execute_installation()

        # Process [status] argument
        elif argument == "status":
            status: str = Status().check_tor()
            raise SystemExit(status)

        # Process [start] argument
        elif argument == "start":
            if Start(self.argument, self.distribution).start_nipy():
                raise SystemExit(f"\n  [*]{self.green} Nipy Started.{self.reset}\n")

        # Process [stop] argument
        elif argument == "stop":
            if Stop(self.argument, self.distribution).stop_nipy():
                raise SystemExit(f"\n  [*]{self.red} Nipy Stopped.{self.reset}\n")

        # Process [restart] argument
        elif argument == "restart":
            # Stop the service
            if Stop(self.argument, self.distribution).stop_nipy():
                # Start the service again
                Start(self.argument, self.distribution).start_nipy()
            raise SystemExit(f"\n  [*]{self.blue} Nipy Re started!{self.reset}\n")
        
        # Process [help] argument
        elif argument == "help":
            raise SystemExit(
                f"\n  [!] Usage: python nipy.py [argument]\n\n"
                f"  - install    | Install NiPy\n"
                f"  - start      | Start the NiPy\n"
                f"  - stop       | Stop the NiPy\n"
                f"  - restart    | Re start the niPy\n"
                f"  - status     | Show NiPy status\n"
                f"  - help       | Show this message\n"
            )

        # Handle invalid argument
        else:
            raise SystemExit(f"\n  [*]{self.red} Invalid argument!{self.reset}\n")


def main() -> NoReturn:
    """
    Main function to handle NiPy with argument. This will also checks root 
    privilege (which is required), System (must be Linux in this case). 

    Parameters:
        None

    Returns:
        NoReturn
    """
    # Check argument
    if len(sys.argv) < 2:
        raise SystemExit("\n  [!]\33[1;35m Usage: python nipy.py help\33[m\n")
    
    # Check Platform system
    if platform.system() != "Linux":
        raise SystemExit("\n  [x]\33[1;31m Sorry: Only for Linux Distributions!\33[m\n")

    # Check Sudo privilege
    if os.geteuid() != 0:
        raise SystemExit("\n  [x]\33[1;31m Error: Sudo privilege required!\33[m\n")

    # Run NiPy
    NiPy(sys.argv[1]).process()


# Run main program
if __name__ == "__main__":
    main()
