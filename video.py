import pdfplumber as pdf
import matplotlib.pyplot as plt
from collections import Counter
import io

# URL del regolamento AnaCredit
path = "Anacredit.pdf"

anacredit = pdf.open( path )

page = anacredit.pages[26]

print( page.extract_table( ) )

filtered_page = [char for char in page.chars if char.get("x0") > 181.0 ]
filtered_page = [char for char in filtered_page if char.get("tag") != 'Artifact']
#print( page.extract_words() )
#print( len(filtered_page) )
for i in filtered_page: #page.chars[2200:2250]:
    #print( i['text'] , end="")
    #print(i)
    pass 

print( '-------------------------------' )
for table in page.extract_table( ):
    for row in table:
        print( row ) 

"""# Lista per raccogliere tutte le dimensioni dei caratteri
sizes = []

for char in filtered_page:
        sizes.append( round(char["size"], 2) )  # arrotonda a 0.1 p


# Conta le occorrenze di ogni dimensione
size_counts = Counter(sizes)

# Stampa ordinate per dimensione
for size, count in sorted(size_counts.items()):
    print(f"Size: {size:>4} pt -> {count} caratteri")

# --- Plotta l'istogramma ---
plt.figure(figsize=(10, 6))
plt.hist(sizes, bins=30, color="steelblue", edgecolor="black")
plt.title("Distribuzione delle dimensioni dei caratteri nel PDF")
plt.xlabel("Dimensione (pt)")
plt.ylabel("Frequenza")
plt.grid(True)
plt.tight_layout()
plt.show()

anacredit.close()"""