#! Python 2.7
# pw.py - An insecure password locker program.


PASSWORDS = {'email': '31809dajse3-',
            'douban': 'dajweqwe1023',
            'sina':   '1231920qjwle',
            'zhihu':  '1231902jkje-q',
            'quora':  'dadadasdasda1',
            'facebook': 'dasdqweadf'}
            
import sys, pyperclip

if len(sys.argv) < 2:
    print "Usage: python pw.py [account] - copy account username"
    sys.exit()
    
account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print "Username for", account, " copied to clipboard."
    
else:
    print "There is no account named ", account