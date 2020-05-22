# MPMP_2_-_Steam_Train_Fuel.

A soultion to solve to the problem proposed here: https://www.youtube.com/watch?v=T29dydI97zY&t=5s.

Please excuse my writing I write software not books

//TODO Write some code

## Step 1: Solve for max distance with n number of stops at max efficiency

#### For 0 stops
1. `Fill up 500 from base`
2. `Forwards 500 miles`
3. `Run out of fuel at 500 miles`
To Travel 500 miles you need 500 units of fuel.

#### For 1 stop
What is the most efficient way of dropping fuel?
We need to do 3 things with the cargo (travel to the cache, the cache it self, & travel from the cache).

1. `Fill up 500 from base`
2. `Forwards 166.67 miles`
3. `Make cache of 166.67 units of fuel`
4. `Backwards 166.67 miles`
5. `Fill up 500 from base`
6. `Forwards 166.67 miles`
7. `Fill up 166.67 from cache (500 total)`
8. `Forwards 500 miles`
9. `Run out of fuel at 666.67 miles`
To Travel 666.67 miles you need 1000 units of fuel.

#### For 2 stops
Repeat for 1 stops twice.
Then treat 1st cache as base until cache is empty.

1. `Fill up 500 from base`
2. `Forwards 166.67 miles`
3. `Make cache of 166.67 units of fuel`
4. `Backwards 166.67 miles`
5. `Fill up 500 from base`
6. `Forwards 166.67 miles`
7. `Add 166.67 to cache (333.34 total)`
8. `Backwards 166.67 miles`
9. `Fill up 500 from base`
10.`Forwards 166.67 miles`
11.`Fill up 166.67 from cache (500 total)`
12.`Forwards 166.67 miles`
13.`Create cache of 166.67 units of fuel`
14.`Backwards 166.67 miles`
15.`Fill up 166.67 from cache (500 total)`
16.`Forwards 166.67 miles`
17.`Fill up 166.67 from cache (500 total)`
18.`Forwards 500 miles`
19.`Run out of fuel at 833.33 miles`
To Travel 833.33 miles you need 1500 units of fuel.

## Step 2: I got stuck so I drew a graph
![alt text](https://raw.githubusercontent.com/RandomRDP/MPMP_2_-_Steam_Train_Fuel/master/Graph%201.png "Wild graph appeared!")
Turns out that if you graph the relationship between miles traveled and units of fuel needed is linear.

### **Step 2a: Test the graph**
To travel 600m is possible with less then 2 stops but more then 1.
For best efficiency the cache needs to be as far from destination as possible (i.e. 1 tank of fuel away).
So the cache needs to be at 100 miles from base and contain 100 units of fuel - any more fuel at the cache would be wasted because there would be no space in the train.

1. `Fill up 300 from base`
2. `Forwards 100 miles`
3. `Make cache of 100 units of fuel`
4. `Backwards 100 miles`
5. `Fill up 500 from base`
6. `Forwards 100 miles`
7. `Fill up 100 from cache (500 total)`
8. `Forwards 500 miles`
9. `Run out of fuel at 600 miles`
To Travel 600 miles you need 800 units of fuel.

![alt text](https://raw.githubusercontent.com/RandomRDP/MPMP_2_-_Steam_Train_Fuel/master/Graph%202.png "Wild graph appeared!")

It works :)

## Step 3: Use graph to solve problem
![alt text](https://raw.githubusercontent.com/RandomRDP/MPMP_2_-_Steam_Train_Fuel/master/Graph%203.png "Wild graph appeared!")

TA DA look at the intersection between Distance = 800 and line of best fit which gives the answer of 1400


# Useful equations
Max distanced traveled with a given number of caches
* `Distance = ((Capacity/3) * Num_Caches) + Capacity`

Max distanced traveled with a given fuel
* `Distance = (Fuel + (2*Capacity))/3`

Min fuel for given distance 
* `Fuel Used = (3*Distance) - (2*Capacity)`
