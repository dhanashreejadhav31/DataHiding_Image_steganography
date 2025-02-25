# DataHiding_Image_steganography

## **📌 Project Overview**
This Steganography Tool allows users to securely hide and retrieve **encrypted messages** within images using **Least Significant Bit (LSB) encoding** and **AES-based encryption**. The tool ensures **confidentiality and undetectability** while providing a **simple, user-friendly interface** through **Streamlit**.

---

## **🚀 Features**
- **Dual-Layer Security** – Combines **LSB steganography** with **AES encryption** for enhanced protection.  
- **Multi-Format Image Support** – Works with **PNG, JPG, JPEG, and BMP** images.  
- **User-Friendly UI** – Built with **Streamlit** for a seamless web-based experience.  
- **Lightweight & Fast** – Optimized for **high-speed encoding and decoding** without significant image quality loss.  
- **Privacy-Focused** – No data storage; all processing happens **locally** in memory.  
- **Easy Deployment** – One-click hosting on **Streamlit Cloud**.  

---

## **📂 Technology Stack**

### **Programming Language:**
- Python

### **Libraries Used:**
- **OpenCV (`cv2`)** → Image processing
- **NumPy** → Image data manipulation
- **Cryptography (`Fernet`)** → Message encryption & decryption
- **CustomTkinter** → GUI for local execution (alternative to Streamlit UI)
- **Streamlit** → Web-based UI for deployment

### **Deployment Platform:**
- **Streamlit Cloud** (for hosting the app)
- **GitHub** (for version control & deployment integration)

---

## **🎯 Target Audience (End Users)**
- **Cybersecurity Professionals** – Securely transmit sensitive information.
- **Law Enforcement & Intelligence Agencies** – Conceal classified data.
- **Businesses & Corporate Users** – Protect confidential information.
- **Ethical Hackers & Penetration Testers** – Analyze steganographic security.
- **Journalists & Activists** – Share sensitive data discreetly.
- **Privacy-Conscious Individuals** – Hide personal messages securely.

---

## **🛠 Installation & Usage**

### **1️⃣ Install Dependencies**
Ensure you have Python installed, then install the required libraries:
```bash
pip install -r requirements.txt
```

### **2️⃣ Run the Application Locally**
For **Streamlit UI**, run:
```bash
streamlit run steganography_app.py
```

For **Tkinter GUI**, run:
```bash
python steganography_app.py
```

---




## **🛠 Troubleshooting & Common Issues**
- **ModuleNotFoundError: No module named 'cv2'** → Ensure OpenCV is installed by running:
  ```bash
  pip install opencv-python-headless
  ```
- **ImportError on Streamlit Cloud** → Make sure `requirements.txt` is present and up to date in your repository.
- **Image Not Encoding Properly** → Ensure the image is in a supported format (`PNG, JPG, JPEG, BMP`).

---



