Flag Hunting - Forensics II, Network Analysis and File Carving/Parsing   
=====   

###### SECTION 1, ASCII (LENGTH: 51)   
Call this number to get your flag: (422) 537 -7946   
Comments:   
* Attempted to call this number, but the number is inactive
* Tried to see if there was anything to do with dial tones, but a flag of the
* Checked T9 Cipher using [InternetMarketingNinjas](https://www.internetmarketingninjas.com/seo-tools/phone-number-spell/)
  * Reviewed the [output](code/WhatDoesSection1PhoneNumberSpell.txt)
  * Determined `HACKERSWIN` was the most viable for a flag   

###### SECTION 2, ARRAY OF WORDS (LENGTH: 60)   
[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]   
Comments:   
* Determined the value outputted is the decimal value for [π](pi) (3.14159265358979)   

###### SECTION 3, COORDINATES (LENGTH: 16)   
(38.99161, -77.02754)  
Comments:    
* Inputted this coordinate into GoogleMaps and viewed in street view   
  * Did not find anything in flag format
* Inputted this coordinate into [GPS-Coordinates.net](https://www.gps-coordinates.net/)   
  * Found address: 8200 Georgia Ave, Silver Spring, MD 20910, USA
  * Inputted this address to determine it's belongs to the restaurant [Golden House](http://silverspringgoldenhouse.com/)
  * Then checked the following review sites to see if any of the recent comments contained the flag format (CMSC389R-{flag})
    * Google Reviews
    * [Yelp](https://www.yelp.com/biz/golden-house-silver-spring-2?q=CMSC389R)
    * [TripAdvisor](https://www.tripadvisor.com/Restaurant_Review-g41378-d5082622-Reviews-Golden_House-Silver_Spring_Montgomery_County_Maryland.html)

###### SECTION 4, REFERENCE (LENGTH: 4)   
Section Number: 1   
Comments:
* Just a reference to the first section

###### SECTION 5, ASCII (LENGTH: 60)   
The imfamous security pr0s at CMSC389R will never find this!   
Comments:
* Checked areas around this string in the hex editor, but found nothing.

###### SECTION 6, ASCII (LENGTH: 991)   
The first recorded uses of steganography Can be traced back to 440 BC when Herodotus Mentions two exampleS in his Histories.[3] Histicaeus s3nt a message to his vassal, Arist8goras, by sha9ving the hRead of his most trusted servan-t, "marking" the message onto his scal{p, then sending him on his way once his hair had rePrown, withl the inastructIon, "WheN thou art come to Miletus, bid _Aristagoras shave thy head, and look thereon." Additionally, demaratus sent a warning about a forthcoming attack to Greece by wrIting it dirfectly on the wooden backing oF a wax tablet before applying i_ts beeswax surFace. Wax tablets were in common use then as reusabLe writing surfAces, sometimes used for shorthand. In his work Polygraphiae Johannes Trithemius developed his so-called "Ave-Maria-Cipher" that can hide information in a Latin praise of God. "Auctor Sapientissimus Conseruans Angelica Deferat Nobis Charitas Gotentissimi Creatoris" for example contains the concealed word VICIPEDIA.[4}   

Comments:
* Noticed that there were random characters that seemed out of place, through close examination, I noticed it included CMSC389 and {}s
  * Then searched the first part of the string and found that the originating text was from [Steganography: History on Wikipedia](https://en.wikipedia.org/wiki/Steganography#History)
  * Using wdiff on I found the portions containing words that were different: `w`
    ```
    $ wdiff -3 section6_text.txt section6_text_wiki.txt
    ======================================================================
     [-Can-] {+can+}
    ======================================================================
     [-Mentions-] {+mentions+}
    ======================================================================
     [-exampleS-] {+examples+}
    ======================================================================
     [-Histicaeus s3nt-] {+Histiaeus sent+}
    ======================================================================
     [-Arist8goras,-] {+Aristagoras,+}
    ======================================================================
     [-sha9ving-] {+shaving+}
    ======================================================================
     [-hRead-] {+head+}
    ======================================================================
     [-servan-t,-] {+servant,+}
    ======================================================================
     [-scal{p,-] {+scalp,+}
    ======================================================================
     [-rePrown, withl-] {+regrown, with+}
    ======================================================================
     [-inastructIon, "WheN-] {+instruction, "When+}
    ======================================================================
     [-_Aristagoras-] {+Aristagoras+}
    ======================================================================
     [-demaratus-] {+Demaratus+}
    ======================================================================
     [-wrIting-] {+writing+}
    ======================================================================
     [-dirfectly-] {+directly+}
    ======================================================================
     [-oF-] {+of+}
    ======================================================================
     [-i_ts-] {+its+}
    ======================================================================
     [-surFace.-] {+surface.+}
    ======================================================================
     [-reusabLe-] {+reusable+}
    ======================================================================
     [-surfAces,-] {+surfaces,+}
    ======================================================================
     [-Gotentissimi-] {+Potentissimi+}
    ======================================================================
     [-VICIPEDIA.[4}-] {+VICIPEDIA.[4]+}
    ======================================================================
    ```
  * Then manually went through and removed the extract characters in each string:    
    `CMSc389R -{PlaIN_dIfF_FLAG}`

###### SECTION 7, COORDINDATES (LENGTH: 16)   
(38.9910941, -76.9328019)   
Comments:   
* Inputted this coordinate into GoogleMaps and viewed in street view   
  * Did not find anything in flag format
* Inputted this coordinate into [GPS-Coordinates.net](https://www.gps-coordinates.net/)   
  * Found address: 8145 Baltimore Ave, College Park, MD 20740, USA
  * Inputted this address to determine it belongs to Campus Village Shoppes with houses multiple restaurants and shops (different suite numbers):   
    * Food Factory   
    * Hanami Japanese Restaurant   
    * DP Dough
  * Then checked the following review sites to see if any of the recent comments contained the flag format (CMSC389R-{flag})
    * Google Reviews
    * [Yelp](https://www.yelp.com/biz/golden-house-silver-spring-2?q=CMSC389R)
    * [TripAdvisor](https://www.tripadvisor.com/Restaurant_Review-g41378-d5082622-Reviews-Golden_House-Silver_Spring_Montgomery_County_Maryland.html)

###### SECTION 8, PNG (LENGTH: 245614)   
Outputted to Section8.png   

Comments:   
* Opened the file and found a flag in the image
  * Found: `CMSC389R-{c0rn3rst0ne_airlin3s_to_the_moon}`

###### SECTION 9, ASCII (LENGTH: 22)   
AF(saSAdf1AD)Snz**asd1   

Comments:
* Unable to determine what could be used to translated   

###### SECTION 10, ASCII (45)   
Q01TQzM4OVIte2gxZGQzbi1zM2N0MTBuLTFuLWYxbDN9   

Comments:
* Determined the string was encoded in Base64
* Found: `CMSC389R-{h1dd3n-s3ct10n-1n-f1l3}`

###### SECTION 11, ARRAY OF DOUBLES (LENGTH: 48)   
[4, 8, 15, 16, 23, 42]   

Comments:
* Put the array into Google and found the are ["the numbers" that frequently recurred in Lost](https://lostpedia.fandom.com/wiki/The_Numbers)   
