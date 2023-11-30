import subprocess


def run_command(command):
    subprocess.run(command.split())


def install_dependencies():

    # Install Aireplay-ng,Airmon-ng,Airodump-ng
    run_command("sudo apt install aircrack-ng")

    # Install Gnome Terminal
    run_command("sudo apt install gnome-terminal")
    
    # Install Python
    run_command("sudo apt install python3")


# Install dependencies
install_dependencies()
