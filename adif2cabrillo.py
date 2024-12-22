# Convert adif file to cabrillo for NAQP
myCall = "AA6XA"
myName = "JEFF"
myState = "CA"
mySection = "SCV"

adifFlnm = input('Enter Adif filename to read: ')
cabFlnm = input('Enter Cabrillo filename to write: ')

fAdif = open(adifFlnm, 'r')
fCab = open(cabFlnm, 'w')

contest = input("Contest name: ")
#write the fixed header
version = 0.11
fCab.write("START-OF-LOG: 3.0\n")
fCab.write("CONTEST: "+contest+"\n")
fCab.write("LOCATION: "+mySection+"\n")
fCab.write("CALLSIGN: "+myCall+"\n")
fCab.write("CATEGORY-OPERATOR: SINGLE-OP\n")
fCab.write("CATEGORY-TRANSMITTER: ONE\n")
fCab.write("CATEGORY-ASSISTED: NON-ASSISTED\n")
fCab.write("CATEGORY-BAND: ALL\n")
fCab.write("CATEGORY-POWER: LOW\n")
fCab.write("CATEGORY-MODE: CW\n")
fCab.write("CATEGORY-STATION: FIXED\n")
fCab.write("CLAIMED-SCORE: \n")
fCab.write("CREATED-BY: AA6XA's adif2cabrillo v"+version+"\n")
fCab.write("NAME: "+myName+"\n")
fCab.write("EMAIL: \n")
fCab.write("ADDRESS: \n")
fCab.write("OPERATORS: "+myCall+"\n")
fCab.write("SOAPBOX: \n")

#loop over lines in Adif file
adifEntries = fAdif.readlines()
for line in adifEntries:
    #only want lines with QSOs
    if line[1:5]=="CALL":
        idx = line.find("FREQ:")
        numChar = int(line[idx+5])
        freq = line[idx+7:idx+7+numChar]
        ii = freq.find(".")
        freq = freq[0:ii]+freq[ii+1:ii+4]

        idx = line..find("MODE:")
        numChar = int(line[idx+5])
        mode = line[idx+7:idx+7+numChar]

        idx = line.find("QSO_DATE:")
        date = line[idx+11:idx+11+4]+"-"+line[idx+11+4:idx+11+6]+"-"+line[idx+11+6:idx+11+8]

        idx = line.find("TIME_ON:")
        numChar = int(line[idx+8])
        time = line[idx+10:idx+10+numChar]

        idx = line.find("CALL:")
        numChar = int(line[idx+5])
        call = line[idx+7:idx+7+numChar]

        # cabrillo rx exchange
        idx = line.find("SRX_STRING:")
        numChar = int(line[idx+11])
        rxExch = line[idx+13:idx+13+numChar]

        # cabrillo tx exchange
        idx = line.find("STX_STRING:")
        numChar = int(line[idx+11])
        txExch = line[idx+13:idx+13+numChar]

        #write line in cabrillo file
        fCab.write("QSO: "+freq+"  "+mode+" "+date+" "+time+" "+myCall+" "+txExch+" "+call+" "+rxExch+" \n")

#write the footer, close files
fCab.write("END-OF-LOG:\n")
fCab.close()
fAdif.close()
