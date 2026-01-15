def two_sum(book, target):
    book.sort()          # same as sort(book.begin(), book.end())
    
    left = 0
    right = len(book) - 1

    while left < right:
        s = book[left] + book[right]

        if s == target:
            return "yes"
        elif s < target:
            left += 1
        else:
            right -= 1

    return "no"

