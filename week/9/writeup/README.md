Writeup 9 - Crypto I
=====

Name: *Brianna Higgins*
Section: *0201*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgment of honor pledge: *Brianna Higgins*

## Assignment 9 Writeup

### Part 1 (60 Pts)

A [few SHA512 passwords](hashes) were recovered from the Cornerstone Airlines web server and based on a gut feeling, these passwords come from this [password list](probable-v2-top1575).  On the Cornerstone Airlines, hints were found indicating that each password is *salted* by pre-pending a single, lowercase character ('a', 'b', ..., 'z'), though there was no indication if the same salt is used for each password.  The script, [part1.py](part1.py), was written to brute force each of these hashes, and print out each of the salts and passwords found.

Given the provided information about the passwords, the script was written to loop through all the possible *salts*, since there was no indication that the same salt was used for each password.  The script, then, loops through all the words in the password list.  Through these loops, every possible combination of password appended by salt is created.  These salt+password combinations were then encrypted using SHA512 and stored as hexadecimal values.  These hexadecimal values were then compared to the recovered hashes.  When a match was found, the matching hash is outputted, followed by the salt+password combination.  

The following salt+password combinations were determined to produce the hashes recovered from the Cornerstone Airlines web server:
```
Hash: 9a23df618219099dae46ccb917fbc42ddf1bcf80583ec980d95eaab4ebee49c7a6e1bac13882cf5dd8d3850c137fdff378e53810e98f7e9508ca8516e883458e
Salt: k Password: neptune
Hash: c35eb97205dd1c1a251ad9ea824c384e5d0668899ce7fbf269f99f6457bd06055440fba178593b1f9d4bfbc7e968d48709bc03e7ff57056230a79bc6b85d92c8
Salt: m Password: jordan
Hash: 70a2fc11b142c8974c10a8935b218186e9ecdad4d1c4f28ec2e91553bd60cfff2cc9b5be07e206a2dae3906b75c83062e1afe28ebe0748a214307bcb03ad116f
Salt: p Password: pizza
Hash: d39d933d91c3e4455beb4add6de0a48dafcf9cb7acd23e3c066542161dcc8a719cbac9ae1eb7c9e71a7530400795f574bd55df17a2d496089cd70f8ae34bf267
Salt: u Password: loveyou
```

### Part 2 (40 Pts)

An interesting trivia was found running on a distant computer, `142.93.117.193 7331`.  From prior experience with highly-contrived, if all the questions are answered, a reward will be provided (in this case a flag).  The script, [part2.py](part2.py), was written to interact with this distant computer by answering all the questions and collecting the reward.   

The distant computer was connected to using `nc 142.93.117.193 7331`.  Upon the connection, the following message was displayed:   
```
=========================================
Hello there! Welcome to my hash workshop.
=========================================
Find me the sha512 hash of CuTU9a1zX3
>>>
```  
From this, it was determined that the format for each question is:
`Find me the <encoding requested> hash of <value>`   
Based on this, the `encoding requested` and `values` were collected for the question and used to encrypt the value using the requested encoding.  Originally, the encoding was done by checking the encoding against pre-determined hash encodings, however upon further inspection of the `hashlib` documentation, the encoding could be sent directly into the function.  This replaced 23 lines of if/else statements to 3 lines of python code.  This value was then sent back to the distant computer, appended with an '\n' to simulate the enter key being pressed and submitting the answer to the trivia question.   

After the first answer was sent, another question was printed using the same format.  Since there was no indication for how many questions were contained per trivia round, the script continued to answer questions until there we no questions left to answer.  After running the script, it was determined the game ends with a final line containing `You win!`.  A condition checking whether `win` is contained in the output from the distant computer was added to stop the script once the game ended.   

In the final line, the following flag was found:
`CMSC389R-{H4sh-5l!ngInG-h@sH3r}`
