# Script Name:                  Automatic OS Update_Windows
# Author:                       Eduardo Ayala
# Date of latest revision:      07/10/2023
# Purpose:                      To check for updates every day at 3am.

# Set Windows Update settings to enable automatic updates
$AUSettings = Get-AutomaticUpdatesSettings
$AUSettings.NotificationLevel = 2  # Notify before download and installation
$AUSettings.ScheduledInstallationDay = 0  # Every day
$AUSettings.ScheduledInstallationTime = 3  # 3:00 AM
$AUSettings.IncludeRecommendedUpdates = 1  # Include recommended updates
Set-AutomaticUpdatesSettings $AUSettings

# Enable automatic updates
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update" -Name AUOptions -Value 4

# Restart Windows Update service to apply changes
Restart-Service -Name wuauserv
