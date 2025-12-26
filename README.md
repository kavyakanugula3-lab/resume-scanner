-# Resume Scanner
## 1. Project Overview
This project is a Python-based Resume Scanner that extracts text from PDF resumes and verifies whether all required technical skills,email ,and mobile number are present. The application cleans and normalizes resume content to handle PDF formatting issues and performs rule-based skill validation. This project helps in understanding file handling, text processing, and basic resume screening logic.
## 2. Features
* Extracts text from PDF resume files
* Clean and normalizes resume content for accurate matching
* Validates wheather all required technical skills are present
* Displays found skills and missing skills clearly
* Confirms skill matching result using rule-based logic
## Technologies Used
- python
- pyPDF2(for PDF text extraction)
- Regular Expressionns(for text cleaning and skill matching)
## Project Structure
resume-scanner/
|--kavya_resume.pdf
|--resume_scanner.py
|--README.md
## How to Run
1. install the required library:pip install pyPDF2
2. place  your resume PDF in the project folder and name it 'resume.pdf'
3. Run the program:py resume_scanner.py
## Sample Output

Email Found:
['kavyakanugula3@gmail.com']

Phone Number Found:
['6300458539']

Skills Found:
['Python', 'Html', 'Css', 'Javascript', 'Django', 'Numpy', 'Pandas', 'Bootstrap', 'Mysql']
Skills Missing:
['React js']

  
