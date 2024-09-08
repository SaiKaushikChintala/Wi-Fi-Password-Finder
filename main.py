import subprocess
from typing import Optional, Dict
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QWidget, QListWidget, QListWidgetItem

class WifiApp(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle('Wi-Fi Profiles and Passwords')
        self.setGeometry(100, 100, 600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.profile_list = QListWidget()
        layout.addWidget(self.profile_list)

        self.load_button = QPushButton('Load Wi-Fi Profiles')
        self.load_button.clicked.connect(self.load_profiles)
        layout.addWidget(self.load_button)

        self.clear_button = QPushButton('Clear')
        self.clear_button.clicked.connect(self.clear_data)
        layout.addWidget(self.clear_button)

        self.result_label = QLabel('')
        layout.addWidget(self.result_label)

        self.profiles_data: Dict[str, Optional[str]] = {}

    def get_wifi_profiles(self) -> list[str]:
        try:
            result = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True, text=True)
            return [line.split(":")[1].strip() for line in result.stdout.splitlines() if "All User Profile" in line]
        except Exception as e:
            self.result_label.setText(f"Error retrieving Wi-Fi profiles: {e}")
            return []

    def get_wifi_password(self, profile_name: str) -> Optional[str]:
        try:
            result = subprocess.run(f'netsh wlan show profile "{profile_name}" key=clear | findstr "Key Content"', shell=True, capture_output=True, text=True)
            for line in result.stdout.splitlines():
                if "Key Content" in line:
                    return line.split(":")[1].strip()
            return "No password found or profile is open."
        except Exception as e:
            self.result_label.setText(f"Error retrieving password for {profile_name}: {e}")
            return None


    def load_profiles(self) -> None:
        profiles = self.get_wifi_profiles()
        if not profiles:
            self.result_label.setText("No Wi-Fi profiles found.")
            return

        self.profile_list.clear()
        self.profile_list.addItems(profiles)
        self.profile_list.itemClicked.connect(self.show_password)

    def show_password(self, item: QListWidgetItem) -> None:
        profile_name = item.text()
        password = self.get_wifi_password(profile_name)
        self.result_label.setText(f"Profile: {profile_name}\nPassword: {password}")

    def clear_data(self) -> None:
        self.profile_list.clear()
        self.result_label.setText('')

if __name__ == "__main__":
    app = QApplication([])
    window = WifiApp()
    window.show()
    app.exec()
