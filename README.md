# Adif2Cabrillo
Convert Adif file to Cabrillo after contests

This script was written using Python 3, and tested on the Linux computers I 
have. In theory it will run on any device that has Python installed, so go 
wild.

Before running the script, edit the first few lines to your name, callsign,
state, and section.
Run the script. It will prompt you for the ADIF file name, then the file name 
to write 
as Cabrillo format. Finally it will prompt for the name of the contest. This
should be whatever the CONTEST field of the header should be.
The script makes some assumptions to fill out the header fields, but these are
easy to change if its wrong once the file has been generated. You will need to 
edit the file anyway if you want to put in a claimed score or your email, etc. 
This can be done with your favorite text editor.

The script assumes your contest logger has written the transmitted and 
received exchanges to the STX_STRING and SRX_STRING fields of the Adif file. 
This appears to be the adif standard for where this information should go. It 
also assumes the frequency is written in the adif in MHz. It's pretty simple, 
so if you need to change it to match your logging program, it shouldn't be too
hard.

Have fun, and let me know if you find any really horrible bugs!
Jeff, aa6xa
