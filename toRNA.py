# Transcribe DNA into an RNA Strand

filename = 'rosalind_rna.txt'
with open(filename, 'r') as file_object:
    rna_sequence = []
    dna_sequence = file_object.read().rstrip()
    dna_list = list(dna_sequence)
    for nucleotide in dna_list:
        match(nucleotide):
            case 'A': 
                rna_sequence.append('A')
            case 'T':
                rna_sequence.append('U')
            case 'C':
                rna_sequence.append('C')
            case 'G':
                rna_sequence.append('G')
    rna_sequence = ''.join(rna_sequence)
    print(f'Transcribed RNA: {rna_sequence}')
    file_object.close()
