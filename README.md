# 🚀 DocDiff AI

An interactive Gradio tool for comparing text files with a built-in OpenAI API key validation script.  

## 📌 Overview  

This project provides two main utilities:  

1. **Document Comparator Tool (`app.py`)**  
   - Upload two text files.  
   - View detailed differences (unified diff).  
   - Get a concise, locally-generated summary of additions and deletions.  

2. **API Key Tester (`test_api_key.py`)**  
   - Quickly check if your OpenAI API key is valid.  
   - Uses `dotenv` to securely load environment variables.  

## ✨ Features  

- 📂 Compare two text files and highlight differences.  
- ✍️ Summarize changes (additions & deletions) automatically.  
- 🖥️ User-friendly Gradio interface.  
- 🔑 Validate your OpenAI API key in seconds.  


## 📂 Project Structure  
```
DocDiff-AI-
├── app.py # Gradio app: Document Comparator Tool
├── dataset1.csv # Sample dataset (not used directly in app.py)
├── file1.txt # Example input file for testing
├── file2.txt # Example input file for testing
├── pyvenv.cfg.txt # Virtual environment config (can be ignored)
├── requirements.txt # Python dependencies
└── test_api_key.py # Script to test OpenAI API key validity
```

## ⚙️ Installation  
1. **Clone the repository**  
```
git clone https://github.com/bharghavi007/docdiff-ai.git
cd docdiff-ai
```
2. **(Optional) Create a virtual environment**
```
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```
3. **Install dependencies**
```
pip install -r requirements.txt
```
## ▶️ Usage
1. Run the Document Comparator Tool
```
python app.py
```
- Open the Gradio link in your browser.
- Upload two .txt files.
- View detailed differences and a summary.

2. Test Your OpenAI API Key
- Create a .env file in the project root:
```
OPENAI_API_KEY=your_api_key_here
```
- Run:
```
python test_api_key.py
```
If the key is valid, you’ll see a small response printed.


## 🤝 Contributing

Contributions are welcome! Please fork this repo, create a new branch, and submit a pull request.

## 📜 License

This project is licensed under the MIT License