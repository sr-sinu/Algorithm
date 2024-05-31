There is a metro rail line with K stations numbered from 0 to K-1. 
There is a direct connection between stations if their numbers differ by one. 
Passengers can ride the metro line in both directions.

The fee for boarding the train is 1. Every time a passenger travels between two adjacent stations the fee increase by 2. 
The metro system charges money at the end of each day based on the passenger's travel history for that day.

There is a total fee limit for a single day. The passenger cannot be charged more than the limit, even if their associated travel 
fees exceed the limit. The limit depends on the maximum station number the passenger visited during the day.

You are given arrays start and dest of length N, describing all the metro rides the passenger took during the day. 
During the x-th ride, the passenger boarded the train at station start[X] and left the train at station dest [X]. 
You are also given an array limit of length K. 
If the largest station number the passenger visited during the day is Y, then the fee limit for this passenger for that day is limit [Y].

Write a function:

def solution(start, dest, limit)

that, given the arrays start and dest, both of length N, 
and the array limit of length K, returns the amount of money the passenger will be charged at the end

Examples:

1. For start = [1, 0, 2, 4], dest = [2, 2, 0, 5] and limit = [3, 17, 7, 4, 5, 17] the function should return 16.
There were four rides:

station 1 to station 2 (cost 3);

station 0 to station 2 (cost 5);

station 2 to station 0 (cost 5);

station 4 to station 5 (cost 3).

The total cost is 16. The largest visited station number is 5. The fee limit for station 5 is 17, so it does not apply in this case.


2. For start = [1, 2, 0, 2, 3], dest = [2, 1, 2, 1, 2] and limit = [4, 8, 18, 16, 20] the function should return 16.
There were five rides:
    - station 1 to station 2 (cost 3);

    - station 2 to station 1 (cost 3);

    - station 0 to station 2 (cost 5);

    - station 2 to station 1 (cost 3);

    - station 3 to station 2 (cost 3).

The total cost would be 17, but is capped at 16 (the daily limit for station 3).

3. For start = [2,2], dest = [4, 3] and limit = [1, 1, 1, 1, 9, 1, 1] the function should return 8.
Assume that:
    - N is an integer within the range [1..30];

    - K is an integer within the range [2..50];

    - each element of arrays start and dest is an integer within the range [0..K-1];

    - each element of array limit is an integer within the range [1..3,000];

    - each ride has a different start and destination station.