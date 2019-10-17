#!/usr/bin/env Rscript
######### Functions ##########

## A function to take a sample of size n from a population "popn" and return its mean
myexperiment <- function(popn,n){
    pop_sample <- sample(popn, n, replace = FALSE)
    return(mean(pop_sample))
}

## Calculate means using a for loop without preallocation:
loopy_sample1 <- function(popn, n, num){
	result1 <- vector() #Initialize empty vector of size 1 
	for(i in 1:num){
		result1 <- c(result1, myexperiment(popn, n))
    }
	return(result1)
}

## To run "num" iterations of the experiment using a for loop on a vector with preallocation:
loopy_sample2 <- function(popn, n, num){
	result2 <- vector(,num) #Preallocate expected size
	for(i in 1:num){
		result2[i] <- myexperiment(popn, n)
    }
	return(result2)
}

## To run "num" iterations of the experiment using a for loop on a list with preallocation:
loopy_sample3 <- function(popn, n, num){
	result3 <- vector("list", num) #Preallocate expected size
	for(i in 1:num){
		result3[[i]] <- myexperiment(popn, n)
    }
	return(result3)
}


## To run "num" iterations of the experiment using vectorization with lapply:
lapply_sample <- function(popn, n, num){ #lapply for lists sapply for vectors
	result4 <- lapply(1:num, function(i) myexperiment(popn, n))
	return(result4)
}

## To run "num" iterations of the experiment using vectorization with lapply:
sapply_sample <- function(popn, n, num){
	result5 <- sapply(1:num, function(i) myexperiment(popn, n))
	return(result5)
}

# Now generate a population:

popn <- rnorm(1000) # Generate the population

n <- 20 # sample size for each experiment
num <- 1000 # Number of times to rerun the experiment

print("The loopy, non-preallocation approach takes:" )
print(system.time(loopy_sample1(popn, n, num)))

print("The loopy, but with preallocation approach takes:" )
print(system.time(loopy_sample2(popn, n, num)))

print("The loopy, non-preallocation approach takes:" )
print(system.time(loopy_sample3(popn, n, num)))

print("The vectorized sapply approach takes:" )
print(system.time(sapply_sample(popn, n, num)))

print("The vectorized lapply approach takes:" )
print(system.time(lapply_sample(popn, n, num)))

hist(popn)

# [1] "The loopy, non-preallocation approach takes:"
#    user  system elapsed 
#   0.030   0.004   0.034 
# [1] "The loopy, but with preallocation approach takes:"
#    user  system elapsed 
#   0.011   0.001   0.012 
# [1] "The loopy, non-preallocation approach takes:"
#    user  system elapsed 
#   0.011   0.001   0.011 
# [1] "The vectorized sapply approach takes:"
#    user  system elapsed 
#   0.008   0.000   0.009 
# [1] "The vectorized lapply approach takes:"
#    user  system elapsed 
#   0.008   0.000   0.008 

