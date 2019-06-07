# hanoi-gym
Open AI gym implementation of Towers of Hanoi

In order to import this project to your local machine, follow these steps:

	1. open terminal and go to the directory you want to use
	2. once you have your working directory, type: 
		git clone https://github.com/oyefmi/hanoi-gym.git
	3. then type: cd hanoi-gym
	4. exectue this command: python3 setup.py install
	5. If TensorFlow isn't installed on your machine, you need to run 
	    - sudo apt install python3 -pip
	    - sudo pip3 install tensorflow

Project also contains an implementation of Deep Reinforcment Learning using a Deep Q Network on the Towers of Hanoi environment.

	- hanoi_DQN.py

state space graph representation of Tower of Hanoi with 3 disks:

![alt text](https://github.com/oyefmi/hanoi-gym/blob/master/ToH_stategraph.png)

Sample Output:

Number of moves to solve: 243
Number of moves to solve: 544
Number of moves to solve: 195
Number of moves to solve: 371
Number of moves to solve: 249
Number of moves to solve: 158
Number of moves to solve: 38
Number of moves to solve: 132
Number of moves to solve: 112
Number of moves to solve: 1006
Number of moves to solve: 121
Number of moves to solve: 315
Number of moves to solve: 226
Number of moves to solve: 226
Number of moves to solve: 472
Number of moves to solve: 491
Number of moves to solve: 82
Number of moves to solve: 273
Number of moves to solve: 112
Number of moves to solve: 41
Number of moves to solve: 456
Number of moves to solve: 847
Number of moves to solve: 239
Number of moves to solve: 33
Number of moves to solve: 214
Number of moves to solve: 417
Number of moves to solve: 251
Number of moves to solve: 77
Number of moves to solve: 198
Number of moves to solve: 128
Number of moves to solve: 379
Number of moves to solve: 164
Number of moves to solve: 69
Number of moves to solve: 388
Number of moves to solve: 140
Number of moves to solve: 127
Number of moves to solve: 265
Number of moves to solve: 123
Number of moves to solve: 228
Number of moves to solve: 73
Number of moves to solve: 139
Number of moves to solve: 303
Number of moves to solve: 190
Number of moves to solve: 103
Number of moves to solve: 189
Number of moves to solve: 200
Number of moves to solve: 861
Number of moves to solve: 247
Number of moves to solve: 387
Number of moves to solve: 41
Number of moves to solve: 183
Number of moves to solve: 287
Number of moves to solve: 213
Number of moves to solve: 48
Number of moves to solve: 289
Number of moves to solve: 355
Number of moves to solve: 354
Number of moves to solve: 265
Number of moves to solve: 348
Number of moves to solve: 170
Number of moves to solve: 1367
Number of moves to solve: 70
Number of moves to solve: 161
Number of moves to solve: 316
Number of moves to solve: 315
Number of moves to solve: 36
Number of moves to solve: 124
Number of moves to solve: 411
Number of moves to solve: 1032
Number of moves to solve: 88
Number of moves to solve: 68
Number of moves to solve: 12
Number of moves to solve: 406
Number of moves to solve: 643
Number of moves to solve: 39
Number of moves to solve: 25
Number of moves to solve: 78
Number of moves to solve: 93
Number of moves to solve: 125
Number of moves to solve: 211
Number of moves to solve: 58
Number of moves to solve: 404
Number of moves to solve: 1387
Number of moves to solve: 24
Number of moves to solve: 43
Number of moves to solve: 474
Number of moves to solve: 249
Number of moves to solve: 71
Number of moves to solve: 169
Number of moves to solve: 52
Number of moves to solve: 194
Number of moves to solve: 1854
Number of moves to solve: 325
Number of moves to solve: 53
Number of moves to solve: 221
Number of moves to solve: 3439
Number of moves to solve: 21
Number of moves to solve: 70
Number of moves to solve: 30

Average number of moves for training model 303.97


Number of moves to solve: 106
Number of moves to solve: 53
Number of moves to solve: 27
Number of moves to solve: 57
Number of moves to solve: 301
Number of moves to solve: 198
Number of moves to solve: 109
Number of moves to solve: 22
Number of moves to solve: 128
Number of moves to solve: 14
Number of moves to solve: 41
Number of moves to solve: 26
Number of moves to solve: 313
Number of moves to solve: 41
Number of moves to solve: 146

Average number of moves for test model 105.46666666666667
