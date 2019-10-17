# Pre-allocation
# And if you are using loops, one operation that is slow in R (and somewhat slow in all languages) is memory allocation for a particular variable that will change during loping (e.g., a variable that is a dataframe). So writing a for loop that resizes a vector repeatedly makes R re-allocate memory repeatedly, which makes it slow. Try this:

a <- NA
for (i in 1:10) {
    a <- c(a, i)
    print(a)
    print(object.size(a))
}

# Here, in each repetition of the for loop, R has to re-size the vector and re-allocate memory. It has to find the vector in memory, create a new vector that will fit more data, copy the old data over, insert the new data, and erase the old vector. This can get very slow as vectors get big.

# On the other hand, if you "pre-allocate" a vector that fits all the values, R doesn't have to re-allocate memory each iteration, and the results can be much faster. Here's how you'd do that for the above case:

a <- rep(NA, 10)

for (i in 1:10) {
    a[i] <- i
    print(a)
    print(object.size(a))
}

# Try timing each of these as you did above using system.time(). To really see the difference, increase the iterations from 10 to, say, 10000.

# Fortunately, R has several functions that can operate on entire vectors and matrices without requiring looping (Vectorization). That is, vectorizing a computer program means you write it such that as many operations as possible are applied to whole data structure (vectors, matrices, dataframes, lists, etc) at one go, instead of its individual elements.

# You will learn about some important R functions that allow vectorization in the following sections.