'''
  input: a collection of integers
  output: the list of elements in the convolution of spectrum
'''

def Convolution(list_int):
    convol_list = []
    list_len    = len(list_int)
    for each_i in range(list_len - 1):
        for each_j in range(each_i + 1, list_len):
            abs_value = abs(list_int[each_i] - list_int[each_j])
            if abs_value:
                convol_list.append(abs_value)
    convol_list = sorted(convol_list)
    return sorted(convol_list, key= lambda k : -convol_list.count(k))

if __name__ == "__main__":
    infile = "input.txt"
    listint = [0, 137, 186, 323]
    listint = open(infile).readlines()[0].strip().split()
    listint = "57 57 71 99 129 137 170 186 194 208 228 265 285 299 307 323 356 364 394 422 493".split()
    listint = map(int, listint)
    convollist = Convolution(listint)
    print len(convollist)
    print " ".join([str(x) for x in convollist])
