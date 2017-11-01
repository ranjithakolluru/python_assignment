
def anagram(str1,str2):
    str1=list(str1)
    print str1
    str1_sort=str1.sort()
    print str1_sort
    str2=list(str2)
    #print str2
    str2_sort=str2.sort()
    print str2_sort
    if str1_sort==str2_sort:
        print "yes,anagram"
    else:
        print "not an anagram"

anagram("heart","heart")
