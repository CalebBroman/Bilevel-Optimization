library(tidyverse)

#lower level function:

lowerProblem <- function(z, x) {
  2*x^2 + 2*x*z + (1/2)*z^2
}

#solution to lower level function given x:

lowerProblemSolution <- function(x) {
  map_dbl(x, \(x) optimize(lowerProblem, c(-10000,1+x), x=x)[[1]])
}

#upper level function:

upperProblem <- function(x) {
  ystar <- lowerProblemSolution(x)
  x^2 - ystar
}

print(optimize(upperProblem, c(-100, 100)))
