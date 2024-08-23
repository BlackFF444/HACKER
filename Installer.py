import os
os.system("pkg install -y root-repo")
os.system("pkg install -y git tsu python wpa-supplicant pixiewps iw")
os.system("cd ..;git clone https://github.com/BlackFF444/HACKER")
os.system("cd ..;chmod +x HACKER/HACKER.py")
print("\033[1;34;40mThanks.\nInstallation Done.\nNow Go To Home Directory[~] And Enter This Command :\nsudo python HACKER/HACKER.py -i wlan0 -K")