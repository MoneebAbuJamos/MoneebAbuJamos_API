# Setup and Run Guide (API)

## Requirements

* Docker Desktop installed

---

## Model Download (Required)

Due to GitHub file size limitations, the model file is hosted externally.

Download the model from:
[https://drive.google.com/file/d/1Xbe2AemtB9VXkad8yXAlOc_OgM7damJK/view?usp=drive_link]

After downloading, place the model file in the following path inside the project:

Moneeb_API/models/qwen.gguf

Make sure:

* The file name is exactly: `qwen.gguf`
* The folder structure is correct (models folder must exist)

---

## Steps

1. Open terminal in the project root directory

2. Run:

docker compose up --build

3. Wait until the server starts

4. Open in browser:

http://localhost:8000/docs

---

## Verification

* Test `/chat` endpoint
* Test `/ocr` endpoint
* Test `/rag` endpoint

---

## Notes

* The system runs fully offline after placing the model file
* No internet connection is required during runtime
* All dependencies and models (except the main LLM file) are included locally
* Make sure Docker has enough memory allocated (recommended: 4GB+)

---

# ==================================================

# Additional Deployment Options (Section 3)

# ==================================================

## Model Setup for EXE Mode (Required)

For the executable version, the model must be placed inside the internal folder used by the packaged system.

After downloading the model, place it in:

deliverables/_internal/models/qwen.gguf

Steps:

1. Navigate to `deliverables`
2. Open `_internal`
3. Create a folder named `models` if it does not exist
4. Place the model file inside:

   _internal/models/qwen.gguf

Notes:

* The model file is NOT included in the repository due to size limitations
* The executable will not start correctly if the model is missing

---

## Additional Required File (Torch Dependency)

Due to GitHub size limitations, the following file is also not included in the repository:

torch_cpu.dll

Download it from:
[https://drive.google.com/file/d/1u1DsiuPRqhhTrSyAfsE6AdFroR6tXNBP/view?usp=drive_link]

After downloading, place it in the following path:

deliverables/_internal/torch/lib/torch_cpu.dll

Steps:

1. Navigate to `deliverables`
2. Open `_internal`
3. Go to `torch/lib`
4. Place the file inside:

   _internal/torch/lib/torch_cpu.dll

Notes:

* This file is required for the executable to run correctly
* The system will fail to start if this file is missing

---

## Option 1: Run using EXE (Recommended)

This option provides the easiest way to run the system in a fully offline Windows environment.

1. Navigate to:

deliverables/

2. Double-click:

run_api.exe

3. Wait a few seconds for the system to start (model loading may take time)

4. The browser will open automatically at:

http://127.0.0.1:8000/docs

---

## Option 2: Run using Batch File (Fallback)

If the executable does not run on the target machine:

1. Navigate to:

deliverables/

2. Double-click:

start.bat

3. The script will:

   * start the executable
   * wait until the server is ready (model fully loaded)
   * automatically open the browser

4. The system will open at:

http://127.0.0.1:8000/docs

---

## Notes for Deployment Options

* Both options run completely offline
* No Docker or Python installation is required for EXE mode
* All dependencies are bundled inside the executable
* The batch file waits for the server to be ready before opening the browser
* First startup may take a few seconds due to model loading