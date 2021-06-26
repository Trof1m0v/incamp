from csv import reader
from re import findall

months = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06',
          'Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}

def read_rows(IFL,columnIndex):
    array = []
    for row in IFL:
        if(row[columnIndex] not in array):
            array.append(row[columnIndex])
    return array

def write_header(nameOfFile,dates,type):
    fileType = ".csv" if type == 0 else ".txt"
    fileObj = open(nameOfFile+fileType,"w")
    fileObj.write("Name/Date,")
    for date in dates:
        year = findall(r"\d{4}",date)
        month = findall(r"[A-Za-z]{3}",date)
        day = findall(r"\d{2}",date)
        if (date == dates[-1]):
            fileObj.write(f"{year[0]}-{months[month[0]]}-{day[0]}")
        else:
            fileObj.write(f"{year[0]}-{months[month[0]]}-{day[0]},")
    return fileObj

def write_row(name, dates, IFL, OFO):
    OFO.write(f"\n{name},")
    used = []
    for date in dates:
        for row in IFL:
            if(row[1] not in used):
                if(row[1] == date):
                    if(row[0] == name):
                        used.append(row[1])
                        hour = f"{row[2]}" if date == dates[-1] else f"{row[2]},"
                        OFO.write(hour)
                        break
                    elif(row == IFL[-1]):
                        OFO.write("0")
                        break
                elif(row[1] != date):
                    used.append(row[1])
                    zero = "0" if date == dates[-1] else "0,"
                    OFO.write(zero)
                    break

def read_and_write(inputCSV,outputName,outputType):
    inputFileObject = open(inputCSV)
    IFL = list(reader(inputFileObject))
    IFL.pop(0)

    names = read_rows(IFL, 0)
    names.sort()
    dates = read_rows(IFL, 1)
    outputCSV = write_header(outputName,dates,outputType)

    for name in names:
        write_row(name, dates, IFL, outputCSV)
    inputFileObject.close()
    outputCSV.close()

if __name__ == "__main__":
    csvName = "acme_worksheet.csv"
    outName = "reading"
    outType = 0
    read_and_write(csvName,outName,outType)