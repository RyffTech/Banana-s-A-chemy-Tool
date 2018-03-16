from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
	windows=[{'script':"Alchemy.py","icon_resources":[(1, "alch.ico")],"dest_base":"alchemy"}], zipfile = None,
	options = {'py2exe': {'bundle_files': 1, "dll_excludes":["tcl85.dll","tk85.dll"],'compressed': True}})
            