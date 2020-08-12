def longestString(s):
    dicts ={}
    start  = maxlength = 0
    for i, value in enumerate(s):
        if value in dicts:
            sum = dicts[value] + 1
            if sum > start:
                start = sum
        num = i - start +1
        if num > maxlength:
            maxlength = num
        dicts [ value] = i
    return maxlength
longestString("abcabcd")