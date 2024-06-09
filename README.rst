-----
Usage
-----

- First clone this repo to your computer

- cd into Pyzim.github.io

- create your virtual environment and activate it 

- run ```pip install -r requirements``` to install pelican with markdown support

- Start writting some content in markdown or restructured text inside the content directory. 
  If you want to write content for pages as opposed to blog articles save the files as markdown files 
  inside the content/pages directory

- When your are finished writting your content you can view your site by running: 

  .. code:: bash

  pelican -lr  

  This will generate some html for your and start the server at port 8000 . You can view your site at http://localhost:8000

- To use the custom theme that we are using for the event you can download it `here: <https://github.com/Pyzim/event-agency-theme>`_ 


You will then need to copy this directory to the project folder and edit pelicanconf.py and change the THEME setting to: 

 .. code:: python
  
  THEME = "event-agency-theme"
