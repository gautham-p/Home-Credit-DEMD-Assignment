$path=Get-Content(".\config\Python.txt")
virtualenv --python=$path virtDEMD
& "./virtDEMD/Scripts/activate.ps1"