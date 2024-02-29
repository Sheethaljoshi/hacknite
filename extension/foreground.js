// foreground.js

// Function to replace links
function replaceLinks() {
    console.log("sdsdfdsf")
    // Get all anchor elements
    const links = document.querySelectorAll('a');
    
    // Iterate over each anchor element
    links.forEach(link => {
        // Check if the href attribute starts with the specified URL
        if (link.href.startsWith('https://hacknite.vercel.app/')) {
            // Fetch the content from the URL
            const embedElement = document.createElement('embed');
            // Set the src attribute
            embedElement.src = 'https://hacknite.vercel.app/mishal';
            // Set the style attribute
            embedElement.style.width = '700px';
            embedElement.style.height = '400px';

            // Append the <embed> element to the document body
            link.replaceWith(embedElement)

            window.addEventListener("message", function(event){
                navigator.clipboard.writeText(event.data)
            })

        }
    });
}

// Call replaceLinks function when the content script is executed
replaceLinks();
