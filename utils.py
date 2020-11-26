punc_ranges = [(0x0000,0x002f),(0x003a,0x0040),(0x005b,0x0060),(0x007b,0x007f), (0x2000,0x206f),(0x2100,0x214f), (0x3000,0x303f), (0xfe30,0xfe4f), (0xff00,0xffef)]

def is_punctuation(text):
    if len(text) > 1:
        return False
    code = ord(text)
    for r in punc_ranges:
        if code >= r[0] and code <= r[1]:
            return True
    return False

def split(text):
    lst = []
    start_idx = 0
    cur_idx = 0
    sl = len(text)
    for cur_idx in range(sl):
        if is_punctuation(text[cur_idx]):
            if cur_idx > start_idx:
                lst.append(text[start_idx:cur_idx])
            start_idx = cur_idx + 1
    if start_idx < sl:
        lst.append(text[start_idx:])
    return lst
