# Love calculator algorithm according to https://www.youtube.com/watch?v=oFsLVG7EAZ4
name1 = (input("input your name ").lower())
name2 = (input("input your name ").lower())

connection = name1 + "loves" + name2

append_str = ""

counted_set = ""


for i in range(len(connection)):

    # chekcking if its already counted
    # assuming it is not counted unless it is
    isCounted = False
    for letter in counted_set:
        if letter == connection[i]:
            isCounted = True

    if not isCounted:
        # start counting from one
        count = 1
        # count the letters to the right side of the letter
        for j in range(i + 1, len(connection)):
            if connection[i] == connection[j]:
                count = count + 1


        # add the number of counts for that letter
        append_str = append_str + str(count)


        # add the letter to the counted set so that it won't be counted again
        counted_set = counted_set + connection[i]



result = append_str

# repeat the process
def loopThrough(result):
    extra_str = ""
    m = len(result)
    for i, j in zip(range(0, int(m / 2)), range(-1, int((m / 2) * -1) - 1, -1)):
        sum2 = int(result[i]) + int(result[j])
        extra_str = extra_str + str(sum2)

    if m % 2 != 0:
        extra_str = extra_str + str(result[int(m / 2)])

    return extra_str




while (len(result) > 2):
    result = loopThrough(result)

print(result)