// Auth pages Js function [Changing input group text on focus]

  $(function () {
      $('input, select').on('focus', function () {
          $(this).parent().find('.input-group-text').css('border-color', '#80bdff');
      });
      $('input, select').on('blur', function () {
          $(this).parent().find('.input-group-text').css('border-color', '#ced4da');
      });
  });

// Mini panel Js function

$(function() {
  // Sidebar toggle behavior
  $('#sidebarCollapse').on('click', function() {
    $('#sidebar, #content').toggleClass('active');
  });
});

// Progress bar Js funstion for counting


$(function() {

  $(".progress").each(function() {

    var value = $(this).attr('data-value');
    var left = $(this).find('.progress-left .progress-bar');
    var right = $(this).find('.progress-right .progress-bar');

    if (value > 0) {
      if (value <= 50) {
        right.css('transform', 'rotate(' + percentageToDegrees(value) + 'deg)')
      } else {
        right.css('transform', 'rotate(180deg)')
        left.css('transform', 'rotate(' + percentageToDegrees(value - 50) + 'deg)')
      }
    }

  })

  function percentageToDegrees(percentage) {

    return percentage / 100 * 360

  }

});

// User health form toggler

function yesnoCheck() {
    if (document.getElementById('previousHealthIssues').checked) {
        document.getElementById('previous-illness1').style.display = 'block';
        document.getElementById('previous-illness2').style.display = 'block';
        document.getElementById('previous-illness3').style.display = 'block';
        document.getElementById('previous-illness4').style.display = 'block';
        document.getElementById('previous-illness5').style.display = 'block';
    }
    else {
        // document.getElementById('ifYes').style.display = 'none';
        document.getElementById('previous-illness1').style.display = 'none';
        document.getElementById('previous-illness2').style.display = 'none';
        document.getElementById('previous-illness3').style.display = 'none';
        document.getElementById('previous-illness4').style.display = 'none';
        document.getElementById('previous-illness5').style.display = 'none';
    }

}

// ==========================
// EHealth medical data form
// ==========================

// $('#medical_form').on('submit',function(event){
//     event.preventDefault();
//     var serializedData = $(this).serialize();
//     alert('Inside ajax login')

//     $.ajax({
//         type:'POST',
//         dataType: 'json',
//         url: $(this).attr('action'),
//         data: serializedData,
//         success:function(TX_data){
//             // document.getElementById("medical_form").reset();
//             this.reset()
//             // toastr.success('Your record was updated succefully');
//               $("#health_form_container").fadeOut("slow");
//               $("#health_form_replacement").fadeIn("slow");


//         },

//         error: function(Bad_Response, Bad_Response_Msg, Response_err){
//             // alert(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
//             alert(Bad_Response.status + ":" + Bad_Response.responseText);
//             // $('#health_form_container').html(Bad_Response.responseText)
//         }
//     });
// });