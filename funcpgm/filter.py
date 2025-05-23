#filter()
'''letters=['a','b','c','d','e','i','o']
def filter_vowels(letter):
    vowels=['a','e','i','o','u']
    return True if letter in vowels else False
filtered_vowels=filter(filter_vowels,letters)
vowels=tuple(filtered_vowels)
print(vowels)
'''

'''numbers=[1,2,3,4,5,6,7,8,9]
def filter_even(numbers):
    return True if numbers%2==0 else False
filtered_even=filter(filter_even,numbers)
evenum=list(filtered_even)
print(evenum)
'''

#using lambda function inside filter()
'''numbers=[1,2,3,4,5,6,7,8,9]
filtered_even=filter(lambda x:(x%2==0),numbers)
even_numbers=list(filtered_even)
print(even_numbers)
'''



'''sntnce=["This","is","python"]
def fil_leng(sntnce):
    return True if len(sntnce)<5 else False
filtered_sntnce=filter(fil_leng,sntnce)
new=list(filtered_sntnce)
print(new)
'''


d=[{"name":"Adrika","score":90},
   {"name":"Ayana","score":80},
   {"name":"Sneha","score":65},
   {"name":"Anakha","score":60},
   {"name":"Saheer","score":95},
   {"name":"Dilshad","score":80},]

def score(d):
    return True if d("score")>70 else False
high_score=list(filter(lambda a:(a["name"] if a["score"]>70 else False),d))
new=list(high_score)
print(list(map(lambda b:b["name"],new)))




    
   
       