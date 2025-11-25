First Draft (Image below):

Very poorly optimized, takes roughly 15-20 seconds for program to finish.  There are a lot of collisions as well, that will be where I first start to attempt to optimize.  
Also going to tie the for loops for empty space checking into one loop.  Going to add a timer as well for first optimization attempt.

<img width="425" height="129" alt="Screenshot 2025-11-20 090755" src="https://github.com/user-attachments/assets/e244b3ab-4ae8-4823-88c0-e77534d79e40" />

First Optimization (ASCII for Key Values):

For the first optimization attempt I used ASCII values for each character in the Title and Quote HashTables and multiplied each by a prime number(7), then added all values together to generate a key.
Much Better than first draft in terms of time and total number of collisions.  I attempted larger and smaller prime numbers to see what kind of difference that made.  On the lower side there was no real change, but on the larger side the overall optimization was much worse (added more overall time and collisions).

<img width="350" height="159" alt="Screenshot 2025-11-20 103554" src="https://github.com/user-attachments/assets/1a7945e2-bbc2-452b-accd-50b7928d42ef" />

Second Optimization (Linked Lists)

The second optimization attempt was creating a linked list method of inserting values to the table.  In this attempt, instead of linearly searching for an available open spot in the list, I placed data items into buckets with a .next property.  The inserted item would travel through the chain of .nexts until finding an empty spot and inserting itself there.  This cut down on time slightly but more importantly cut down on the amount of overall collisions.  A lot of empty index spaces, though that is due to my hard coded list size.

<img width="270" height="119" alt="Screenshot 2025-11-23 124653" src="https://github.com/user-attachments/assets/1cd3e996-8a25-44ff-8126-e4fac65b8244" />

Third Optimization (Hashing update, Array size change):

This attempt changed the hashing function to a larger prime number with an overflow mod number.  This in addition to the array size being 1.5X bigger than the exact necessary amount increases the overall optimization a fair bit.  The larger the array, the less collisions and quicker it completes.  This also comes at a cost for empty indexes as well obviously.  The linked list method has contributed dramatically to the number of empty indexes which makes sense.  That will be the next area to optimize.

<img width="323" height="128" alt="Screenshot 2025-11-25 100025" src="https://github.com/user-attachments/assets/2fd3b4d8-0ef8-4e89-a130-e214601f3bce" />

Fourth Optimization (Maybe do something with table size?)
