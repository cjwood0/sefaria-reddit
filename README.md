# SefariaQuoteBot

You can quote Jewish stuff on Reddit.

This project was difficult to complete, mostly beause it would involve joining the Sefaria deveopment team to fix their API and normalize some endpoints.

The problem is compounded by the fact that I am not Jewish, I cannot read Hebrew, and the structure and organization of Jewish texts varies wildy across books/collections. I organized a community of redditors  to help collect transliterations and abbreviations, but the project ultimately stalled due to not having the time available to commit to joining the Sefaria development team.

---

## Usage

You can quote a lot of stuff. Use `[]` for English and `{}` for Hebrew. The bot replies if it can find the text on Sefaria.

* [Genesis 1:1]

* [lev 1:1-5]

* {sota 2b}

* {Mishna Berakhot 4.2}

I don't really know what will or won't work. See https://github.com/Sefaria/Sefaria-Project/wiki/Text-References

## Installation

Clone the repo and execute `pip3 install`

## Environment Variables

`USERNAME` - Your Reddit username

`PASSWORD` - Your Reddit password

`CLIENT_ID` - Your Reddit client_id, accessible in your settings when you create an app

`CLIENT_SECRET` - Your Reddit app client_secret, found with your client_ido target.


## Running

`python3 sefaria_bot.py`

## Hosting

SefariaQuoteBot can be easily be deployed to Heroku:

1. Install the Heroku CLI and `heroku login`
2. Create your own SefariaQuoteBot app with `heroku create <optional-name>`
3. Set your heroku environment variables
4. Deploy SefariaQuoteBot using `git push heroku master`


## Contributing

Feel free to request access to the repo.
