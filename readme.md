# Better Trump Logo Bot

Welp this bot makes me a bit sad now. Probably due for some improvements. But was my first foray into an image bot (other than animated gifs).

## Method 

### Image Generation

I'm using Pillow, an updated version of the Python Imaging Library (PIL) to take a template image `logo_template.png` and over lay the text slogan beneath the campaign logo above. PIL handles outtputing the font onto the image as well.

PIL's font rendering is really ugly at small font sizes in my experience, but at this font size it worked okay.

I managed to figure out the exact font used in this logo using [What The Font!](https://www.myfonts.com/WhatTheFont/) on the origin logo.

Since text can be variable number of characters, I wrote a function to insert whitespace between characters so it extends to 80% or so of the image. I think this is esentially text justification, right?

See the text in this generated logo for example:

![Example Logo Justification](https://pbs.twimg.com/media/CzReoX2WQAYyCQz.jpg:large)

### Text Generation

I got pretty lazy here, as figuring out the font spacing and rendering was all new to me, and took a while.

The formula is:

- Line 1: Word that starts **T**, at least 3 syllables.
- Line 2: Word that starts with **P**, at least 3 syllables.
- Line 3: Make America **X** Again! Where **XX** is some random word with negative connotation.

I just build the words list up in `corpus/` from copy/pasting from some online word list or dictionaries as I recall.



