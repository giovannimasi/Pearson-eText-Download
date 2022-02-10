# Pearson-eText-Download 1.0.0
In case of problems contact me on Telegram @itsjustme00

If you think this tool is shit...note that actually Pearson is shit: pages are provided through a simple png for each page.

Anyway...thats how to use it

## Tutorial
For using this tool you need to have the book activated in your Pearson account...NO PIRACY

Make sure python is installed...

Finally these are the information you'll need:

* _etext-cdn-token_:  the cookie that connect your account session to the download links
* The book id
* Pages number

Here's how to get them.

### _etext-cdn-token_

This token is a cookie representing your Pearson account session, necessary to get a valid download link for each page.

1. First of all go to My Pearson Place, log into your account and open the ebook you want to download. This step will assure the creation of the cookie in your browser.
2. Reach the cookie section of your browser (For example, Chrome let you reach this in `Settings > Advanced`, or Edge Chromium has the left section menu...check for your browser)
3. Search for `pearson-intl.com` (you can use the search bar), open it and expand `etext-cdn-token`. What you'll need is his value

### Book Id and pages count

Necessary for recognising your book

1. Go back to the ebook and slide pages until the last one.
2. Open Inspect tool and select the last page.
3. This will be an <img> element. Search for src attribute and double click on the link. This link contains all the information remained.

Book Id has this structure `12345/abcdefghijklmnopqrstuwxyz` and is placed between `prod1/` and `/pages`

Pages number is just after that (e.g. `page123`). Make sure you selected the **last page**

That is the number you will need.

### The Tool

Execute `start.py`, paste the requested information and wait for the program to download and create the pdf file.

At the end you will be asked to delete the png sources for the pdf. I advise to do that.
