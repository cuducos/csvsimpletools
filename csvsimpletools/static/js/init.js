var tried_to_submit = false;
var required_fields = ['csv', 'input_delimiter', 'command'];

$(document).ready(function(){

  $('button.example').show().hover(
    function (e) {
      btn_id = $(this).attr('id');
      box_id = btn_id.replace('btn_', 'box_');
      $('#' + box_id).show('fast');
    },
    function (e) {
      btn_id = $(this).attr('id');
      box_id = btn_id.replace('btn_', 'box_');
      $('#' + box_id).hide('fast');
    }
  );

  $('form').first().submit(function (e) {
    tried_to_submit = true;
    if (!is_valid()) e.preventDefault();
  });

  for (var i = 0; i < required_fields.length; i++) {
    $('*[name=' + required_fields[i] + ']').change(is_valid);
  }

  $('input[disabled]').removeAttr('disabled');

});


var is_valid = function () {

    if (tried_to_submit) {

      var form = document.forms[0];
      var errors = [];
      var groups = $('.form-group');

      // clean previous errors
      groups.removeClass('has-error');

      // add errors
      for (var i = 0; i < required_fields.length; i++) {
        var field = required_fields[i];
        if (form[field].value === '') errors.push(field);
      }

      // color label with errors
      if (errors.length > 0) {
        groups.each(function(){
          for (var i = 0; i < errors.length; i++) {
            var fields = $(this).find('*[name=' + errors[i] + ']');
            if (fields.length > 0) $(this).addClass('has-error');
          }
        });
        return false;
      }

      return true;

    }

};
