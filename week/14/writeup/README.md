Writeup 10 - Crypto II
=====

Name: *Brianna Higgins*
Section: *0201*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Brianna Higgins*

## Assignment 10 Writeup

### Part 1 (70 Pts)

Starting from the initial request, it is apparent that the task will incorporate a possible SQL injection.  This was determined from the bolded letters in the starting point "**S**uch a **q**uick, **l**ittle".  

When originally visiting the [website](http://cornerstoneairlines.co:8080/), it was discovered it belongs to the "Cornerstone Airlines Shop".  Upon checking the various pages on the website, it was found that it is simple in design and allows the user to click on hyperlinks to view various products.  The website did not provide an visible input fields, so using an input field to initiate an attack was not an option.  

Without an visible input fields on the website, I looked at the source code of the main page and found that a table was being generated.  Each item in the table had a hypertext reference containing `/item?id=#`, where # is the id number of each item.  Referencing the slides from detailing sql injection, I put the string `0' or '1'='1`.  (This was tested through Google Translate, since I attempted to do this on campus). This displayed all the output contained in the table and contained:
```
FLAG
CMSC38R-{y0U-are_the_5ql_n1nja}
$ priceless
```

### Part 2 (30 Pts)

https://xss-game.appspot.com/

On the welcome page, they promise there will be cake at the end!   

#### Level 1: Hello, *w*orld of XSS

Since the page provides an input field, I started by inserting a `<script>alert();</script>` into the query box and hitting the search button.  Success and onto Level 2.

#### Level 2: Persistence is key
Since the page provided another input field, I attempted to repeat what I did in Level 1 to no avail.  I, then, tested to see if the input field took HTML format by testing `<strong>Test</strong>`.  This worked, so I tried to see if I could create an HTML button that will alert when clicked: `<button onclick="alert()"`.  When the page reloaded, the button appeared and upon clicking it, the alert displayed.  Success and onto Level 3.

#### Level 3: That sinking feeling...
This level provided "Since you can't enter your payload anywhere in the application, you will have to manually edit the address in the URL bar below".  This was useful without using the hints, so I checked the format of the URL.  It appears that the number of the image goes at the end of the URL `/level3/frame#<value>` where <value> is the number of the image.  I tested `/level3/frame#4` which displayed the text Image 4 and broken image icon.  Seeing this, I attempted to `/level3/frame#4'onerror="alert()"`, since the image shouldn't load.  Success and onto Level 4.

#### Level 4: Context matters
This level provided an input box again, running the original timer, it opens another page with the URL `https://xss-game.appspot.com/level4/frame?timer=3`.  Similar to the SQL injection from Part I, I attempted to add `');alert('` to the end of the script to end the script and include an alert.  Success and onto Level 5.

#### Level 5: Breaking protocol
This level provided an initial page with a hyperlink to `Sign up`.  This redirects to a page with a textbox to enter an email and a submit feature.  The URL for page ended with `signup?next=confirm`.  In the URL is provides what the next button on the page.  Seeing this, I changed the value to `next=javascript:alert()` and reloaded the page.  Then, after entering a value into the textbox and hitting next, the alert window appeared.  Success and onto Level 6.

#### Level 6: Follow the "White Rabbit"
The last level provides the objective "Find a way to make the __make the application request an external file__ which will cause it to execute an alert()."  Looking at the page, it shows that it loads the file from the URL "/static/gadget.js".  I googled `static/gadget.js` and found that it's from the Google API.  I attempted to find a file that would alert, but to no avail, so I decided to take a new approach to the problem, by creating the "external file" within the URL.  After doing some research, you can do this by using `data:text/plain`.  Using this, I tried `/level6/frame#data:text/plain,alert()` and the alert appeared.  Success, now time to debrief.

#### Congratulations!
As promised, there was cake at the end!
