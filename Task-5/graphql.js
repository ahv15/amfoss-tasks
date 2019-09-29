const axios = require('axios');
const endpoint = 'https://api.github.com/graphql'
const token = ' 5a43ae4c62c3db0efe50aece73d1882d4dffc38f'
const oauth = {Authorization: 'bearer ' + token}
const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
})

readline.question(`Enter users id`, (user) => {
  readline.close()
})
const query = '{' +
                'repositoryOwner(login: "${user}") { ' +
                  '... on User {' +
                         'name, '+
                          'avatarUrl, '+
                            'bio, '+
                             '}' +
                            '}' +
                           '}' 
                    

axios.post(endpoint, {query: query}, {headers: oauth})
  .then(function (response) {
    console.log(response.data);
  })
  .catch(function (error) {
    console.log('Couldnt find username');
  });
