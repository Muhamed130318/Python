print("Enter two words to test if they are anagrams")

word1 = input("Enter the first word:")
word2 = input("Enter the second word:")

w1Sorted = ''.join(sorted(word1))
w2Sorted = ''.join(sorted(word2))

if w1Sorted == w2Sorted:
    print(word1 + " and " + word2 + " are anagrams.")
else:
    print(word1 + " and " + word2 + " are not anagrams.")
    