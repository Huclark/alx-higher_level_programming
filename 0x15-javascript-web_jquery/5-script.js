$('DIV#add_item').on('click', () => {
  const item = '<li>Item</li>';
  $('UL.my_list').append(item);
});
