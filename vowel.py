letter=input('enter a letter')
letter=letter.lower()
match letter:
      case 'a'|'e'|'i'|'o'|'u':
           print('vowel')
      case other:
           print('consonant')