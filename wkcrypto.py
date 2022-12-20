from .koreanunisep import *

wk = {'ㄱ': '11', 'ㄴ': '12', 'ㄷ': '13', 'ㄹ': '14', 'ㅁ': '15', 'ㅂ': '16', 'ㅅ': '17',
 'ㅇ': '18', 'ㅈ': '19', 'ㅊ': '20', 'ㅋ': '21', 'ㅌ': '22', 'ㅍ': '23', 'ㅎ': '24',
  'ㄲ': '25', 'ㅆ': '26', 'ㄸ': '27', 'ㅃ': '28', 'ㅉ': '29',

'ㅏ': '30', 'ㅑ': '31', 'ㅓ': '32', 'ㅕ': '33', 'ㅗ': '34', 'ㅛ': '35', 'ㅜ': '36',
 'ㅠ': '37', 'ㅡ': '38', 'ㅣ': '39', 'ㅐ': '40', 'ㅔ': '41', 'ㅚ': '42', 'ㅟ': '43',
  'ㅒ': '44', 'ㅖ': '45', 'ㅘ': '46', 'ㅝ': '47', 'ㅙ': '48', 'ㅞ': '49',

  '.ㄱ': '0011', '.ㄴ': '0012', '.ㄷ': '0013', '.ㄹ': '0014', '.ㅁ': '0015', '.ㅂ': '0016',
   '.ㅅ': '0017', '.ㅇ': '0018', '.ㅈ': '0019', '.ㅊ': '0020', '.ㅌ': '0021', '.ㅋ': '0022',
    '.ㅍ': '0023', '.ㅎ': '0024', '.ㄲ': '0025', '.ㅆ': '0026', '.ㄵ': '0027', '.ㄶ': '0028',
     '.ㄺ': '0029', '.ㄻ': '0030', '.ㄼ': '0031', '.ㄾ': '0032', '.ㄿ': '0033',
    
'1': '0051', '2': '0052', '3': '0053', '4': '0054', '5': '0055', '6': '0056', '7': '0057',
 '8': '0058', '9': '0059', '0': '0060',
 
 'A': '0111', 'B': '0112', 'C': '0113', 'D': '0114', 'E': '0115', 'F': '0116', 'G': '0117',
  'H': '0118', 'I': '0119', 'J': '0120', 'K': '0121', 'L': '0122', 'M': '0123', 'N': '0124',
   'O': '0125', 'P': '0126', 'Q': '0127', 'R': '0128', 'S': '0129', 'T': '0130', 'U': '0131',
    'V': '0132', 'W': '0133', 'X': '0134', 'Y': '0135', 'Z': '0136',
    
    '.': '0081', ',': '0082', '?':'0083',':': '0084'}

reverse_wk= dict(map(reversed,wk.items()))

def wk_encode(t):
    outp = []
    t = koreansep(t)
    for i in t:
        if len(i)==3:
            outp.append(wk[i[0]])
            outp.append(wk[i[1]])
            if i[2] != "":
                outp.append(wk["."+i[2]])
            else:
                pass
        else:
            if i in wk.keys():
                outp.append(wk[i])
            else:
                outp.append(i)

    return "".join(outp)

def wk_decode(t):
    outp = []
    t = list(t)
    i = 0
    l = len(t)
    while True:
        if i>=l-1:
            break
        
        if t[i]=="1" or t[i]=="2" or t[i]=="3" or t[i]=="4":
            outp.append(reverse_wk[t[i]+t[i+1]])
            i += 2
        elif t[i]=="0" and t[i+1]=="0" and int("".join(t[i+1:i+4]))<=33 and int("".join(t[i+1:i+4]))>=11:
            outp.append(list((reverse_wk["".join(t[i:i+4])]))[1])
            i += 4
        else:
            outp.append(reverse_wk["".join(t[i:i+4])])
            i += 4

    return "".join(outp)

input_text = Element("input_text")
output_text = Element("output_text")

def wkinandout():
    output_text.element.innerText = wk_encode(input_text.value)
    input_text.clear()
