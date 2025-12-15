; Inno Setup Script for Ebook Screenshot Tool
; This creates a Windows installer for the application

[Setup]
AppName=Ebook Screenshot Tool
AppVersion=1.0
AppPublisher=Ebook Screenshot Tool
DefaultDirName={autopf}\EbookScreenshotTool
DefaultGroupName=Ebook Screenshot Tool
OutputDir=installer_output
OutputBaseFilename=EbookScreenshotTool_Setup
Compression=lzma
SolidCompression=yes
SetupIconFile=
WizardImageFile=
WizardSmallImageFile=
PrivilegesRequired=lowest
ArchitecturesAllowed=x64
ArchitecturesInstallIn64BitMode=x64

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop icon"; GroupDescription: "Additional icons:"
Name: "quicklaunchicon"; Description: "Create a &Quick Launch icon"; GroupDescription: "Additional icons:"; Flags: unchecked

[Files]
Source: "ebook_screenshot.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "get_coordinates.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "launcher.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "run.bat"; DestDir: "{app}"; Flags: ignoreversion
Source: "requirements.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "README.md"; DestDir: "{app}"; Flags: ignoreversion
; Note: Python and dependencies should be installed separately or bundled

[Icons]
Name: "{group}\Ebook Screenshot Tool"; Filename: "python.exe"; Parameters: """{app}\launcher.py"""; WorkingDir: "{app}"; IconFilename: "{sys}\shell32.dll"; IconIndex: 147
Name: "{group}\Coordinate Helper"; Filename: "python.exe"; Parameters: """{app}\get_coordinates.py"""; WorkingDir: "{app}"; IconFilename: "{sys}\shell32.dll"; IconIndex: 147
Name: "{group}\Uninstall Ebook Screenshot Tool"; Filename: "{uninstallexe}"
Name: "{autodesktop}\Ebook Screenshot Tool"; Filename: "python.exe"; Parameters: """{app}\launcher.py"""; WorkingDir: "{app}"; IconFilename: "{sys}\shell32.dll"; IconIndex: 147; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\Ebook Screenshot Tool"; Filename: "python.exe"; Parameters: """{app}\launcher.py"""; WorkingDir: "{app}"; IconFilename: "{sys}\shell32.dll"; IconIndex: 147; Tasks: quicklaunchicon

[Run]
Filename: "python.exe"; Parameters: "-m pip install -r requirements.txt"; WorkingDir: "{app}"; StatusMsg: "Installing Python dependencies..."; Flags: runhidden

[Code]
function InitializeSetup(): Boolean;
begin
  // Check if Python is installed
  if not RegQueryStringValue(HKEY_LOCAL_MACHINE, 'SOFTWARE\Python\PythonCore\3.11\InstallPath', '', Result) and
     not RegQueryStringValue(HKEY_LOCAL_MACHINE, 'SOFTWARE\Python\PythonCore\3.10\InstallPath', '', Result) and
     not RegQueryStringValue(HKEY_LOCAL_MACHINE, 'SOFTWARE\Python\PythonCore\3.9\InstallPath', '', Result) and
     not RegQueryStringValue(HKEY_LOCAL_MACHINE, 'SOFTWARE\Python\PythonCore\3.8\InstallPath', '', Result) then
  begin
    MsgBox('Python 3.8 or higher is required but was not found. Please install Python first.', mbError, MB_OK);
    Result := False;
  end
  else
    Result := True;
end;

