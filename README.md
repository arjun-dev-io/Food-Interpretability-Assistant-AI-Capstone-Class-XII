# Food Label Interpretability Assistant

## How to Run the App

Follow the steps below to set up and run the application.

### Step 1 — Install Python

Install **Python 3.11** on your computer.

During installation, make sure you tick:

**☑ Add Python to PATH**

---

### Step 2 — Download the Project

Download this GitHub repository as a ZIP file.

1. Click **Code → Download ZIP** on the GitHub repository.
2. Extract the ZIP file to a location of your choice.
3. Open the extracted **Food-Label-Interpretability-Assistant** folder.

You should see:

```text
Food-Label-Interpretability-Assistant
│
├── app.py
├── README.md
├── requirements.txt
└── models
    └── nova_classifier.joblib
```

**`README.md` contains these instructions.** It can also be viewed directly on the GitHub repository page.

**Do not move or rename the `models` folder or `nova_classifier.joblib`.**

---

### Step 3 — Open Command Prompt in the Project Folder

Make sure Command Prompt is opened **from inside the `Food-Label-Interpretability-Assistant` folder**.

The easiest way is to open the project folder in File Explorer, select the address bar, type `cmd`, and press **Enter**.

The Command Prompt should open with the project folder as its current location.

---

### Step 4 — Install the Required Packages

In Command Prompt, run:

```text
py -3.11 -m pip install -r requirements.txt
```

Press **Enter** and wait for the installation to finish.

**This only needs to be done once.**

---

### Step 5 — Start the App

After the installation is complete, run:

```text
py -3.11 -m streamlit run app.py
```

Press **Enter**.

The application should open automatically in your web browser.

If it does not, Command Prompt will display a local address similar to:

```text
http://localhost:8501
```

Open that address in your browser.

---

## Using the App

Once the app opens:

1. Enter the **product name**.
2. Enter the nutritional values from the food package.
3. Make sure the values are **per 100 g or 100 ml**.
4. Click **Analyze Product**.
5. The app will display the predicted NOVA group, confidence, explanation, and other results.

---

## Important

Keep the project structure unchanged:

```text
Food-Label-Interpretability-Assistant
│
├── app.py
├── README.md
├── requirements.txt
└── models
    └── nova_classifier.joblib
```

Do **not** delete, rename, or move `nova_classifier.joblib`.

### To close the app

Return to the Command Prompt window running the application and press:

```text
Ctrl + C
```

---

## If Something Goes Wrong

If you encounter an error, take a screenshot of the Command Prompt showing the error and send it to the project coder.
