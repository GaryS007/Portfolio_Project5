const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
var deleteButtons = document.getElementsByClassName("btn-delete");
var deleteConfirm = document.getElementById("deleteConfirm");
var submitButton = document.getElementById("submitButton");

// Event Listener for delete review buttons

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let id = e.target.getAttribute("id");
        deleteConfirm.href = `delete/${reviewId}`;
        deleteModal.show();
    });
}