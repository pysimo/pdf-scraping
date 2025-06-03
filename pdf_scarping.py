import pdfplumber
 

# URL del regolamento AnaCredit
path = "Anacredit.pdf"

#anacredit = pdf.open( path )

#page = anacredit.pages[26]

with pdfplumber.open(path) as pdf:
    page = pdf.pages[26]  # Pagina 27 = index 26

    # Estrai rettangoli (box)
    rects = page.rects
    print("Rettangoli:")
    for r in rects:
        print(r)

    # Estrai linee (frecce)
    lines = page.lines
    print("\nLinee:")
    for l in lines:
        print(l)

    # Estrai testo (per etichettare i box)
    words = page.extract_words()
    print("\nTesto nei box:")
    for w in words:
        print(w['text'], w['x0'], w['top'])


