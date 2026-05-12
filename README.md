# 🔐 Cybersecurity Toolkit: Password Strength Checker
A professional-grade terminal utility for analyzing password security. Developed as part of my **Software Engineering** studies at **ASTU**.

## 🚀 Features
* **Real-time Analysis:** Checks length, complexity, and character variety.
* **Visual Feedback:** Professional banner and color-coded results (Strong/Medium/Weak).
* **Privacy-First:** All checks are performed locally in your terminal; no data is sent or stored.
* **System Integration:** Can be installed as a global command on **Kali Linux** and **macOS**.

---

## 🛠 Installation

### Option 1: The Fast Way (Global Command)
Run these commands in your terminal to install `abdi-check` as a native system tool:

```bash
curl -L [https://raw.githubusercontent.com/abdi-ba/password-checke/main/abdi.py](https://raw.githubusercontent.com/abdi-ba/password-checke/main/abdi.py) -o abdi-check
chmod +x abdi-check
sudo mv abdi-check /usr/local/bin/
