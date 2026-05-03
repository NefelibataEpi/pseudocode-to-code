from collections import deque


def ladder_length(beginWord, endWord, wordList):
    word_set = set(wordList)

    if endWord not in word_set:
        return 0

    queue = deque([beginWord])
    visited = set([beginWord])
    distance = 1

    while queue:
        size = len(queue)

        for _ in range(size):
            current = queue.popleft()

            if current == endWord:
                return distance
            
            neighbors = get_neighbors(word_set, current)
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
            
        distance += 1
    
    return 0


def get_neighbors(wordList, current):
    neighbors = []

    for i in range(len(current)):
        for j in "abcdefghijklmnopqrstuvwxyz":
            newWord = current[:i] + j + current[i+1:]
            if newWord in wordList:
                neighbors.append(newWord)
    
    return neighbors


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

print(ladder_length(beginWord, endWord, wordList))