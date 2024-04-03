$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (response) {
  $.each(response.results, function (index, item) {
    $('<li>').text(item.title).appendTo('UL#list_movies');
  });
});
