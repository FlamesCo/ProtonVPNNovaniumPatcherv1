## patch protonvpn and upgrade to visonary key

## bypas protonvpn and upgrade to visonary keya
protonvpn="/Applications/ProtonVPN.app"
print("Welcome to Novanium Proton Tech AG Patcher")
print("This script will patch protonvpn and upgrade to visonary key")
print("Please make sure you have the latest version of protonvpn and visonary key")
import os 
import sys
import time
import subprocess
print("Generating app license")
protonvpnapp="/Applications/ProtonVPN.app/Contents/MacOS/ProtonVPN/Login.nib"
## activate the license
os.system("defaults write com.protonvpn.mac.vpn.login LicenseActivated -bool true")

## generate the license key and save it to the protonvpn login
## make it so protonvpn thinks that the license is activated even on trial
os.systemargv = [protonvpnapp, "-generateLicenseKey".__contains__("P2PEnabled")]
os.system("defaults write com.protonvpn.mac.vpn.login LicenseActivated -bool true")

## disable protonvpn phone home
os.system("defaults write com.protonvpn.mac.vpn.license -bool true")

print("Adding plus plan")
sys.license = "ProtonVPN Plus"
print("Generating app license done")
sys.exit