$(function() {
  var $related_select_boxes = $("select[data-related-dependent]");
  $related_select_boxes.each(function(index) {
    var $select_box = $(this);
    var relatedDependent = $(this).data("relatedDependent");
    var relatedUrl = $(this).data("relatedUrl");
    var emptyLabel = $(this).data("emptyLabel");
    // empty and set readonly until we have real things to put in it
    $select_box.empty();
    $select_box.append($("<option></option>").attr("value", "").text(emptyLabel));
    $select_box.prop("readonly", true);
    $("#id_" + relatedDependent).change(function(event) {
      var data = {};
      data['value'] = $(this).val();
      $.ajax({
        url: relatedUrl,
        type: "GET",
        data: data,
        success: function(data) {
          $select_box.empty();
          $select_box.append($("<option></option>").attr("value", "").text(emptyLabel));
          if(data.length > 0) {
            $select_box.prop("readonly", false);
          } else {
            $select_box.prop("readonly", true);
          }
          $.each(data, function(index, object) {
            $select_box.append($("<option></option>").attr("value", object.value).text(object.key));
          });
        },
        error: function () {
          $select_box.empty();
          $select_box.append($("<option></option>").attr("value", "error").text("Error"));
          $select_box.prop("readonly", true);
        }
      })
    });
  })
});
