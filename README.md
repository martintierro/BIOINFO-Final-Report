# BIOINFO-Final-Report
By Martin Tierro, Jade Tan, Jarrett Singian, & Patricia Villaroman

This project contains python scripts for data manipulation that perform conversion from fasta to csv and random sampling. It also contains the programs used in performing phylogenetic analysis and BEAST analysis as part of our BIOINFO Final Report. 

# How to Run

Step 1 - Convert Fasta to CSV:
- 
- To convert your fasta file to csv, place your fasta file in the same directory as this README. Change the input filename and output filename to your liking in convertfastatocsv.py
- Run by opening a command terminal and entering '**py convertfastatocsv.py**'

Step 2 - Random Sampling:
- 
- Change the input filename, output filename, and sample size to your liking in csv_random_sampling.py
- Run by opening a command terminal and entering '**py csv_random_sampling.py**'

Step 3 - MUSCLE:
- 
- Open a command terminal and navigate to the Programs directory.
- Run by entering '**muscle.exe -in input.fasta -out output.fasta**'

Step 4 - IQTREE:
- 
- Place your input fasta file in the same directory as iqtree2.exe
- Run by entering '**iqtree2.exe -s example.phy -m GTR+F+I+G4**'

Step 5 - FigTree:
-
- Run FigTree v1.4.4.exe
- Open the treefile you wish to view

Step 6 - TempEst:
-
- Run TempEst v1.5.3.exe
- Open the treefile you wish to view
- Select best-fitting root and set function to "correlation" to maximize the correlation coefficient

Step 7 - BEAST:
-
- Run BEAUti v1.10.4.exe
- Import your input fasta file
- Change all settings to "exponential"
- Generate BEAST XML file
- Run BEAST v1.10.4.exe
- Import your generated BEAST XML file
- Select "Run"

Thanks for reading! 