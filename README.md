# 🚀 Detective Lens and Flask

Detective Lens is a web-based object detection system powered by YOLOv8 and Flask. It allows users to upload images, detect objects, and extract relevant information seamlessly.

## 📌 Features
- 🖼️ **Object Detection**: Detects objects in uploaded images using YOLOv8.
- 🔍 **Text Extraction**: Extracts text from images automatically.
- 🌐 **Web-Based Interface**: Simple and user-friendly Flask-powered UI.
- 🗂️ **Organized Output Storage**: Saves processed images with unique filenames to prevent overwriting.

## 🛠️ Technologies Used
- Python 🐍
- Flask 🌍
- OpenCV 🎥
- PyTorch 🔥
- YOLOv8 🎯

## 📂 Project Structure
```
Detective_Lens/
│── app.py                # Flask application
│── static/               # Static files (CSS, JS, Images)
│── templates/            # HTML templates
│── uploads/              # Uploaded images
│── results/              # Processed images with detections
│── model/                # YOLOv8 model files
│── requirements.txt      # Dependencies
│── README.md             # Project documentation
```

## 🚀 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/Detective_Lens.git
cd Detective_Lens
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Flask Application
```bash
python app.py
```

### 4️⃣ Access the Web App
Open your browser and go to:
```
http://127.0.0.1:5000/
```

## 🎯 Usage
1. Upload an image via the web interface.
2. The YOLOv8 model detects objects in the image.
3. Processed images are displayed and saved in the `results/` folder.


## 📜 License
This project is licensed under the MIT License.

---
🌟 **Star this repository if you found it useful!** 🌟

