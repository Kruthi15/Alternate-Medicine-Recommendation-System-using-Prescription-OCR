import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import CountVectorizer
import pytesseract
from PIL import Image
import warnings
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk  

def preprocessing(compositions):
    vectorizer = CountVectorizer()
    x = vectorizer.fit_transform(compositions)
    return x, vectorizer

def train(x):
    model = NearestNeighbors(n_neighbors=7, metric='euclidean')
    model.fit(x)
    return model

def predict(db, vectorizer, model, med, compositions):
    med = med.lower()
    index = db[db['name'].str.lower() == med].index
    if len(index) == 0:
        return []
    index = index[0]
    composition = compositions[index]
    composition_vector = vectorizer.transform([composition])
    distance, index = model.kneighbors(composition_vector)
    similarMeds = [(db['name'][i], db['price(₹)'][i]) for i in index[0]]
    return similarMeds

def browse_image():
    imagepath = filedialog.askopenfilename(title="Select Prescription", filetypes=(("Image files", "*.png *.jpg *.jpeg"), ("All files", "*.*")))
    if imagepath:
        process_image(imagepath)


def process_image(imagepath):
    image = Image.open(imagepath)
    ocr_text = pytesseract.image_to_string(image)
    lines = ocr_text.split('\n')
    for line in lines[:-1]:
        inp = line.lower()
        valid_words = []
        for word in inp.split():
            if db['name'].str.lower().str.contains(word).any():
                valid_words.append(word)
        if valid_words:
            inp = ' '.join(valid_words)
            similarMeds = predict(db, vectorizer, model, inp, compositions)
            display_result(inp, similarMeds)

def display_result(input_text, similar_meds):
    result_window = tk.Toplevel(root)
    result_window.title("Similar medicines for " + input_text)
    tree = ttk.Treeview(result_window, columns=("Medicine", "Composition", "Price"))
    tree.heading("#0", text="Medicine")
    tree.heading("#1", text="Composition")
    tree.heading("#2", text="Price")
    for name, price in similar_meds:
        composition1 = db.loc[db['name'] == name, 'short_composition1'].values[0]
        composition2 = db.loc[db['name'] == name, 'short_composition2'].values[0]
        tree.insert("", "end", text=name, values=(composition1 + ' ' + composition2, "₹ " + str(price)))
    tree.pack(expand=True, fill=tk.BOTH)

if __name__ == "__main__": 
    dbpath = '/Users/Sidhanth/Desktop/ML/A_Z_medicines_dataset_of_India.csv'
    warnings.filterwarnings("ignore")
    db = pd.read_csv(dbpath)
    db.fillna('', inplace=True)
    compositions = db['short_composition1'] + ' ' + db['short_composition2']
    x, vectorizer = preprocessing(compositions)
    model = train(x)

    root = tk.Tk()
    root.title("Similar medicine finder")
    root.geometry("250x50")

    browse_button = tk.Button(root, text="Select prescription image", command=browse_image)
    browse_button.pack()

    root.mainloop()
