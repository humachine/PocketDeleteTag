## Delete All Articles of a Tag from Pocket

Ever wanted to delete all the articles of a particular tag from Pocket? 
The Pocket app (or the website) does not have a mode to bulk delete/favourite artilces of a tag.
This repo is a way to use the Pocket API to achieve the same. Here's the steps:
- Create a new app on Pocket's Developers page and obtain the consumer key.
- Save it somewhere safe (default: pocket.apikeys in the working directory)
- Run RetrieveInfo.py to trigger the process to obtain an access token. It should take you to a page where you can authorize the deleteTag app.
- Once authorized, just enter the tag when prompted
- Lo! 


