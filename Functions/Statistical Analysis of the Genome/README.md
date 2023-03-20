
Define a function called freq() that computes the histogram of a virus sequence list. For this function, you cannot use any function defined in any module.
Use the function freq() to plot a frequency histogram (bargraph plot) of the virus sequence, where the frequency of each nucleotide should appear as a blue bar, and the x axis should depict the four nucleotides A,C,G and T from left to right in alphabetical order.

A so-called 2-gram is defined as a block of two consecutive letters. For instance, in the sequence AACTGC we can find five different 2-grams: AA, AC, CT, TG and GC (notice that two consecutive 2-grams overlap in one letter). It is easy to see that in a sequence of 𝑁 letters, we can count  𝑁−1 2-grams (many of them may be repeated, so the total number of different 2-grams is possibly smaller).
For sequences composed by letters whose alphabet is of size 4 (like the virus RNA, whose alphabet is made by four letters A,C,G and T), there are a total of  24=16 possible 2-grams: AA,AC,AG,AT,...,TT.
By modifying the function freq() (or otherwise), compute and plot a histogram (bar graph plot) of the frequency of 2-grams in the virus sequence.
The x axis should depict all sixteen combinations of the four nucleotides.

Let  𝑁(𝑖𝑗) be the frequency (that is, the number of occurrences) of the 2-gram 'ij' in the virus sequence, for  𝑖,𝑗=𝐴,𝐶,𝐺,𝑇. The transition matrix  𝐓={𝑇𝑖𝑗} of a given sequence is defined such that the general term  𝑇𝑖𝑗=𝑁(𝑖𝑗)/𝑁𝑡𝑜𝑡(𝑖), where  𝑁𝑡𝑜𝑡(𝑖) is the frequency of letter 'i' showing up in the sequence. By construction, all rows of  𝐓 should sum up one.
Compute the  4×4 transition matrix 𝐓 of the virus sequence. Print this matrix and display it as a heatmap of this matrix using seaborn.

Define a function called  𝑑𝑒𝑣𝑖𝑎𝑡𝑖𝑜𝑛(𝑥). The input of the function is a walk list  𝑥. This function performs the following computation:
- It iteratively considers all possible sublists 𝑥𝑘=[𝑥(0),...,𝑥(𝑘)], where  𝑘=1,2,4,… runs through powers of  2.
- For each possible value of 𝑘, the function computes  Δ(𝑘)=𝑚𝑎𝑥(𝑥𝑘)−𝑚𝑖𝑛(𝑥𝑘).
- The function 𝑑𝑒𝑣𝑖𝑎𝑡𝑖𝑜𝑛 finally returns a list of the form  [(𝑘,Δ(𝑘))] for all possible values of 𝑘.
- That final list is called the scaling.

Compute the function 𝑑𝑒𝑣𝑖𝑎𝑡𝑖𝑜𝑛(𝑥) for both the detrended_virus_walk and the five simple random walks. Make a scatter plot of all resulting scalings to compare all of these. Make sure that the axis of the plot are in logarithmic scales.

A power law function  𝑓(𝑧)=𝑎𝑧𝑏 appears as a straight line when plotted in logarithmic axes. This is so because taking logarithms at both sides of the power law function, we have  log(𝑓(𝑧))=𝑏log(𝑧)+log(𝑎), so if we perform a logarithmic transformation 𝑌̃=log(𝑓(𝑧)) and 𝑋̃=log(𝑧), in the new variables the power law function is a straight line 𝑌̃=𝑏𝑋̃+log(𝑎), with slope 𝑏.
Fit a power law function of the form 𝑓(𝑧)=𝑎𝑧𝑏 to the 𝑠𝑐𝑎𝑙𝑖𝑛𝑔 data for the detrended_virus_walk by making a linear fit to the logarithmically transformed data. Display the fitted curve together with the scatter plot of the scaling data.





