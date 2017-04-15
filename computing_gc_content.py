# http://rosalind.info/problems/gc/


def calculate_gc_content(dna_strings):
    list = []
    result = {}
    for key, val in dna_strings.items():
        total = len(val)
        gc = 0
        for symbol in val:
            if symbol == 'G' or symbol == 'C':
                gc += 1

        gc_content = (100 * float(gc))/float(total)
        list.append({
                         "dna_string" : key,
                         "total_string" : total,
                         "total_gc" : gc,
                         "gc_content" : gc_content
                    })
    return list

def show_higher_gc(dna_strings):
    list = calculate_gc_content(dna_strings)
    key_highest = ''
    highest_value = 0
    print(list)
    for item in list:
        if item['gc_content'] > highest_value:
            highest_value = item['gc_content']
            key_highest = item['dna_string']
    print('Highest is : {key} - {value}'.format(key=key_highest,value=highest_value))


def main():
    dna_strings = {}
    dna_str_lbl = ''
    with open("rosalind_gc.txt", "r") as file:
        for line in file:
            if line.startswith('>'):
                dna_str_lbl = line
                dna_strings[dna_str_lbl] = ''
            else:
                dna_strings[dna_str_lbl] += line.replace('\n','')
    show_higher_gc(dna_strings)


if __name__ == "__main__":
    main()