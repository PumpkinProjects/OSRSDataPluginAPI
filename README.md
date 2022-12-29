
# OSRSDataPluginAPI

This Project is the API and web-interface for a [RuneLite](https://runelite.net/) plugin designed to capture user metrics and data for [Old School RuneScape](https://oldschool.runescape.com/). This project uses said metrics and data collected (E.g. PvE Stats, PvE Drops, Skilling Experience Gains, etc.) and allows users to visualize the history of their account through the lens of a data driven perspective.

# Stack Information

This project is built using Python's [FastAPI](https://fastapi.tiangolo.com/) and [Vite-React](https://vitejs.dev/). Which communicates with a [MongoDB](https://www.mongodb.com/home) database where data is stored by a Java based plugin installed into RuneLite.

### Recommended Minimum Requirements
All current as of 12/29/2022

* Python Version: 3.9.16
* Node Version: 16.9.0
* NPM Version: 9.2.0
* Yarn Version: 1.22.19
* Linux Distro: Ubuntu 14.04

# FAQ

**Can I clone and host this application?**

As this project exist in the MIT space you're free to clone and attempt to use this project. Obviously without several key pieces outside of this project running it will be a challenge. If you really wish to use this project and want help please do not hesitate to ask any members for assistance.

**Do you track sensitive information like usernames or passwords?**

Definitely not! The goal of this project upfront is to anonymously capture user data in regards to only already publicly avalaible details on Old School Runescapes Highscore page. Unless users specifically opt into linking their details to their anonymous identified provided by the plugin our system and anyone else will never be able to know whos data is whos. Even when users opt in to claim their anonymous identified it's strongly encouraged to make their credentials something unrelated to their runescape account. Privacy and security is extremely important to this project!

## License

[MIT](https://choosealicense.com/licenses/mit/)

