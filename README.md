# SCT_CT_4
keylogger


#  Keyboard Input Logger (Educational Use Only)

This project demonstrates how to capture and log keyboard input **safely and ethically** for educational purposes.
The program records keystrokes **only within the application itself**, not system-wide, and saves them to a log file.

> ⚠️ **Disclaimer:**
> This project is strictly for learning keyboard event handling and should **NOT** be used for creating malicious keyloggers.
> Always ensure user consent and follow all legal and ethical guidelines.

---

## 📌 Features

* Logs keys pressed during program execution
* Stores each key in a text file (`input_log.txt`)
* Runs transparently (no background or hidden behavior)
* Intended for learning keyboard event handling in Python

---

## 📂 Project Structure

```
├── input_log.txt        # File where keys are saved
├── key_input_logger.py  # Main program
└── README.md            # Project documentation
```

---

## 🛠️ Technologies Used

* **Python 3.x**
* **keyboard** library for key event capture

---

## ▶️ How to Run the Program

### 1. Install dependencies

```bash
pip install keyboard
```

### 2. Run the script

```bash
python key_input_logger.py
```

### 3. Start typing

Every key you press **within the running program** will be logged to `input_log.txt`.

Stop the program anytime using:

```
Ctrl + C
```


## ⚠️ Ethical Use

This program:

* Does **NOT** run in the background
* Does **NOT** capture system-wide keystrokes
* Does **NOT** store sensitive information
* Is strictly for **learning purposes**

Misuse of keylogging tools can violate privacy laws.

---
