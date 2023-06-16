# Define the user information
$firstName = "Franz"
$lastName = "Ferdinand"
$jobTitle = "TPS Reporting Lead"
$department = "TPS Department"
$company = "GlobeX USA"
$officeLocation = "Springfield, OR"
$email = "ferdi@GlobeXpower.com"
$username = "ferdi"

# Define the Active Directory parameters
$adUserParams = @{
    GivenName = $firstName
    Surname = $lastName
    Title = $jobTitle
    Department = $department
    Company = $company
    Office = $officeLocation
    SamAccountName = $username
    UserPrincipalName = "$username@yourdomain.com"
    Name = "$lastName, $firstName"
    EmailAddress = $email
    Enabled = $true
    PasswordNeverExpires = $true
    AccountPassword = (ConvertTo-SecureString -String "Password123" -AsPlainText -Force)  # Set the desired password
}

# Create the user in Active Directory
New-ADUser @adUserParams -PassThru

# Output the created user details
Write-Host "User '$firstName $lastName' has been created in Active Directory."