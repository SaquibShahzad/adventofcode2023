
# imported the requests library
import requests
file_url = "https://adventofcode.com/2023/day/8/input"
# URL of the image to be downloaded is defined as image_url
# create HTTP response object
r = requests.get(file_url)

# send a HTTP request to the server and save
# the HTTP response in a response object called r
with open("input.txt", 'wb') as f:

    # Saving received content as a png file in
    # binary format

    # write the contents of the response (r.content)
    # to a new file in binary mode.
    f.write(r.content)
