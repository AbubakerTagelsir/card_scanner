# Card Scanner

For the project installation first you have to install docker using the link below 
https://docs.docker.com/engine/install/ubuntu/

Then you can run the Dockerfile from the project to setup the enviroment

On Windows
https://docs.docker.com/docker-for-windows/

On Linux
https://docs.docker.com/engine/reference/commandline/run/


To submit the image scanning requests make a post request into 
/scanner/new

To list all the cards on the system 
/scanner

the images will be processed using pytesseract to extract the data from them then the data will be stored into a database table which will be used to fetch the list of the cards on the website

Project Structure

![alt project struture](https://github.com/AbubakerTagelsir/card_scanner/blob/master/struture.png?raw=true)


https://github.com/AbubakerTagelsir/card_scanner/blob/master/struture.png
