left = [1, 2, 3, 4]
right = [1, 1, 3, 4, 5, 6, 7]

merge = []  # Final sorted array store karega


def merge_arrays(left, right):

    i = 0  # left array ka pointer
    j = 0  # right array ka pointer

    n = len(left)   # left array ki length
    m = len(right)  # right array ki length

    # Jab tak dono arrays mein elements available hain
    while i < n and j < m:

        # Dono current elements ko compare karo
        if left[i] <= right[j]:

            merge.append(left[i])  # Chhota element result mein add karo
            i += 1                 # left pointer ko aage badhao

        else:
            merge.append(right[j]) # right ka chhota element add karo
            j += 1                 # right pointer ko aage badhao


    # Agar left array mein elements bach gaye hain
    while i < n:
        merge.append(left[i])  # Remaining left elements add karo
        i += 1


    # Agar right array mein elements bach gaye hain
    while j < m:
        merge.append(right[j]) # Remaining right elements add karo
        j += 1


    return merge  # Final sorted array return karo


print(merge_arrays(left, right))