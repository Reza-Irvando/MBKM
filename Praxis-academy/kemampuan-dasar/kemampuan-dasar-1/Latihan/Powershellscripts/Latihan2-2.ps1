Write-Host "Hello, Guru99!"
Get-WmiObject -Class Win32_OperatingSystem –ComputerName localhost |
Select-Object -Property CSName,FreeVirtualMemory 
