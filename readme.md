# Rainybear

Being a small Python script to convert bookmarks from a Raindrop CSV export into a format that can be imported as notes into Bear.

An individual Markdown file is created for each bookmark. When imported into Bear, it creates a note with  the following format:

- the title of the bookmark becomes the title of the note
- if there is an excerpt in the bookmark, this becomes the body of the note
- the url is included below the excerpt
- Raindrop tags are converted into Bear tags with the format `#bookmark/tag_name`
- Additional Bear tags are created from the bookmark's creation date, in the format `#bookmark/yyyy/mm/dd`

## Usage
1. In Raindrop, select the bookmarks you want and export them in CSV format
2. Name the export file `bookmarks.csv` and place it in the `input` directory
3. Run the converter with `python converter.py`
4. In Bear, import the contents of the `output` directory

## Notes
- This entire script was written by ChatGPT4, so I'm not going to take any credit for it. E&EO etc etc etc