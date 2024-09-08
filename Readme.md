# WiFinder

## Description

WiFinder is a desktop application that retrieves and displays saved Wi-Fi profiles and their corresponding passwords on Windows machines. Built using Python and PyQt, WiFinder provides a simple and intuitive user interface, allowing users to easily view the Wi-Fi networks their system has connected to and retrieve the saved passwords for these profiles.

## Features

- Display a list of all saved Wi-Fi profiles on the system.
- Retrieve and display the password for a selected Wi-Fi profile.
- Clear the profile list and reset the display area.
- Error handling for profiles without saved passwords or when no profiles are available.

## Technologies Used

- [Python](https://www.python.org/)
- [PyQt6](https://pypi.org/project/PyQt6/)
- [subprocess](https://docs.python.org/3/library/subprocess.html) (to interact with system commands)

## Usage

1. Install the required dependencies (`PyQt6`).
2. Run the application.
3. Click the "Load Wi-Fi Profiles" button to load all saved profiles.
4. Select a profile from the list to view its password.
5. Optionally, clear the list by clicking the "Clear" button.

## Example

1. Load saved Wi-Fi profiles.
2. Click a profile name to see its corresponding password.
3. The application will show the profile name and password in the display area.

## Requirements

- Python 3.x
- PyQt6
- Windows OS (since it uses `netsh` commands)
