# LLeMeTeach

LLeMeTeach is a Python-based tool designed to assist teachers and professors in creating lecture slides enhanced with interactive Manim videos. By integrating with Google's Gemini 1.5 Pro API, LLeMeTeach enables educators to generate visually engaging and conceptually clear instructional videos through their lecture modules.

## Features

- **Automatic Slide Generation**: LLeMeTeach takes key topics and dynamically generates slides with interactive animations.
- **Manim Video Integration**: Uses Manim to create animations that visualize complex concepts.
- **AI-Powered Customization**: Leveraging Gemini 1.5 Pro, it tailors visual explanations based on the input prompt and topic, enhancing student understanding.

## Installation

1. Clone the repository:
   git clone https://github.com/imbishal7/LLeMeTeach.git
   cd LLeMeTeach
2. Install the required libraries:
   pip install -r requirements.txt
3. Obtain a Gemini API key and save it securely. Save it in the environment variable GOOGLE_API_KEY.

## Usage
1. Run the following command in your terminal.
   streamlit run app.py
2. It will start a webserver where you can upload your course modules (PDF), and then within a few minutes, you will be able to download the slides.

# Contributing

We welcome contributions! If you have ideas to improve or expand LLeMeTeach, feel free to open an issue or submit a pull request.
