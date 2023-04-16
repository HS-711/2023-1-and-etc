#순차검색 재귀
def seq_search_ox(s,key):
    if s!=[]:
        if s[0]==key:
            return True
        else:
            return seq_search_ox(s[1:],key)
    else:
        return False
'''
#순차검색 while
def seq_search_ox(s,key):
    while s!=[]:
        if s[0]==key:
            return True
        else:
            s=s[1:]
    return False

#순차검색 for
def seq_search_ox(s,key):
    for x in s:
        if x==key:
            return True
    return False
'''
'''
이분탐색은 자료가 sort되어있다는 것을 전제로 한다.
#이분검색 일반형(재귀형)
def bin_search_ox(ss,key):
    if ss!=[]:
        mid=len(ss)//2
        if key==s[mid]:
            return True
        elif key<ss[mid]:
            return bin_search_ox(ss[:mid],key)
        else:
            return bin_search_ox(ss[mid+1:],key)
    return False
'''
'''
이진탐색 while형
def bin_search_ox(ss,key):
    while ss!=[]:
        mid=len(ss)//2
        if key == ss[mid]:
            return True
        elif key<ss[mid]:
            ss=ss[:mid]
        else:
            ss=ss[mid+1:]
    return False
'''

s=[65,5,4,2,1]
key=1
print(seq_search_ox(s,key))
