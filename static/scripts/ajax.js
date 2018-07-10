function send_sentence() {
    $.ajax({
        type: "POST",
        url: "/ajax",
        data: $('form').serialize(), //to correct this
        type: 'POST',
        success: function(response) {
            console.log(response);
        },
        error: function(error) {
            console.log(error);
        }
    });
}
