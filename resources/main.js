$(document).ready(function() {

  $("form#upload input").change(function() {
    $("form#upload").submit();
  });

  $("form#upload input[type=text]").on('paste', function() {
    setTimeout(function () {
        $("form#upload").submit();
    }, 100);
  });

});
