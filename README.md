# droneNLedu

This repository contains necessary functions to control a Cheerson CX-10WD over Wifi via a computer running Python 3.

![Micro Drone](https://github.com/JadinTredup/Drone-Controls/blob/master/Wifi-PyDrone/Images/drone%20photo.jpg "Cheerson Micro Drone")

## Requirements:
### Hardware:
- Cheerson CX10WD-TX Micro-Drone, Available on Amazon
- Host Laptop

### Software:
- Python 3
- NumPy
- (Optional) OpenCV with Python Bindings

## Installation on Windows:
### Installing Python3:
Navigate to the [Python Downloads Page for Windows](https://www.python.org/downloads/windows/) and select "Download Windows x86-64 executable installer" for Python 3.7.1. Run the Executable file making sure to check "Add Python3 to PATH" box at the bottom of the dialog box. Once the setup is finished you can move on to installing dependencies.
![Python Path](https://github.com/JadinTredup/Drone-Controls/blob/master/Wifi-PyDrone/Images/python-path.JPG "Python Path")

After installation has completed, the installer will ask for permission to disable your systems path length limit. This is to because windows has recently implemented a length limit for system path length. Allow Python to disable the path length limit by selecting the option shown below. 
![Disable Path](https://github.com/JadinTredup/Drone-Controls/blob/master/Wifi-PyDrone/Images/python-disable-limit.JPG "Disable Path")

### Installing Dependencies:
Most of the modules needed to run this code is either bundled with Python3 or are contained within this repository. The only necessary dependency we will need to install for ourselves is NumPy - a package for scientific computing within Python. Installing new packages in Python3 is very easy using the Pip3 command.

Pip is the package management system built into Python which allows for easy command-line installation and removal of a variety of software packages. Pip is a recursive acronym meaning "Pip Installs Packages." Because we are using Python3 we will be using the Pip3 command to install our package. Open up a command-prompt by typing "cmd" into the start menu search bar

![Command Prompt](https://github.com/JadinTredup/Drone-Controls/blob/master/Wifi-PyDrone/Images/command-prompt.JPG "Command Prompt")

Once the command prompt is open enter the following command:
```
pip3 install numpy
```
#### Optional: Install OpenCV
Being able to simply control the drone will only get us so far. Part of the motivation for controlling these micro-drones with python is the ability to extend their functionality through the use of a host computer. We are able to do this as long as we have some sort of feedback from the drone. In experimental cases, cameras place around the environment are used to help localize the drone. If you are interested in extending the functionality of your drone to include camera-feedback, you will also need an image-processing package called "OpenCV." We can do so easily with the command line by running:
```
pip3 install opencv-python
```

## Downloading the Code
To download this code, navigate to the upper right hand corner of this respository and press "download .ZIP" You may extract the .ZIP file into a folder of your choice. In the examples below we have extracted it to a folder within our Documents titled "Drone-Controls-master."

![Download Zip](https://github.com/JadinTredup/droneNLedu/blob/master/images/downloadzip.png "Download Zip")

## Verifying the Installation:
To verify the installation we will need to first connect to the Wifi network established by the CX10-WD-TX then run a test program from the host PC.

### 1. Connect the Drone:
Communication to the drone is handled via dedicated Wifi signal emitted from the drone itself. To make a connection to the drone, power it on then navigate to the Wifi section of the Host-PC and select its Wifi network. The name of the network should be some variation of "CX10-XXXXX."

### 2. Navigate to Directory:
Navigate to the directory in which the code was extracted into by entering the following into a command prompt and replacing "YOUR-PATH" with the path to the directory:
```
cd \YOUR-PATH\
```
If you do not know the path to the folder you can find it by navigating the folder and clicking in the address bar (seen below) to get the full path. You can copy it from here. For example, extracting the full repository into your Documents folder would have a resulting path similar to the following:
```
cd C:\users\EGG101\Documents\Drone-Controls-master\Drone-Controls-master\Wifi-PyDrone
```
![Folder path](https://github.com/JadinTredup/Drone-Controls/blob/master/Wifi-PyDrone/Images/locate-directory.JPG "Folder Path")
### 3. Run the test code
Once in the directory we can run the test program to verify that we have properly completed the prerequisites.

*__IMPORTANT NOTE: Please remove the props from the drone before testing. The testing script establishes a connection to the drone and send a quick take-off command, then powers off the motors. If the props are left on it is very likely the drone will take off in a random direction and possibly injure someone.__*

From the command prompt, run the command:
```
python test_mp.py
```
__NOTE: If you have another version of python already installed then you may need to replace "python" with "python3" or in some cases, even "py."__
