Writeup 5 - Binaries I
======

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION HERE*

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *PUT YOUR NAME HERE*

## Assignment 5 Writeup

`my_memset`
For the first function, I chunk the code into three sections to implement it.  The three sections were essentially one line of the code.   
`void memset(char *str, char val, int strl)`   
I started by taking the parameters and adding them to the stack.  Referencing the lecture slides, I found that parameters were in the following registers:   

`rdi`: 1st parameter   
`rsi`: 2nd parameter   
`rdx`: 3rd parameter   

I then moved onto the loop conditions.  These were simple, because it involved checking the value of the iterator against the parameter.   

I, then, moved onto the body of the loop.  This was a little more complicated for me, since I was originally trying to use all 64 bit registers.  I found that I need to use a lower bit register to access the  character being added and that I had to convert a 4 byte variable (DWORD) to a 8 byte variable (QWORD).

With the loop, I originally had the loop conditions after pushing the parameter to the stack and then trying to jump to the end if the condition (`jl`: `i < strl`).  However, the loop only iterated once with this set up and I found that in x86, for loops are implemented as a do-while loop.   

`my_strncpy`   
I followed the same process as above breaking the code snippet into parts and implementing each.

The difference for this function was implementing the body statement: `dst[i] = src[i]`.  This function was difficult to implement because at first I was receiving segmentation faults (meaning the program was attempting to access an area of memory that it was not allowed to access or had not been assigned yet).  To debug this, I used `gdb`.  I found it helpful to use `layout asm`, which provides a table at the top of the window with each assembly instruction.  I was able to find the line that was causing the segmentation fault and work through debugging my code.

Overall, I felt it helpful to comment what I wanted the line to do and then try to implement it.  Each step had to be broken down to it's simplest form, which turned one line of C code into sometimes 10 lines of x86.
