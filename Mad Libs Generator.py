def input_noun():
    word=input('Enter a noun: ')
    return word

def input_pronoun():
    word=input('Enter a pronoun: ')
    return word

def input_verb():
    word=input('Enter a verb: ')
    return word

def input_adjective():
    word=input('Enter an adjective: ')
    return word

print('Mad Libs Generator')
print('The computer has a sentence on its mind. We will ask you to provide some parts of speech. Then finally you\'ll be shown the sentence created with your given words!!!')
import random
choice=random.randint(1,6)
if choice==1:
    noun=input_noun()
    pronoun=input_pronoun()
    sentences=[f'{pronoun} is a {noun}.', f'{pronoun} bought a new {noun}.', f'That {noun} accused {pronoun} of robbery.']
    print(sentences[random.randint(0,2)])
elif choice==2:
    noun=input_noun()
    verb=input_verb()
    sentences=[f'This {noun} {verb} a scoundrel.', f'The {noun} {verb} around him.', f'He {verb} a very naughty {noun}.']
    print(sentences[random.randint(0,2)])
elif choice==3:
    noun=input_noun()
    adjective=input_adjective()
    sentences=[f'He has a {adjective} {noun}.', f'You might remember that {adjective} guy from our {noun}.', f'He threw the {adjective} ball towards that {noun}.']
    print(sentences[random.randint(0,2)])
elif choice==4:
    pronoun=input_pronoun()
    verb=input_verb()
    sentences=[f'The big boy {verb} {pronoun}.', f'The peon told {pronoun} to {verb} the letter.', f'I might {verb} {pronoun} one day.']
    print(sentences[random.randint(0,2)])
elif choice==5:
    pronoun=input_pronoun()
    adjective=input_adjective()
    sentences=[f'Thomas told {pronoun} that she\'s {adjective}.', f'The {adjective} man told {pronoun} to follow that path.', f'{pronoun} most probably knew the answer very {adjective}.']
    print(sentences[random.randint(0,2)])
elif choice==6:
    noun=input_noun()
    adjective=input_adjective()
    sentences=[f'{noun} is a very {adjective} boy.', f'That {noun} is very {adjective}.', f'This {noun} is very {adjective}.']
    print(sentences[random.randint(0,2)])
import emoji
print(emoji.emojize('Laughing...ARE YOU??? :grinning_face: :rolling_on_the_floor_laughing: :winking_face:', variant='emoji_type'))
print(emoji.emojize('Thanks for playing the game!!! :star-struck:', variant='emoji_type'))