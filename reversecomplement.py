# Print out Reverse Complement of DNA Sequence
import sys

COMPLEMENT_TABLE = {
    "A": "T",
    "G": "C",
    "C": "G",
    "T": "A",
}

# Open txt file & read as one string, stripping white space
dna_seq = open(sys.argv[1]).read().strip()
complement_seq: list = []

for nucleotide in dna_seq:
    if nucleotide in COMPLEMENT_TABLE.keys():
        complement_seq.append(COMPLEMENT_TABLE[nucleotide])
print("".join(complement_seq)[::-1])
