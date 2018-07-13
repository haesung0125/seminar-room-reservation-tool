# seminar-room-reservation-tool
command line tool for seminar room reservation for Department of Physics, SNU

Introdution
------------
We often need to reserve seminar rooms for various reasons, such as study groups with your friends, lab meetings with your lab members, etc. If you have to reserve seminar rooms for several times at once, it will be great to have a automation tool for that. By analyzing the seminar room reservation pages we can find out the reservation system can be easily accessible with simple lines of codes. So this is the output, although it didn't finish yet.

Goal
------------
1. Understand the seminar room reservation system
2. Make a simple command line tool for seminal room reservation.
3. Make it iterable.
4. Make GUI tool with Electron, if I have some time.

Information needed to make a reservation
------------
1. Name of the meeting
2. Room number
3. Name of the professor
4. Date
5. starting time
5. ending time
6. Contact Information
7. Password

How to use
-----------
1. Go to the directory where reservation.py exists.
2. execute script as below.
  python3 reservation.py -d <date> -n <name> -r <room number> -s <starting time> -e <ending time> -p <prof name> -c <contact>

Options
---------
  -d, --date     Date to reserve a room. ex)2018-07-09
  -n --name      name of the meeting
  -r --room      Seminar Room Number. ex)23-312,56-321
  -s --start     Seminar starting time in 4 digit number. ex)1000(10 a.m.), 1400(2 p.m.)
  -e --end       Seminar ending time in 4 digit number. ex)1000(10 a.m.), 1400(2 p.m.)
  -p --prof      Name of the Professor
  -c --contact   Contact Information
  -w --password  Password needed for cancellation. Default is "Alpine" if you don't use this option.

Warning
----------
The seminar room reservation is only possible inside university's network. So does this software.

Licence
-------
This software is distributed under GPL v3.0
