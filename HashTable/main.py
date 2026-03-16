from HashTable import hashTable
def main():
    myHash = hashTable()
    myHash.set('a', 'apple')
    myHash.delete('a')
    myHash.set('b', 'banana')
    for i in myHash.table:
        print(i)
main()