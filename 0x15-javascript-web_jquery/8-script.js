$.getJSON('https://swapi.co/api/films/?format=json', function (data) {
  const listObj = data.results;
  for (const i of listObj) {
    $('UL#list_movies').append('<li>' + i.title + '</li>');
  }
});
