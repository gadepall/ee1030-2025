#Image Compression using Truncated SVD
Uses Power Iteration + Deflation algorithm

##To run:

Include svd.c and input.txt in same folder

In input.txt put path for input image(jpg or png)
On next line put value for K
On next line put path for output image(as pgm format only)

**Example:**
```
inputcases/einstein.jpg
50
output/einstein_k50.pgm
```

To Compile:

```
gcc svd.c -lm
./a.out
```
