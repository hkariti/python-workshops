def count_cis(bins_pairs, chromosomes):
    counter = 0
    for i, j in bins_pairs:
        if chromosomes[i] == chromosomes[j]:
            counter += 1
    return counter

def verify_non_negative(list_of_numbers):
    for i in list_of_numbers:
        if i < 0:
            raise ValueError("List must be non-negative")

