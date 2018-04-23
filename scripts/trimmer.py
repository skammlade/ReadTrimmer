# Author: Sara Kammlade
# Date: 2018/04/22
# Purpose: trim low quality bases from sequencing .fq/.fastq file and create new read file
# Run: python trimmer.py C:\Users\sarak\GitHub\ReadTrimmer\data\readFile.fq 30

def findIndexOfFirstBadPhredScore(scoreString, scoreCutoffValue):   
    for score in scoreString:
        position=0
        while position < len(scoreString) and int(ord(scoreString[position]))+33 >= scoreCutoffValue:
            position=position+1
        return position



# get readFile and phred score minimum
# read command line arguments into input variables
import sys
readFile=sys.argv[1]
minimumPhredScore=int(sys.argv[2])

asciiTest=int(ord('H'))-33
minimumASCII=chr(minimumPhredScore+33)

print(readFile)
print(minimumPhredScore)
print(asciiTest)

# input file for read, output file for write


# create output file
outputTrimmedReadFile=open("readFile-trimmed.fq","w+")

# iterate through input file, reading 4 lines at a time
from itertools import islice
with open(readFile) as infile:
    line1header=infile.readline()
    line2bases=infile.readline()
    line3blank=infile.readline()
    line4scores=infile.readline()


    # find and store cutoff point
    cutoffPosition=findIndexOfFirstBadPhredScore(line4scores, minimumPhredScore)
    print(cutoffPosition)

    #int(ord(score))+33 >= scoreCutoffValue:

    # 1st line: print first line

    # 2nd line: print up to cutoff point

    # 3rd line: print 

    # 4th line: print up to cutoff point

