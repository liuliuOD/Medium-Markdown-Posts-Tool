# Medium Markdown Posts Tool

Creating Medium posts directly in the Medium editor can be cumbersome, especially for those who prefer using markdown. This tool aims to simplify the process and provide a more efficient way to compose and manage your Medium articles.

## Introduction

Welcome to the Medium Markdown Posts Tool! This tool is designed to simplify the process of creating [Medium](https://medium.com) posts by leveraging the [Medium API](https://github.com/Medium/medium-api-docs) and allowing you to use familiar markdown syntax. Say goodbye to the hassle of navigating the Medium editor UI with this streamlined command line tool.

## Features

- Command Line Interface: Create your `Medium` posts using simple command line interactions.
- Markdown Support: Write your posts using markdown, making it easy to structure and format your content.
- Effortless Publishing: Seamlessly publish your articles directly from the command line.

## Installation

- `Install Dependencies:`
  ```bash
  $ poetry install
  $ poetry shell
  ```
- `Configure Medium API Key:`
Obtain your `Medium API key` from the Medium > Settings > Security and apps > Integration tokens.

## Usage

- Creating a New Post
  ```bash
  $ python3 main.py --title your_custom_title --file your filepath --format md_or_html_default_md
  ```

## Contribution

Contributions are welcome! If you have ideas for improvements or want to fix a bug, feel free to open an issue or submit a pull request.

## License

This project is released under the AGPL v3 license. See the [LICENSE](./LICENSE) file for more details.

## References

- [Medium API Documentation](https://github.com/Medium/medium-api-docs)
