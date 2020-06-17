# Crack Checker

<img src="./assets/cw_logo.png">

## The way it works
The CrackCheck.py is a program that concentrates on parsing information from the website [CrackWatch](https://crackwatch.com/?ref=57955)'s API.<br>
Since the API provided the information for the games avaliable in JSON format, we tried utilizing the *requests*, and the *json* module to parse it.
In the latest release, the implementation has been changed to locally storing the data received from the website and parsing through that data.

The link to the API is [here](https://crackwatch.com/api), and since it only provided the pages and not the search for the games themselves, we were forced to parse the entire page to check for the presence of the game in the cracked list.<br>
The code, in the end, performed a simple operation to check for whether or not the game was present in the specific page of the API's response.

```python
# the 'link' below is to the website's api call "https://api.crackwatch.com/api/games?&is_cracked=true&page="
url = urlopen(link) 
data = loads(url.read()) # loads has been imported from the JSON module in python.
strdata = str(data)

# the part below checks if the page is empty at the end of the search and returns a response to the user.
if(strdata!="[]"):
    if (strdata.find(title) != -1):
        return True
    else:
        return False
```
This is put in a loop and iterates through the pages, checking whether or not the game title has been found.

---
Stated in their API usage terms, is the fact that you cannot call it more than once per second, as such, we've fine tuned it to be within the terms.<br>
I've sent a bug report to the CrackWatch admins, and it has been noted and they are working on it.

## 17/06/2020 Update
The admins at CrackWatch have responded back and are working on the issue as of right now, the program as well has been optimized quite a bit, leaning into the factor of storing the data when we get it rather than trying to retrieve it all at once.

The API service seems to fail infrequently, and as such is given in the Try and Except, in the program.
Feel free to utilize it anyway.