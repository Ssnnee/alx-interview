#!/usr/bin/node

const request = require('request');
const { promisify } = require('util');

const requestAsync = promisify(request);

async function getFilmCharacterNames(filmId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${filmId}/`;

  try {
    const { body } = await requestAsync(url);
    const film = JSON.parse(body);

    for (const characterUrl of film.characters) {
      try {
        const { body: charBody } = await requestAsync(characterUrl);
        const character = JSON.parse(charBody);
        console.log(character.name);
      } catch (charError) {
        console.error(`Error fetching character data: ${charError.message}`);
      }
    }
  } catch (error) {
    console.error(`Error fetching film data: ${error.message}`);
  }
}

const filmId = process.argv[2];
if (!filmId) {
  console.error('Please provide a film ID as an argument.');
  process.exit(1);
}

getFilmCharacterNames(filmId);

