# Script Name:                  Log Retrieval via Powershell
# Author:                       Eduardo Ayala
# Date of latest revision:      05/04/2023
# Purpose:                      Log Retrieval via Powershell

# Output all events from the System event log that occurred in the last 24 hours to a file on your desktop named last_24.txt
Get-EventLog -LogName System -After (Get-Date).AddDays(-1) | Out-File -FilePath .\Desktop\last_24.txt

# Output all “error” type events from the System event log to a file on your desktop named errors.txt
Get-EventLog -LogName System -EntryType Error | Out-File -FilePath .\Desktop\errors.txt

# Print to the screen all events with ID of 16 from the System event log
echo Get-EventLog -LogName System -InstanceId 16

# Print to the screen the most recent 500 entries from the System event log.
echo Get-EventLog -LogName System -Newest 20 | Format-Table -AutoSize -wrap

# Print to the screen all sources of the 500 most recent entries in the System event log.
echo Get-EventLog -LogName System -Newest 500 