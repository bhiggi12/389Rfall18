Writeup 7 - Forensics I
======

Name: *Brianna Higgins*
Section: *0201*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Brianna Higgins*

## Assignment 7 Writeup

### Part 1 (40 pts)

1. The file is JPEG file.   
  From `file image`:
  ```   
  image: JPEG image data
  ```
  From `exiftool image`:   
  ```
  File Type : JPEG
  ```   


2. The photo was taken John Hancock Center in Chicago, Illinois, United States.   
  From `exiftool image`:   
  ```
  GPS Latitude  : 41 deg 53' 54.87" N
  GPS Longitude : 87 deg 37' 22.53" N
  GPS Position  : 41 deg 53' 54.87" N, 87 deg 37' 22.53" W
  ```

3. The photo was taken August 22, 2018 at 11:33:24.   
  From `exiftool image`:   
  ```
  Date/Time Original  : 2018:08:22 11:33:24
  Create Date         : 2018:08:22 11:33:24
  ```

4. This was taken using the back camera of an Apple iPhone 8.   
  From `exiftool image`:      
  ```
  Make              : Apple
  Camera Model Name : iPhone 8
  Lens Make         : Apple
  Lens Model        : iPhone 8 back camera 3.99m f/1.8
  ```

5. This photo was taken at 539.537 meters above sea level.   
  From `exif image`:
  ```
  Altitude Reference : Sea Level
  Altitude           : 539.537
  ```
  From `exiftool image`:
  ```
  GPS Altitude : 539.5 m Above Sea Level
  ```

6. The following flags were found:
  * Using `strings - n 15 image`:   
  `CMSC389R-{look_I_f0und_a_str1ng}`

  * Using `binwalk --dd="png:png" image`:   
  `CMSC389R-{abr@cadabra}`   

    ```
    kali:~/week7# binwalk --dd="png:png" image

    DECIMAL       HEXADECIMAL     DESCRIPTION
    --------------------------------------------------------------------------------
    0             0x0             JPEG image data, EXIF standard
    12            0xC             TIFF image data, big-endian, offset of first image directory: 8
    9899          0x26AB          Copyright string: "Copyright Apple Inc., 2017"
    2395936       0x248F20        PNG image, 960 x 720, 8-bit/color RGBA, non-interlaced
    2395977       0x248F49        Zlib compressed data, best compression

    kali:~/week7# cd _image.extracted/
    kali:~/week7/_image.extracted# ls
    248F20.png  248F49  248F49.zlib
    ```
    [View 248F20.png Here](images/248F20.png)

### Part 2 (60 pts)
Flag: `CMSC389R-{dropping_files_is_fun}`  

Using `file binary`, I determined `binary` was an ELF (Executable and Linkable Format) file, which is a common standard file format for executable files, object code, shared libraries, and core dumps.
```
kali:~/week7# file binary
binary: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=f746ed8f3cb01a771dd1a2379285153e3c0fd18f, not stripped
```

With this information, I changed the file to an executable file using `chmod +x binary` and ran file using `./binary`.  This output "Where is your flag?"  Checking within the folder, I found that there was no file outputted in the folder.  
```
kali:~/week7# chmod +x binary
kali:~/week7# ./binary
Where is your flag?
```   

To understand what this file was doing, I decided to look at the underlying code using Cutter.  Using the Pseudocode Window in Cutter, I determined the executable's behavior is as follows:
1. Creates a string `/tmp/.stego`   
2. Opens the file `/tmp/.stego`   
3. Writes something to `/tmp/.stego`   
4. Closes `/temp/.stego`   
5. Outputs `Where is your flag?`   

Code: [Psuedocode Generated with Cutter](code/binary_pseudocode.txt)

After learning the behavior of this file and having already executed the file, I checked the `tmp` folder and found the `.stego` file.  (`ls -a` was used, since the leading `.` means the file is hidden.)
```
kali:/tmp# ls -a
.
..
.stego
```

Using similar tasks to Part 1, I checked the file type for `.stego` and found that it was a data file.  Which was not very helpful.   
```
kali:/tmp# file .stego
.stego: data
```

I, then, used `binwalk` to search for embedded files and executable code.  I found there was a JPEG image.
```
kali:/tmp# binwalk -e .stego

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
1             0x1             JPEG image data, JFIF standard 1.01
```

I opened the file in a hex editor to look at position 0x1.  Referencing [Gary Kessler's File Signatures](https://www.garykessler.net/library/file_sigs.html), I found that the file signature for a JPEG image is a leading `FF D8 FF E0 xx xx 4A 46 49 46 00` and a trailing `FF D9`.  Reviewing `.stego`, I found that the file begins with `00 FF D8 FF E0 00 10 4A 46 49 46 00` and ends with `FF`.  Based on this I removed the leading `00` and added `D9` to the end.

I, then, attempted to open [.stego](images/stego) with an image viewer and found it was showed an image of a stegosaurus.  After checking `ExifTool` and `strings` and finding nothing, I checked to see if anything was hidden in the image using `steghide`.  I tried the passphrase `stegosaurus` and the file was output.
```
kali:/tmp#
steghide extract -sf .stego -xf stego_out.txt
Enter passphrase:
wrote extracted data to "stego_out.txt".
```
Checking the output of [stego_out.txt](extras/stego_out.txt), the flag was found.
```
kali:/tmp# cat stego_out.txt
Congrats! Your flag is: CMSC389R-{dropping_files_is_fun}
```
