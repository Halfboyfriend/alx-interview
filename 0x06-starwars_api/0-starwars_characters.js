#!/usr/bin/node
const request = require('request');

async function getMoviesCharacter(id) {
    const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;
   const data = await request(url, (error, response, body) => {
        if(error){
            console.log(`Failed to retrieve movie data for movieId ${id}`);
            return;
        }

        if (response.statusCode !== 200){
            console.log(`Failed to retrieve movie data for movieId ${id}`);
            return;
        }

        const movieDt = JSON.parse(body);
        const characters = movieDt.characters;


        characters.forEach(element => {
            request(element, (CharError, CharReponse, CharBody) => {
                if(CharError){
                    console.log(`Failed to retrieve movie data for movieId ${id}`)
                    return;
                }
        
                if (CharReponse.statusCode !== 200){
                    console.log(`Failed to retrieve movie data for movieId ${id}`)
                    return;
                }

                const CharacterData = JSON.parse(CharBody);
                const CharacterName = CharacterData.name;
                console.log(CharacterName);
            })
        });
    })

    return data;

}

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: node star_wars_characters_request.js <Movie ID>');
  process.exit(1);
}

getMoviesCharacter(movieId)
