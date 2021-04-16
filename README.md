```
 ██████   ██████                                   ██████████                  ███
░░██████ ██████                                   ░░███░░░░░█                 ░░░
 ░███░█████░███  ██████ █████████████   ██████     ░███  █ ░████████   ███████████████████   ██████
 ░███░░███ ░███ ███░░██░░███░░███░░███ ███░░███    ░██████ ░░███░░███ ███░░██░░██░░███░░███ ███░░███
 ░███ ░░░  ░███░███████ ░███ ░███ ░███░███████     ░███░░█  ░███ ░███░███ ░███░███░███ ░███░███████
 ░███      ░███░███░░░  ░███ ░███ ░███░███░░░      ░███ ░   ░███ ░███░███ ░███░███░███ ░███░███░░░
 █████     ████░░██████ █████░███ ████░░██████     █████████████ ████░░███████████████ ████░░██████
░░░░░     ░░░░░ ░░░░░░ ░░░░░ ░░░ ░░░░░ ░░░░░░     ░░░░░░░░░░░░░ ░░░░░ ░░░░░██░░░░░░░░ ░░░░░ ░░░░░░
                                                                      ███ ░███
                                                                     ░░██████
                                                                      ░░░░░░
```

It does not create memes it just creates videos from those memes.

## Installation

for simplicity sake ive included almost everything in this repository but I could'nt mash teseract-ocr in here so just download tesseract-ors [here](https://github.com/UB-Mannheim/tesseract/wiki).
Which is not true anymore I've included it this folder.

But that doesn't matter very much

## use

To use this software make sure you have python<sup>1</sup> installed and activate this projects venv by `$> venv\Scripts\activate.bat`.
Now you should see `(venv)$> ...`
If you see an error above don't worry aslong as you're seeing the `(venv)` prefix it should be oké.

## Documentation

You'll first need to make a `secret.py` file. And in there you want the following variables:
|Variable|Value|
|---|---|
|USERNAME|"Your username"|
|PASSWORD|"Your password"|
|CLIENTID|"Your client id<sup>°</sup>"|
|CLIENTSECRET|"Your clients secret<sup>°</sup>"

```
You'll need to make a new script project on reddit. There youl see a short string of text underneath the project name. Thats your clientid. Then when you click on edit you'll see a long string of caracters. That's your client secret.
```

You might wanna chech some external info for this right [here](https://praw.readthedocs.io/en/latest/getting_started/quick_start.html).

Here comes the documentation on theutilisation of this "pakket".

## Info

Some info you need to know whilst using this software.  
1 the code is not user friendly so a little bit of python can come in helpfull  
2 Some common meme pages are :

- memes
- dankmemes
- memeeconomy
- pewdiepieSubmissions (can also include a lot of crap)

3 This is still in development soo expect a lot of changes (also I'm very lazy<sup>2</sup> so don't worry when i do nothing for like two weeks just invoke me.)
4 Don't be afraid to change my (mediocre/bad) code. Go ahead and change it. Have fun with it!

## unshure info

1. It might be plausible that their is a python interpreter in here so if yoou don't have python installed give it a try.

2) Not lazy perse I just don't have a very long attention span so I might have left this project behind but if you invoke me I'll shure work on it.
