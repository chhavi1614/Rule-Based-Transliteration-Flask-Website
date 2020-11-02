mapping = {'n~': 'ँ', 'n:': 'ं', 'h:': 'ः', 'm:': 'ँ', 'a^': 'अ', 'a': 'अ', 'aa': 'आ', 'i': 'इ', 'ii': 'ई', 'u': 'उ',
           'uu': 'ऊ', 'rx': 'ऋ', 'rx~': 'ॠ', 'lx': 'ऌ',
           'lx~': 'ॣ.', 'e~': 'ऍ', 'e': 'ए', 'ei': 'ए', 'ai': 'ऐ', 'o~': 'ऑ', 'o': 'ओ', 'oo': 'ओ', 'au': 'औ', 'k': 'क',
           'k~': 'क़', 'kh': 'ख', 'kh~': 'ख़',
           'g': 'ग', 'g~': 'ग़', 'gh': 'घ', 'ng~': 'ङ', 'ch': 'च', 'chh': 'छ', 'j': 'ज', 'j~': 'ज़', 'jh': 'झ',
           'nj~': 'ञ', 't:': 'ट', 't:h': 'ठ', 'd:': 'ड',
           'd~': 'ड़', 'd:h': 'ढ', 'dh~': 'ढ़', 'nd~': 'ण', 't': 'त', 'th': 'थ', 'd': 'द', 'dh': 'ध', 'n': 'न', 'n!': 'ऩ',
           'p': 'प', 'ph~': 'फ़', 'ph': 'फ', 'b': 'ब',
           'bh': 'भ', 'm': 'म', 'y': 'य', 'y~': 'य़', 'r~': '॰', 'r': 'र', 'r:': 'ऱ', 'l': 'ल', 'l~': 'ऴ', 'l:': 'ळ',
           'v': 'व', 'sh': 'श', 'shh': 'ष', 's': 'स',
           'h': 'ह', 'c': 'क', 'f': 'फ', 'q': 'क', 'w': 'व', 'x': 'ज', 'z': 'ज', 'aa1': 'ा', 'i1': 'ि', 'ii1': 'ी',
           'u1': 'ु', 'uu1': 'ू', 'rx1': 'ृ', 'rx~1': 'ॄ',
           'rxx1': 'ॄ', 'e~1': 'ॅ', 'e1': 'े', 'ei1': 'े', 'ai1': 'ै', 'o~1': 'ॉ', 'o1': 'ो', 'oo1': 'ो', 'au1': 'ौ',
           'ha1': '्', 'om:': 'ॐ', 'v4': '॑', 'v5': '॒', 'v6': '॓',
           'v7': '॔', 'v11': '्', 'v1': '़'}

schwa = "a"

avail = {'a', 'a!',
         'aa',
         'ai',
         'au',
         'b',
         'bh',
         'c',
         'ch',
         'chh',
         'd',
         'd:',
         'd:h',
         'dh',
         'dh~',
         'd~',
         'e',
         'ei',
         'e~',
         'f',
         'g',
         'gh',
         'g~',
         'h',
         'h:',
         'i',
         'ii',
         'j',
         'jh',
         'j~',
         'k',
         'kh',
         'kh~',
         'k~',
         'l',
         'l:',
         'lx',
         'lx~',
         'l~',
         'm',
         'm:',
         'n',
         'n!',
         'n-',
         'n:',
         'nd~',
         'ng~',
         'nj~',
         'n~',
         'o',
         'om:',
         'oo',
         'ox',
         'o~',
         'p',
         'ph',
         'ph~',
         'q',
         'qs~',
         'r',
         'r:',
         'rx',
         'rx~',
         'r~',
         's',
         'sh',
         'shh',
         't',
         't:',
         't:h',
         'th',
         'u',
         'uu',
         'v',
         'v1',
         'v10',
         'v21',
         'v4',
         'v5',
         'v6',
         'v7',
         'vx',
         'vxx',
         'w',
         'x',
         'y',
         'y~',
         'z',
         'zh',
         'zz'}

volwel = {"a", "aa", "i", "ii", "u", "uu", "rx", "rx~", "lx", "lx~", "e", "ei", "ai", "o", "oo", "au"}


def formatting(word):
    word = word.lower()
    le = len(word)
    if le < 2:
        word = word + "a"
        le = le + 1
    if (word[le - 1:le] not in volwel) or (word[le - 1] == 'a' and word[le - 2] != 'a'):
        word = word + "a"
    if word[le - 1] == 'e':
        le = len(word)
        word = word[0:le - 1]
        word = word + "a"
    return word


def vowPos(gWord):
    for i in range(len(gWord)):
        if gWord[i] in volwel:
            return i
    return -1


def syllable(phones):
    curr = ""
    ans = []
    for i in range(len(phones)):
        curr = curr + phones[i]

        if phones[i] in volwel:
            ans.append(curr)
            curr = ""
    return ans


def fin_phone(input):
    oldValue = ""
    converted = []
    i = 0
    newValue = ""
    while i < (len(input)):
        newValue = oldValue + input[i]
        if newValue in avail:
            oldValue = newValue
        elif (i + 1 < len(input)) and ((newValue + input[i + 1]) in avail):
            oldValue = newValue + input[i + 1]
            i = i + 1
        else:
            if oldValue != "":
                converted.append(oldValue)
            oldValue = input[i]
        i = i + 1

    converted.append(oldValue)

    for i in range(len(converted) - 1):
        if converted[i] == "ai" and converted[i + 1] == "i":
            converted[i] = "a"
            converted[i + 1] = "ii"
    return converted


def fin_syll(input):
    phones = fin_phone(input)
    syll_ip = syllable(phones)
    return syll_ip


def Trans(mw):
    word = formatting(mw)
    output = ""
    syll_ip = fin_syll(word)
    for i in range(len(syll_ip)):
        type = 0  # CV
        phone_ip = fin_phone(syll_ip[i])
        vpos = vowPos(phone_ip)
        if vpos > 0:
            if (phone_ip[vpos] == schwa):
                phone_ip[vpos] = ""
            else:
                phone_ip[vpos] = phone_ip[vpos] + "1"
            if (vpos != 1):
                type = 1  # CCV, CCCV
        elif (vpos < 0):
            type = 2
        else:
            type = 3  # V

        if (type == 0):  # CV
            for f in range(len(phone_ip)):
                if phone_ip[f] in mapping:
                    output = output + mapping[phone_ip[f]]
        elif (type == 3):  # V
            if phone_ip[0] in mapping:
                output = output + mapping[phone_ip[0]]
        elif (type == 1):  # CCV, CCCV
            f = 0
            while f < (vpos - 1):
                if phone_ip[f] in mapping:
                    output = output + mapping[phone_ip[f]]
                    if "ha1" in mapping:
                        output = output + mapping["ha1"]
                f = f + 1
            while f < (vpos + 1):
                if phone_ip[f] in mapping:
                    output = output + mapping[phone_ip[f]]
                f = f + 1
        # print(output)
    return output


def getTransliteration(input):
    i = 0
    temp = ''
    ans = ''
    input = input + " "
    while i < len(input):
        if input[i].isalpha():
            temp = temp + input[i]
        else:
            if temp != '':
                ans = ans + Trans(temp)
            temp = ""
            ans = ans + input[i]
        i += 1
    return ans
