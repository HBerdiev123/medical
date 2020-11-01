$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-book").modal("show");
      },
      success: function (data) {
        $("#modal-book .modal-content").html(data.html_form);
      }
    });
  };


  var loadApp = function(){
    console.log('pppp')
    $.ajax({
      url: "/appointment/create", 
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-book").modal("show");
      },
      success: function (data) {
        $("#modal-book .modal-content").html(data.html_form);
      }
    });

  };
  
    var loadSchedule= function(){
    var url = $(this).attr('data-url')
    console.log('processed')
    $.ajax({
      url: url, 
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-book").modal("show");
      },
      success: function (data) {
        $("#modal-book .modal-content").html(data.html_form);
      }
    });

  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#book-table tbody").html(data.html_book_list);
          $("#modal-book").modal("hide");
        }
        else {
          $("#modal-book .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };

    var saveSchedule = function () {
    var form = $(this);
    // console.log('working')
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#book-table tbody").html(data.html_book_list);
          $("#modal-book").modal("hide");
        }
        else {
          $("#modal-book .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };

  /* Binding */

  // Create book
  $(".js-create-book").click(loadApp);
  $("#modal-book").on("submit", ".js-book-create-form", saveForm);
  // Update book
  $("#book-table").on("click", ".js-update-book", loadForm);
  $("#modal-book").on("submit", ".js-book-update-form", saveForm);
  
  // $(".js-create-schedule").click(loadForm);
  $("#book-table").on("click", ".js-create-schedule", loadForm);
  $("#modal-book").on("submit", ".js-schedule-create-form", saveSchedule);
  // Update schedule
  $("#book-table").on("click", ".js-update-schedule", loadForm);
  $("#modal-book").on("submit", ".js-schedule-update-form", saveForm);
  
  $("#book-table").on("click", ".js-delete-book", loadForm);
  $("#modal-book").on("submit", ".js-book-delete-form", saveForm);

  $("#book-table").on("click", ".js-delete-schedule", loadForm);
  $("#modal-book").on("submit", ".js-schedule-delete-form", saveForm);

});