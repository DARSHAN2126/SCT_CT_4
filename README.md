# SCT_CT_4
RECORD keylogger && keystrokes

---

# 📘 **Keystroke Logger (Safe Version)**

A simple and safe Python program that captures and logs keystrokes **only while the program window is active**.
This project is intended **only for educational** where demonstrating keystroke handling is required.

⚠️ **This is NOT a background/system-wide keylogger.**
It does **not** run hidden, does **not** capture sensitive data, and works only when the program is in focus.

---

## 🚀 Features

* Logs keystrokes in real-time
* Records timestamps for each key press
* Saves logs to a text file (`key_log.txt`)
* Stops on **ESC** key
* Clear and beginner-friendly code
* Safe and ethical key-capture implementation

---

## 📁 Project Structure

```
project-folder/
│
├── keylogger.py       # Main program with timestamp logging
└── key_log.txt        # Output log file (auto-created)
```

---

## 🛠️ Requirements

| Package    | Purpose                    |
| ---------- | -------------------------- |
| `keyboard` | Capturing keystroke events |

Install the required dependency:

```bash
pip install keyboard
```

> **Note:** On Linux, this module may require root permissions.

---

## 📌 Usage

Run the script:

```bash
python keylogger.py
```

You will see:

```
Keystroke Logger (Safe Version with Timestamp)
Logs keys only while this window is active.
Press ESC to stop.
```

Every key press will appear in the terminal **and** be stored in `key_log.txt`.

---

## 📝 Example Log Output

```
--- Logging started at 2025-12-04 20:34:11 ---
2025-12-04 20:34:15 - h
2025-12-04 20:34:15 - e
2025-12-04 20:34:16 - l
2025-12-04 20:34:16 - l
2025-12-04 20:34:17 - o
```

---

## 🔒 Ethics & Disclaimer

This project is intended **strictly for educational purposes**.
Do **not** use it to collect keystrokes without explicit permission.
Unauthorized keylogging is illegal and unethical.

---
