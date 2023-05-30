# Before using the program, ensure that you have the following dependencies installed:

- Airodump-ng: Airodump-ng is a wireless packet capture tool that will be used to capture handshake packets. Install it by following the instructions provided by the Aircrack-ng project.
- Airmon-ng: Airmon-ng is a script used for switching wireless network interfaces to monitor mode. Install it by following the instructions provided by the Aircrack-ng project.
- Aireplay-ng: Aireplay-ng is a wireless packet injection tool that can be used to force handshake packet generation. Install it by following the instructions provided by the Aircrack-ng project.
- Gnome Terminal: Gnome Terminal is the default terminal emulator for the GNOME desktop environment. It is required for running the program and executing the necessary commands.
- Python: Python is the programming language used for the development of the Handshake Acquisition and Decoding Program. Install Python by following the instructions provided by the official Python website.
- WiFi Adapter with Monitor Mode: To capture handshake packets, you need a WiFi adapter that supports monitor mode. Refer to the documentation of your WiFi adapter to enable monitor mode.

# What this script DO?

## This script automatically disconnects devices from a Wi-Fi network and captures the handshake packets for further analysis

- The script will display wireless network information using the iwconfig command.

- It will then kill any interfering processes using the sudo airmon-ng check kill command.

- Enter the interface name when prompted. This is the name of your Wi-Fi interface, such as wlan0 or eth0.

- Enter the filename when prompted. This is the name you want to give to the file where the handshake packets will be captured.

- The script will run sudo airodump-ng on the specified interface, displaying available networks. Note down the BSSID and channel of the network you want to capture the handshake for.

- Enter the desired BSSID and channel when prompted.

- The script will start capturing the handshake packets in a separate thread using sudo airodump-ng.

- A new terminal window will open, running the deauthentication command using sudo aireplay-ng. This command will send deauthentication packets to the target network to force clients to reconnect and generate handshake packets.

- While the handshake capture is in progress, you can wait for the desired amount of time to capture enough packets. Once done, press "Stop" in the terminal where the script is running.

- The script will stop the monitor mode on the specified interface using sudo airmon-ng stop and display the message "Monitor mode isključen" (Monitor mode disabled).
# After capturing the handshake packets, you can use a decryption script to decrypt the captured data and retrieve the Wi-Fi network password.
- sudo aircrack-ng filename-01.cap -w /usr/share/wordlists/rockyou.txt
# Which adapters support
- https://deviwiki.com/wiki/List_of_Wireless_Adapters_That_Support_Monitor_Mode_and_Packet_Injection


