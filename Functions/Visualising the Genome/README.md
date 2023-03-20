# Visualising the Genome

Define the function 𝑚𝑎𝑝𝑝𝑖𝑛𝑔(x) that, given a letter-list  𝑥𝐿, generates a number-list 𝑥𝑁, by mapping each of the 4 letters into a different number.
Specifically, implement the changes:
- A --> -2
- C --> -1
- G --> 1
- T --> 2

(For example,  𝑥𝐿=[𝐴, 𝑇, 𝑇, 𝐴, 𝐶, 𝐺] is mapped into  𝑥𝑁=[−2, 2, 2, −2, −1, 1].)

Implement the function called  𝑤𝑎𝑙𝑘𝑒𝑟(x) that, given a list 𝑥 of N numbers [x(0), x(1), x(2),...,x(N-1)], outputs a "walk list" 𝑦=[𝑦(0),𝑦(1),...,𝑦(𝑁)], defined recursively as:
- y(0) = 0
- y(n) = y(n-1) + x(n-1), if 0 < 𝑛 ≤ 𝑁

Given points (𝑥𝑖,𝑦𝑖) in the plane, a least-squares fit to a line 𝑦=𝑎𝑥+𝑏 gives formulas for the slope 𝑎 and the intercept  𝑦=𝑏 as:

<img width="347" alt="Screenshot 2023-03-20 at 18 35 18" src="https://user-images.githubusercontent.com/128386124/226434716-d5571603-40c9-4220-997c-851581e38bcc.png">

where  ⟨𝑟𝑖⟩ denotes the average of the numbers 𝑟𝑖.

Define a function called linear_fit() that:
takes a (finite) list of points  𝑧=[(𝑥0,𝑦0),(𝑥1,𝑦1),(𝑥2,𝑦2),...] as an input, fits a straight line to 𝑦=𝑎𝑥+𝑏 by performing a least-squares fit,
returns the values of 𝑎 and  𝑏.

Using,

def linear_fit_test(z):
    a,b=np.polyfit(*zip(*z), 1)
    return a,b
    
we compare the output of both functions for some well-chosen list of points to ensure that your function works appropriately.

Using the function linear_fit() we define a function called linear_trend() that:
- takes a list of numbers  𝑧=[𝑧0,𝑧1,𝑧2,...]as an input;
- fits a straight line to  𝑦=𝛼𝑥+𝛽 to the data of the form  (𝑝,𝑧𝑝);
- finally returns a list of the same size as 𝑧, such that the p-th element of that list displays 𝛼𝑝+𝛽 .

Plot a graph that shows the list virus_walk = walker(mapping(str2)), along with the best straight line fit obtained from linear_trend(walker(mapping(str2))), where str2 is a list that contains the virus sequence.
The detrended virus walk removes the linear trend (detrends) from the virus walk. Its generic p-th element is:
- detrended_virus_walk[𝑝]=virus_walk[𝑝]−(𝑎𝑝+𝑏)
 
In a second plot, we show the detrended virus walk.

A simple random walk is defined as a walk list  𝑦=[𝑦(0),𝑦(1),...,𝑦(𝑁)], defined recursively as:
- y(0) = 0
- y(n) = y(n-1) + x(n-1), if 0 < 𝑛 ≤ 𝑁
where for each n the steps x(n) are random values extracted from some set.

Generate five simple random walks of length equal to walker(mapping(str2)) with steps generated at random from the set  {−2,2}. Shown in a plot, the detrended walk detrended_virus_walk, together with these five simple random walks.

