Writeup 10 - Crypto II   
=====   

Name: *Brianna Higgins*   
Section: *0201*   

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.   

Digital acknowledgment of honor pledge: *Brianna Higgins*   

## Assignment 10 Writeup   

### Part 1 (70 Pts)   
In order to show the notary that this signature scheme is vulnerable to a hash length extension attack, the script [stub.py](stub.py) was developed.  Prior to development, it was determined the digital notary, located at `nc 142.93.118.186 1234` using MD5 hashing to sign messages.  The notary can either generate a signature by prepending a message with a random secret, or test a signature against a new message.  Each time a new signature is requested, a new secret for the data will be generated, but the same secret for every signature test.  However, it is not provided how long of a secret the notary uses for signing, except that it is between 6 and 15 bytes long.   

To understand how the notary works, I connected to `nc 142.93.118.186 1234`.  Upon connecting, I found the notary had three options:   
```   
Hello, and welcome to the MD5 Digital Notary!   
What would you like to do today?   
1) Sign some data   
2) Test a signature's validity   
3) Quit :(   
```   
I entered `1` and read through the instructions and provided a message `CMSC389R Rocks!` (taken from the lecture slides).  I, then, placed took the generated hash and placed it into the script.  Using the already provided code, a fake hash was created containing the addition of `malicious`.  Since it was provided that the padding was between 6 and 15 bits, I created paddings for every possible value.  I originally attempted to manually enter these values, but determined it would be more efficient to connect to the server with sockets and send each padded value.  Since I was not manually entering the values in, I found that the script was not providing any output of interest.  To account for this, I included a second timeout to allow the response from the server to be delivered back prior to collecting it.   

After running this script, it was determined the notary was already aware that his signature scheme was vulnerable to a hash length extension attack, since the following message was outputted:   
```   
Wow... I've never signed this data before!   
This is crazy... I can't let anyone know that my service is broken!   
Hey, if I give you this flag, you better keep quiet about this!   
CMSC389R-{i_still_put_the_M_between_the_DV}   
Made in Maryland - Substantial   
```   

Per the request of the assignment:   
```   
Hash From Which I Used to Craft My Crafted Hash: 39511bfcd383d4435920fa569dffed84   
Crafted Hash: 25bef4978dc0b5127a813c8c2ac0ac9f   
Payload Sent to Notary: CMSC389R Rocks!��malicious   
```   

### Part 2 (30 Pts)   

I started by creating my message in `message.public`.  Then I reviewed the lecture slides to determine what commands to use to accomplish this task.      

I began by importing the provided public key:      
`gpg --import pgassignment.key`      
I, then, encrypted the message using the provided public key:      
`gpg -e -r "UMD Cybersecurity president@csec.umiacs.umd.edu" message.public`      
(The lecture slides provided `gpg -e -u "Your name" -r "Their name" msg.txt` generates msg.txt.gpg, but I found that the `-u "Your name"` could be omitted)      
Since I ran this more than once, I found that if you try to overwrite an already existing file, gpg prompts the user and allows them to provide a new file name.  At this time, I wrote the private message to `message.private`.   

The following commands one could type in the terminal to go about:   
* generating keys   
`# gpg --gen-key` (Real name and Email address will be requested, confirmed, and a password will be requested)   
* importing someone else's public keys   
`# gpg --import <other public key>`   
* encrypting a message for that someone else and dumping it to a file   
`gpg -e -u "Your name" -r "Their name" msg.txt`   
