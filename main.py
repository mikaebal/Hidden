def hidden(matrix, n):
    # Your implementation here!
    # ur doing great 
    # skipping some letters: 
    # e, z, b, v, w, q, etc
    # initialize list
    # frequency counter
    # loop over the rows 
    # loop letters
    # skip over ns
    # add letter
    # return dict 

    # hidden_letter = []
    # frequency = 0
    # for row in matrix():


    letters = []
    i = 0 

    for row in matrix:
        for letter in row:
            if i % n == 0:
                letters.append(letter)
            i += 1
    return ''.join(letters)

        

matrix_1 = (
    ('u','e','r','e', ' ', 'e'),
    ('d', 'z', 'o', 'b', 'i', 'v'),
    ('n',),
    ('w', 'g', 'q', ' ', '5', 'g', 'w'),
    ('r',),
    ('y', 'e'),
    ('u', 'a', 'u', 't')
)
assert hidden(matrix_1, 2) == 'ur doing great'
assert hidden(matrix_1, 3) == 'uedbnqgya'
assert hidden(matrix_1, 525600) == 'u'
assert hidden(matrix_1, 1) == 'uere edzobivnwgq 5gwryeuaut'

matrix_2 = (
    ('💜',),
)
assert hidden(matrix_2, 17) == '💜'
assert hidden(matrix_2, 1) == '💜'

print("All tests passed! Discuss time and space complexity if time remains!")

