// CUSTOM JS START

// JQUERY HOME PAGE TITLE SUBSTR PART
$(document).ready(function() {
  $(".card-text").each(function(index, value) {
    let text;
    if (value.innerHTML.length > 110) {
      text = value.innerHTML.substr(0, 110) + "...";
    } else {
      text = value.innerHTML;
    }
    value.innerHTML = text;
  });
});

// REMOVE RECIPE FROM LIST FUNCTION
function removeRecipe(_id) {
  window.location.href = "/remove?_id" + _id;
}

// ADD NEW RECIPE MODAL APPEAR
function addRecipe() {
  $("#exampleModal").modal("show");
}

// EDIT RECIPE MODAL APPEAR
function editRecipe() {
  $("#exampleModal1").modal("show");
}
// EXAMPLE STARTER JAVASCRIPT FOR DISABLING FORM SUBMISSIONS IF THERE ARE INVALID FIELDS
(function() {
  "use strict";
  window.addEventListener(
    "load",
    function() {
      // FETCH ALL THE FORMS WE WANT TO APPLY CUSTOM BOOTSTRAP VALIDATION STYLES TO
      let forms = document.getElementsByClassName("needs-validation");
      // LOOP OVER THEM AND PREVENT SUBMISSION
      let validation = Array.prototype.filter.call(forms, function(form) {
        form.addEventListener(
          "submit",
          function(event) {
            if (form.checkValidity() === false) {
              event.preventDefault();
              event.stopPropagation();
            }
            form.classList.add("was-validated");
          },
          false
        );
      });
    },
    false
  );
})();

// CUSTOM JS END
