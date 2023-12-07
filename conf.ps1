$pythonInstallerUrl = "https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe"

$installerPath = "C:\Temp\python_installer.exe"

Invoke-WebRequest -Uri $pythonInstallerUrl -OutFile $installerPath

Start-Process -Wait -FilePath $installerPath -ArgumentList "/quiet", "InstallAllUsers=1", "PrependPath=1"

Remove-Item -Path $installerPath -Force

choco install -y python3

python --version

pip install pyautogui numpy sounddevice keyboard

$dest = Read-Host "Where do you want the script to be located"
$whereami = Read-Host "Where is the script you installed"

try {
    Move-Item -Path $whereami -Destination $dest -Force
    Write-Host "Script moved successfully."
}
catch {
    Write-Host "Error moving script: $_"
}

try {
    New-Item -ItemType Directory -Path (Join-Path $dest "prjfiles") -Force
    Write-Host "'prjfiles' folder created successfully."
}
catch {
    Write-Host "Error creating 'prjfiles' folder: $_"
}
