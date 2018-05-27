// Import general CSS
import 'materialize-css';
import 'materialize-css/dist/css/materialize.css';

// Import specific CSS
import './main.css';

// Javascript libs
import $ from 'jquery';

$(document).ready(function() {

  $("form#upload input").change(function() {
    $("form#upload").submit();
  });

  $("form#upload input[type=text]").on('paste', function() {
    setTimeout(function () {
        $("form#upload").submit();
    }, 100);
  });

  $("input.snippet").click(function() {
    this.select();
  })

});
