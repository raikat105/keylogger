# 🖥️ Advanced Keylogger Application

**Advanced Keylogger Application** is a Python-based tool designed to monitor and record keystrokes on a system. Developed for educational and research purposes, this application demonstrates how keylogging mechanisms operate, aiding in understanding system security and potential vulnerabilities.

> ⚠️ **Disclaimer:** This project is intended for educational and ethical research purposes only. Unauthorized use of keyloggers is illegal and unethical. Always obtain proper authorization before deploying such tools.

## 🧰 Tech Stack

- **Language:** Python 3
- **Libraries:** `pynput`, `cryptography`
- **Platform:** Cross-platform (Windows, Linux, macOS)

## 🚀 Features

- **Keystroke Logging:** Captures and records all keystrokes made by the user.
- **Encrypted Storage:** Utilizes the `cryptography` library to securely store logged data.
- **Stealth Operation:** Runs in the background without disrupting user activities.
- **Modular Design:** Easily extendable for additional features like email reporting or remote logging.

## 🛠️ Installation & Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/raikat105/keylogger.git
   cd keylogger
   ```

2. **Install dependencies:**

   Ensure you have Python 3 installed. Then, install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**

   ```bash
   python keylogger.py
   ```

   The keylogger will start running in the background, capturing keystrokes and storing them securely.

## 📁 Project Structure

```
keylogger/
├── keylogger.py
├── requirements.txt
└── README.md
```

- `keylogger.py`: Main script to initiate the keylogger.
- `requirements.txt`: Lists all Python dependencies.
- `README.md`: Project documentation.
- 
