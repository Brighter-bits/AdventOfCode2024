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

OH MY GOD. It's midnight, Day 17. I have just implemented Didi's shortest path algorithm and finished part 1. Part2? That's a problem for Day 18.

Day 19. It's over.



# Day 17

Still depressed after yesterday, first part looks easy enough

And it was, it was also really fun

Part two though, looks to be a ~~Brute Force~~ Mathematical Problem.

Uhhhh, I got close? I may have had to slightly adjust my jumping because the calculation was more of an estimate than an accurate calculation. Now, BACK TO DAY 16!

# Day 18

Another path finding one, this time however, I think I'll be able to use flood fill. Which should be useful for getting around the gaps.

Flood fill worked perfectly, for both parts, I feel so cool. Now, BACK TO DAY 16!

# Day 19

Looks quite simple, I can just brute force it, truncating the string each time until I find an exact match

It's not working, it keeps giving me 170, I need to find a different solution. 

Nevermind, it works.

So, brute forcing will take too long... but memoisation, could change everything. Interestingly, trying to change a global variable inside a cached function doesn't exactly work, because the cache only stores
the return value. So I used the putting a function inside a function I learned from my halfway complete Day 16 Part 2 and have the function return a number.

My god that was fast, I love memoisation.

# Day 20

Another maze... Why do they keep giving me mazes? ERIC WHY???? 

I'll go through, note which walls have stuff on the other side, and then use a recursive to get to the end, which I can memoise.

Scratch that, I can just put every coord into an array, since the index is the number of picoseconds. I then find the difference and see if it is above 102 (100 + the two picoseconds cheating), if so then it's
valid.

Part 2? What? How am I supposed to do this? How am I supposed to make a diamond?

Okay, a few hours and I think I have it, it's a pretty long if statement, but it'll work. Nevermind, too low.

Ok, so the reason it was too low was because I was only looking at the positive coords, which actually may have decreased the number of possible cheats by 75%...

Whoops. But it seems to be working now. Nevermind, I forgot that python's range is top exclusive. So I was going from -20 to 19. Which meant I was slightly off.

Anyway, technically it's past midnight now, but that's fine. I'm still under 24h.

# Day 21

Today looks quite complicated, but I think with some recursive stuff, it shouldn't be too bad.

I'm currently using a whole load of switch statements. I have a feeling I was supposed to implement Dijkstra's.

My worst nightmare happened and I accidentally put in the wrong output, I spent ages debugging that. Now, I need 25 robots, so hopefully memoisation will save me.

Might need to use Counter.

Today has been tough, not been able to complete it in the day, but I haven't used AId yet. I have an idea however, so I need to remember this for tomorrow.

This isn't going to be elegant.

To put it simply, it seems the read thing that affects everything is the movement between the numbers, not the direction pads.
So just get every single combination of the keypad runs and get the smallest one. This may not work. But I'm hopeful.

I pray this works tomorrow.

Urgh, that took far too long. Turns out that manually inputting all the codes means that you're likely to input a whole load of stuff wrong and in the wrong order.

It's done now though.

# Day 22

Umm, this problem is just a whole load of calculations, isn't it brute force problem with some memoisation of course?

Part 1 complete, well that was quick, the next part seems brute forceable too? I may need to optimise it slightly.

Written the code, I should probably optimise it, but if I wait like, an hour, it should be done.

Nevermind, I have optimised it slightly. It now counts the number of commas in a string to determine the position of the price.

For some reason it's not working. Ah, it turns out, that the program would confuse a sequence of [1, 2, 3, 4] with [-1, 2, 3, 4] as the program would ignore the -. So the start of the sequence now has a comma
[,1,2,3,4] so that the first number's sign is checked.

# Day 23

I woke up at 5AM. I feel amazing.

So, with part 1, I considered using a dictionary, but wasn't sure how I would do it, so I didn't. Instead, I took two linked nodes and then check if they both connected to another node, thus making a
triangle/group of 3.

I may have spent a while debugging because I looked for t anywhere in the node instead of just at the start.

Unfortunately, the second part required me to actually use a dictionary. I spent about an hour just staring at the screen. But it turns out it was actually quite simple.
All you need to do is choose a node, and then save every node it connects to as a list. Then check each list, if it doesn't appear then it doesn't connect and so we get rid of it.

# Day 24

Okay, I can do this, make a dict containing all of the connections, then begin substituting the actual values in until I get the number.

Huh, quite a lot of subroutines today, it's quite nice. Part two however, looks like a brute force only kind of thing... 

Alright, turns out you can do something with a thing called a half-adder, which is where you use an AND and a XOR to create a logic system which also outputs whether you need to carry a one to the next place
value.

This is different from a full-adder which allows you to add your carry over into the equation instead of just outputting one.

Unfortunately, I don't understand the "logic" (haha) behind it, so I'm going to avoid it unless I have to delve into it. 


Turns out I have to learn adders at some point anyway, so may as well now.

Half adders have A and B go into both a XOR gate an AND gate. The AND gate gives the carryover while the XOR gives the digit.

Full adders are made up of a half adder, but the XOR output is given to another XOR gate with the previous carryover and another AND gate. The second AND gate's carryover is put in an OR with the previous AND
gate's carryover to get the actual carryover. Meanwhile, the second XOR gate gives the digit.

As such, if the program is supposed to add together perfectly, then the program must be using Full Adders. With the outputs from AND gates going to more AND gates to simulate carryovers

So all I need to do is visualise it. Honestly, I could probably do this manually.

The first addition (x00, y00) will have an AND and a XOR gate. The XOR gate will go to z00. The AND will then go to a variable we shall call G.

The second addition (x01, y01) will go to a AND and a XOR gate. But the AND output will go to OR with the previous AND and the XOR will go to another XOR with the previous AND.

I might just draw this.

# Day 25

Looks very easy for some reason, just have to add up the lists and see if any exceed 7

That's it? No Part 2? Oh... it's over.

Well, this year was fun. Maybe I'll go back and make my code prettier at a later date, but for now? This is good. I guess I'll have to do previous years or wait for the next.

Merry Christmas

