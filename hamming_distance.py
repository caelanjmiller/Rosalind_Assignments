# Calculate Hamming Distance Between Two DNA Sequences
import itertools

seq_one: str = input("What is your first sequence?: ")
seq_two: str = input("What is your second sequence?: ")

hamming_distance: int = 0
for i,j in itertools.zip_longest(list(seq_one), list(seq_two)):
    if i != j:
        hamming_distance += 1
    else:
        hamming_distance += 0
print(f"Hamming Distance Between Sequence 1 & 2: {hamming_distance}")
