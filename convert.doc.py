import img2pdf
import os
import tkinter as tk
from tkinter import filedialog

def convert_png_to_pdf(png_file, pdf_file):
    with open(png_file, "rb") as file:
        img_bytes = file.read()

    pdf_bytes = img2pdf.convert(img_bytes)

    with open(pdf_file, "wb") as file:
        file.write(pdf_bytes)

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    png_file = filedialog.askopenfilename(title='Select PNG file', filetypes=[('PNG Files', '*.png')])
    if not png_file:
        print("No file selected.")
        return

    if not os.path.isfile(png_file):
        print(f"The file {png_file} does not exist.")
        return

    pdf_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[('PDF Files', '*.pdf')])

    convert_png_to_pdf(png_file, pdf_file)

if __name__ == "__main__":
    main()

    print("Conversion complete.")
