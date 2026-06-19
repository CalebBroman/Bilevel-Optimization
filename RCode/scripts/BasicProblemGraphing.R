library(tidyverse)

xseq <- -400:400/100

ProblemData <- tibble(x=xseq, 
                           minimizer=lowerProblemSolution(xseq),
                           upperFunction=upperProblem(xseq))

graph <- ggplot(ProblemData) + 
            geom_path(aes(x=x, y=minimizer, color="Minimizer")) +
            geom_path(aes(x=x, y=upperFunction, color="Upper Function"))


print(graph)