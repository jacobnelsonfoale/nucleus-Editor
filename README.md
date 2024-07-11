# nucleolusTextEditor
[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) \
Simple Hackable editor made with Python

*Consult Wiki for install guide https://github.com/jacobnelsonfoale/nucleus-Editor/wiki*

# Linux
## Running binary files

Install wget from your Linux distro's package manager `sudo apt install wget`

To install nucleus-editor run `wget https://github.com/jacobnelsonfoale/nucleus-Editor/releases/download/v24.2/NT`

*Alternatively you can just grab this binary file from the latest releases on GitHub*

Make sure file is executable `chmod +x NT`

Run file `./NT`

## Adding to path

Adding nucleus to $PATH allows you to run the text editor from anywhere on your system in the terminal with the NT command. Alternatively I would recommend for convenience to rename NT to nt if you want to make it easier to run in the terminal.

Find Location of path `echo $PATH`

/usr/local/bin is going to be the location 99.99% of the time `sudo mv NT /usr/local/bin`

Run command to make sure everything is working properly `NT`

*If you run into any problems try to repeat the install steps once again to make sure something did not go wrong.*

# Windows
You can run nucleus-editor under windows but no documentation has been written yet. Consult the wiki for any updates or changes https://github.com/jacobnelsonfoale/nucleus-Editor/wiki/Getting-Started#windows.
