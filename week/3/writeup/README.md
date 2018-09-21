Writeup 3 - OSINT II, OpSec and RE
======

Name: *Brianna Higgins*
Section: *0201*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Brianna Higgins*

## Assignment 3 Writeup

### Part 1 (100 pts)

A security evaluation exercise of  CornerstoneAirlines was conducted during the timeframe of 7 September 2018 - 13 September 2018.  This security evaluation was requested by the company and resulted in the identification of multiple vulnerabilities.  Per the request of Fred Krueger, owner of the website, the following suggestions are provided as guidance in how the vulnerabilities discovered can be repaired.

##### 1. Strength of Passwords
The password that was used for Fred Krueger's account on the Administrator server was identified to be 'pokemon'.  Two approaches could be used to determine this password: (1) by using a bruteforce attack using a dictionary and (2) by entering a known interest of the user.  From this, it is suggested that minimum password requirements be implemented for the server.  Lafayette University provides [guidelines for strong passwords](https://its.lafayette.edu/policies/strongpasswords/) which can provide a basis for this policy.  This websites identifies that weak passwords include those that:
- Any word that can be found in a dictionary, in any language (e.g., airplane or aeroplano).
- A dictionary word with some letters simply replaced by numbers (e.g., a1rplan3 or aer0plan0).
- A repeated character or a series of characters (e.g., AAAAA or 12345).
- A keyboard series of characters (e.g., qwerty or poiuy).
- Personal information (e.g., birthdays, names of pets or friends, Social Security number, addresses).   

As was demonstrated during the exercise, Mr. Krueger’s password was able to be identified in less than an hour using an open source dictionary of known passwords.  Following Lafayatte University’s guidelines, it is suggested that passwords
- Are at least 8 characters—the more characters, the better
- Contain a mixture of both uppercase and lowercase letters
- Contain a mixture of letters and numbers
- Include at least one special character, e.g., ! @ # ? ]
  - Prevent the usage of < or >, as they might cause problems   

These requirements can be enforced when the passwords are being created.  The system can check if the password created is found within known open source password dictionaries and check that the minimum requirements are met.   

Another suggestion would be to implement a form of two-factor authentication, which would allow the users to utilize something they know (such as a short pin or password) and something they have (such as a phone or other device) in which they can use to receive a one-time code.  This would require more work from an attacker to acquire both components to effectively identify the password.  The brute force dictionary attack that was used during the exercise would be ineffective, as the one-time code would be changing during the course of the attack running.   

By enforcing the use of strong passwords or implementing the use of two-factor authentication for this server, it will allow for the server to be more secure and for the data stored on it to be better protected.


##### 2. Exposed Administrator Server
The company's public website contains an obvious navigation link to the company's administrator server.  In the navigation bar of the website, there is an element titled 'Admin' and when the user visits the page, it provides the IP address to the server.  To address this vulnerability, CornerstoneAirlines should not link the administrative server to the public website.  A better security practice would be provide the IP address only to internal personnel to the company and to require valid credentials for the IP address to be accessed.  Referencing the [National Institute of Standards and Technology (NIST) suggestions - Web Server Security Requirements Guide (SRG)](https://www.stigviewer.com/stig/web_server_security_requirements_guide/), V5597 states, “A web server that is part of a web server cluster must route all remote management through a centrally managed access control point.”  By not allowing all users to access this page, it would prevent the IP address of the administrator server from being exposed.  An alternative page containing the message “Access Denied” or “Page Not Found” could be created with the address routing to “CornerstoneAirlines.co/404PageNotFound” to mask the IP address and keep the integrity of the company’s administrator server.

##### 3. Repetitive Command Execution
Over the course of the exercise, the administrator server was inundated with commands at a rate that would not be attributed to a normal user.  During the brute force attack to enter the server, hundreds of commands were being sent to the server and no security measure was in place to disrupt them.  From this vulnerability, it is suggested to implement a lockout threshold for each account.  Microsoft outlines this idea in this [account lockout threshold overview](
https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/account-lockout-threshold) and provides information for implementation.  Similar to the above suggestions, it will counter the ability to effectively execute a continued brute force attack on the server by requiring the user to validate their identity or waiting for a cold down period before the attempt can be continued.
