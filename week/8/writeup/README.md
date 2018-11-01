Writeup 8 - Forensics II, Network Analysis and File Carving/Parsing
=====

Name: *Brianna Higgins*
Section: *201*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Brianna Higgins*

## Assignment 8 Writeup

### Part 1 (45 Pts)
1. The hackers used the **traceroute** command on the following websites:   
  * csec.umd.edu (packet: 138-141)  [Screenshot from Wireshark ](images/wireshark_traceroute_csec.png)  
  * google.com (packets: 502-505)   

2. The hackers use the names `laz0rh4x` and `c0uchpot4doz`.  (Found in the [Chatroom Text](chatroom sessions/))

3. The hacker, `laz0rh4x`, is using IP 104.248.224.85 and connecting from DigitalOcean, US, NYC.   
The hacker, `c0uchpot4dox`, is using IP 206.189.113.189 and connecting from DigitalOcean, US, NYC.    
(found using `whois` command)  

4. The hackers used `Port 2749` to communicate on the server.   
  (Found in the info field of packets in Wireshark)

5. They mentioned their plans in the chatroom, saying it is set for "tomorrow at 1500" (The date of the original session was 24 October 2018 around 2245 EDT, so the plans would have happened on 25 October 2018).
Chatroom sessions can be found: [c0uchpot4dox](chatsessions/chatroom_session_c0c0uchpot4dox.txt) and [laz0rh4x](chatsessions/chatroom_session_laz0rh4x.txt)

6. They sent a file via google drive: [https://drive.google.com/file/d/1McOX5WjeVHNLyTBNXqbOde7l8SAQ3DoI/view?usp=sharing](https://drive.google.com/file/d/1McOX5WjeVHNLyTBNXqbOde7l8SAQ3DoI/view?usp=sharing)

7. They expect to see each other the next day (25 October 2018).

### Part 2 (55 Pts)

1. Parser can be found: [stub.py](code/stub.py)   

2. The following information was gathered using [stub.py](code/stub.py) to parse [update.fpff](code/update.fpff)
    1. `update.fpff` was generated `2018-10-25 00:40:07`.   
    2. `update.fpff` was authored by `laz0rh4x`.   
    3. According the `section count` found in the header of `update.fpff`, there *should be* `9` sections.  However letting the parse until the end of the file reveals there are *really* `11` sections.
    4. The following information is the generated output from [stub.py](code/stub.py).
    ```
    ------- HEADER -------
    MAGIC: 0xdeadbeef
    VERSION: 1
    TIMESTAMP: 2018-10-25 00:40:07
    AUTHOR: laz0rh4x
    SECTION COUNT: 9
    ```
    ```
    -------  BODY  -------
    SECTION 1
    TYPE: SECTION_ASCII (0x9) LENGTH: 51 (0x33)
    Call this number to get your flag: (422) 537 - 7946
    # Comment: This phone number is currently inactive if called.

    SECTION 2
    TYPE: SECTION_WORDS (0x5) LENGTH: 60 (0x3c)
    [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
    # Comment: This is pi: 3.14159265358979

    SECTION 3
    TYPE: SECTION_COORD (0x6) LENGTH: 16 (0x10)
    (38.99161, -77.02754)
    # Comment: These coordinates are located in Silver Spring (8212 Colonial Ln, Silver Spring, MD 20910, USA)

    SECTION 4
    TYPE: SECTION_REFERENCE (0x7) LENGTH: 4 (0x4)
    Section Number: 1

    SECTION 5
    TYPE: SECTION_ASCII (0x9) LENGTH: 60 (0x3c)
    The imfamous security pr0s at CMSC389R will never find this!

    SECTION 6
    TYPE: SECTION_ASCII (0x9) LENGTH: 991 (0x3df)
    The first recorded uses of steganography Can be traced back to 440 BC when Herodotus Mentions two exampleS in his Histories.[3] Histicaeus s3nt a message to his vassal, Arist8goras, by sha9ving the hRead of his most trusted servan-t, "marking" the message onto his scal{p, then sending him on his way once his hair had rePrown, withl the inastructIon, "WheN thou art come to Miletus, bid _Aristagoras shave thy head, and look thereon." Additionally, demaratus sent a warning about a forthcoming attack to Greece by wrIting it dirfectly on the wooden backing oF a wax tablet before applying i_ts beeswax surFace. Wax tablets were in common use then as reusabLe writing surfAces, sometimes used for shorthand. In his work Polygraphiae Johannes Trithemius developed his so-called "Ave-Maria-Cipher" that can hide information in a Latin praise of God. "Auctor Sapientissimus Conseruans Angelica Deferat Nobis Charitas Gotentissimi Creatoris" for example contains the concealed word VICIPEDIA.[4}
    # Comment: Contains hidden flag

    SECTION 7
    TYPE: SECTION_COORD (0x6) LENGTH: 16 (0x10)
    (38.9910941, -76.9328019)
    # Comment: These coordinates are located in College Park (8145 Baltimore Ave, College Park, MD 20740, USA)

    SECTION 8
    TYPE: SECTION_PNG (0x1) LENGTH: 245614 (0x3bf6e)
    Outputted to Section8.png
    # Comment: Contains flag in text of image

    SECTION 9
    TYPE: SECTION_ASCII (0x9) LENGTH: 22 (0x16)
    AF(saSAdf1AD)Snz**asd1

    SECTION 10
    TYPE: SECTION_ASCII (0x9) LENGTH: 45 (0x2d)
    Q01TQzM4OVIte2gxZGQzbi1zM2N0MTBuLTFuLWYxbDN9
    # Comment: Base64 for flag

    SECTION 11
    TYPE: SECTION_DWORDS (0x2) LENGTH: 48 (0x30)
    [4, 8, 15, 16, 23, 42]
    # Comment: "The numbers" that frequently recurred in Lost (https://lostpedia.fandom.com/wiki/The_Numbers)
    ```   
    5. The following flags were found in [update.fpff](code/update.fpff)   
      * Section 6: `CMSc389R -{PlaIN_dIfF_FLAG}`   
      Found by doing a wdiff on the output from Section 6 with the text from [Steganography: History on Wikipedia](https://en.wikipedia.org/wiki/Steganography#History), the extra characters translated to a flag.   
      * Section 8: `CMSC389R-{c0rn3rst0ne_airlin3s_to_the_moon}`   
      Text found in [Section8.png](images/Section8.png)   
      * Section 10: `CMSC389R-{h1dd3n-s3ct10n-1n-f1l3}`   
      Convert output from Section 10 from Base64 to ASCII   
