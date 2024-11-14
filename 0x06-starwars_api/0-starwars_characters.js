#!/usr/bin/node

const request = require("request");
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  printCharacters(characters, 0);
});

function printCharacters(characters, index) {
  if (index >= characters.length) {
    return;
  }
  request(characters[index], (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }
    const characterData = JSON.parse(body);
    console.log(characterData.name);
    printCharacters(characters, index + 1);
  });
}
