import sys
from cx_Freeze import setup, Executable

include_files = ['DOCX_feature_extraction.py',
                 'DOCX_DataPreprocessing.py',
                 'WORD_main.py',
                 'WORD_LOGO.ico',
                 "D:\GITHUB\AI_WORD_GUI_실행 파일\msvcp140.dll",
                 "D:\GITHUB\AI_WORD_GUI_실행 파일\sklearn\.libs\vcomp140.dll"]

includes = ['PyQt5.QtWidgets', 'PyQt5.QtCore', 'PyQt5.QtGui',
            'pandas', 'numpy', 'sklearn', 'functools',
            're', 'zipfile', 'xml.etree.ElementTree']

package = ["numpy"]

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

# Create an executable
exe = Executable(
    script="main.py",
    base=base,
    icon="WORD_LOGO.ico",
)

setup(
    name="Word Search",
    version="1.0",
    description="Word Search Program",
    options={
        "build_exe": {
            "include_files": include_files,
            "includes": includes,
            "packages": package,
        }
    },
    executables=[exe]
)
