# Strobe
Strobe updates your wallpaper automatically.
For now, only one image collector is available (Meteosat-11 data)

![Demo](https://faydoom.github.com/Strobe/demo.png)

## Installation
	git clone https://github.com/FayDoom/Strobe.git
	pip install --requirement requirements.txt

## Usage
	python main.py

## Run at startup (windows)
	$path = "PATH TO main.py" #e.g.: "C:/Users/<username>/Desktop/Strobe/main.py"
	$action  = New-ScheduledTaskAction -Execute 'pythonw.exe' -Argument $path
	$trigger =  New-ScheduledTaskTrigger -AtStartup
	Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "Strobe-Wallpaper" -Description "Strobe, the wallpaper updater"
