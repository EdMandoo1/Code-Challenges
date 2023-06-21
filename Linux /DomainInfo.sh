# Script Name:                 Domain Info
# Author:                       Eduardo Ayala
# Date of latest revision:      05/10/2023
# Purpose:                      Ask user for domain info

#Variable
$domain = Facebook.com

# Prompt user to enter a domain name
read -p "Facebook.com" domain

# Run whois command and display output
echo "WHOIS Lookup:"
whois $domain

# Run dig command and display output
echo "DIG Lookup:"
dig $domain

# Run host command and display output
echo "HOST Lookup:"
host $domain

# Run nslookup command and display output
echo "NSLOOKUP Lookup:"
nslookup $domain

echo "Facebook revealed"

