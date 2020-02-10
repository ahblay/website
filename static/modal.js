// Get the modal
var modal = document.getElementById("schedule-modal");

// Get the image and insert it inside the modal - use its "alt" text as a caption
var img = document.getElementById("schedule-calendar");
var modalImg = document.getElementById("modal-content");
img.onclick = function(){
  modal.style.display = "block";
  modalImg.src = this.src;
}

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}