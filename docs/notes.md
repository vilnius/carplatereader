# Notes

## Meeting at SĮ Susisiekimo Paslaugos, 2015-12-03

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
* As of now, GPS is processed every 30 seconds, not very reliable.
* Cameras in newer buses may have GPS coordinates inside video stream.
* Cameras need to be certified if you don't want law problems.
* There are separate accounts for m.ticket, m.parking, "vilniečio kortelė", other services... so each user
has to create separate accounts with separate amounts - single account for everything would be great.
* Extra application with a button for a driver is not a good idea - he must execute his duties, not do something unrelated
* There are problems with getting sold ticket data from buses, so terabytes of video footage transfer is 
out of the question, however if our application would catch "suspicious activities" and store these tiny video fragments
separately - it may be possible.

## New ideas
* Citizens can subscribe and get SMS notifications when their bus(es) are being late (Alfredas)
* Reverse engineer m.ticket and m.parking applications (source is missing), it would be possible to go open-source (Artūras)
