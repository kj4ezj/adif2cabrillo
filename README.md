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
1. [Example](#example)
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
git@github.com:kj4ezj/adif2cabrillo.git
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

## Example
Given a file named `input.adi` in the root of this repo...
```aidf
ADIF v3.1.0 Export from KLog
https://www.klog.xyz/klog
<PROGRAMVERSION:5>2.3.4
<PROGRAMID:4>KLOG <APP_KLOG_QSOS:3>153<APP_KLOG_LOG_DATE_EXPORT:13>20241222-1537<EOH>
<CALL:5>N4JHP <QSO_DATE:8>20241214 <TIME_ON:6>023539 <RST_RCVD:2>57 <RST_SENT:2>57 <BAND:3>10M <MODE:3>SSB <SUBMODE:3>USB <CQZ:1>5 <ITUZ:1>8 <DXCC:3>291 <COMMENT:16>ARRL 10m contest <CLUBLOG_QSO_UPLOAD_STATUS:1>Y <CONT:2>NA <DARC_DOK:1>8 <EQSL_QSL_RCVD:1>N <EQSL_QSLRDATE:8>20241213 <EQSL_QSL_SENT:1>Y <EQSL_QSLSDATE:8>20241214 <FREQ:4>28.5 <GRIDSQUARE:6>EM97RF <LOTW_QSLRDATE:8>20241213 <LOTW_QSLSDATE:8>20241213 <LOTW_QSL_RCVD:1>N <LOTW_QSL_SENT:1>N <MY_ANTENNA:9>Antron 99 <MY_GRIDSQUARE:6>AB12ce <MY_RIG:12>Yaesu FT-900 <NAME:12>Jason <OPERATOR:5>KZ4KI <PROP_MODE:5>ION <QRZCOM_QSO_UPLOAD_STATUS:1>Y <QSL_RCVD:1>N <QSL_SENT:1>N <QSO_COMPLETE:1>Y <QSO_RANDOM:1>Y <QTH:20>Blacksburg, Virginia <SRX:1>0 <STX:1>0 <STATION_CALLSIGN:5>KZ4KI <TX_PWR:3>100 <EOR>
<CALL:5>VE6FI <QSO_DATE:8>20241214 <TIME_ON:6>165828 <RST_RCVD:2>59 <RST_SENT:2>59 <BAND:3>10M <MODE:3>SSB <SUBMODE:3>USB <CQZ:1>5 <ITUZ:1>9 <DXCC:1>1 <COMMENT:16>ARRL 10m contest <CLUBLOG_QSO_UPLOAD_STATUS:1>Y <CONT:2>NA <DARC_DOK:4>3127 <EQSL_QSL_RCVD:1>N <EQSL_QSLRDATE:8>20241214 <EQSL_QSL_SENT:1>Y <EQSL_QSLSDATE:8>20241217 <FREQ:6>28.482 <GRIDSQUARE:6>DO33ER <LOTW_QSLRDATE:8>20241214 <LOTW_QSLSDATE:8>20241214 <LOTW_QSL_RCVD:1>N <LOTW_QSL_SENT:1>N <MY_ANTENNA:9>Antron 99 <MY_GRIDSQUARE:6>AB12ce <MY_RIG:12>Yaesu FT-900 <NAME:30>Evan or Denis <PROP_MODE:3>ION <QRZCOM_QSO_UPLOAD_STATUS:1>Y <QSL_RCVD:1>N <QSL_SENT:1>N <QSO_COMPLETE:1>Y <QSO_RANDOM:1>Y <QTH:32>Sturgeon County, Alberta, Canada <SRX:1>0 <STX:1>0 <STATION_CALLSIGN:5>KZ4KI <TX_PWR:3>100 <EOR>
<CALL:4>XE3R <QSO_DATE:8>20241214 <TIME_ON:6>170437 <RST_RCVD:2>59 <RST_SENT:2>59 <BAND:3>10M <MODE:3>SSB <SUBMODE:3>USB <CQZ:1>6 <ITUZ:2>10 <DXCC:2>50 <COMMENT:16>ARRL 10m contest <CLUBLOG_QSO_UPLOAD_STATUS:1>Y <CONT:2>NA <DARC_DOK:4>2678 <EQSL_QSL_RCVD:1>N <EQSL_QSLRDATE:8>20241214 <EQSL_QSL_SENT:1>Y <EQSL_QSLSDATE:8>20241217 <FREQ:6>28.466 <GRIDSQUARE:6>EK09KK <LOTW_QSLRDATE:8>20241214 <LOTW_QSLSDATE:8>20241214 <LOTW_QSL_RCVD:1>N <LOTW_QSL_SENT:1>N <MY_ANTENNA:9>Antron 99 <MY_GRIDSQUARE:6>AB12ce <MY_RIG:12>Yaesu FT-900 <NAME:13>Mario Fuentes <PROP_MODE:3>ION <QRZCOM_QSO_UPLOAD_STATUS:1>Y <QSL_RCVD:1>N <QSL_SENT:1>N <QSO_COMPLETE:1>Y <QSO_RANDOM:1>Y <QTH:11>COA, Mexico <SRX:1>0 <STX:1>0 <STATION_CALLSIGN:5>KZ4KI <TX_PWR:3>100 <EOR>
<CALL:4>OR6T <QSO_DATE:8>20241214 <TIME_ON:6>171648 <RST_RCVD:2>59 <RST_SENT:2>59 <BAND:3>10M <MODE:3>SSB <SUBMODE:3>USB <CQZ:2>14 <ITUZ:2>27 <DXCC:3>209 <COMMENT:22>ARRL 10m contest - 868 <CLUBLOG_QSO_UPLOAD_STATUS:1>Y <CONT:2>EU <DARC_DOK:4>6596 <EQSL_QSL_RCVD:1>N <EQSL_QSLRDATE:8>20241214 <EQSL_QSL_SENT:1>Y <EQSL_QSLSDATE:8>20241217 <FREQ:5>28.44 <GRIDSQUARE:6>JO20KV <LOTW_QSLRDATE:8>20241214 <LOTW_QSLSDATE:8>20241214 <LOTW_QSL_RCVD:1>N <LOTW_QSL_SENT:1>N <MY_ANTENNA:9>Antron 99 <MY_GRIDSQUARE:6>AB12ce <MY_RIG:12>Yaesu FT-900 <NAME:23>Hagelandse Contest Club <PROP_MODE:3>ION <QRZCOM_QSO_UPLOAD_STATUS:1>Y <QSL_RCVD:1>N <QSL_SENT:1>N <QSO_COMPLETE:1>Y <QSO_RANDOM:1>Y <QTH:20>Tielt-Winge, Belgium <SRX:1>0 <STX:1>0 <STATION_CALLSIGN:5>KZ4KI <TX_PWR:3>100 <EOR>
```
...running this program as-is (without changing the `my*` variables or contest details)...
```bash
./adif2cabrillo.py
```
...then entering `input.adi` for the input filename prompt and `output.log` for the output filename prompt, there will be a file called `output.log` in the root of this repo containing the following:
```cabrillo
START-OF-LOG: 3.0
CONTEST: ARRL-10
LOCATION: SCV
CALLSIGN: AA6XA
CATEGORY-OPERATOR: SINGLE-OP
CATEGORY-TRANSMITTER: ONE
CATEGORY-POWER: LOW
CATEGORY-ASSISTED: NON-ASSISTED
CATEGORY-BAND: 10M
CATEGORY-MODE: SSB
CATEGORY-STATION: FIXED
CATEGORY-OVERLAY: LIMITED
CERTIFICATE: YES
CLAIMED-SCORE: 
CREATED-BY: https://github.com/kj4ezj/adif2cabrillo/tree/v0.1.0
GRID-LOCATOR: AB12ce
NAME: JEFF
ADDRESS: Winchester Mystery House
ADDRESS: 525 S Winchester Blvd
ADDRESS: San Jose, CA
ADDRESS: 95128
EMAIL: someone@example.com
OPERATORS: AA6XA
SOAPBOX: 
QSO: 28500 PH 2024-12-14 0235 AA6XA 57 CA N4JHP 57 VA
QSO: 28482 PH 2024-12-14 1658 AA6XA 59 CA VE6FI 59 AB
QSO: 28466 PH 2024-12-14 1704 AA6XA 59 CA XE3R 59 COA
QSO: 28440 PH 2024-12-14 1716 AA6XA 59 CA OR6T 59 868
END-OF-LOG:
```
Then I review the file, count my QSOs...
```bash
cat output.log | grep -cP '^QSO'
```
...calculate my score, manually add it to `CLAIMED-SCORE` in the header, and submit it!

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

***
> **_Legal Notice_**  
> This repo contains assets created in collaboration with a large language model, machine learning algorithm, or weak artificial intelligence (AI). This notice is required in some countries.
