# til-page-builder

A command-line tool for authoring "Today I Learned" posts in Markdown, which can be converted to HTML for publishing on the web.

<div align="center" style="width: 100%">
  <div style="display: flex; align-items: flex-start; justify-content: space-around;">
    <img width="150" src="./assets/bob_the_builder.png" alt="Bob the builder image">
    <img width="225" src="./assets/til_to_html.png" alt="TIL to HTML image">
  </div>
</div>

## Features
Converts **text** or **markdown** files to **html** files that can be rendered as web pages.

### Common features
* Parses the first line as **web page title** and top level heading if followed by 2 empty newlines.
* Parses all **text blocks**, delimeted by an empty line, as **`p` tags** for the html.
* Generates and adds a **Table of Contents** at the top of every generated docuement for better reader experience.

### Exclusive to markdown
* Parses **headings** just like github markdown. For example, a line starting with `# ` translates to an `h1`,  `## ` to and `h2`, and so on...
* Any piece of text wrapped with `**` is converted to `strong` tag (bolded) in html, and wrapped with `*` is converted to `em` tag (italicized).

## Usage

The driver file for this tool is located at `src/til_builder_main.py`. This is the file that needs to be executed for to perform all kinds of actions that the tool supports.

There are several ways in which you can use this tool.

### Default Behavior

At its core, the tool takes either a text file or a folder containing files as a positional argument and then generates corresponding html files to `./til` folder by default.

**Note:** The following commands assume that you are currently located in the src folder that contains the `til_builder_main.py` driver file.

1. Converting a file

```
python til_builder_main.py file.txt
```

2. Converting all files within a folder

```
python til_builder_main.py <folder path>
```

### Flags/Options for custom behavior

Here are some examples demonstrating usage of custom flags supported by the tool.

1. `-v` or `--version` : Displays the program name and the version that is in use.
```
python  .\src\til_builder_main.py --version
```

Output:

```
TIL Page Builder: 0.1.0
```

2. `-h` or `--help` : Displays a help message that describes usage of all kinds of commandline arguments supported.

```
python  .\src\til_builder_main.py --help
```

Output:
```
usage: TIL Page Builder [-h] [-o OUTPUT] [-v] [input_path]

Converts text files for TIL posts to HTML files for publishing on the web.

positional arguments:
  input_path            The path to a text file or a folder containing files to be converted to corresponding html file(s)

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Generates the html files in the provided directory, by default it is './til'
  -v, --version         Show the name and version of the project
```

3. `-o` or `--output` : Generates the html files in the provided directory, by default it is './til'.

For example, in order to generate the html files in a directory `./dist/html_files`
```
python til_builder_main.py --output ./dist/html_files
```
4. `-c` or `--config`: Allows specification of a [TOML](https://toml.io/en/) configuration file containing all required options for the program.

For example: Using a TOML file containing:
```TOML
output = "./build"
lang = "fr"
```
```
python til_builder_main.py myfile.txt --config config.toml
```

Will set the output directory and language of the HTML files  instead of having to use `--output` and `--lang`. Using `-c` or `--config` will override any other config flags provided.

## Examples

### General Use Case

This example demonstrates the app behavior for a `markdown` file.

[**examples\til-yattag.md**](https://github.com/Amnish04/til-page-builder/blob/master/examples/til-yattag.md)
![TIL Markdown](https://github.com/Amnish04/til-page-builder/assets/78865303/eb3197a2-59e7-4058-85dd-feeeb3af8fa2)

Run the command for conversion.
```
python src/til_builder_main.py examples/til-yattag.md
```

**Generated HTML Page**
![Generated Page](https://github.com/Amnish04/til-page-builder/assets/78865303/7dcdec5f-5a9c-4d2d-88f0-12b3285e93da)

***

### Table of Contents Demo

![TOC Demo](https://github.com/Amnish04/til-page-builder/assets/78865303/c5a141aa-2ac9-4405-b696-b5ca526492a4)


## Contributing

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)

Please read the [CONTRIBUTING.md](https://github.com/Amnish04/til-page-builder/blob/static-analysis-tooling/CONTRIBUTING.md) file for all the details required to get you started as an official contributor for this project.

## License

[MIT](https://github.com/Amnish04/til-page-builder/blob/master/LICENSE)

