import random

# Numele fișierului sursă și al celui de ieșire
input_file = "chapter3_unshuffle.csv"
output_file = "chapter3.csv"

with open(input_file, "r", encoding="utf-8") as fin, open(output_file, "w", encoding="utf-8") as fout:
    for line in fin:
        parts = line.strip().split(";")
        
        if len(parts) != 5:
            continue  # Sărim peste liniile incorecte
        
        intrebare, raspA, raspB, raspC, corect = parts
        
        raspunsuri = [raspA, raspB, raspC]
        
        # Determinăm textul răspunsului corect
        text_corect = raspunsuri[ord(corect) - ord("A")]
        
        # Amestecăm răspunsurile
        random.shuffle(raspunsuri)
        
        # Determinăm noua literă a răspunsului corect
        new_correct_index = raspunsuri.index(text_corect)
        new_correct_letter = chr(ord("A") + new_correct_index)
        
        # Scriem linia în noul fișier
        fout.write(f"{intrebare};{raspunsuri[0]};{raspunsuri[1]};{raspunsuri[2]};{new_correct_letter}\n")

print("Amestecarea răspunsurilor s-a terminat. Verifică fișierul 'grile_shuffle.txt'.")
