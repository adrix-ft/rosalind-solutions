# Rosalind Solutions

My solutions to problems on [Rosalind](https://rosalind.info) — a platform for learning bioinformatics through problem solving.

Solving these problems to build algorithmic thinking for bioinformatics, strengthen Python skills, and prepare for GSoC and competitive research applications.

---

## Progress

![Problems Solved](https://img.shields.io/badge/Problems%20Solved-15+-brightgreen)
![Language](https://img.shields.io/badge/Language-Python-blue)
![Platform](https://img.shields.io/badge/Platform-Rosalind-orange)

---

## Problem List

| # | Problem ID | Problem Name | Topic | Solution |
|---|-----------|--------------|-------|----------|
| 1 | DNA | Counting DNA Nucleotides | String Algorithms | [solution](counting_dna_nucleotides.py) |
| 2 | RNA | Transcribing DNA into RNA | String Algorithms | [solution](transcribe_dna_into_rna.py) |
| 3 | REVC | Complementing a Strand of DNA | String Algorithms | [solution](complementing_a_strand_of_dna.py) |
| 4 | GC | Computing GC Content | String Algorithms | [solution](./GC.py) |
| 5 | HAMM | Counting Point Mutations | String Algorithms | [solution](./HAMM.py) |
| 6 | PROT | Translating RNA into Protein | Molecular Biology | [solution](./PROT.py) |
| 7 | SUBS | Finding a Motif in DNA | String Algorithms | [solution](./SUBS.py) |
| 8 | CONS | Consensus and Profile | String Algorithms | [solution](./CONS.py) |
| 9 | FIBD | Mortal Fibonacci Rabbits | Combinatorics | [solution](./FIBD.py) |
| 10 | GRPH | Overlap Graphs | Graphs | [solution](./GRPH.py) |

*Table updated as new solutions are added.*

---

## Structure

```
rosalind-solutions/
├── DNA.py          # Counting DNA Nucleotides
├── RNA.py          # Transcribing DNA into RNA
├── REVC.py         # Complementing a Strand of DNA
├── GC.py           # Computing GC Content
├── HAMM.py         # Counting Point Mutations
└── README.md
```

Each file is named after the official Rosalind problem ID. Solutions are written in Python 3 using standard libraries and Biopython where relevant.

---

## How to Run

Each solution is a standalone Python script. Clone the repo and run any solution directly:

```bash
git clone https://github.com/adrix-ft/rosalind-solutions
cd rosalind-solutions
python DNA.py
```

Most problems read input from the terminal or a hardcoded test string. Paste the Rosalind sample dataset when prompted.

---

## Topics Covered

- String Algorithms — nucleotide counting, motif finding, sequence alignment
- Molecular Biology — transcription, translation, codon tables
- Combinatorics — Fibonacci variants, probability
- Graphs — overlap graphs, de Bruijn graphs
- Dynamic Programming — edit distance, sequence alignment scoring

---

## Why Rosalind

Rosalind problems are directly relevant to real bioinformatics work. Problems like edit distance, sequence alignment, and graph traversal are the algorithmic foundations of tools like BLAST, BWA, and variant callers. Solving them builds the intuition to understand and eventually contribute to these tools.

This repo is also preparation for GSoC 2027 and PGEE (IIIT Hyderabad MS by Research entrance exam), both of which test algorithmic bioinformatics knowledge.

---

## Author

**Adarsh** 

BSc Bioinformatics — <!--Swami Vivekanand Subharti University-->

GitHub: [adrix-ft](https://github.com/adrix-ft)

ORCID: [0009-0002-7040-170X](https://orcid.org/0009-0002-7040-170X). 

---

## License

MIT License — free to use and adapt with attribution.
