# 🧠✋ FingerMath – AI-Powered Gesture Calculator using OpenCV & MediaPipe


![image](https://github.com/user-attachments/assets/c2b73654-b5ef-4b5f-a386-584e24053bfc)


**FingerMath** is a real-time hand gesture-based calculator built using **OpenCV**, **MediaPipe**, and Python. This intuitive tool allows users to perform basic arithmetic operations like **Addition, Subtraction, Multiplication**, and **Division** using just their fingers — no physical input devices needed.

> 🚀 Developed by [Shanmugapriyan Jagadeeswaran](https://github.com/priyan-inspires)

---

## 🎯 Features

- 🖐️ Real-time hand detection using MediaPipe
- ✌️ Finger counting logic for both hands
- ➕➖✖️➗ Perform **ADD**, **SUB**, **MUL**, **DIV** operations using finger gestures
- 🧠 Smart interface using OpenCV GUI
- 🎮 Touchless operation selection using index fingertip pointing
- 🔁 Easy reset and exit functionality

---

## 🧪 Demo

##add linkedin page
---

## 🧰 Tech Stack

- **Python**
- **OpenCV** – for computer vision and GUI
- **MediaPipe** – for hand and finger landmark detection
- **NumPy** – for data processing

---

## 🖥️ How It Works

1. **Two hands** are detected via webcam.
2. User points the **index finger** to select an operation (`ADD`, `SUB`, `MUL`, `DIV`).
3. The number of fingers shown on **each hand** are taken as operands.
4. The result of the operation is shown on the screen.
5. Press `R` to reset or `ESC` to exit.

---

## 🛠️ Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/priyan-inspires/FingerMath.git
cd FingerMath

# 2. Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the project
python finger_math.py
⸻

🎓 Future Enhancements
	•	🔊 Add voice assistant feedback
	•	🔢 Display numbers as digits on screen (gesture-to-text)
	•	📱 Port to mobile using MediaPipe Lite
	•	📊 Add support for more complex mathematical operations
	•	🧠 Integrate with AI model for hand sign recognition

⸻

🙋‍♂️ Author

Made with 💻 by Shanmugapriyan Jagadeewaran 
📌 GitHub | LinkedIn
Priyan-inspires |  https://www.linkedin.com/shanmugapriyan-jagadeeswaran
⸻

⭐ Star This Repo

If you like this project, please give it a ⭐️! It motivates me to build more gesture-powered AI applications.

⸻

📜 License

MIT License. Feel free to use, modify, and distribute this project.
