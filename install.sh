#!/bin/bash

# Make bash trap to detect Ctrl+C
trap bashtrap INT
bashtrap() {
    echo -e "\nCTRL+C Detected! executing installation..."
    exit
}

# Install requirements for NiPy
function install_requirements {
	# Prompt the user to continue installation...
	echo -e "You are about to install NiPy! Continue? [Ctrl+C to exit] \c"
    read $prompt

    # Set requirements file
    File="requirements.txt"
    
    # Check requirements file
	if [ -e $File ]; then
       echo $(pip install -r $File)
       echo ""
       echo -e "[!] Run 'sudo python nipy.py install' to install script."
       exit
       
	else 
		echo "[x] Requirements file does not exist!"
		exit
	fi
}


# Main function
function main {
	# Get input from user
	echo "Welcome to NiPt installer"
	echo "1) Install"
	echo "2) NiPy (python) Github"
	echo "3) Nipe (perl)   Github"
	echo -e "Choose the option: \c"
	read operation

    # Select Operation	
    if [ $operation == "1" ]; then
        install_requirements
    elif [ $operation == "2" ]; then
    	echo $(open "https://github.com/kourva/nipy")
    elif [ $operation == "3" ]; then
    	echo $(open "https://github.com/htrgouvea/nipe")
    else
    	exit
    fi
}

# Run main function
main