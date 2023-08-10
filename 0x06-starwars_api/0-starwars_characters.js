#!/usr/bin/node
// Write a script that prints all characters of a Star Wars movie:
const request = require('request');
const { json } = require('stream/consumers');

async function getMoviesCharacter(id) {
    const url = `https://swapi.dev/api/films/${id}/`;
   const data = await request(url, (error, response, body) => {
        if(error){
            console.log(`Failed to retrieve movie data for movieId ${id}`)
            return
        }

        if (response.statusCode !== 200){
            console.log(`Failed to retrieve movie data for movieId ${id}`)
            return
        }

        const movieDt = JSON.parse(body);
        const characters = movieDt.characters


        characters.forEach(element => {
            request(element, (CharError, CharReponse, CharBody) => {
                if(CharError){
                    console.log(`Failed to retrieve movie data for movieId ${id}`)
                    return
                }
        
                if (CharReponse.statusCode !== 200){
                    console.log(`Failed to retrieve movie data for movieId ${id}`)
                    return
                }

                const CharacterData = JSON.parse(CharBody);
                const CharacterName = CharacterData.name
                console.log(CharacterName)
            })
        });
    })

    return data

}

getMoviesCharacter(3)