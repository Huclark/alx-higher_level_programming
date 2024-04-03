$(() => {
  $('DIV#add_item').on('click', () => {
    $('<li>').text('Item').appendTo('.my_list');
  });

  $('DIV#remove_item').on('click', () => {
    $('li:last').remove();
  });

  $('DIV#clear_list').on('click', () => {
    $('.my_list').empty('li');
  });
});
