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

# Day 10

ASCII let's go! I can actually do this. Just need to split by commas and newlines, then do some fun ASCII stuff.

... I accidentally completed the first part of 2023 Day 15... That was silly of me.

The actual puzzle shouldn't be too bad, it seems similar to the word search, so I should be fine.


Part 1 had quite a few errors, a single off by one error where I tried to find an adjacent 0 first instead an adjacent 1,
unfortunately, I made a terrible mistake, I kept counting every single route to every single 9 instead of just one route.

I fixed it without too much editing. My face must have practically lit up after reading part 2, which wanted every single route.

That was almost certainly the fastest part 2 I've ever done. Now I'll be bored for the rest of the day.

# Day 11

Seems simple enough, you're just adding stuff in arrays.

Oh god, oh god, it gets exponential. What the hell???? I have a feeling I'll need a smarter solution than brute force...

After some thinking, it's definitely something to do with recursion. Once a stone gets to 0, it follows a set pattern of splitting which doesn't change. Although how I would use that I have no clue.

Actually, just testing with a single 0, barely gets me to 35 blinks. Slightly less than halfway. There has to be an even better way than just counting the number of zeroes and the index.

Turns out I'm supposed to use the dreaded memoisation I avoided last year, it's actually really easy to implement. Now I just need to somehow make it work even better.

Just a quick Note: Memoisation, or basically caching, is where you take the known result of a calculation and then use it instead of recalculating it. For example, what is one plus one?
You don't need to use your fingers to count it because it's so easy. Same with square numbers. Computers have (basically) perfect memory, and do don't need to a calculation
a billion times to remember the answer, just once.

Next is Counter, which is basically what I've been doing with my dictionaries but optimised properly. It counts how many times something occurs, that's it.

OH MY GOD, I've fallen in love with Counters and Caching. So this is why people like it, who would have known. Probably me, if I hadn't chickened out last year.

# Day 12

Looks like some flood fill stuff, I couldn't do stuff like this last year, but this year is different. I flood fill and then count "edges". We will always hit the field at the top left, so we only need to go
right and down each time.

Can't actually only go right and down as I also need to check for the edges on the left and top.

Whoa, another day which took far too long. A few problems include

- Being unable to see the s at the end of a variable and using the wrong length
- Trying to count everything twice
- Letters being to the left of the topmost left item (solved by just getting rid of efficiency)
- Going in circles (literally)
- And more!

But it's over and it's still technically the 12th. There's still 5 minutes till midnight

# Day 13

The input looks annoying to parse, but won't be impossible. After that "ax + by = n" Hooray! And once I check it works, I can just brute force maybe?

There's a limit of 100 so it should be fine. Oh, fun fact, people call HCF, GCD for some reason. Doing more research, there's another thing I can use

Frobenius' coin problem says that if the HCF is 1 then the largest number which cannot be formed is ab - a - b, which is useful.

Actually, just brute force it.

OH MY GOD IT'S A SIMULTANEOUS EQUATION!

OH MY GOD I NEED SO MANY DECIMAL PLACES!

Okay, so I completely forgot you can use matrices to calculate simultaneous equations. Whoops, I've just done long, complex but very simple maths. I also forgot how exactly my 4d array was organised so I spent
a while on that. Which was a bit of a pain. Overall, good fun.

# Day 14

Looks simple enough, just take the coord, add the velocity * 100 and then mod by the grid

Turns out MOD always returns a positive number and also it's the product of the numbers, not the sum (Bloody SMC Q1 all over again)

I have to iterate, I tried to be smart about it but I'm stupid, so now I'm just going to fill up my drive until I see a Christmas tree.

Also, I'm going to have to use PIL and NUMPY, still don't get the hype around NUMPY.

NOPE, more research suggests that I use MatPlotLib instead.

More research suggests using PIL

ARGH, Got my XVelocity and YCoord mixed around, there we go, I finally found my Christmas Tree

# Day 15

Overall, seems quite simple, I just have to follow the movement along, if there's a wall, stop, if not, move.

A single off by one error, but overall, nice and easy.

This Second part looks quite a bit harder. Actually, upon further inspection, it might just be a simple edit to the move function.

I have a slight problem in that I move things form the last object to be moved to the first due to how the recursion works. So I'm going to overcomplicated this and create a buffer of movements which only gets
executed if everything can move.

WHOOPS, may have accidentally spent a bit too long making the thing look pretty, it's done now though.

# Day 16

This does not look good. How are you supposed to do a maze? A path finding algorithm? Flood fill? Might have to learn Djistrkaaoisadaoisdnaosidbaosid's shortest path algorithm, or O*.

Oh, no

I'm sobbing and crying, I don't know what to do. Time to ask for AId.

This is going to take a lot of time to learn. Why is it always the days ending in 6? Thank god there's no December 26th

# Day 17

Still depressed after yesterday, first part looks easy enough

And it was, it was also really fun

Part two though, looks to be a ~~Brute Force~~ Mathematical Problem.