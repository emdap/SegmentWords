import extract_words

words = extract_words.extract()

def segment(hash, msg=None, old=None, b=0, i=0):
    prev = -1
    if not(msg):
        msg = []
    if not(old):
        old = []
    while i < 1 + (len(hash)):
        s = ' ' + hash[b:i] + ' '
        #print(s)
        if s in words:
            #print(s)
            if hash[i:i+3] == 'ing':
                i+=3
                s = ' ' + hash[b:i] + ' '
            msg.append(s.strip())
            old.append(s.strip())
            prev = b
            #print('found! ', prev, msg, old)
            b = i
        i+=1
    #print('checking')
    if b < i - 1:
        #print('recall')
        if len(msg) == 0:
            return(['no message'])
        if prev<0:
            b=0
            #print('backtrack')
            for j in range(len(msg)-1):
                b+=len(msg[j])
            if len(old)==0:
                rem = ''
            else:
                rem = msg.pop()
            i = b + len(rem) + 1
            return segment(hash, msg, old, b, i)
        else:
            rem = msg.pop()
            b = prev
            i = b + len(rem) + 1
        return segment(hash, msg, old, b, i)

    return msg

def run_segs(tags):
    ''' Takes hashtags in list format, each list indice is a new hashtag to segment.
    '''
    all = []
    for tag in tags:
        msg = segment(tag)
        seg = ''
        for i in range(len(msg)):
            seg += msg[i] + ' '
        all.append(seg.strip())
    return all    
