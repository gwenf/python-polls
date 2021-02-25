# Python Polls

This is a live survey/poll app.

## Initial Plan

1. Anyone can vote
2. Anyone can add an option to the poll (during a certain time period)
3. The options can just be a picture (uploaded would be nice, but even just as a link to an image URL would be okay)
4. Can use social login from Twitch or Github

Basically, let people make suggestions or requests, and then let everyone else vote on those suggestions/requests

For example. If I were to do a "Build this thing in CSS" challenge on Twitch, I'd want people to be able to suggest screenshots, and for people to vote on which one they'd like to see.

## Requirements

Poll owner (person who created the poll):
1. Create a poll
2. Toggle the option to allow people to add options to the poll (they can toggle off and on when they want)
3. Can allow voting to start
4. Can choose to time the voting or manually turn off and on
5. Can give other people roles, like mod
6. Can log in with Twitch

Mod (bonus feature?):
1. Can remove poll choices
2. Can vote

Poll voters (people who participate in a poll):
1. Anyone can vote
2. Anyone can add an option to the poll (during a certain time period)
3. Don't need to be logged in unless they are adding options to the poll

## Technologies

- Python 3.9+
- Poetry
- Fast API
- Postgres
- SQLAlchemy
- Uvicorn

## Local Development

1. Clone this repo and `cd` into repo directory
2. Check your Python version: `python -V`. If less than 3.9, use `pyenv` to install and switch to 3.9+.
3. Make sure [Poetry](https://python-poetry.org/docs/) is installed
4. Create a virtual environment: `python -m venv venv`
5. Install dependencies: `poetry install`
6. Run the server: `poetry run uvicorn main:app --reload`
7. Access swagger at: http://127.0.0.1:8000/docs

## Schema

User
- username
- email
- create_at
- updated_at

Poll
- title
- type: ChoiceField (e.g. text or image)
- created_by
- create_at
- updated_at
- is_add_choices_active
- is_voting_active

Choice
- poll_id
- text
- image (nice to have feature)
- votes
- created_by
- create_at
- updated_at

Moderator
- mod_for
- mod_user
- create_at
- updated_at

Ban
- poll_owner_id
- banned_by (poll owner or moderator)
- user_id (person who is banned)
- create_at
- updated_at

## Design API

// TODO: social auth endpoints

**polls/**

- GET: list of the users polls
- POST: create a new poll
- DELETE: all polls???

**polls/:id/**

- GET
- PATCH
- DELETE

**polls/:id/choices/**

- GET
- POST

**polls/:id/choices/:id/**

- GET
- PATCH
- DELETE

**banned-users/**

- GET

**users/:id/ban/**

- POST
- DELETE

**users/:id/mod/**

- POST
- DELETE

## Planning TODOs

- [x] List all requirements
- [x] Create schema
- [x] Design API
- [x] Create mockups
- [x] Choose technologies
