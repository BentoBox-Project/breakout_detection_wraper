from rpy2.robjects.packages import SignatureTranslatedAnonymousPackage, importr
from rpy2.robjects.vectors import IntVector, FloatVector
import csv
import os

mydata = []

with open('datos.csv', 'r') as csvfile:
    dat = csv.reader(csvfile)
    for line in dat:
        mydata.append(float(line[0]))

minsize = 30
method = 'multi'
degree = 1
with open('Codigo.R') as code:
    rcode = os.linesep.join(code.readlines())
    wrapper = SignatureTranslatedAnonymousPackage(rcode, "Codigo")
result = wrapper.Detect(FloatVector(mydata), minsize, method, degree)
print(result)

