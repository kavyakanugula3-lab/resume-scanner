import PyPDF2
import re

# Open the resume PDF
file = open("kavya_resume.pdf", "rb")
reader = PyPDF2.PdfReader(file)

text = ""

# Read all pages
for page in reader.pages:
    text += page.extract_text()

file.close()

print("----- Resume Text -----")
print(text)

email = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print("\nEmail Found:")
print(email)

phone = re.findall(r"\b\d{10}\b", text)
print("\nPhone Number Found:")
print(phone)

resume_text = re.sub(r'[^a-zA-Z]', '', text)
resume_text = resume_text.lower()

skills_list = [
    "python", "html", "css", "javascript",
    "django", "numpy", "pandas", "bootstrap",
    "mysql","react js"
]

found_skills = []
missing_skills = []

for skill in skills_list:
    if skill in resume_text:
        found_skills.append(skill.capitalize())
    else:
        missing_skills.append(skill.capitalize())

print("\nSkills Found:")
print(found_skills)

print("\nSkills Missing:")
print(missing_skills)

