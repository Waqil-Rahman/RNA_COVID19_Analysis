# Analysis on DNA to test for COVID-19 
## RNA_COVID19_Anaylsis

This project is an investigation on the genetic structure of SARS-CoV-2, the coronavirus that is causing the COVID-19 pandemic (or, at least, the original variant as it emerged in Wuhan). In particular, we are going to analyse in some detail a so-called DNA nucleotide sequence.

So what is this? DNA stands for desoxyribonucleic acid. SARS-CoV-2 coronavirus is what is called a RNA (ribonucleic acid) virus, meaning that the genetic material of the virus is essentially simply a single strand of RNA, i.e. a long RNA chain. Both DNA and RNA are assembled as a chain of 'nucleotides', organic molecules which usually are symbolized as letters: Adenine ('A'), Cytosine ('C'), Guanine ('G'), Thymine ('T') (in RNA Uracil 'U' is found instead of Thymine). A sequence of nucleotides is therefore a sequence of letters, for instance CATCGATCAGTAGAGTTTAC... In a nutshell, the genetic material of the virus can be described as a long sequence of these four letters.

The story is more intricate, this is a project on computational virology in collabartion with [Bart's and The London School of Medicine and Dentistry](https://www.qmul.ac.uk/fmd/).

 The starting point of the project is to consider a DNA sequence. For those of you that don't have any interest in genetics, you can simply assume that the starting point is to consider a very long sequence of letters, where each letter is extracted from an alphabet of four letters (A,C,G,T).
 
This project consists in four parts. In each of the parts it will code up some specific functions, run some codes.

- The first part is about loading data. This data is just a file that depicts a very long 4-letter sequence of DNA nucleotides, something like ATATCGTAGCTAT... This letter sequence characterises the virus genetic material. From now on we will call this the virus sequence.
- The second part is about some basic manipulation and visualisation of the virus sequence.
- The third part is about computing some statistics of this sequence and do some additional visualisation.

Reference: [Wu, F., Zhao, S., Yu, B. et al. A new coronavirus associated with human respiratory disease in China. Nature 579, 265–269 (2020)](https://www.nature.com/articles/s41586-020-2008-3)
