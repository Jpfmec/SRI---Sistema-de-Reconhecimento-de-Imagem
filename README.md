#  SRI - Image Recognition System

> A Deep Learning-powered tool capable of classifying objects in images with high precision using the EfficientNet V2 architecture.

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white)
![Model](https://img.shields.io/badge/Model-EfficientNet%20V2%20(Large)-success)

##  Project Overview

The **SRI (Sistema de Reconhecimento de Imagem)** is a Python application that leverages state-of-the-art Convolutional Neural Networks (CNNs) to analyze and identify the content of images directly from the web.

The core of the project is built upon the **EfficientNet V2 Large** model, an architecture renowned for its efficiency and top-tier accuracy on the ImageNet dataset. This system was designed to be interactive, robust, and educational, demonstrating how to integrate pre-trained computer vision models into real-world applications.

### Key Features
* **URL Analysis:** Processes images directly from a web URL without requiring manual downloads.
* **Cutting-edge Deep Learning:** Utilizes the `EfficientNet_V2_L` model, outperforming classic architectures like ResNet50.
* **Detailed Feedback:** Provides the primary classification along with the AI's confidence score.
* **Robust Error Handling:** Implements a `try/except` system to prevent crashes when dealing with broken links or invalid file types.
* **Interactive CLI:** A user-friendly command-line interface with loop-based navigation.

##  Tech Stack

* **Language:** Python 3.12
* **AI Framework:** [PyTorch](https://pytorch.org/) & Torchvision
* **Image Processing:** PIL (Pillow)
* **Web Requests:** Requests

##  Getting Started

### Prerequisites
Ensure you have **Python 3.12** installed on your machine.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR-USERNAME/SRI-Image-Recognizer.git](https://github.com/YOUR-USERNAME/SRI-Image-Recognizer.git)
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Usage

Run the main script via terminal:
```bash
python main.py
