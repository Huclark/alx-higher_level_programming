function fetchTranslation () {
  const code = $('INPUT#language_code').val();
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + code;

  $.get(url, function (data) {
    $('DIV#hello').text(data.hello);
  });
}

$(() => {
  $('INPUT#btn_translate').on('click', fetchTranslation);

  $(document).on('keypress', function (e) {
    if (e.which === 13) {
      fetchTranslation();
    }
  });
});
