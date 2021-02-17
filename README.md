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

## Schema

User
- username
- email
- create_at
- updated_at

Poll
- title
- created_by
- create_at
- updated_at
- is_add_choices_active
- is_voting_active

Choice
- poll_id
- text
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

## Planning TODOs

- [x] List all requirements
- [x] Create schema
- [ ] Design API
- [ ] Create mockups
- [ ] Choose technologies
