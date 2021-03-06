# Most Common Phrase
A command line tool that counts the most common three word sequences from a text file. 

## How to Run the Program
There are two ways to process text files:

- The first is to run `python count_phrases.py <paths to textfiles>` in the root directory. The text files
will be relative paths to the files on your machine. E.g. `python count_phrases.py text_file_one.txt ../text_file_two.txt`
- NOTE: no need to wrap the text files in quotes when you enter in your relative path, 
these will already be processed as strings. 
- From there, this should output the top 100 most common three word sequences.

You can also use `stdin` to pipe a text file to the script:

- The second way to run this file is to use stdin to process a text file. 
- You will run this command in your terminal: `cat <relative_path_to_file.txt> | python ./count_phrases.py`
- This will automatically output the top 100 most common three word sequences. 

You may also use echo to the same effect:

- echo "dogs are great dogs are great dogs are great dogs are great" | python count_phrases.py

## Running Using Docker
- For ease of testing and as an example I have included a text file in this repo. 
- In the root directory run `docker run -it --rm --name my-running-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python count_phrases.py origin_of_species.txt`
- This should output 100 of the most common phrases for that text file. 

## Running the Test Suite
- make sure you have `nose` installed `pip install nose`
- in the root directory run `python -m nose`
- this will output passing values for the tests

## Plans for the Future
I would really like this to be a playground for a fully fledged docker app to do more language processing on. 
I think it might be cool to examine an author's or artist's full catalogue and see what phrases or words they
tend to lean on. This means learning a bit more about docker's full functionality. 

I would also like to add support for unicode characters.