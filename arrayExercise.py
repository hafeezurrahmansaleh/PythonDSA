expenses = [
    ['January', 2200],
    ['February', 2350],
    ['March', 2600],
    ['April', 2130],
    ['May', 2190]
]
# 1. In Feb, how many dollars you spent extra compare to January?
print(f'Extra expense in February: {expenses[1][1] - expenses[0][1]}')

# 2. Find out your total expense in first quarter (first three months) of the year.
total_expense = 0
for expense in expenses:
    total_expense += expense[1]
print(f'Total expense in the first quarter: {total_expense}')

# 3. Find out if you spent exactly 2000 dollars in any month
month = ''
for expense in expenses:
    if expense[1] == 2200:
        month = expense[0]
        break
if month:
    print(f'I spent 2000 in {month}')
else:
    print('I did not spent exactly 2000 in any month')

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expenses.append(['June', '1980'])
print(expenses)

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
for expense in expenses:
    if expense[0] == 'April':
        expense[1] = expense[1] - 200

print(expenses)
print('\n')

# """ Exercise 2: """

heroes = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

# 1. Length of the list
print(f'Length of the heroes list: {len(heroes)}')

# 2. Add 'black panther' at the end of this list
heroes.append('black panther')
print(heroes)

# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
heroes.remove('black panther')
heroes.insert(3, 'black panther')
print(heroes)

# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heroes[1:3] = ['doctor strange']
print(heroes)

# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heroes.sort()
print(heroes)
print(f'Length of the heroes list: {len(heroes)}')

# #### Exercise 3 ####
max_num = int(input('Enter the max number: '))
odd_numbers = [n for n in range(max_num) if n % 2 != 0]
print(odd_numbers)
