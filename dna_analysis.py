dna_sequence = "ATGCGTATCGGATCGATTACG"

sequence_length = len(dna_sequence)

nucleotide_counts = {"A": 0, "T": 0, "G": 0, "C": 0}

valid_bases = ["A", "T", "G", "C"]

for nucleotide in dna_sequence:
    if nucleotide in valid_bases:
        nucleotide_counts[nucleotide] += 1
    else:
        print(f"Invalid base found: {nucleotide}")

bases = list(nucleotide_counts.keys())
index = 0

while index < len(bases):
    nucleotide = bases[index]
    print(f"{nucleotide}: {nucleotide_counts[nucleotide]}")
    index += 1

def calculate_gc_content(sequence):
    gc_count = sequence.count("G") + sequence.count("C")
    gc_percentage = (gc_count / len(sequence)) * 100
    return gc_percentage

print(f"\nSequence Length: {sequence_length}")

gc_content = calculate_gc_content(dna_sequence)

print(f"GC Content: {gc_content:.2f}%")
