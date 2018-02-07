$(function () {

  var registerSelectRelated = function () {
    // get all of the related select boxes
    var $related_select_boxes = $("select[data-related-dependent]");
    $related_select_boxes.each(function (index) {
      // first get important variables
      var $select_box = $(this);
      var relatedDependent = $select_box.data("relatedDependent");
      var relatedUrl = $select_box.data("relatedUrl");
      var emptyLabel = $select_box.data("emptyLabel");
      // next, check if part of a formset. That changes some names.
      var select_box_id = $select_box.attr('id');
      // Looks for "id_" then a valid python identifier, then a dash, number, dash, then another valid python ident
      var matches = select_box_id.match(/id_([0-9a-zA-Z_]+)-([0-9]+)-([0-9a-zA-Z_]+)/);
      if (matches !== null && matches.length === 4) {
        var formsetName = matches[1];
        var formsetNumber = matches[2];
        var fieldName = matches[3];
        relatedDependent = formsetName + '-' + formsetNumber + '-' + relatedDependent;
      }

      var $relatedDep = $("#id_" + relatedDependent);
      $relatedDep.off("change.relatedselect");
      $relatedDep.on("change.relatedselect", function (event) {
        var data = {};
        data['value'] = $(this).val();
        $.ajax({
          url: relatedUrl,
          type: "GET",
          data: data,
          success: function (data) {
            $select_box.empty();
            $select_box.append($("<option></option>").attr("value", "").text(emptyLabel));
            if (data.length > 0) {
              $select_box.prop("readonly", false);
            } else {
              $select_box.prop("readonly", true);
            }
            $.each(data, function (index, object) {
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
    });
  };
  registerSelectRelated();

  // register a page observer for form/formset changes
  MutationObserver = window.MutationObserver || window.WebKitMutationObserver;
  var observer = new MutationObserver(function (mutations, observer) {
    // fired when a mutation occurs
    console.log('Re-registering select related fields');
    registerSelectRelated();
  });
  // <form> should be broad enough to catch what we want.
  $('form').each(function () {
    observer.observe(this, {
      childList: true
    });
  })
});
