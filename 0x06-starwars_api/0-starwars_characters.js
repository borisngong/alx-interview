#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
if (!filmId) {
  console.error('Please provide a film ID as an argument.');
  process.exit(1);
}

request(`https://swapi-api.hbtn.io/api/films/${filmId}`, (err, res, body) => {
  if (err) {
    console.error('Error fetching film:', err);
    return;
  }

  if (res.statusCode !== 200) {
    console.error('Failed to fetch film. Status code:', res.statusCode);
    return;
  }

  const actors = JSON.parse(body).characters;
  exactOrder(actors, 0);
});

const exactOrder = (actors, index) => {
  if (index === actors.length) return;

  request(actors[index], (err, res, body) => {
    if (err) {
      console.error('Error fetching character:', err);
      return;
    }

    if (res.statusCode !== 200) {
      console.error('Failed to fetch character. Status code:', res.statusCode);
      return;
    }

    console.log(JSON.parse(body).name);
    exactOrder(actors, index + 1);
  });
};
