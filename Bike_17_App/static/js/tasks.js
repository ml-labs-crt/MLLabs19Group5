// $(document).ready(function () {
//     $("#btntodo").click(function () {
//         $("#newtask").slideToggle("slow");
//         $("#doingpanel").slideUp("slow");
//         $("#donepanel").slideUp("slow");
//     });
// });
// $(document).ready(function () {
//     $("#btndoing").click(function () {
//         $("#todopanel").slideUp("slow");
//         $("#doingpanel").slideDown("slow");
//         $("#donepanel").slideUp("slow");
//     });
// });
$(document).ready(function () {
    $("#btnSignout").click(function () {
       cookie.clear();
    });
});

$(document).ready(function(){
    $("#travelsearch").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      $("#travellistTable tr").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
  });

// $(function () {
//     $('.btnlocation').click(function () {
//         $.ajax({
//             url: '/gmap',
//             data: $('form').serialize(),
//             success: function (response) {
//                 window.open('/gmap', '_blank');
//                 // alert("successful")
//             },
//             error: function (error) {
//                 console.log(error);
//             }
//         });
//     });
// });
// $(function () {
//     $(".dropdown-menu").on('click', 'li a', function () {
//         $(this).parents(".dropdown").find('.btn').html($(this).text() + ' <span class="caret"></span>');
//         $(this).parents(".dropdown").find('.btn').val($(this).data('value'));
//     });
// // });
// $(document).ready(function() {
//     $("#selectall").click(function() {
//         var checkflag = document.getElementById("#selectall").checked;
//         var chksingle = document.getElementsByName("check");
//         for (var i= 0; i< chksingle.length;i++)
//         {
//            chksingle[i].checked = checkflag;
//         }
//     });
// });
