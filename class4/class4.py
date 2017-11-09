#Lists
'''
people = ['Anna', 'Bob', 'Kate']
nums = [1, 20, 0.58, 'abc', [1, 2, 3] ]
name = 'Kate'
if name in people:
    print('Yes!')
else:
    print ('No.')

''' 
'''
nums = [1, 2, 3]
for n in nums:
    print (n)
'''
'''
nums = []
for n in range (5):
    print(n)
    nums.append(n)
    print(nums)
print(nums)
print('Length:', len(nums))
'''
'''
#Cрез списка
text = "mama nana cat apple"
words = text.split()
#print(words)
#print(words[1])
#print(words[0:2])
for w in words [::2]:
    print (w)
'''
'''
nums = [[1, 2, 3]]*3
print(nums)
for n in nums [::1]:
    print (n)
'''
'''
nums = [[1, 2, 3]]*3
print(nums)
for row in nums:
    for n in row:
        print(n, end=' ')
    print()
'''
'''
w = "word"
[].append('w')
n = []
n.append('w')
'''
'''
w = "word"
letters =[]
for j in w:
    letters.append(j)
print(letters)
'''
'''
w = "hello"
l = list(w)
#str(l)
'''
'''
nums = [1,2,3]
nums_str = str(nums [0])
for d in nums[1:]:
    nums_str = nums_str + ' ' + str(d)
print(nums_str)
'''
"""
nums = [1,2,3]
nums_str = ""
for d in nums:
    nums_str = nums_str + str(d) + "  "
print([nums_str])
nums_str = nums_str[:-1]
print([nums_str])
"""
'''
Shell
letters = list('hello')
#letters
#'!'.join(letters)in Shell
>>> letters= list('hello')
>>> letters.pop()
'o'
>>> lt = letters.pop()
>>> lt
'l'
>>> letters = list('hello')
>>> letters
['h', 'e', 'l', 'l', 'o']
>>> new = letters.pop()
>>> letters
['h', 'e', 'l', 'l']
>>> new
'o'
'''
'''
#otobrazhenie bez bukv v konce
letters = list('hello')
letters.pop(-1)
'''
'''
#Cолько раз элемент в листе
letters = list('hello')
print(letters.index('e'))
print (letters)
'''
'''
#Сортировка по убыванию
nums = [2,3,14,1,1,0]
print(sorted(nums, reverse=True))
'''
'''
#по алфавиту в обратную
letters = list ('hello world!')
print(sorted(letters, reverse=True))
'''
'''
shell
>>> nums = [1,2,3,4,14,1,0,2]
>>> nums
[1, 2, 3, 4, 14, 1, 0, 2]
>>> nums [::-1]
[2, 0, 1, 14, 4, 3, 2, 1]
>>> nums = [1,2,3,4,14,1,0,2]
>>> nums.reverse()
>>> nums
[2, 0, 1, 14, 4, 3, 2, 1]
>>> 
'''
nums = [[1,2,3,4]]*5
#print(nums)
'''
for i in range (len(nums)):
    print(i, nums[i])
    if i % 2 == 0:
        print ('чётное'))
'''
#reversing 2nd and 4th rows
for row in nums:
    print(row)
    row.reverse() 
