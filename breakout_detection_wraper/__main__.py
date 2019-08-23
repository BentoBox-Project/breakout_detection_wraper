import csv
import os

from rpy2.robjects.packages import SignatureTranslatedAnonymousPackage, importr
from rpy2.robjects.vectors import IntVector, FloatVector


def main():
    mydata = []
    # Open and Read the data file from a csv to convert it to a list
    with open('breakout_detection_wraper/fuel_data.csv', 'r') as csvfile:
        dat = csv.reader(csvfile)
        for line in dat:
            mydata.append(float(line[0]))

    # Define the parameters to configure the break out detection algoritm
    minsize = 30
    method = 'multi'
    degree = 1
    # Open the R file to run it on the wrapper
    with open('breakout_detection_wraper/breakout_function.R') as code:
        rcode = os.linesep.join(code.readlines())
        # Create the wrapper as an anonymous package signature
        wrapper = SignatureTranslatedAnonymousPackage(rcode, "Codigo")
    # Execute the method from the wrapper
    result = wrapper.Detect(FloatVector(mydata), minsize, method, degree)
    # Print the result returned from the R function
    print(result)


if __name__ == '__main__':
    main()
