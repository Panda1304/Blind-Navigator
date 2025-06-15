# Blind Navigator AI

Blind Navigator AI is a browser‑based assistive tool that lets blind or visually‑impaired users understand their surroundings using only their device’s camera and audio output—no extra hardware required.

---

## Problem Statement

For people who are blind or visually impaired, moving around independently—especially in new or crowded places—can be really tough. Tools like walking sticks or guide dogs help, but they don’t tell you what exactly is around you. Imagine not knowing if there’s a staircase ahead, a cycle blocking your path, or a person suddenly walking towards you. It can be stressful and even dangerous.

This affects millions of people across the world, especially in places where advanced assistive devices are too expensive or not easily available. We wanted to work on something that actually helps real people and felt meaningful. That’s why we chose this problem.

With AI and computer vision becoming more accessible, we thought: why not use a phone’s camera to "see" the surroundings and describe them out loud? Our goal is to give visually impaired users more confidence and independence, just with their phone—no fancy hardware needed.

---
## Proposed Solution

We’re building a mobile-based AI assistant that helps visually impaired users understand their surroundings in real time. Using the phone’s camera, our app will detect nearby objects—like people, vehicles, stairs, or obstacles—using a pre-trained object detection model (YOLOv8). It then converts that visual information into simple, spoken descriptions using text-to-speech (TTS), so the user can hear what’s around them.

The goal is to make it feel like the phone is their "eyes that talk"—giving them real-time awareness without needing any expensive or extra hardware. It’s lightweight, runs locally, and is designed to be simple, fast, and genuinely helpful.


---

## Features

* **Object detection** with YOLOv8
* **Spatial awareness** (e.g., “person on your left”, “chair ahead”)
* **Text‑to‑speech narration** (online with gTTS or offline with pyttsx3)
* **Image & video upload** for offline analysis

---

## Tech Stack

| Layer            | Technology                                |
| ---------------- | ----------------------------------------- |
| Object detection | YOLOv8 (Ultralytics) + OpenCV             |
| Frame processing | OpenCV, NumPy                             |
| LLM Inference    | TinyLLaMA (via transformers or llama.cpp) |
| Speech synthesis | gTTS                                      |

---

## Quick Start

### 1. Clone & install

```bash
# 1. Clone the repo
$ git clone https://github.com/your‑handle/blind‑navigator‑ai.git
$ cd blind‑navigator‑ai

# 2. Create a virtualenv (optional but recommended)
$ python -m venv .venv && source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 3. Install dependencies
$ pip install -r requirements.txt
```

### 2. Run example script

```bash
$ python app.py  # or your CLI script if different
```

---

### Output
# Blind Navigator AI

Blind Navigator AI is a browser‑based assistive tool that lets blind or visually‑impaired users understand their surroundings using only their device’s camera and audio output—no extra hardware required.

---

## Problem Statement

Navigating unfamiliar or crowded places can be difficult and even dangerous for visually‑impaired people. Traditional aids like canes and guide dogs offer limited, short‑range feedback. Blind Navigator AI combines real‑time computer vision with natural language descriptions so users can “hear” what’s around them.

---

## Features

* **Object detection** with YOLOv8
* **Spatial awareness** (e.g., “person on your left”, “chair ahead”)
* **Text‑to‑speech narration** (online with gTTS or offline with pyttsx3)
* **Image & video upload** for offline analysis

---

## Tech Stack

| Layer            | Technology                                |
| ---------------- | ----------------------------------------- |
| Object detection | YOLOv8 (Ultralytics) + OpenCV             |
| Frame processing | OpenCV, NumPy                             |
| LLM Inference    | TinyLLaMA (via transformers or llama.cpp) |
| Speech synthesis | gTTS & pyttsx3                            |

---

## Quick Start

### 1. Clone & install

```bash
# 1. Clone the repo
$ git clone https://github.com/your‑handle/blind‑navigator‑ai.git
$ cd blind‑navigator‑ai

# 2. Create a virtualenv (optional but recommended)
$ python -m venv .venv && source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 3. Install dependencies
$ pip install -r requirements.txt
```

### 2. Run example script

```bash
$ python app.py  # or your CLI script if different
```

---
### Input and Output Image
![image](https://github.com/user-attachments/assets/030ed6d1-0ee2-4f13-8e84-8e65fbcff58b)
![image](https://github.com/user-attachments/assets/ded9106a-5ca4-4c7f-99a8-18cfcb350bf9)

### TTS Output - Speech will be heard
![image](https://github.com/user-attachments/assets/e2f6d09f-28f2-4300-b6ce-0225058b9315)

---

## Roadmap

* [ ] Add obstacle distance estimation with monocular depth ↑
* [ ] Support for multi‑language narration
* [ ] Mobile PWA wrapper for on‑the‑go use

---

## Contributing

Pull requests are welcome! Please open an issue first to discuss what you’d like to change.

1. Fork → clone → create a feature branch
2. Write clear, test‑covered code
3. Run `ruff` + `black` before committing
4. Open a PR

---


