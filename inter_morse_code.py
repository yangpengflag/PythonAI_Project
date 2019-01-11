

# 方法一，笨办法，手动组合字典
def uniqueMorseRepresentations1(self, words):
    ref = {'a':".-",
           "b":"-...",
           "c":"-.-.",
           "d":"-..",
           "e":".",
           "f":"..-.",
           "g":"--.",
           "h":"....",
           "i":"..",
           "j":".---",
           "k":"-.-",
           "l":".-..",
           "m":"--",
           "n":"-.",
           "o":"---",
           "p":".--.",
           "q":"--.-",
           "r":".-.",
           "s":"...",
           "t":"-",
           "u":"..-",
           "v":"...-",
           "w":".--",
           "x":"-..-",
           "y":"-.--",
           "z":"--.."}
    res = []
    for word in words:
        s = ''
        for i in word:
            s += ref.get(i)
        res.append(s)
    print(len(set(res)))

uniqueMorseRepresentations1(self=uniqueMorseRepresentations1,words=["gin", "zen", "gig", "msg"])



# 利用字典的zip函数拼接字母和摩尔斯密码为字典
def uniqueMorseRepresentations2(self, words):
    morsecode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    charlist = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    morsemap = dict(zip(charlist,morsecode))
    morselist=[]
    for i in words:
        s = ""
        for j in i:
            s += morsemap.get(j)
            #print(s)

        morselist.append(s)

    print(morselist)
    print(len(set(morselist)))


uniqueMorseRepresentations2(self=uniqueMorseRepresentations2,words=["gin", "zen", "gig", "msg"])


# 方法三用ord()函数求出a的ASCII值, chr() 是将ASCII值变为字符.  ord('a') = 97 ,   ord("A") = 65
def uniqueMorseRepresentations3(self, words):
    morsecode = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    lenth = len(set("".join(morsecode[ord(s) - 97] for s in word) for word in words))
    print(lenth)


uniqueMorseRepresentations3(self=uniqueMorseRepresentations3,words=["gin", "zen", "gig", "msg"])