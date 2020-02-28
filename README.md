# Reboot Router Solution
___
> Purpose: ```Check for an internet connection and if there is not one, open the router web ui and 'press' the reboot buttom.```
    
> Requirements: ```This solution is built for a Netgear C7800 modem / router but could be used for any Netgear router with the same ui. (e.g., my previous Netgear router had the same ui)```
>
___
## Installation 
1. Run pip install -r requirements from the folder you installed Reboot_Router to install the required python packages.

2. Download and install firefox geckodriver if you do not already have it installed on your machine. Follow the instructions here: https://github.com/mozilla/geckodriver/releases

3. Create a file named 'params.ini' in your directory and populate it like this:

           [Defaults]
           Gecko_Path: full path to the firefox geck driver executable
           User_Name: user name usually set as admin
           Password: your router password
                    
4. Create a windows "autocheck.bat" file and populate it like this:
           
           @echo off
           cd 'full path to where reboot router is installed'
           python main.py >> routercheck.log

5. Add a scheduler task in Windows to run the autocheck.bat file every 15 minutes.

6. (Optional): Your log files may grow to be large so you could also create and schedule a windows cleanlog.bat file and populate it as follows:
           
           @echo off
           cd 'full path to where reboot router is installed'
           for /f %%a in ('powershell -Command "Get-Date -format yyyy_MM_dd__HH_mm_ss"') do set datetime=%%a
           copy routercheck.log %datetime%_Backup_routercheck.log
           break>routercheck.log
           copy geckodriver.log %datetime%_Backup_geckodriver.log
           break>geckodriver.log
           rem delete older logs - keep last 4 weeks
           for /f "skip=8 eol=: delims=" %%F in ('dir /b /o-d /a-d 2*.log') do @del "%%F"
