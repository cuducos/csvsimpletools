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

});
