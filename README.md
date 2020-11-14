<img src=/img/ftpgear.png><br><br><img src="https://forthebadge.com/images/badges/built-with-love.svg" height="40" length="40"> <img src="https://forthebadge.com/images/badges/made-with-python.svg" height="40" length="40"> <img src="https://forthebadge.com/images/badges/fuck-it-ship-it.svg" height="40" length="40">
# FTPGear
FTPGear is a small script which allows you to perform some FTP actions<br>
### More specificly
* list files on directory        
* create file        
* delete file        
* create directory        
* remove directory        
* change directory        
* rename directory or file  
* create mass files/directories
## Ftplib
**ls**
```py
ftp.dir()
```
**fcreate**
```py
ftp.storbinary('STOR ' + filename)
```
**fremove**
```py
ftp.delete(filename)
```
**rename**
```py
ftp.rename(name, new_name)
```
**dcreate**
```py
ftp.mkd(directoryname)
```
**dremove**
```py
ftp.rmd(directoryname)
```
**cdir**
```py
ftp.cwd(directoryname)
```
# CLI Interface
<img src=/img/ftpgear.gif><br>
## Example
<img src=/img/directory.gif><br>
