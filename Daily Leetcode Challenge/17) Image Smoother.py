"""
661. Image Smoother

Easy

An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).

Given an m x n integer matrix img representing the grayscale of an image, return the image after applying the smoother on each cell of it.


Example 1:
Input: img = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[0,0,0],[0,0,0],[0,0,0]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0

Example 2:
Input: img = [[100,200,100],[200,50,200],[100,200,100]]
Output: [[137,141,137],[141,138,141],[137,141,137]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137
For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141
For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138
 

Constraints:

m == img.length
n == img[i].length
1 <= m, n <= 200
0 <= img[i][j] <= 255

"""


# Solution 

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        # Check if the input image is empty
        if not img or not img[0]:
            return []

        # Get the dimensions of the image
        m, n = len(img), len(img[0])

        # Initialize the result matrix with zeros
        result = [[0] * n for _ in range(m)]

        # Iterate through each pixel in the image
        for i in range(m):
            for j in range(n):
                # Initialize variables to calculate the sum and count of neighboring pixels
                total = 0
                count = 0

                # Iterate over the 3x3 neighborhood of the current pixel
                for ni in range(i - 1, i + 2):
                    for nj in range(j - 1, j + 2):
                        # Check if the neighboring pixel is within the image boundaries
                        if 0 <= ni < m and 0 <= nj < n:
                            # Accumulate the sum of pixel values and increment the count
                            total += img[ni][nj]
                            count += 1

                # Update the result matrix with the floor of the average
                result[i][j] = total // count

        # Return the smoothed image
        return result
    
    