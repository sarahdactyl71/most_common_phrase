# Most Common Phrase
A command line tool that counts the most common three word sequences from a text file. 

## How to Run the Program
There are two ways to process text files.

- The first is to run `python count_phrases.py` in the root directory.
- This will put up a prompt asking you to input the paths to your textfiles.
- If you would like to enter more than one file just separate the files by a comma eg. `../origin_of_species.txt', '../moby_dick.txt'`
- From there this should output the top 100 most common three word sequences.

- The second way to run this file is to use stdin to process a text file. 
- You will run this command in your terminal: `cat <relative_path_to_file.txt> | python ./count_phrases.py`
- This will automatically output the top 100 most common three word sequences. 

## Running Using Docker
- For ease of testing and as an example I have included a text file in this repo. 
- In the root directory run `docker run -it --rm --name my-running-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python count_phrases.py`
- This will throw a prompt asking for the path to your file. 
- Type in your input, for this app I used `origin_of_specied.txt`
- This should output 100 of the most common phrases for that text file. 

## Running the Test Suite
- make sure you have `nose` installed `pip install nose`
- in the root directory run `python -m nose`
- this will output passing values for the tests

## Plans for the Future
I would really like this to be a playfround for a fully fledged docker app to do more language processing on. 
This means learning a bit more about docker's functionality as well as seeing how that connected to other services
like Kubernetes. 

This brings me to my next plan, that I would like to refactor to consider handling huge amounts of data at one time. 
I am not sure what that would take, but I imagine that it would involve a bit of learning about scalability. 