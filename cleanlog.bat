@echo off
cd C:\Users\John\PycharmProjects\Reboot_Router
for /f %%a in ('powershell -Command "Get-Date -format yyyy_MM_dd__HH_mm_ss"') do set datetime=%%a
copy routercheck.log %datetime%_Backup_routercheck.log
break>routercheck.log
copy geckodriver.log %datetime%_Backup_geckodriver.log
break>geckodriver.log
rem delete older logs - keep last 4 weeks
for /f "skip=8 eol=: delims=" %%F in ('dir /b /o-d /a-d 2*.log') do @del "%%F"
