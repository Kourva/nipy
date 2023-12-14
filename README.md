<div align="center">
   <img align="left" width="200px" src="https://styleguide.torproject.org/static/images/tor-logo/color.svg" />
   <h1 align="left"><b>Nipy</b></h1>
   <p align="left" >An engine to make Tor network your default gateway (coded in Python)</p>
</div>
<br>

# Intro
So, basically this is same as [`nipe`](https://github.com/htrgouvea/nipe) but coded in Python.<br>
Both doing same thing with same output but found this project cool to make, I will make the GUI version too...

# Installation
For installation, everything is ready to go, Just have a Linux system which has Python installed and here you go.
1. **Clone repository**:
```bash
git clone https://github.com/Kourva/nipy
```
2. **Navigate to source's directory**:
```bash
cd nipy
```
3. **Make installer executable** (this will install requirements):
```bash
chmod +x install.sh
```
4. **Running installer**:
```bash
./install.sh
```
> Select 1 and hit Enter in next prompt to begin installation process
5. **Install NiPy**:
```bash
sudo nipy.py install
```
With this command you will install nipy in your system (basically this will install tor and iptables based on your system distribution)<br>
And everything is ready to go.

# Usage
1. **To start the NiPy**:
```bash
sudo python nipy.py start
```
> Simple output:
> ```plaintext
>   [*] Nipy Started.
> ```
2. **To stop the NiPy**:
```bash
sudo python nipy.py stop
```
> Simple output:
> ```plaintext
>   [*] Nipy Stopped.
> ```
3. **To restart the NiPy**:
```bash
sudo python nipy.py restart
```
> Simple output:
> ```plaintext
>  [*] Nipy Re started!
> ```
4. **To see status of NiPy**:
```bash
sudo python nipy.py status
```
> Simple output:
> ```plaintext
>  [+] Status: Running...
>  [+] IP    : xxx.xxx.xxx.xxx
> ```
> or If you are not connected:
> ```plaintext
>   [!] Could not get status for TOR! Is Nipy running??
> ```
5. **To see help message**:
```bash
sudo python nipy.py help
```
> Simple output:
> ```plaintext  
>  [!] Usage: python nipy.py [argument]
>
>  - install    | Install NiPy
>  - start      | Start the NiPy
>  - stop       | Stop the NiPy
>  - restart    | Re start the niPy
>  - status     | Show NiPy status
>  - help       | Show this message
> ```



