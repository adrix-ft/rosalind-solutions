dna = "your dna sequence".lower()
reverse_dna = dna[::-1]
translation_table = str.maketrans("actg", "tgac")
complimentory = reverse_dna.translate(translation_table)
print(complimentory.upper())
