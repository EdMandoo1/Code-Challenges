# Script Name:                  CSV to powershell
# Author:                       Eduardo Ayala
# Date of latest revision:      06/21/2023
# Purpose:                      Add data to CSV via Powershell

# Define the data
$data = @"
Department,Role,Name
Executive Team,CEO,Anna Müller
Executive Team,COO,Malik Ahmed
Executive Team,CTO,Noah Bauer
Executive Team,CFO,Aria Schmidt
Engineering,Chief Engineer,Rohit Gupta
Engineering,Senior Engineer,Sophia Nguyen
Engineering,Senior Engineer,Felix Wagner
Engineering,Engineer,Marcus Johnson
Engineering,Engineer,Olivia Lehmann
Engineering,Engineer,David Schmitt
Project Management,Project Manager,Maya Schmidt
Project Management,Project Manager,Xavier Lehmann
Project Management,Project Manager,Leila Braun
Sales & Marketing,Chief Marketing Officer,Ethan Bauer
Sales & Marketing,Head of Sales,Sanjay Schmidt
Sales & Marketing,Marketing Manager,Mia Becker
Sales & Marketing,Marketing Coordinator,Aiden Müller
Sales & Marketing,Sales Representative,Esha Wagner
Sales & Marketing,Sales Representative,Omar Krause
Customer Success,Head of Customer Success,Hannah Müller
Customer Success,Customer Success Manager,Farhan Schmidt
Customer Success,Customer Success Representative,Aria Bauer
Customer Success,Customer Success Representative,Naomi Braun
Operations,Operations Manager,Lauren Fischer
Operations,Logistics Coordinator,Rohit Meyer
Operations,Procurement Specialist,Maya Schmidt
Operations,HR Manager,Amara Schulz
Operations,IT Specialist,Lucas Keller
Operations,Legal Counsel,Hannah Koch
Research & Development,R&D Manager,Ava Bauer
Research & Development,Research Scientist,Marcus Johnson
Research & Development,Research Scientist,Olivia Lehmann
Research & Development,Research Scientist,David Schmitt
"@ | ConvertFrom-Csv

# Set the output path
$outputPath ="/home/eddie/New_Folder/team_data.csv"

# Export the data to a CSV file
$data | Export-Csv -Path $outputPath 

# Display a success message
Write-Host "CSV file exported to $outputPath"
