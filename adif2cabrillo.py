#!/bin/env python3

# Convert adif file to cabrillo for NAQP
import re

### FILL THIS STUFF IN FIRST ###
contest = "ARRL-10"
myAddress = """Winchester Mystery House
525 S Winchester Blvd
San Jose, CA
95128"""
myCall = "AA6XA"
myEmail = "someone@example.com"
myGrid = "AB12ce"
myName = "JEFF"
myState = "CA"
mySection = "SCV"
### ^^^^^ ###

adifFlnm = input('Enter Adif filename to read: ')
cabFlnm = input('Enter Cabrillo filename to write: ')

fAdif = open(adifFlnm, 'r')
fCab = open(cabFlnm, 'w')

#write the fixed header
version = 0.11
fCab.write("START-OF-LOG: 3.0\n")
fCab.write("CONTEST: "+contest+"\n")
fCab.write("LOCATION: "+mySection+"\n")
fCab.write("CALLSIGN: "+myCall+"\n")
fCab.write("CATEGORY-OPERATOR: SINGLE-OP\n")
fCab.write("CATEGORY-TRANSMITTER: ONE\n")
fCab.write("CATEGORY-POWER: LOW\n")
fCab.write("CATEGORY-ASSISTED: NON-ASSISTED\n")
fCab.write("CATEGORY-BAND: 10M\n")
fCab.write("CATEGORY-MODE: SSB\n")
fCab.write("CATEGORY-STATION: FIXED\n")
fCab.write("CATEGORY-OVERLAY: LIMITED-ANTENNA\n")
fCab.write("CERTIFICATE: YES\n")
fCab.write("CLAIMED-SCORE: \n")
fCab.write("CREATED-BY: https://github.com/kj4ezj/adif2cabrillo v"+version+"\n")
fCab.write("GRID-LOCATOR: "+myGrid+"\n")
fCab.write("NAME: "+myName+"\n")
fCab.write(re.sub(r'(?m)^', 'ADDRESS: ', myAddress)+"\n")
fCab.write("EMAIL: "+myEmail+"\n")
fCab.write("OPERATORS: "+myCall+"\n")
fCab.write("SOAPBOX: \n")

# ARRL state/province ID map
arrl_identifiers = {
    # United States
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    # Canadian provinces
    "Alberta": "AB",
    "British Columbia": "BC",
    "Labrador": "LB",
    "Manitoba": "MB",
    "New Brunswick": "NB",
    "Newfoundland": "NF", # partial
    "Newfoundland and Labrador": "NF",
    "Nova Scotia": "NS",
    "Northwest Terr": "NT",
    "Nunavut": "NU",
    "Ontario": "ON",
    "Prince Edward": "PE",
    "Quebec": "QC",
    "Saskatchewan": "SK",
    "Yukon": "YT",
    # Mexican states
    "Aguascalientes": "AGS",
    "Baja California Sur": "BCS", # must be before BCN
    "Baja California": "BCN",
    "Campeche": "CAM",
    "Chiapas": "CHI",
    "Chihuahua": "CHH",
    "Ciudad de Mexico": "CMX",
    "Ciudad de México": "CMX",
    "Coahuila": "COA",
    "Colima": "COL",
    "Durango": "DGO",
    "Estado de Mexico": "EMX",
    "Estado de México": "EMX",
    "Guanajuato": "GTO",
    "Guerrero": "GRO",
    "Hidalgo": "HGO",
    "Jalisco": "JAL",
    "Mexico City": "CMX",
    "Mexico State": "EMX",
    "Michoacan": "MIC",
    "Michoacán": "MIC",
    "Morelos": "MOR",
    "Nayarit": "NAY",
    "Nuevo Leon": "NLE",
    "Nuevo León": "NLE",
    "Oaxaca": "OAX",
    "Puebla": "PUE",
    "Queretaro": "QRO",
    "Querétaro": "QRO",
    "Quintana Roo": "QUI",
    "San Luis Potosi": "SLP",
    "San Luis Potosí": "SLP",
    "Sinaloa": "SIN",
    "Sonora": "SON",
    "Tabasco": "TAB",
    "Tamaulipas": "TAM",
    "Tlaxcala": "TLX",
    "Veracruz": "VER",
    "Yucatan": "YUC",
    "Yucatán": "YUC",
    "Zacatecas": "ZAC"
}

# ARRL location or serial number received
def get_arrl_exchange(line):
    # look for QSO serial number in the COMMENT field, ignoring numbers like "10m contest"
    comment_match = re.search(r'<COMMENT[^<]+', line)
    if comment_match:
        comment_content = re.search(r'>(.*?)<', comment_match.group(0))
        if comment_content:
            comment_text = comment_content.group(1)
            number_match = re.search(r'\b([0-9]+)\b', comment_text)
            if number_match:
                return number_match.group(1)

    # look for location in the QTH field
    qth_match = re.search(r'<QTH[^<]+', line)
    if qth_match:
        qth_content = re.search(r'>(.*?)<', qth_match.group(0))
        if qth_content:
            qth_text = qth_content.group(1)
            # look for two or three letter state (US, Mexico) or Canadian province identifiers
            uppercase_match = re.search(r'\b[A-Z]{2,3}\b', qth_text)
            if uppercase_match:
                return uppercase_match.group(1)
            else:
                # look for full state/province names and match them to a list
                for key, value in arrl_identifiers.items():
                    if key in qth_text:
                        return value

    # return MISSING if nothing is found
    return "MISSING"

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

        idx = line.find("MODE:")
        numChar = int(line[idx+5])
        mode = line[idx+7:idx+7+numChar]
        if re.match(r"^(AM|FM|SSB)$", mode):
            mode = "PH"

        idx = line.find("QSO_DATE:")
        date = line[idx+11:idx+11+4]+"-"+line[idx+11+4:idx+11+6]+"-"+line[idx+11+6:idx+11+8]

        idx = line.find("TIME_ON:")
        numChar = int(line[idx+8])
        time = line[idx+10:idx+10+numChar]

        idx = line.find("CALL:")
        numChar = int(line[idx+5])
        call = line[idx+7:idx+7+numChar]

        # cabrillo rx exchange
        idx = line.find("<RST_RCVD:")
        numChar = int(line[idx+10])
        rxRST = line[idx+12:idx+12+numChar]

        rxExchange = get_arrl_exchange(line)

        # cabrillo tx exchange
        idx = line.find("<RST_SENT:")
        numChar = int(line[idx+10])
        txRST = line[idx+12:idx+12+numChar]

        #write line in cabrillo file
        fCab.write("QSO: "+freq+" "+mode+" "+date+" "+time+" "+myCall+" "+txRST+" "+myState" "+call+" "+rxRST+" "rxExchange"\n")

#write the footer, close files
fCab.write("END-OF-LOG:\n")
fCab.close()
fAdif.close()
