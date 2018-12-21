# http://www.rcsb.org/pdb/download/download.do?doQueryIds=getchecked&qrid=83A59375&nocache=7670272

print('Start!')
Name = [line.rstrip() for line in open('Name.txt')]
name_length = len(Name)
#print(Name)

Details = [line.rstrip() for line in open('Details.txt')]
Protein = open('Protein.csv', 'w')

for i in range(0, name_length):
    # sequence_file = 'Sequence/' + str(Name[i]) + '_A.fasta.txt'
    sequence_file = 'Sequence/' + str(Name[i]) + '.fasta.txt'
    protein_sequence = [line.rstrip() for line in open(sequence_file)]
    sequence_length = len(protein_sequence)

    Protein.write(Name[i] + ', ')

    for j in (1, sequence_length-1):
        Sequence = protein_sequence[j]

        Protein.write(Sequence)

    Protein.write(', ' + Details[i] + '\n')

Protein.close()
print('Done!')