# codons ![](https://travis-ci.org/ibrahawari/codons.svg?branch=master)


Synonymous codons are distinct 3‐nucleotide codons that code for the same amino acid. While synonymous codons are used interchangeably, they are not used equally frequently within coding regions of the genome. This Python program analyzes the codon usage in the human genome based on a sampling of RNA transcript sequences.  Each transcript sequence must be provided in a file following FASTA format. The nucleotide position in the file of the start codon must be provided as well. The program accepts one or more file name and start position pairs. The output of the program is a list of the 20 amino acids and "Stp". For each amino acid, it lists the synonymous codons, and the number of times it was
seen within the supplied coding sequences, and the percent utilization of this codon among all its synonymous codons. 

An example of four mRNA transcripts is provided: insulin (60), hemoglobinB (51), rhodopsin (96), and collagen1 (127).  

Try running the following command as a demo:

    python codons.py insulin.fa 60 hemoglobinB.fa 51 rhodopsin.fa 96 collagen1.fa 127
