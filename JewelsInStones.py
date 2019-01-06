
# 解题思路，循环拿J的元素与S中的元素对比，如果相等则+1，自己最开始的解法，中规中矩^_^
def numJewelsInStones(J, S):
    i = 0
    l = len(S)
    for x in J:
        for xx in range(l):
            #print(S[xx])
            if (x == S[xx]):
               i+=1
        else:
            continue
    print(i)


numJewelsInStones("aA","aAAbbbb")
numJewelsInStones("z","ZZ")
numJewelsInStones("zqwe","aAbBCcddSSDDGTwWeEeee")


# 解题思路，与上面不同，由于J中元素唯一，则反过来用S中的元素来判断是否存在于J中，存在则+1(借鉴了网友的思路，学习了)
def numJewelsInStones1(J, S):
    i = 0
    for s in S:
        if s in J:
            i += 1
    print(i)

numJewelsInStones1("aA","aAAbbbb")
numJewelsInStones1("z","ZZ")
numJewelsInStones1("zqwe","aAbBCcddSSDDGTwWeEeee")

# 将字符转为了列表，统计同时存在J和S中元素的个数(借鉴了网友的思路，学习了)
def numJewelsInStones2(J, S):
     print(sum([s in J for s in S]))

numJewelsInStones2("aA","aAAbbbb")
numJewelsInStones2("z","ZZ")
numJewelsInStones2("zqwe","aAbBCcddSSDDGTwWeEeee")