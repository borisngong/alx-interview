#!/usr/bin/node

const request = require("request");

const movieId = process.argv[2];

if (!movieId) {
  console.error("Please provide a movie ID.");
  process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const film = JSON.parse(body);
    const characters = film.characters;

    characters.forEach((characterUrl) => {
      request(characterUrl, function (error, response, body) {
        if (!error && response.statusCode === 200) {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    });
  } else {
    console.error("Failed to fetch movie data:", error);
  }
});