library(tidyverse)
library(plotly)

#

lowerProblem <- function(z1, z2, x) {
  (z1 + x)^2 + (x-2)*z1*z2 + z2^2
}

#solution to lower level function given x:

lowerProblemSolution <- function(x) {
  #todo
}

#upper level function:

upperProblem <- function(x) {
  ystar <- lowerProblemSolution(x)
  sum(ystar) + x
}
