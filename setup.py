from cx_Freeze import setup, Executable
import sys
import os

os.environ['TCL_LIBRARY'] = "C:\\Users\\Sostenes\\AppData\\Local\\Programs\\Python\\Python38-32\\tcl\\tcl8.6"
os.environ['TCL_LIBRARY'] = "C:\\Users\\Sostenes\\AppData\\Local\\Programs\\Python\\Python38-32\\tcl\\tk8.6"

base = None

if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [Executable("ImportDetalhePapeis.py", base=base)]

packages = [
    "os",
    "urllib",
    "urllib.request",
    "bs4",
    "BeautifulSoup",
    "idna",
]

options = {
    'build_exe':{
        'packages': packages,
        'include_files':[
            os.path.join('C:\\Users\\Sostenes\\AppData\\Local\\Programs\\Python\\Python38-32\\DLLs\\tcl86t.dll'),
            os.path.join('C:\\Users\\Sostenes\\AppData\\Local\\Programs\\Python\\Python38-32\\DLLs\\tk86t.dll')
        ]
    },
}

setup(name="ImportaFundamentus",
        options=options,
        version="1.0",
        description= "Download Fundamentus",
        executables=executables,
      )
