#!/usr/bin/node
// Write a script that prints all characters of a Star Wars movie:
const axios = require('axios');

function getMovieCharacters(movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;
  
  axios.get(url)
    .then(response => {
      const characters = response.data.characters;
      
      characters.forEach(characterUrl => {
        axios.get(characterUrl)
          .then(characterResponse => {
            const characterName = characterResponse.data.name;
            console.log(characterName);
          })
          .catch(error => {
            console.error(`Failed to retrieve character data for ${characterUrl}`);
          });
      });
    })
    .catch(error => {
      console.error(`Failed to retrieve movie data for Movie ID: ${movieId}`);
    });
}

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: node script.js <Movie ID>');
  process.exit(1);
}

getMovieCharacters(movieId);
