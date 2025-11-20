First Draft (Image below):

Very poorly optimized, takes roughly 15-20 seconds for program to finish.  There are a lot of collisions as well, that will be where I first start to attempt to optimize.  
Also going to tie the for loops for empty space checking into one loop.  Going to add a timer as well for first optimization attempt.

<img width="425" height="129" alt="Screenshot 2025-11-20 090755" src="https://github.com/user-attachments/assets/e244b3ab-4ae8-4823-88c0-e77534d79e40" />

First Optimization (ASCII for Key Values):

For the first optimization attempt I used ASCII values for each character in the Title and Quote HashTables and multiplied each by a prime number(7), then added all values together to generate a key.
Much Better than first draft in terms of time and total number of collisions.  I attempted larger and smaller prime numbers to see what kind of difference that made.  On the lower side there was no real change, but on the larger side the overall optimization was much worse (added more overall time and collisions).

<img width="350" height="159" alt="Screenshot 2025-11-20 103554" src="https://github.com/user-attachments/assets/1a7945e2-bbc2-452b-accd-50b7928d42ef" />

Second Optimization (Linked Lists)
