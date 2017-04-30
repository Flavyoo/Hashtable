The Hashtable program requires the stdarray and stdio modules from Princeton. It prevents collisions by using
one two dimensional array of size 1031; This way if two or more elements hash to the same index, the program puts them in the 
inner array that exists in the hash index, and when get() is called, it traverses that inner array to find the element.

Please do not copy the code and turn it in as homework or project. For any other purposes feel free to use it.
