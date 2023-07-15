# Given: A file containing at most 1000 lines
# Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines

filename = 'rosalind_ini5.txt'
with open(filename,'r') as file_object:
    print(''.join(file_object.readlines()[1::2]))
    