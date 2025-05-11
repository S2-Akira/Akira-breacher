# Akira Breacher v4.0
**A powerful, multi-target brute force tool with GUI and support for SSH, FTP, and HTTP basic authentication.**

## Description

Akira Breacher is a versatile brute force tool designed for penetration testing and security auditing. With a modern and intuitive graphical user interface (GUI) built using `Tkinter`, it allows users to perform brute force attacks on various protocols such as **SSH**, **FTP**, and **HTTP Basic Authentication**. The tool features **dark mode**, an **AI-powered guess mode**, and can be customized to fit different attack scenarios.

This project is for educational and research purposes only. Use it responsibly and only with permission.

## Features
- **GUI Interface**: A user-friendly interface for performing brute-force attacks.
- **Multi-Protocol Support**: SSH, FTP, and HTTP Basic Authentication.
- **Dark Mode**: Toggle between light and dark themes for better visibility.
- **AI Mode**: Option to enable AI-powered password guessing.
- **Password Generation**: Generate passwords based on charset and max length.
- **Real-time Logging**: View attack results and status in real-time.

## Requirements

To run Akira Breacher, you will need the following:

- **Python 3.x**
- **Tkinter** (for GUI)
- **Paramiko** (for SSH)
- **Requests** (for HTTP)
- **ftplib** (for FTP)

You can install the required dependencies with:

```bash
pip install paramiko requests
Installation
Clone this repository to your local machine:

bash
Copy
Edit
git clone https://github.com/S2-Akira/akira-breacher.git
Navigate into the project directory:

bash
Copy
Edit
cd akira-breacher
Install the necessary Python dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the application:

bash
Copy
Edit
python akira_breacher.py
Usage
Start the Tool: When the application is launched, you will be presented with tabs for different attack modes: SSH Brute, FTP Brute, and HTTP Basic Auth.

Enter Attack Parameters:

Target Host/IP: The IP address or hostname of the target system.

Port: The port to connect to (default is 22 for SSH and 21 for FTP).

Username: The username to brute force.

Charset: The character set used to generate passwords (default includes lowercase, uppercase, digits, and special characters).

Max Length: The maximum password length to generate.

Enable AI Mode: Optionally enable the AI-powered guess mode to attempt more intelligent password guesses.

Start Attack: Press the "Start Attack" button to initiate the brute force attack. The progress and results will be displayed in the output window.

Stop Attack: Press the "Stop" button to halt the attack at any time.

Screenshot

Contributing
If you'd like to contribute to the project, feel free to fork the repository, submit a pull request, or report any issues. Contributions are always welcome!

Steps to contribute:
Fork the repository

Create a new branch (git checkout -b feature-name)

Commit your changes (git commit -am 'Add new feature')

Push to the branch (git push origin feature-name)

Open a pull request

License
This project is licensed under the MIT License - see the LICENSE file for details.

Disclaimer
Akira Breacher is designed for educational purposes only. Unauthorized use of this tool can lead to severe consequences, including legal action. Only use this tool on systems you own or have explicit permission to test.

Created by S2-Akira
GitHub: https://github.com/S2-Akira
