
# Backend Environment Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/jdxxmahmud/medico
```

### Step 2: Navigate to the Backend Directory
```bash
cd medico/backend
```

### Step 3: Create a Virtual Environment
```bash
python -m venv medico-env
```

### Step 4: Check/Add Virtual Environment to `.gitignore`
Check if `medico-env` is already in `.gitignore`. If not, add it manually:

Make sure you are in the **medico** directory.

```bash
echo "back-end/medico-env" >> .gitignore
```

### Step 5: Activate Virtual Environment

Make sure you are in the **back-end** directory.

On Windows:
```bash
.\medico-env\Scripts\activate
```
Using PowerShell:
```bash
.\medico-env\Scripts\activate.ps1
```
On macOS/Linux:
```bash
source medico-env/bin/activate
```

### Step 6: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 7: Run the Backend Server

Make sure you are in the **backend** directory

```bash
uvicorn src/main:app --reload
```

### Step 8: Create your Branch to Update using Git Bash
```bash
git branch {your_branch_name}
git checkout {your_branch_name}
```

Your backend environment for the Medico project is now set up and running.

You can access the backend API at [http://127.0.0.1:8000](http://127.0.0.1:8000).

To access the backend documentation, go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

### Additional Notes:
- Make sure to activate the virtual environment (`medico-env`) every time you work on the backend.
- For a clean environment, create a new virtual environment and repeat the installation steps.
- Always check the project's documentation for any updates or additional setup instructions.

Customize this documentation according to your specific project details and structure.


#### In this version, I've added section headings, improved formatting, and included hyperlinks with icons for better readability. Adjustments can be made based on your specific preferences or project needs.
