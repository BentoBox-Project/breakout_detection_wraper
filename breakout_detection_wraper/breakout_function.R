#IMPORTING
library(BreakoutDetection)

#statements
Detect <- function(tsdata, min, met, deg )
{
    res = breakout(tsdata, min.size=min, method=met, beta=.001, degree=deg, plot=FALSE)
    return(res)
}

