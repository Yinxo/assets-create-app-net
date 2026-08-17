@echo off
title Hausideen - lokaler Server
cd /d "%~dp0"
powershell -NoProfile -ExecutionPolicy Bypass -Command "$ip=(Get-NetIPAddress -AddressFamily IPv4 -PrefixOrigin Dhcp,Manual ^| Where-Object { $_.IPAddress -like '192.168.*' -or $_.IPAddress -like '10.*' } ^| Select-Object -First 1).IPAddress; Write-Host ''; Write-Host '   Hausideen laeuft lokal' -ForegroundColor Cyan; Write-Host '   ----------------------'; Write-Host ''; Write-Host '   Am TV-Browser eingeben:' -ForegroundColor Yellow; Write-Host ('   http://' + $ip + ':4012') -ForegroundColor Green; Write-Host ''; Write-Host '   Neue Bilder erscheinen dann in ~6 Sekunden von selbst.' -ForegroundColor DarkGray; Write-Host '   Fenster zum Beenden schliessen (oder Strg+C).' -ForegroundColor DarkGray; Write-Host ''"
py -m http.server 4012 --bind 0.0.0.0
