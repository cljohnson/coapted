def main():
    this_text = r"There are some old lessons that must be learned again and again.\r\n"
    print "this_text = " + this_text + "length of this_text = " + str(len(this_text))
    string = r"\r\n"
    replace_nl(this_text,string)
    this_text.strip()
    print "this_text after replace_nl = " + this_text + " length of this_text = " + str(len(this_text))
def replace_nl(txt, string):
    try:
        chop = txt.find(string)
        txt = txt[0:chop] + txt[chop+1:]
        replace_nl(txt)
    except:
        pass
    return txt
if __name__ == "__main__":
    main()