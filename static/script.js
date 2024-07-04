// document.addEventListener("DOMContentLoaded", () => {
// console.log("DOMContentLoaded");

(()=> {
        let socket = io.connect('http://127.0.0.1:5000');
        socket.on('update_image', data => {
                console.log(data["image"]);

                let arrayBufferView = new Uint8Array(data["image"]);
                let blob = new Blob([arrayBufferView], { type: "image/jpeg" });
                let urlCreator = window.URL || window.webkitURL;
                let imgBlobUrl = urlCreator.createObjectURL(blob);
                console.log(imgBlobUrl);

                let imgInserted = document.createElement("img");
                let imageGallery = document.querySelector(".image-gallery");

                imgInserted.src = imgBlobUrl;
                imgInserted.className = "grid-item";
                // imageGallery.appendChild(imgInserted);
                imageGallery.prepend(imgInserted);
        });
})();
// });