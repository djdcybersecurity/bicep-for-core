# 🩺 Audio to SOAP Note – Clinical Automation Pipeline

This project automates the conversion of clinical audio recordings into structured SOAP notes using a Whisper transcription model and a Language Learning Model (LLM) via OU's LiteLLM proxy.

---

## ⚙️ Setup (Ubuntu 22.04)

1. **Create & activate Python virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate



Install dependencies

pip install -r requirements.txt


Create a .env file
Add the following to a file named .env in your project root:

OPENAI_API_KEY=your_litellm_key_here
OPENAI_BASE_URL=https://litellm.lib.ou.edu
OPENAI_MODEL=amazon.nova-lite-v1:0

🎯 Usage

Run the following command to transcribe audio and generate a SOAP note:

python audio_to_soap.py --audio audio/<your_audio_file>.wav --output-dir results/


Example:

python audio_to_soap.py --audio audio/017af3f5-d145-41a2-95a4-5acfa0f1bd06.wav --output-dir results/


The output will be saved as a JSON file (e.g., case001_soap.json) in the results/ folder.

📁 Project Structure
├── audio/              # Input .wav files
├── results/            # Transcription and SOAP note outputs
├── src/                # Core logic modules
├── audio_to_soap.py    # Entry point to run the pipeline
├── list_models.py      # Utility to test LLM access
├── whisper_test.py     # Whisper-only transcriber
├── .gitignore          # Excludes .env and venv
├── README.md           # This file

🧠 How It Works

Transcribes audio using OpenAI Whisper.

Processes transcription using a selected LLM via LiteLLM.

Outputs a structured SOAP (Subjective, Objective, Assessment, Plan) note in JSON format.

🛡️ Notes

.env and venv/ are excluded from version control using .gitignore.

Tested on Ubuntu 22.04 in an Azure VM with Python 3.12.

Ensure your API key from litellm.lib.ou.edu
 is active and has model access.

📫 Feedback / Issues

If something breaks, check:

Whisper CPU/FP16 warnings

API key permissions on LiteLLM

Model selection is correct in .env

Or open an issue here or on GitHub
.


---


