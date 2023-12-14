#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Standard library modules
import platform
from typing import NoReturn, Tuple, Union


class Device:
    def __init__(self) -> NoReturn:
        """
        This checks OS Release information and gets ID and ID_LIKE for 
        OS's username and distribution

        Parameters:
            None

        Returns:
            None
        """
        self.username: str = ""
        self.distribution: str = ""


    def get_device_info(self) -> Union[Tuple[str, str], NoReturn]:
        """
        This will get Device information using Platform Library

        Parameters:
            None

        Returns:
            On success: Username & Distribution (typing.Tuple[str, str])
            On failure: NoReturn"""
        try:
            # Get Os release info
            OS_info: Dict[str, str] = platform.freedesktop_os_release()

            # Extract ID and Distro info
            ID_like: str = OS_info["ID_LIKE"].lower()
            Distro: str = OS_info["ID"].lower()        

            # Update username & distribution for fedora based systems 
            if ID_like == "fedora" or Distro == "fedora":
                self.username = "toranon"
                self.distribution = "fedora"

            # Update username & distribution for Arch & CentOS based systems 
            elif ID_like in ["arch", "centos"] or Distro in ["arch", "centos"]:
                self.username = "tor"
                self.distribution = "arch"

            # Update username & distribution for Void Linux 
            elif Distro == "void":
                self.username = "tor"
                self.distribution = "void"

            # Update username & distribution for Debian based systems 
            elif ID_like == "debian":
                self.username = "debian-tor"
                self.distribution = "debian"

            # Raise error if could not detect distribution
            else:
                return None

            # Return device info
            return (self.username, self.distribution)

        except:
            return None