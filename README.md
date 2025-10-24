# Sign Synth

**Sign Synth** is an AR/VR accessibility project that translates spoken classroom language into expressive avatar gestures. Built with Unity and Python, it aims to support inclusive, multimodal communication for students who rely on visual cues or sign-based interaction.

This project focuses on mapping speech-to-text input to avatar animations using a modular gesture logic. It’s designed to be scalable, adaptable, and expressive — with a strong emphasis on real-world usability and emotional nuance.

## 🎯 Project Goals
- Enable real-time speech-to-sign translation in AR/VR environments
- Support expressive avatar gestures that go beyond basic signing
- Build a modular pipeline that can be extended to new phrases, emotions, and contexts
- Prioritize accessibility, clarity, and delight in user experience

## 🧠 Core Components
- `main.py`: Speech-to-text pipeline and gesture trigger logic
- `gesture_map.json`: Phrase-to-gesture mapping using fuzzy matching
- `Animations`: Contains Unity `.fbx` and `.anim` files (not uploaded due to GitHub size limits)
- `.gitignore`: Cleans up Unity and Python clutter for clean version control

## ⚠️ Note on Assets
Due to GitHub’s 100MB file limit, animation assets are not included in this repository. The `Animations` folder contains expressive gestures like wave, nod, jump, and shrug — all mapped to classroom phrases. These are available upon request or can be re-generated using Unity’s animation tools.

## 🛠️ How It Works
1. Speech input is transcribed using a Python-based STT pipeline
2. Transcribed phrases are matched against a gesture map
3. Matching gestures trigger Unity animations via socket or file-based communication
4. Avatar responds in real time with expressive, context-aware gestures

## 👩‍💻 Author
Created by [Sanvi Mahajan](https://github.com/Sanvi-Mahajan) 🦋

---

Want help adding a demo badge, GIF, or future roadmap section? I’ve got you whenever you’re ready. This README gives your project depth, clarity, and credibility — even without the heavy assets.
