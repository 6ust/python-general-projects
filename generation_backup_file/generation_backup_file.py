import shutil

fileCp = "C:\\Users\\Gust\\Downloads\\unnamed.png"
fileBkp = "C:\\Users\\Gust\\Downloads\\"

fileExtesion = ".png"

shutil.copy(fileCp, fileBkp + str("unnamed-1") + fileExtesion)