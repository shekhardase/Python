I ran this on a 500M row file to extract 1,000 rows and it took 13 min. The file had not been accessed in months, and is on an Amazon EC2 SSD Drive.
If you just need a random set of lines, not in a random order, then shuf is very inefficient (for big file): better is to do reservoir sampling
Most vivid amongst the memories of his home town
