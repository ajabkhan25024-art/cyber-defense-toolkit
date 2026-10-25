import hashlib

word1 = "pakistan123"
word2 = "pakistan124"

md5_1 = hashlib.md5(word1.encode()).hexdigest()
sha256_1 = hashlib.sha256(word1.encode()).hexdigest()
sha256_2 = hashlib.sha256(word2.encode()).hexdigest()

print("Word 1:", word1)
print("MD5:", md5_1)
print("SHA-256:", sha256_1)
print("-------------------")
print("Word 2:", word2)
print("New SHA-256:", sha256_2)

