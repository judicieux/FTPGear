from ftplib import FTP
from colorama import Fore,Style,init
import socket
import mmap
import os

def login():
    logo()
    host = input(f'{Fore.YELLOW}[Host] > ')
    global username
    username = input('[Username] > ')
    password = input('[Password] > ')
    print("")
    try:
        global ftp
        ftp = FTP(host=host)
        login_status = ftp.login(user=username, passwd=password)
        file = open('response.txt', 'w')
        file.write(login_status)
        file.close()
        with open('response.txt') as f:
            s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            if s.find(b'230') != -1:
                handler()
            elif s.find(b'530 Login authentication failed') != -1:
                exit()
            else:
                exit()
    except SyntaxError:
        exit()
    except TimeoutError:
        exit()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def logo():
    logo = f"""{Fore.YELLOW}
    ███████╗████████╗██████╗  ██████╗ ███████╗ █████╗ ██████╗ 
    ██╔════╝╚══██╔══╝██╔══██╗██╔════╝ ██╔════╝██╔══██╗██╔══██╗
    █████╗     ██║   ██████╔╝██║  ███╗█████╗  ███████║██████╔╝
    ██╔══╝     ██║   ██╔═══╝ ██║   ██║██╔══╝  ██╔══██║██╔══██╗
    ██║        ██║   ██║     ╚██████╔╝███████╗██║  ██║██║  ██║
    ╚═╝        ╚═╝   ╚═╝      ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
    
         [+] Github : https://github.com/hypostat1c [+]
    """
    print(logo)

def handler():
    hostname = socket.gethostname()
    where = ftp.pwd()
    cmd = input(f'{Fore.YELLOW}' + hostname + f'{Fore.BLUE}@{Fore.YELLOW}' + username + '[' + f'{Fore.BLUE}' + where + f'{Fore.YELLOW}' + ']' + f'{Fore.BLUE}~$ ')
    try:
        if cmd == 'ls':
            print(f'{Fore.BLUE}')
            print(ftp.dir())
            print('')
            handler()
        elif cmd == 'fcreate':
            filename = input(f'{Fore.BLUE}[File Name] > ')
            ftp.storbinary('STOR ' + filename)
            print(f'{Fore.GREEN}+ Created +\n' + filename)
            handler()
        elif cmd == 'fremove':
            filename = input(f'{Fore.BLUE}[File Name] > ')
            ftp.delete(filename)
            print(f'{Fore.RED}+ Deleted +\n' + filename)
            handler()
        elif cmd == 'rename':
            filename = input(f'{Fore.BLUE}[File/Directory Name] > ')
            new_filename = input(f'{Fore.BLUE}[New Name] > ')
            ftp.rename(filename, new_filename)
            print(f'{Fore.GREEN}+ Renamed +\n' + new_filename)
            handler()
        elif cmd == "ftpbreak":
            breakerdir = input(f'{Fore.BLUE}[Name] > ')
            for i in range(99999999):
                ftp.mkd(breakerdir)
        elif cmd == 'dcreate':
            directoryname = input(f'{Fore.BLUE}[Directory Name] > ')
            ftp.mkd(directoryname)
            print(f'{Fore.GREEN}+ Created +\n' + directoryname)
            handler()
        elif cmd == 'dremove':
            directoryname = input(f'{Fore.BLUE}[Directory Name] > ')
            ftp.rmd(directoryname)
            print(f'{Fore.RED}+ Deleted +\n' + directoryname)
            handler()
        elif cmd == 'cdir':
            directoryname = input(f'{Fore.BLUE}[Directory Name] > ')
            ftp.cwd(directoryname)
            handler()
        elif cmd == 'help':
            a = f"""{Fore.GREEN}
              + Commands +              
                    
        ls = list files on directory        
        fcreate = create file        
        fremove = delete file        
        dcreate = create directory        
        dremove = remove directory        
        cdir = change directory        
        rename = rename directory or file  
        ftpbreak = create mass files/directories
            """
            print(a)
            handler()
        else:
            handler()
        if cmd == 'clear':
             clear()
        else:
            clear()
    except OSError:
        exit()
    except TypeError:
        exit()
    except KeyboardInterrupt:
        handler()
login()
