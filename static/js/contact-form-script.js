/*==============================================================*/
// Raque Contact Form  JS
/*==============================================================*/
  // $(document).ready(function(){

  //       $('#sendEmail').on('click', function(e){
  //         e.preventDefault()
  //         console.log('Button is pressed')
  //       });

  //   });

(function ($) {
    "use strict"; // Start of use strict
    $("#contactForm").validator().on("submit", function (event) {
        if (event.isDefaultPrevented()) {
            // handle the invalid form...
            formError();
            submitMSG(false, "Did you fill in the form properly?");
        } else {
            // everything looks good!
            event.preventDefault();
            submitForm();
        }
    });

     $('#sendEmail').on('click', function(e){
          e.preventDefault()
          console.log('Button is pressed')
        });

    function submitForm(){
        // Initiate Variables With Form Content
        var name = $("#id_name").val();
        var email = $("#id_email").val();
        var msg_subject = $("#id_subject").val();
        var phone_number = $("#id_phone").val();
        var message = $("#id_message").val();
        var csrfmiddlewaretoken = $("input[name=csrfmiddlewaretoken]").val()

        // var csrf_token = '{% csrf_token %}';
        $.ajax({
            type: "GET",
            url: "/contacts/",
            data: {"name=" + name + "&email=" + email + "&subject=" + msg_subject + "&phone=" + phone_number + "&message=" + message +"&csrfmiddlewaretoken="+csrfmiddlewaretoken},
            
            success : function(text){
                if (text == "success"){
                    formSuccess();
                } else {
                    formError();
                    submitMSG(false,text);
                }
            }
        });


       // var form = document.getElementById('contactForm')
       // var fd = new FormData(form)
       // // console.log(fd)
       // // console.log(form)
       // var forma = $('form').serialize()
       // console.log(csrf_token)
       // console.log(csrfmiddlewaretoken)
    //    $.ajax({
    //     url: "/contacts/",
    //     data:  {csrfmiddlewaretoken: csrf_token},
    //     cache: false,
    //     processData: false,
    //     contentType: false,
    //     type: 'POST',
    //     success: function (dataofconfirm) {
    //         console.log('success')
    //     }
    // });

    }

    function formSuccess(){
        $("#contactForm")[0].reset();
        submitMSG(true, "Message Submitted!")
    }

    function formError(){
        $("#contactForm").removeClass().addClass('shake animated').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function(){
            $(this).removeClass();
        });
    }

    function submitMSG(valid, msg){
        if(valid){
            var msgClasses = "h4 tada animated text-success";
        } else {
            var msgClasses = "h4 text-danger";
        }
        $("#msgSubmit").removeClass().addClass(msgClasses).text(msg);
    }
}(jQuery)); // End of use strict