(function ($, window, document, undefined) {
    'use strict';

    var $form = $('#contact-form');

    $form.on("submit", function (e) {
        
        $(".submit-btn").after('<div class="ml-2 d-inline-block"><div class="spinner-border spinner-border-sm text-primary loading-icon" role="status"><span class="sr-only">Loading...</span></div></div>');
        
        var name = $("input[name='form-name']").val(),
            email = $("input[name='form-email']").val(),
            phone = $("input[name='form-phone']").val(),
            msg = $("textarea[name='form-message']").val();
        
        Email.send({
            SecureToken : "77aae7af-2662-4247-9b04-4511f0c97bf7",
            To : "contact@domainname.com",
            From : "admin@domainname.com",
            Subject : "Message from BDLAB",
            Body : "<p><b>Message:</b>" + msg + "</p><br><b>Phone:</b>" + phone + "<br><b>Email:</b>" + email
        }).then(
          function(){
              $(".loading-icon").remove();
              alert("Your message successfully sent");
              $("input[name='form-name']").val(null);
              $("input[name='form-email']").val(null);
              $("input[name='form-phone']").val(null);
              $("textarea[name='form-message']").val(null);
          }
        );
        
        e.preventDefault();
    });
}(jQuery, window, document));