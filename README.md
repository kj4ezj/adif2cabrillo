# adif2cabrillo
> Forked from [kabelj/Adif2Cabrillo](https://github.com/kabelj/Adif2Cabrillo).
> Thank you Jeff ([AA6XA](https://www.qrz.com/db/AA6XA)) for your work creating the original, and for giving back to the FLOSS and ham radio community!

Use this Python 3 script to convert [ADIF files](https://www.adif.org) (\*.adi, \*.adif) to [Cabrillo format](https://wwrof.org/cabrillo) (\*.log, \*.cbr) to submit for contests. I run this on Linux Mint but it should "just work" on any computer with Python 3.

<!-- contents box begin -->
<table>
<tr/>
<tr>
<td>
<p/>
<div align="center">
<b>Contents</b>
</div>
<p/>
<!-- contents markdown begin -->

1. [Usage](#usage)
1. [See Also](#see-also)

<!-- contents markdown end -->
<p/>
</td>
</tr>
</table>
<!-- contents box end -->

This fork is designed _specifically for [klog](https://github.com/ea4k/klog)_ because the upstream `adif2cabrillo` program was incompatible with `klog`. It parses the `QTH` field for locations, and looks for serial numbers in the `COMMENTS` field while ignoring numbers like "10m" in "ARRL 10m contest" if you put stuff like that in your comments.

## Usage
Clone this repo.
```bash
git clone git@github.com:ea4k/klog.git
```
Navigate into the repo, open the script with your text editor of choice...
```bash
vim adif2cabrillo.py
```
...and edit the stuff at the top of the file. You will need to edit all of the `my*` variables, as well as the header fields (e.g. `CATEGORY-OPERATOR`). Once you have all that filled in, save the file and close your editor.

Finally, run the program.
```bash
./adif2cabrillo.py
```
It will prompt you for the ADIF file name, then the file name to write in Cabrillo format.

## See Also
Here are some links I found helpful.
- [adif.org](https://www.adif.org) - ADIF specification
- [arrl.org](https://www.arrl.org)
    - [10m Contest](https://www.arrl.org/10-meter)
    - [Cabrillo Tutorials](https://www.arrl.org/cabrillo-format-tutorial)
    - [Contest Log Submission](https://contest-log-submission.arrl.org)
    - [Multipliers](https://contests.arrl.org/contestmultipliers.php)
        - [Canada](https://contests.arrl.org/contestmultipliers.php?a=ve)
        - [Mexico](https://contests.arrl.org/contestmultipliers.php?a=xe)
        - [United States](https://contests.arrl.org/contestmultipliers.php?a=usa)
        - [US Sections](https://contests.arrl.org/contestmultipliers.php?a=wve)
- [Cabrillo Specification](https://wwrof.org/cabrillo)
    - [Header](https://wwrof.org/cabrillo/cabrillo-v3-header)
    - [QSO Data](https://wwrof.org/cabrillo/cabrillo-qso-data)
- [klog](https://github.com/ea4k/klog)
