const modal = document.getElementById("modal")

htmx.on("htmx:afterSwap", (e) => {
  // Response targeting #dialog => show the modal
  if (e.detail.target.id == "dialog") {
    $('.modal')
      .modal('show');
  }
})

htmx.on("htmx:beforeSwap", (e) => {
  // Response targeting #dialog => hide the modal
  if (e.detail.target.id == "dialog" && !e.detail.xhr.response) {
    $('.modal')
    .modal('hide');
    e.detail.shouldSwap = false
    // Hidden a dialog content after cancel or saving changes
    document.getElementById("dialog").innerHTML = ""
  }
})

htmx.on("hidden.bs.modal", () => {
// Hidden a dialog content after cancel or saving changes
  document.getElementById("dialog").innerHTML = ""
})
