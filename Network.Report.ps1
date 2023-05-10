# Script Name:                  Newwork Report via Powershell
# Author:                       Eduardo Ayala
# Date of latest revision:      05/09/2023
# Purpose:                      Create Network report

# Create network_report.txt file that holds the contents of ipconfig /all
new-item -Path 'C:\Users\Ghost|Desktop\Network_Report.txt' -ItemType File

# Use Select-String to search network_report.txt and return only the IPv4 address
Get-Content network_report.txt | Select-String -Pattern '\bIPv4 Address\b' | Out-File network_report.txt