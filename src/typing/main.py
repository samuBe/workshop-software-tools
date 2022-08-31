from typing import List, Union

number = Union[float, int]
names: List[str] = list()
scores: List[number] = list()

while True:
    name = input('Enter your name: ')
    score = input('Enter your score: ')
    # To do append the name and score to a list

    stop = input("Press q to stop: ")
    if stop == "q":
        break


# To do set the following

maximum_score = 5
maximum_name = 'Samuel'
average_score = 9

print(report(maximum_name, maximum_score, average_score))
