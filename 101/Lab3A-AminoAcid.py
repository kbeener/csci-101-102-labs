# Kristin Beener
# CSCI 101 - Section C
# Python Lab 3A

print('Input the chemical elements of the amino acid:')
carbon = int(input('CARBON>'))
hydrogen = int(input('HYDROGEN>'))
nitrogen = int(input('NITROGEN>'))
oxygen = int(input('OXYGEN>'))
sulfer = int(input('SULER>'))

if carbon == 3 and hydrogen == 7 and nitrogen == 1 and oxygen == 2 and sulfer == 0:
    amino_acid = 'Alanine'
    chem_eq = (f"C_{carbon}H_{hydrogen}N_{nitrogen}O_{oxygen}S_{sulfer}")
    print('The amino acid for', chem_eq , 'is', amino_acid)
    print('OUTPUT', chem_eq)
    print('OUTPUT', amino_acid)

elif carbon == 6 and hydrogen == 14 and nitrogen == 4 and oxygen == 2 and sulfer == 0:
    amino_acid = 'Arginine'
    chem_eq = (f"C_{carbon}H_{hydrogen}N_{nitrogen}O_{oxygen}S_{sulfer}")
    print('The amino acid for', chem_eq , 'is', amino_acid)
    print('OUTPUT', chem_eq)
    print('OUTPUT', amino_acid)

elif carbon == 4 and hydrogen == 8 and nitrogen == 2 and oxygen == 3 and sulfer == 0:
    amino_acid = 'Asparagine'
    chem_eq = (f"C_{carbon}H_{hydrogen}N_{nitrogen}O_{oxygen}S_{sulfer}")
    print('The amino acid for', chem_eq , 'is', amino_acid)
    print('OUTPUT', chem_eq)
    print('OUTPUT', amino_acid)

elif carbon == 3 and hydrogen == 7 and nitrogen == 1 and oxygen == 2 and sulfer == 1:
    amino_acid = 'Cysteine'
    chem_eq = (f"C_{carbon}H_{hydrogen}N_{nitrogen}O_{oxygen}S_{sulfer}")
    print('The amino acid for', chem_eq , 'is', amino_acid)
    print('OUTPUT', chem_eq)
    print('OUTPUT', amino_acid)

elif carbon == 6 and hydrogen == 9 and nitrogen == 3 and oxygen == 2 and sulfer == 0:
    amino_acid = 'Histidine'
    chem_eq = (f"C_{carbon}H_{hydrogen}N_{nitrogen}O_{oxygen}S_{sulfer}")
    print('The amino acid for', chem_eq , 'is', amino_acid)
    print('OUTPUT', chem_eq)
    print('OUTPUT', amino_acid)

elif carbon == 5 and hydrogen == 10 and nitrogen == 2 and oxygen == 3 and sulfer == 0:
    amino_acid = 'Glutamine'
    chem_eq = f"C_{carbon}H_{hydrogen}N_{nitrogen}O_{oxygen}S_{sulfer}"
    print('The amino acid for', chem_eq , 'is', amino_acid)
    print('OUTPUT', chem_eq)
    print('OUTPUT', amino_acid)


