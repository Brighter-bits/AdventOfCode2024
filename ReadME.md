In order to get better at documenting code I will be using this from Day 7 Onwards to record the progress of the creation of my solution.

# Day 6

I lied, Day 6 is absolutely kicking my behind. The first part was simple enough, simply leave a trail of breadcrumbs behind and count the number of breadcrumbs.
Part two is a lot harder. I've tried many methods but eventually optimised it down to simply putting an object on the squares the guard went to, 1966 was my answer. Wrong.
More debugging, literal hours, and still nothing. Thus, having taken so long, I am going to ask the AI for a hint. A hint bear in mind, not an outright explanation. Thus I have failed
Day 6, I hope it is a good learning point for me.

It's been three hours, the AI was no help, I began looking at someone else's code, it looked very similar to mine, it seemed I had the right idea. No idea why I kept getting 1934.
Never make me do Day 6 again. I was supposed to document each attempt and iteration, but I'm too tired for it.

# Day 7

I've been sleeping all day, but let's begin. The puzzle is quite simple, using addition and multiplication to try and create a target number.
There's almost certainly a clever solution using prime factors or even normal factors, (Chinese remainder theorem  I swear), but why not just brute force.
For each line there's around 2<sup>9</sup> possible solutions, so on average 2<sup>8</sup> calculations to get to the solution. Shouldn't be too bad.

The start was quite simple, I kept getting a very low number however as I was not adding up each of the values, just counting how many were valid.
Everything now works, after some fiddling around with keeping the mask the same length as the number of operators, the only problem is implementing this into part 2 would need ternary.
Unfortunately, I'll also have to get rid of my lambda function. Never mind, I can keep it.

Looking at it now, we've suddenly gone from 2<sup>9</sup> to 3<sup>9</sup> which explains why the code is suddenly so much slower. Turn out I can actually use Ternary.
There's probably a better way to do it, but I'm quite happy with my solution. I had to switch up how python handled the mask though, as previously it was
a binary number which played nice, but I had to change it to an integer which just so happened to not have a digit greater than 2. Overall, good day, if I hadn't
slept through most of it.

# Day 8

I've only slept 1/4 of the day away (I need to fix my sleep schedule). First part looks simple enough (though I always say that).
First, make a separate 2D array for each kind of node, get the distances, multiply by -1 to get the opposite direction. Then once you have all of the antinodes, overlay all of the arrays and count.

Perfect, now I just need to do the same, but continue extrapolating the vector until it goes out of bounds! It was going well, until I found that apparently this time each antenna also is an antinode.

Added that and it worked perfectly

# Day 9

Once again, first part was quite nice, work from the top until there are no free spaces left. Part two looks a lot harder.
My solution is probably going to be a dictionary with the index as the key and the number of free spaces as the value.

I kept getting everything wrong, because the program would see the free space left behind by the numbers jumping forward and decide to move them backwards, so I had to change that. Otherwise, good day