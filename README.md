# Get-Sched-Go
This would be a web application which will be your next stop to planning your day easily and effectively.
We will schedule your task and also hand you a CSV output if you need to export to your frequently used calender.

Clone this repository and run manage.py as a django web application and enjoy this app.
## How to clone and make it running?
* First step is clone this repository to your local machine.
* sudo apt-get install python3 python3-pip
* sudo pip3 install -r requirements.txt
## Basic Features
## Personalised mode:
* ### Personal details and habits:
    * **Input** as query/form from user
        * Sleep Preferences/slots:
            * Duration __fullfilled__
            * Timing 
        * Work Preferences:
            * Timings Day/Night __fullfilled__
            * Duration Continous/sparsed
            * Stamina
        * Meals (availability timing and preferred)
        * Personal Interests and Hobbies:
            * Chillout Preferences
            * follows **football** / **NBA** __fullfilled__
        * Travel times/buffer
            * Assuming 2 venues (by default)
    * Consequences and blah blah
* ### Processing Inputs
    * Initial Inputs:
        * Base Time table (autoumatically generated by course code  given by user) __fullfilled__ __fullfilled__
    * Regular Inputs: __fullfilled__
        * Insti Events 
        * Assignments and pre-declared quizzes help-sessions
        * Tutorial prep (solve/ view tutorial)
        * Daily/weekly target (eg complete a lecture/tv series)
* ### Event Details:
    * Priority: __fullfilled__
        * Acad/personal
        * Indespensable (eg quiz exam assignment)
        * High (Game of thrones,meeting with friends)
        * preferred (regular study slot , sleep)
        * mediocre (sports)
        * least (dedicated chillout)
    * Timing: __fullfilled__
        * fixed timing
        * deadlined (hard/soft)
        * flexible
 Event shcheduling will take into consideration mainly these above mentioned two parameters
    * Other addons 
        * venue __fullfilled__
        * description __fullfilled__
        * buffer time/recovery time.
* ### Interface and working:
    * Account based service __fullfilled__
    * will ask for basic profile info i.e. **"Personal details and habits"** __fullfilled__
    * add event for a day/week. __fullfilled__FOR day
    * get events from instructor __fullfilled__
    * fix meetings with friends and instructor 
    * group study/meet by schedule interaction.
    * estimate of events like exam prep, assignment etc. as given be peers __fullfilled__
    * exporting schedule in some format (eg csv for google calender) __fullfilled__
