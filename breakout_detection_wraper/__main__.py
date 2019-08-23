import csv
import os

from rpy2.robjects.packages import SignatureTranslatedAnonymousPackage, importr
from rpy2.robjects.vectors import IntVector, FloatVector


def main():
    mydata = []

    with open('breakout_detection_wraper/fuel_data.csv', 'r') as csvfile:
        dat = csv.reader(csvfile)
        for line in dat:
            mydata.append(float(line[0]))

    minsize = 30
    method = 'multi'
    degree = 1
    with open('breakout_detection_wraper/breakout_function.R') as code:
        rcode = os.linesep.join(code.readlines())
        wrapper = SignatureTranslatedAnonymousPackage(rcode, "Codigo")
    result = wrapper.Detect(FloatVector(mydata), minsize, method, degree)
    print(result)


if __name__ == '__main__':
    main()
