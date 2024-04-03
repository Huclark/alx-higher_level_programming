$(() => {
  $('INPUT#btn_translate').on('click', () => {
    const code = $('INPUT#language_code').val();
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + code;

    $.get(url, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
