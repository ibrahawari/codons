import sys

def print_dictionary(dictionary):
    for acid in dictionary:
        print acid["Name"]
        for key in sorted(acid, key = acid.get):
            if ((key != "Name") & (key != "Total")):
                if (acid["Total"] == 0):
                    percentage = 0.0
                else:
                    percentage = ((acid[key] / (acid["Total"] * 1.0) * 100))
                print "\t%s\t%i\t%f%s" % (key, acid[key], percentage, "%")

def build_dictionary(s, code, dictionary):
    i = s - 1
    j = s
    k = s + 1
    while True:
        triplet = code[i] + code[j] + code[k]
        for acid in dictionary:
            if (triplet in acid.keys()):
                acid[triplet] += 1
                acid["Total"] += 1
                break
        if (acid["Name"] == "Stp"):
            break
        i += 3
        j += 3
        k += 3
    return dictionary

def clean_code(f):
    text = ''
    for line in f:
        text += line
    lines = text.splitlines()
    code = ''
    for i in range(1, len(lines)):
        code += lines[i]
    code = code.replace("T", "U")
    return code    
    
def analyze(filename, start, dictionary):
    f = open(filename)
    s = int(start)
    code = clean_code(f)
    dictionary = build_dictionary(s, code, dictionary)
    f.close()
    return dictionary

def create_dictionary():
    dictionary = []
    Ala = {"Name" : "Ala", "GCU" : 0, "GCC" : 0, "GCA" : 0, "GCG" : 0, "Total" : 0}
    dictionary.append(Ala);
    Arg = {"Name" : "Arg", "CGU" : 0, "CGC" : 0, "CGA" : 0, "CGG" : 0, "AGA" : 0, "AGG" : 0, "Total" : 0}
    dictionary.append(Arg);
    Asn = {"Name" : "Asn", "AAU" : 0, "AAC" : 0, "Total" : 0}
    dictionary.append(Asn);
    Asp = {"Name" : "Asp", "GAU" : 0, "GAC" : 0, "Total" : 0}
    dictionary.append(Asp);
    Cys = {"Name" : "Cys", "UGU" : 0, "UGC" : 0, "Total" : 0}
    dictionary.append(Cys);
    Gln = {"Name" : "Gln", "CAA" : 0, "CAG" : 0, "Total" : 0}
    dictionary.append(Gln);
    Glu = {"Name" : "Glu", "GAA" : 0, "GAG" : 0, "Total" : 0}
    dictionary.append(Glu);
    Gly = {"Name" : "Gly", "GGU" : 0, "GGC" : 0, "GGA" : 0, "GGG" : 0, "Total" : 0}
    dictionary.append(Gly);
    His = {"Name" : "His", "CAU" : 0, "CAC" : 0, "Total" : 0}
    dictionary.append(His);
    Ile = {"Name" : "Ile", "AUU" : 0, "AUC" : 0, "AUA" : 0, "Total" : 0}
    dictionary.append(Ile);
    Leu = {"Name" : "Leu", "UUA" : 0, "UUG" : 0, "CUU" : 0, "CUC" : 0, "CUA" : 0, "CUG" : 0, "Total" : 0}
    dictionary.append(Leu);
    Lys = {"Name" : "Lys", "AAA" : 0, "AAG" : 0, "Total" : 0}
    dictionary.append(Lys);
    Met = {"Name" : "Met", "AUG" : 0, "Total" : 0}
    dictionary.append(Met);
    Phe = {"Name" : "Phe", "UUU" : 0, "UUC" : 0, "Total" : 0}
    dictionary.append(Phe);
    Pro = {"Name" : "Pro", "CCU" : 0, "CCC" : 0, "CCA" : 0, "CCG" : 0, "Total" : 0}
    dictionary.append(Pro);
    Ser = {"Name" : "Ser", "UCU" : 0, "UCC" : 0, "UCA" : 0, "UCG" : 0, "AGU" : 0, "AGC" : 0, "Total" : 0}
    dictionary.append(Ser);
    Stp = {"Name" : "Stp", "UAA" : 0, "UAG" : 0, "UGA" : 0, "Total" : 0}
    dictionary.append(Stp);
    Thr = {"Name" : "Thr", "ACU" : 0, "ACC" : 0, "ACA" : 0, "ACG" : 0, "Total" : 0}
    dictionary.append(Thr);
    Trp = {"Name" : "Trp", "UGG" : 0, "Total" : 0}
    dictionary.append(Trp);
    Tyr = {"Name" : "Tyr", "UAU" : 0, "UAC" : 0, "Total" : 0}
    dictionary.append(Tyr);
    Val = {"Name" : "Val", "GUU" : 0, "GUC" : 0, "GUA" : 0, "GUG" : 0, "Total" : 0}
    dictionary.append(Val);
    return dictionary
            
if __name__ == "__main__":
    filenames = []
    starts = []
    for i in range(len(sys.argv)):
        if (i % 2):
            filenames.append(sys.argv[i])
        elif (i):
            starts.append(sys.argv[i])
    dictionary = create_dictionary()
    for i in range(len(filenames)):
        dictionary = analyze(filenames[i], starts[i], dictionary)
    print_dictionary(dictionary)
