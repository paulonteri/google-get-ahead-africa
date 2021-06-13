"""
Histograms and Areas (Incomplete)

Given an array of non-negative integers that represent the bars (y value) in a histogram (with the array index being the x value),
 find the rectangle with the largest area under the curve and above the x-axis 
 (i.e. the largest rectangle that fits inside the histogram). Return the pair of array indices that represent the rectangle.

Test Cases
    Note that there may be other valid answers.
    For array [2,4,2,1], the largest area is 6, with height 2, and width from indices 0 to 2:
    https://s3.amazonaws.com/mimirplatform.production/files/e5f4e1f0-3f38-4bfb-9d47-7d28201fb652/Screenshot%20from%202020-07-12%2014-18-32.png

    For array [2,4,2,1,10,6,10] the largest area is 18, with height 6 and width from indices 4 to 6:
    https://s3.amazonaws.com/mimirplatform.production/files/4ed3362e-c8f8-43f6-bde6-a6556d8d0d2b/Screenshot%20from%202020-07-12%2014-19-44.png

https://www.geeksforgeeks.org/largest-rectangle-under-histogram
https://leetcode.com/problems/largest-rectangle-in-histogram/
"""
