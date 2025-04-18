from pypdf import PdfReader

def main():
    filename = input("Enter the filename: ")
    pdftext_singlepage(filename)

def pdftext_singlepage(filename):
    inputfile = PdfReader(filename)
    totalpages = len(inputfile.pages)
    page = inputfile.pages[1]
    text = page.extract_text()

    print(f"Total pages: {totalpages}\nText:\n{text}")

if __name__ == "__main__":
    main()