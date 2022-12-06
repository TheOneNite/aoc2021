from inputs import day6

test = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'

tests = ['bvwbjplbgvbhsrlpgdmjqwftvncz', 'mjqjpqmgbljsphdztnvjfqwrcgsmlb', 'nppdvjthqldpwncqszvftbrmjlhg','nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg','zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw']

buff = day6
prev = 0

candidates = []

for i in range(0, len(buff)):
    candidates.append(buff[i:i+14])
    prev = i


def checkDupe(string):
    for c in string:
        if string.count(c) > 1:
            return False
    return True

codes = list(filter(checkDupe, candidates))
print(codes)
start = codes[0]
print(buff.index(start)+14)
