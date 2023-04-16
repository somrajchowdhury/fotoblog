function preview() {
    // get the '<img>' element using it's ID
    const previewImg = document.getElementById("preview-image");
    /* set the 'src' attribute to the image file selected in
       the '<input type=file />' tag for the profile photo
       'target' returns a reference to the object on which the
       event originally occurred. */
    previewImg.src = URL.createObjectURL(event.target.files[0]);
    // As now we have the fetched the URL and set the preview
    // image, free memory when the preview image loads completely
    previewImg.onload = function() {
        URL.revokeObjectURL(previewImg.src);
    }
}
