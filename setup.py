import os

os.system("sudo apt update && sudo apt install sudo apt-get install p7zip-full curl wget nginx git -y")
os.system("wget https://buildbot.libretro.com/stable/1.21.0/emscripten/RetroArch.7z")
os.system("7z x RetroArch.7z ")
os.system("git clone https://github.com/ppeccin/javatari.js")
os.system("sudo mkdir /var/www/html/retroarch")
os.system("sudo mkdir /var/www/html/javatari")
os.system("sudo cp -r Retroarch/retroarch/* /var/www/html/retroarch")
os.system("sudo cp -r javatari.js/release/stable/5.0/standalone/* /var/www/html/javatari")
os.system("wget not done yet")
