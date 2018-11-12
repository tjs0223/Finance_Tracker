# Figure out how to connect OFX with acct in secure way
# especially if this is on GH

''' example code to help remember syntax for python. tabs and colons
def main():

    i = 2
    while (i<5):
        print("TEST")
        i +=2



main()'''
import ofxclient
from pprint import pprint
from ofxclient import institution

ofxhome_id    = '783'
your_username = 'genewilder'
your_password = 'ihatecandy'
 # yeah I know, you can't pass the 'pass' in
# the constructor.. I'm lame and maybe I'll fix
# it later
'''institution = ofxclient.Institution(
    id = ofxhome_id,
    username = your_username
)'''

inst = ofxclient.Institution(
        id = '031176110',
        org = '	ING DIRECT',
        url = 'https://ofx.capitalone360.com/OFX/ofx.html',
        # dummy username and password - test authentication
        username = 'user',
        password = 'pass'
)
inst.password = your_password
# work to use access code instead of username / password combo: 11/10/2018
#inst.authenticate([inst.username,inst.password])
inst.accounts()

# You HAVE to call save() but only just once. Calling save
# repeatedly won't hurt anything.
# Note that ffter calling this, you would never need to specify the
# institution.password again as it will be loaded from the keychain
#
# save() triggers saving of cache information (see ~/.ofxclient) as well
# as a config file (see ~/.ofxclient.conf)
inst.save()
accounts = inst.accounts()
print(accounts)
print("Accounts printed")


# returns an ofxparse.Statement object
# see an the ofx.account.statement portion of their docs:
# https://github.com/jseutter/ofxparse/blob/master/README
# statement = accounts[0].statement(days=5)


# get the balance
#print ("balance: %s" % statement.balance)
accounts = inst.accounts()
for a in accounts:
    # a StringIO wrapped string of the raw OFX download
    download  = a.download(days=5)
    print (download.read())
