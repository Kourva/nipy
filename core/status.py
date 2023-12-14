"""
status.py file used in nipy.py file
"""
# -*- coding: utf-8 -*-


# Standard library modules
from typing import NoReturn, Dict, Union

# Related Thirty-Party modules
import requests


class Status:
    def __init__(self) -> NoReturn:
        # Set initial URL to send request
        self.url: str = "https://check.torproject.org/api/ip"
        self.red: str = "\33[1;31m"
        self.green: str = "\33[1;32m"
        self.blue: str = "\33[1;34m"
        self.reset: str = "\33[m"

    def check_tor(self) -> str:
        """
        Method to check tor status for nipy

        Parameters:
            None

        Returns:
            result (str): Information about IP or Error message
        """
        try:
            # Send get request to API and get results
            response: Dict[str, Union[str, bool]] = requests.get(url=self.url).json()

            # Fetch Tor and IP status from result
            is_tor: bool = response["IsTor"]
            ip_addr: str = response["IP"]

            # Set the status based on tor detection
            running: str = (
                f"{self.green if is_tor else self.red}"
                f"{'Running...' if is_tor else 'Not running!'}"
                f"{self.reset}"
            )

            # Return the result
            return (
                f"\n  [+] Status: {running}\n"
                f"  [+] IP    : {self.blue}{ip_addr}{self.reset}\n"
            )

        except requests.exceptions.RequestException:
            return (
                f"\n  [!]{self.red} Could not get status for TOR! Is Nipy running??{self.reset}\n"
            )
