#Given a string of s length ~200 letters and 4 letters (a,b,c,d)
#Return a slice of this string from indices a to b and c through d, inclusively

def string_index(s,a,b,c,d):
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    phrase = f"{s[a:b+1]} {s[c:d+1]}"
    print(str(phrase))

string_index('90wSz7RS5GgcGg9yhuwEnojIAEgrettajCogaCAUGZpvka6uhVnu7isNBnjgh0EhcQzhlDqMu0aTF85SXKBiznrsWmAk79yFmC5SDnSrPUGFNS6iXSykjgWavXNhBP4mXRUsmInQ7pJQtuberculosuscHHhD1dIeE.',
25,31,140,151)