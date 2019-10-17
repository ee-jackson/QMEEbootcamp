#!/usr/bin/env Rscript

# This function calculates heights of trees given distance of each tree 
# from its base and angle to its top, using  the trigonometric formula 
#
# height = distance * tan(radians)
#
# ARGUMENTS
# degrees:   The angle of elevation of tree
# distance:  The distance from base of tree (e.g., meters)
#
# OUTPUT
# The heights of the tree, same units as "distance"

TreeHeight <- function(degrees, distance){
  radians <- degrees * pi / 180
  height <- distance * tan(radians)
  return (height)
}

tree.data<-read.csv("../data/trees.csv", header = TRUE)


tree.data$Tree.Height.m<-TreeHeight(tree.data$Angle.degrees, tree.data$Distance.m)


write.csv(tree.data,"../results/TreeHts.csv")