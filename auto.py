import pprint

message = 'It was a bright cold day in April, and the clocks were strking thriteen.'
count = {}

for character in message:
    count.setdefault(character,0)
    count[character] = count[character]+1

pprint.pprint(count)


theBoard = {'top-L':'O', 'top-M':'O', 'top-R' :'O',
            'mid-L':'X', 'mid-M':'X', 'mid-R':' ',
            'bot-L':' ', 'bot-M':' ', 'bot-R':'X'}

def printBoard(board):
    print(board['top-L'] + '|'+ board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|'+ board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['bot-L'] + '|'+ board['bot-M'] + '|' + board['bot-R'])

printBoard(theBoard)


