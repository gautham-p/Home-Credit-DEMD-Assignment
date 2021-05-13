$path=Get-Content(".\config\Python.txt")
$path2=Get-Content(".\config\Libraries.txt")
virtualenv --python=$path virtDEMD
& "./virtDEMD/Scripts/activate.ps1"
pip install $path2
pip install uvicorn fastapi python-multipart