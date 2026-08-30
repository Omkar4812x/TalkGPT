# 🎙️ TalkGPT - Voice-Enabled ChatGPT Assistant

> **Hands-free Python voice assistant integrating SpeechRecognition, OpenAI GPT models, and pyttsx3 text-to-speech audio synthesis.**

---

## ✨ Features

- 🎙️ **Voice Speech Recognition**
  - Captures spoken voice input via system microphone using Google Speech Recognition (`SpeechRecognition`).
- 🧠 **OpenAI GPT Intelligence**
  - Connects to OpenAI API (`gpt-3.5-turbo` / `gpt-4o`) with automatic retry and quota handling.
- 🔊 **Text-To-Speech (TTS) Voice Feedback**
  - Synthesizes spoken audio responses using offline `pyttsx3` text-to-speech engine.

---

## 🛠️ Tech Stack

- **Language**: Python 3.10+
- **Voice / Audio**: `SpeechRecognition`, `pyttsx3`, `PyAudio`
- **AI Gateway**: OpenAI Python SDK, `python-dotenv`

---

## 🚀 Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Omkar4812x/TalkGPT.git
   cd TalkGPT
   ```

2. **Install dependencies**:
   ```bash
   pip install openai speechrecognition pyttsx3 pyaudio python-dotenv
   ```

3. **Set your OpenAI API Key**:
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Run Assistant**:
   ```bash
   python TalkGPT.py
   ```

---

## 📄 License

Distributed under the MIT License.
