# Notes

## Meeting at SĮ Susisiekimo Paslaugos, 2015-12-03

People we met:
* Alfredas, +370 686 60445
* Artūras Lapinskas, + 370 616 55982, arturas.lapinskas@vilniustransport.lt

* Only the police (not municipality!) can fine bad drivers on A lanes; however laws are being introduced
in Seimas to change that; but it may happen only after a year or more. Police is already overwhelmed
with speeding camera tickets, so extra load is not welcome. A lot of manual work at police, could
be improved.
* Privacy laws are strict in our land, licence plates are considered "part of identity" - can't store them, share them.
* Not only the licence plate is required to impose a fine, but also face of driver, his licence number,
count of passangers. A lot of bureaucracy, Lithuanian laws need to be changed.
Links to Regitra database could also be needed, etc.
* Police, VAD, Vilnius Airport, etc. have each separate camera networks. There are attempts to
integrate all of them into a single system, share them. This is not going well.
* It is already planned to put a stationary camera somewhere as a pilot project that would stream video.
Povilas/we could get access to this stream and use it to test our ideas, make MVP.
* Most cameras that are on streets of Vilnius are analogous, low quality, there are plans to expand
network, add digital high quality cameras, streaming videos, but this will happen in couple of years.
* There are around 600 buses, ~50 cameras inside, ~50 facing outside. No Internet connection
inside buses, all data stored inside memory cards, used only when there are accidents/crimes.
* As of now, GPS coordinates of a bus are determined and sent every 30 seconds (?), not very accurate, dots are jumping: http://www.stops.lt/vilnius/gps.txt
* Cameras in newer buses may have GPS coordinates inside video stream.
* Cameras need to be certified if you don't want law problems.
* There are separate accounts for m.ticket, m.parking, "vilniečio kortelė", other services... so each user
has to create separate accounts - single account for everything would be great.
* Extra application with a button for a driver is not a good idea - he must execute his duties, not do something unrelated
* There are problems with getting sold ticket data from buses, so terabytes of video footage transfer is
out of the question, however if our application would catch "suspicious activities" and store these tiny video fragments
separately - it may be possible.

## New ideas
* Citizens can subscribe and get SMS notifications when their bus(es) are being late (Alfredas)
  * they have pretty sweet infrastructure to track traffic and movement of public transport, so possibilities to improve public transport are great
* Reverse engineer m.ticket and m.parking applications (source is missing), it would be possible to go open-source (Artūras)
  * Basically the problem is that apps and whole server infrastructure was made by some shady private company. Due to some tricky contract "Susisiekimo paslaugos" cannot retrieve neither the source code, nor move service onto their own servers. Maintanence, new feature implementation cost a fortune;
  * to retrieve the code, etc. government must sue the private company, but they do not want to do it as service would be shutdown, all in all it is complicated and I digress;
  * m.parking is used by 60% of users, so if private company shuts it down - it's not good;
  * ultimate plan to have "vilniečio kortelė", "m.ticket", "m.parking" as one system with different apps. Now all these 3 apps are completely separate, so, for example, user who has 30 eur in "vilniečio kortelė", can't use that money with "m.ticket";
  * we should ask Artūras for app specifications;
  * we asked to present this in a meetup, though they have many business trips, and hardly can make it;
  * they would be very happy if we rewrite those applications, probably made them open-source and move the infrastructure into the hands of government.
* *Somewhat related idea*: Buses are like blood inside the transportation body of Vilnius City, if buses are stopping and/or moving very slowly -- you know that there is a traffic jam there. This could be determined automatically and it can be very useful for car drivers! [Note: it's already done: http://stops.lt/vilnius/#vilnius/map/en and push 'show traffic' button on the right side, though it could be somewhat with better UI/UX, or even a separate app. Also accuraccy is unknown]
