def to_rna(dna_strand):
    rna_strand = []
    for char in dna_strand:
        if char in 'G':
            rna_strand.append('C')
        if char in 'C':
            rna_strand.append('G')
        if char in 'T':
            rna_strand.append('A')   
        if char in 'A':
            rna_strand.append('U')   
    return ''.join(rna_strand)    