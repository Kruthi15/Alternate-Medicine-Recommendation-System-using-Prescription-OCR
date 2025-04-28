Alternate Medicine Recommendation System using Prescription OCR
Project Overview
This project is a simple desktop application that helps users find similar alternate medicines based
on a prescription image.
It uses OCR (Optical Character Recognition) to read medicine names from a prescription photo and
suggests alternate medicines
with similar compositions and prices from a dataset.
How it Works
- User selects a prescription image (JPG, PNG, JPEG).
- The system reads the text using Tesseract OCR.
- It identifies medicine names from the text.
- For each medicine found, it suggests similar alternate medicines based on composition similarity.
- Results are displayed in a clean table (medicine name, composition, and price).
Tech Stack
- Python
- Pandas (for data handling)
- scikit-learn (for similarity finding)
- Tesseract OCR (for text extraction from images)
- Tkinter (for simple GUI)
Requirements
- Python 3.x
- Libraries:
- pandas
- scikit-learn
- pytesseract
- pillow
- tkinter
- Tesseract OCR installed on your machine
- Install Tesseract OCR: https://github.com/tesseract-ocr/tesseract
How to Run
1. Install the required Python libraries:
pip install pandas scikit-learn pytesseract pillow
2. Install Tesseract OCR and configure its path if needed in the code.
3. Download the medicine dataset: A_Z_medicines_dataset_of_India.csv
4. Run the Python script:
python alternate_medicine_finder.py
5. Click the "Select prescription image" button and choose your prescription image.
Notes
- The more clear and readable your prescription image is, the better the results.
- The system suggests up to 7 alternate medicines for each detected medicine.
- It works best with simple prescriptions. Handwritten prescriptions might need better OCR tuning.
Sample Output
- A new window shows similar medicines, their composition, and their prices neatly.
