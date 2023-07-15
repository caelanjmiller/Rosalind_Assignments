# Output GC of FASTA DNA Sequence
from Bio import SeqIO
from Bio.Seq import Seq

def fasta_to_Seq_conversion(FASTA: str) -> Seq:
    """ Convert FASTA Files to Seq objects"""
    sequence_objects_array = []
    for sequence_record in SeqIO.parse(FASTA, 'fasta'):
        sequence_objects_array.append(sequence_record)
    return sequence_objects_array


def gc_content_calculator(FASTA: str, ) -> str:
    sequence_objects_array = fasta_to_Seq_conversion(FASTA)
    id_names_array = []
    gc_content_num = []
    for sequence in sequence_objects_array:
        gc_content_counter = 0
        id_name = sequence.id
        id_names_array.append(id_name)
        sequence_array = list(sequence.seq)
        for nucleotide in sequence_array:
            match(nucleotide):
                case 'G' | 'C':
                    gc_content_counter += 1
        gc_percent = (gc_content_counter / len(sequence.seq) * 100)
        gc_content_num.append(gc_percent)
        gc_dict = dict(zip(id_names_array, gc_content_num))
        for id, gc_count in gc_dict.items():
            highest_gc_content = 
    return (
        
    ) 

rosalind = gc_content_calculator('rosalind.fasta')
print(rosalind)