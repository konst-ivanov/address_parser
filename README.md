This project contains the script that transforms address strings consisting of street names and house numbers into JSON objects.

The script should be executed with the arguments:
* `-i <input_file_path>`  : path to the file containing address strings, one on each row,
* `-o <output_file_path>` : path to the JSON file where the result will be saved,

i.e.:
```
python parse_address_lines.py -i files/input.txt -o files/output.json
```

You can find the example of input and output in the `files` folder.
