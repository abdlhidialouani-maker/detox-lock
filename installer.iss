; Inno Setup script - turns DetoxLock.exe into a real installer (DetoxLock_Setup.exe)
; Free tool: https://jrsoftware.org/isdl.php

[Setup]
AppName=Detox Lock
AppVersion=1.0
AppPublisher=Detox Lock
DefaultDirName={autopf}\Detox Lock
DefaultGroupName=Detox Lock
DisableProgramGroupPage=yes
OutputDir=installer_output
OutputBaseFilename=DetoxLock_Setup
SetupIconFile=icon.ico
UninstallDisplayIcon={app}\DetoxLock.exe
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=lowest

[Tasks]
Name: "desktopicon"; Description: "Create a &Desktop shortcut"; GroupDescription: "Shortcuts:"

[Files]
Source: "dist\DetoxLock.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{autodesktop}\Detox Lock"; Filename: "{app}\DetoxLock.exe"; Tasks: desktopicon
Name: "{autoprograms}\Detox Lock"; Filename: "{app}\DetoxLock.exe"

[Run]
Filename: "{app}\DetoxLock.exe"; Description: "Start Detox Lock now"; Flags: nowait postinstall skipifsilent
