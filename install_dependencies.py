import subprocess


def run_command(command):
    subprocess.run(command.split())


def install_dependencies():
    # Install Airodump-ng
    run_command("sudo apt install aircrack-ng")

    # Install Airmon-ng
    run_command("sudo apt install aircrack-ng")

    # Install Aireplay-ng
    run_command("sudo apt install aircrack-ng")

    # Install Gnome Terminal
    run_command("sudo apt install gnome-terminal")


# Install dependencies
install_dependencies()
