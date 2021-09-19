The test code is commented out at the bottom of each python file with a
description of what each test does although i haven't included a lot as the 
functions are very restrictive in what they can/cant do and there is no 
point testing functions that are used by others as they will be tested in the process.

On main there will be a output text box and a blank area to the right where the
graphs go once you generate them with weeding, put a number in the text box above 
and it should be clear via the graphs what it is doing. a number around 4 is pretty good
i am pretty proud of the visualisation and the metric. it sorts the dataset based
on average time between takeouts of the book. then the number you enter is 
how many interquartile ranges above the 75th percentile the limit is for recommending to
remove a book. it then outputs a list of books and the average time between takeout
for each.

To search for a book type in id/name (you can get names by typing in random
numbers for id's) then click info and it will provide a list. to reset the 
text box click clear box.

To take out a book type memberid,bookid,timeindaystotakeout in the box then click checkout
e.g 1234,15515,25 will take out the book 15515 to person with memberid 1234 for 25 days.
To return it just type in 15515 and click return. these will take a few seconds as it is
writing 306000 logs, if you want to make it faster just delete 99.9% of the logs you'll still
have 306 left or i can generate you another dataset with more/less. 

I like how i sorted the logs by time, when i write it back to the file. for all logs 
this used to take around 30 seconds each time you wanted to check in/return a book and that
wasn't good, i could have fixed it by reducing the amount of logs but thats lazy so i found
that what took the most time was converting the dates into datetime objects so i can sort it
based on that field. i solved this by making the dates year/month/day instead of day/month/year
so it can be sorted without the conversion. this small thing saves around 25seconds per write

I like my log gen and book gen. i first made a script to scrape 8000 book titles 
off a title gen site, then i replicated some randomly to make 22000 total books.
My log gen used to work in quadratic time as it would generate a list of logs then go through
all of them and make sure none are overlapping. this capped around 20000 logs which i wasn't 
happy with so i made a new algorithm which worked in linear time. This generator took two days total
to code.

Wont open outside of idle idk why