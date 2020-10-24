# Satellite-Wallpaper

* Open Task Scheduler (press [Windows Key] and type "Task Scheduler")

* In task scheduler, click [Create Task]
![Task Scheduler First Page](https://github.com/williamsnell/Satellite-Wallpaper/blob/main/readme_images/snip_1.PNG)

* Name your task something useful, like "Update Desktop Image"
![Task Name](https://github.com/williamsnell/Satellite-Wallpaper/blob/main/readme_images/snip_2.PNG)

* In the "Triggers" tab, click [New]
* Select "Daily"
* Tick "Repeat Task Every: " and select your desired refresh interval from the dropdown menu (I've selected every hour) 
* Click [OK]

![Task Triggers](https://github.com/williamsnell/Satellite-Wallpaper/blob/main/readme_images/snip_3.PNG)

* Under the "Actions" tab, click [New]
* Find your python executable path, and put it in the Program/script box
  * For a conda environment, for example, this should be by default: 
  
    "C:\Users\[Your Name]\AppData\Local\conda\conda\envs\[Environment Name]\python.exe"
* In the "Add arguments (optional)" box, type the path to the python script in quotation marks, e.g.:
    "C:\Users\[Your Name]\Downloads\desktop_background_script.py"
* Click [OK]

![Task Actions](https://github.com/williamsnell/Satellite-Wallpaper/blob/main/readme_images/snip_4.PNG)

* Click OK to save your task
